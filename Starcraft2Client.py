from __future__ import annotations

import asyncio
import copy
import ctypes
import logging
import multiprocessing
import os.path
import re
import sys
import typing
import queue
from pathlib import Path

import nest_asyncio
import sc2
from sc2.bot_ai import BotAI
from sc2.data import Race
from sc2.main import run_game
from sc2.player import Bot

from MultiServer import mark_raw
from Utils import init_logging, is_windows
from worlds.sc2wol import SC2WoLWorld
from worlds.sc2wol.Items import lookup_id_to_name, item_table
from worlds.sc2wol.Locations import SC2WOL_LOC_ID_OFFSET
from worlds.sc2wol.MissionTables import lookup_id_to_mission
from worlds.sc2wol.Regions import MissionInfo

if __name__ == "__main__":
    init_logging("SC2Client", exception_logger="Client")

logger = logging.getLogger("Client")
sc2_logger = logging.getLogger("Starcraft2")

import colorama

from NetUtils import ClientStatus, RawJSONtoTextParser
from CommonClient import CommonContext, server_loop, ClientCommandProcessor, gui_enabled, get_base_parser

nest_asyncio.apply()
max_bonus: int = 8
victory_modulo: int = 100


class StarcraftClientProcessor(ClientCommandProcessor):
    ctx: SC2Context

    def _cmd_difficulty(self, difficulty: str = "") -> bool:
        """Overrides the current difficulty set for the seed.  Takes the argument casual, normal, hard, or brutal"""
        options = difficulty.split()
        num_options = len(options)
        difficulty_choice = options[0].lower()

        if num_options > 0:
            if difficulty_choice == "casual":
                self.ctx.difficulty_override = 0
            elif difficulty_choice == "normal":
                self.ctx.difficulty_override = 1
            elif difficulty_choice == "hard":
                self.ctx.difficulty_override = 2
            elif difficulty_choice == "brutal":
                self.ctx.difficulty_override = 3
            else:
                self.output("Unable to parse difficulty '" + options[0] + "'")
                return False

            self.output("Difficulty set to " + options[0])
            return True

        else:
            self.output("Difficulty needs to be specified in the command.")
            return False

    def _cmd_disable_mission_check(self) -> bool:
        """Disables the check to see if a mission is available to play.  Meant for co-op runs where one player can play
        the next mission in a chain the other player is doing."""
        self.ctx.missions_unlocked = True
        sc2_logger.info("Mission check has been disabled")
        return True

    def _cmd_play(self, mission_id: str = "") -> bool:
        """Start a Starcraft 2 mission"""

        options = mission_id.split()
        num_options = len(options)

        if num_options > 0:
            mission_number = int(options[0])

            self.ctx.play_mission(mission_number)

        else:
            sc2_logger.info(
                "Mission ID needs to be specified.  Use /unfinished or /available to view ids for available missions.")
            return False

        return True

    def _cmd_available(self) -> bool:
        """Get what missions are currently available to play"""

        request_available_missions(self.ctx)
        return True

    def _cmd_unfinished(self) -> bool:
        """Get what missions are currently available to play and have not had all locations checked"""

        request_unfinished_missions(self.ctx)
        return True

    @mark_raw
    def _cmd_set_path(self, path: str = '') -> bool:
        """Manually set the SC2 install directory (if the automatic detection fails)."""
        if path:
            os.environ["SC2PATH"] = path
            check_mod_install()
            return True
        else:
            sc2_logger.warning("When using set_path, you must type the path to your SC2 install directory.")
        return False


class SC2Context(CommonContext):
    command_processor = StarcraftClientProcessor
    game = "Starcraft 2 Wings of Liberty"
    items_handling = 0b111
    difficulty = -1
    all_in_choice = 0
    mission_req_table: typing.Dict[str, MissionInfo] = {}
    announcements = queue.Queue()
    sc2_run_task: typing.Optional[asyncio.Task] = None
    missions_unlocked: bool = False  # allow launching missions ignoring requirements
    current_tooltip = None
    last_loc_list = None
    difficulty_override = -1
    mission_id_to_location_ids: typing.Dict[int, typing.List[int]] = {}

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(SC2Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            self.difficulty = args["slot_data"]["game_difficulty"]
            self.all_in_choice = args["slot_data"]["all_in_map"]
            slot_req_table = args["slot_data"]["mission_req"]
            self.mission_req_table = {
                mission: MissionInfo(**slot_req_table[mission]) for mission in slot_req_table
            }

            self.build_location_to_mission_mapping()

            # Look for and set SC2PATH.
            # check_game_install_path() returns True if and only if it finds + sets SC2PATH.
            if "SC2PATH" not in os.environ and check_game_install_path():
                check_mod_install()

    def on_print_json(self, args: dict):
        # goes to this world
        if "receiving" in args and self.slot_concerns_self(args["receiving"]):
            relevant = True
        # found in this world
        elif "item" in args and self.slot_concerns_self(args["item"].player):
            relevant = True
        # not related
        else:
            relevant = False

        if relevant:
            self.announcements.put(self.raw_text_parser(copy.deepcopy(args["data"])))

        super(SC2Context, self).on_print_json(args)

    def run_gui(self):
        from kvui import GameManager, HoverBehavior, ServerToolTip
        from kivy.app import App
        from kivy.clock import Clock
        from kivy.uix.tabbedpanel import TabbedPanelItem
        from kivy.uix.gridlayout import GridLayout
        from kivy.lang import Builder
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.floatlayout import FloatLayout
        from kivy.properties import StringProperty

        import Utils

        class HoverableButton(HoverBehavior, Button):
            pass

        class MissionButton(HoverableButton):
            tooltip_text = StringProperty("Test")
            ctx: SC2Context

            def __init__(self, *args, **kwargs):
                super(HoverableButton, self).__init__(*args, **kwargs)
                self.layout = FloatLayout()
                self.popuplabel = ServerToolTip(text=self.text)
                self.layout.add_widget(self.popuplabel)

            def on_enter(self):
                self.popuplabel.text = self.tooltip_text

                if self.ctx.current_tooltip:
                    App.get_running_app().root.remove_widget(self.ctx.current_tooltip)

                if self.tooltip_text == "":
                    self.ctx.current_tooltip = None
                else:
                    App.get_running_app().root.add_widget(self.layout)
                    self.ctx.current_tooltip = self.layout

            def on_leave(self):
                self.ctx.ui.clear_tooltip()

            @property
            def ctx(self) -> CommonContext:
                return App.get_running_app().ctx

        class MissionLayout(GridLayout):
            pass

        class MissionCategory(GridLayout):
            pass

        class SC2Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago"),
                ("Starcraft2", "Starcraft2"),
            ]
            base_title = "Archipelago Starcraft 2 Client"

            mission_panel = None
            last_checked_locations = {}
            mission_id_to_button = {}
            launching: typing.Union[bool, int] = False  # if int -> mission ID
            refresh_from_launching = True
            first_check = True
            ctx: SC2Context

            def __init__(self, ctx):
                super().__init__(ctx)

            def clear_tooltip(self):
                if self.ctx.current_tooltip:
                    App.get_running_app().root.remove_widget(self.ctx.current_tooltip)

                self.ctx.current_tooltip = None

            def build(self):
                container = super().build()

                panel = TabbedPanelItem(text="Starcraft 2 Launcher")
                self.mission_panel = panel.content = MissionLayout()

                self.tabs.add_widget(panel)

                Clock.schedule_interval(self.build_mission_table, 0.5)

                return container

            def build_mission_table(self, dt):
                if (not self.launching and (not self.last_checked_locations == self.ctx.checked_locations or
                                            not self.refresh_from_launching)) or self.first_check:
                    self.refresh_from_launching = True

                    self.mission_panel.clear_widgets()

                    if self.ctx.mission_req_table:
                        self.last_checked_locations = self.ctx.checked_locations.copy()
                        self.first_check = False

                        self.mission_id_to_button = {}
                        categories = {}
                        available_missions, unfinished_missions = calc_unfinished_missions(self.ctx)

                        # separate missions into categories
                        for mission in self.ctx.mission_req_table:
                            if not self.ctx.mission_req_table[mission].category in categories:
                                categories[self.ctx.mission_req_table[mission].category] = []

                            categories[self.ctx.mission_req_table[mission].category].append(mission)

                        for category in categories:
                            category_panel = MissionCategory()
                            category_panel.add_widget(
                                Label(text=category, size_hint_y=None, height=50, outline_width=1))

                            # Map is completed
                            for mission in categories[category]:
                                text = mission
                                tooltip = ""

                                # Map has uncollected locations
                                if mission in unfinished_missions:
                                    text = f"[color=6495ED]{text}[/color]"

                                    tooltip = f"Uncollected locations:\n"
                                    tooltip += "\n".join([self.ctx.location_names[loc] for loc in
                                                          self.ctx.locations_for_mission(mission)
                                                          if loc in self.ctx.missing_locations])
                                elif mission in available_missions:
                                    text = f"[color=FFFFFF]{text}[/color]"
                                # Map requirements not met
                                else:
                                    text = f"[color=a9a9a9]{text}[/color]"
                                    tooltip = f"Requires: "
                                    if len(self.ctx.mission_req_table[mission].required_world) > 0:
                                        tooltip += ", ".join(list(self.ctx.mission_req_table)[req_mission - 1] for
                                                             req_mission in
                                                             self.ctx.mission_req_table[mission].required_world)

                                        if self.ctx.mission_req_table[mission].number > 0:
                                            tooltip += " and "
                                    if self.ctx.mission_req_table[mission].number > 0:
                                        tooltip += f"{self.ctx.mission_req_table[mission].number} missions completed"

                                mission_button = MissionButton(text=text, size_hint_y=None, height=50)
                                mission_button.tooltip_text = tooltip
                                mission_button.bind(on_press=self.mission_callback)
                                self.mission_id_to_button[self.ctx.mission_req_table[mission].id] = mission_button
                                category_panel.add_widget(mission_button)

                            category_panel.add_widget(Label(text=""))
                            self.mission_panel.add_widget(category_panel)

                elif self.launching:
                    self.refresh_from_launching = False

                    self.mission_panel.clear_widgets()
                    self.mission_panel.add_widget(Label(text="Launching Mission: " +
                                                             lookup_id_to_mission[self.launching]))
                    if self.ctx.ui:
                        self.ctx.ui.clear_tooltip()

            def mission_callback(self, button):
                if not self.launching:
                    mission_id: int = next(k for k, v in self.mission_id_to_button.items() if v == button)
                    self.ctx.play_mission(mission_id)
                    self.launching = mission_id
                    Clock.schedule_once(self.finish_launching, 10)

            def finish_launching(self, dt):
                self.launching = False

        self.ui = SC2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

        Builder.load_file(Utils.local_path(os.path.dirname(SC2WoLWorld.__file__), "Starcraft2.kv"))

    async def shutdown(self):
        await super(SC2Context, self).shutdown()
        if self.sc2_run_task:
            self.sc2_run_task.cancel()

    def play_mission(self, mission_id: int):
        if self.missions_unlocked or \
                is_mission_available(self, mission_id):
            if self.sc2_run_task:
                if not self.sc2_run_task.done():
                    sc2_logger.warning("Starcraft 2 Client is still running!")
                self.sc2_run_task.cancel()  # doesn't actually close the game, just stops the python task
            if self.slot is None:
                sc2_logger.warning("Launching Mission without Archipelago authentication, "
                                   "checks will not be registered to server.")
            self.sc2_run_task = asyncio.create_task(starcraft_launch(self, mission_id),
                                                    name="Starcraft 2 Launch")
        else:
            sc2_logger.info(
                f"{lookup_id_to_mission[mission_id]} is not currently unlocked.  "
                f"Use /unfinished or /available to see what is available.")

    def build_location_to_mission_mapping(self):
        mission_id_to_location_ids: typing.Dict[int, typing.Set[int]] = {
            mission_info.id: set() for mission_info in self.mission_req_table.values()
        }

        for loc in self.server_locations:
            mission_id, objective = divmod(loc - SC2WOL_LOC_ID_OFFSET, victory_modulo)
            mission_id_to_location_ids[mission_id].add(objective)
        self.mission_id_to_location_ids = {mission_id: sorted(objectives) for mission_id, objectives in
                                           mission_id_to_location_ids.items()}

    def locations_for_mission(self, mission: str):
        mission_id: int = self.mission_req_table[mission].id
        objectives = self.mission_id_to_location_ids[self.mission_req_table[mission].id]
        for objective in objectives:
            yield SC2WOL_LOC_ID_OFFSET + mission_id * 100 + objective


async def main():
    multiprocessing.freeze_support()
    parser = get_base_parser()
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    args = parser.parse_args()

    ctx = SC2Context(args.connect, args.password)
    ctx.auth = args.name
    if ctx.server_task is None:
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()

    await ctx.shutdown()


maps_table = [
    "ap_traynor01", "ap_traynor02", "ap_traynor03",
    "ap_thanson01", "ap_thanson02", "ap_thanson03a", "ap_thanson03b",
    "ap_ttychus01", "ap_ttychus02", "ap_ttychus03", "ap_ttychus04", "ap_ttychus05",
    "ap_ttosh01", "ap_ttosh02", "ap_ttosh03a", "ap_ttosh03b",
    "ap_thorner01", "ap_thorner02", "ap_thorner03", "ap_thorner04", "ap_thorner05s",
    "ap_tzeratul01", "ap_tzeratul02", "ap_tzeratul03", "ap_tzeratul04",
    "ap_tvalerian01", "ap_tvalerian02a", "ap_tvalerian02b", "ap_tvalerian03"
]

wol_default_categories = [
    "Mar Sara", "Mar Sara", "Mar Sara", "Colonist", "Colonist", "Colonist", "Colonist",
    "Artifact", "Artifact", "Artifact", "Artifact", "Artifact", "Covert", "Covert", "Covert", "Covert",
    "Rebellion", "Rebellion", "Rebellion", "Rebellion", "Rebellion", "Prophecy", "Prophecy", "Prophecy", "Prophecy",
    "Char", "Char", "Char", "Char"
]


def calculate_items(items):
    unit_unlocks = 0
    armory1_unlocks = 0
    armory2_unlocks = 0
    upgrade_unlocks = 0
    building_unlocks = 0
    merc_unlocks = 0
    lab_unlocks = 0
    protoss_unlock = 0
    minerals = 0
    vespene = 0
    supply = 0

    for item in items:
        data = lookup_id_to_name[item.item]

        if item_table[data].type == "Unit":
            unit_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Upgrade":
            upgrade_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Armory 1":
            armory1_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Armory 2":
            armory2_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Building":
            building_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Mercenary":
            merc_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Laboratory":
            lab_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Protoss":
            protoss_unlock += (1 << item_table[data].number)
        elif item_table[data].type == "Minerals":
            minerals += item_table[data].number
        elif item_table[data].type == "Vespene":
            vespene += item_table[data].number
        elif item_table[data].type == "Supply":
            supply += item_table[data].number

    return [unit_unlocks, upgrade_unlocks, armory1_unlocks, armory2_unlocks, building_unlocks, merc_unlocks,
            lab_unlocks, protoss_unlock, minerals, vespene, supply]


def calc_difficulty(difficulty):
    if difficulty == 0:
        return 'C'
    elif difficulty == 1:
        return 'N'
    elif difficulty == 2:
        return 'H'
    elif difficulty == 3:
        return 'B'

    return 'X'


async def starcraft_launch(ctx: SC2Context, mission_id: int):
    sc2_logger.info(f"Launching {lookup_id_to_mission[mission_id]}. If game does not launch check log file for errors.")

    with DllDirectory(None):
        run_game(sc2.maps.get(maps_table[mission_id - 1]), [Bot(Race.Terran, ArchipelagoBot(ctx, mission_id),
                                                                name="Archipelago", fullscreen=True)], realtime=True)


class ArchipelagoBot(sc2.bot_ai.BotAI):
    game_running: bool = False
    mission_completed: bool = False
    boni: typing.List[bool]
    setup_done: bool
    ctx: SC2Context
    mission_id: int

    can_read_game = False

    last_received_update: int = 0

    def __init__(self, ctx: SC2Context, mission_id):
        self.setup_done = False
        self.ctx = ctx
        self.mission_id = mission_id
        self.boni = [False for _ in range(max_bonus)]

        super(ArchipelagoBot, self).__init__()

    async def on_step(self, iteration: int):
        game_state = 0
        if not self.setup_done:
            self.setup_done = True
            start_items = calculate_items(self.ctx.items_received)
            if self.ctx.difficulty_override >= 0:
                difficulty = calc_difficulty(self.ctx.difficulty_override)
            else:
                difficulty = calc_difficulty(self.ctx.difficulty)
            await self.chat_send("ArchipelagoLoad {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
                difficulty,
                start_items[0], start_items[1], start_items[2], start_items[3], start_items[4],
                start_items[5], start_items[6], start_items[7], start_items[8], start_items[9],
                self.ctx.all_in_choice, start_items[10]))
            self.last_received_update = len(self.ctx.items_received)

        else:
            if not self.ctx.announcements.empty():
                message = self.ctx.announcements.get(timeout=1)
                await self.chat_send("SendMessage " + message)
                self.ctx.announcements.task_done()

            # Archipelago reads the health
            for unit in self.all_own_units():
                if unit.health_max == 38281:
                    game_state = int(38281 - unit.health)
                    self.can_read_game = True

            if iteration == 160 and not game_state & 1:
                await self.chat_send("SendMessage Warning: Archipelago unable to connect or has lost connection to " +
                                     "Starcraft 2 (This is likely a map issue)")

            if self.last_received_update < len(self.ctx.items_received):
                current_items = calculate_items(self.ctx.items_received)
                await self.chat_send("UpdateTech {} {} {} {} {} {} {} {}".format(
                    current_items[0], current_items[1], current_items[2], current_items[3], current_items[4],
                    current_items[5], current_items[6], current_items[7]))
                self.last_received_update = len(self.ctx.items_received)

            if game_state & 1:
                if not self.game_running:
                    print("Archipelago Connected")
                    self.game_running = True

                if self.can_read_game:
                    if game_state & (1 << 1) and not self.mission_completed:
                        if self.mission_id != 29:
                            print("Mission Completed")
                            await self.ctx.send_msgs(
                                [{"cmd": 'LocationChecks',
                                  "locations": [SC2WOL_LOC_ID_OFFSET + victory_modulo * self.mission_id]}])
                            self.mission_completed = True
                        else:
                            print("Game Complete")
                            await self.ctx.send_msgs([{"cmd": 'StatusUpdate', "status": ClientStatus.CLIENT_GOAL}])
                            self.mission_completed = True

                    for x, completed in enumerate(self.boni):
                        if not completed and game_state & (1 << (x + 2)):
                            await self.ctx.send_msgs(
                                [{"cmd": 'LocationChecks',
                                  "locations": [SC2WOL_LOC_ID_OFFSET + victory_modulo * self.mission_id + x + 1]}])
                            self.boni[x] = True

                else:
                    await self.chat_send("LostConnection - Lost connection to game.")


def request_unfinished_missions(ctx: SC2Context):
    if ctx.mission_req_table:
        message = "Unfinished Missions: "
        unlocks = initialize_blank_mission_dict(ctx.mission_req_table)
        unfinished_locations = initialize_blank_mission_dict(ctx.mission_req_table)

        _, unfinished_missions = calc_unfinished_missions(ctx, unlocks=unlocks)

        message += ", ".join(f"{mark_up_mission_name(ctx, mission, unlocks)}[{ctx.mission_req_table[mission].id}] " +
                             mark_up_objectives(
                                 f"[{len(unfinished_missions[mission])}/"
                                 f"{sum(1 for _ in ctx.locations_for_mission(mission))}]",
                                 ctx, unfinished_locations, mission)
                             for mission in unfinished_missions)

        if ctx.ui:
            ctx.ui.log_panels['All'].on_message_markup(message)
            ctx.ui.log_panels['Starcraft2'].on_message_markup(message)
        else:
            sc2_logger.info(message)
    else:
        sc2_logger.warning("No mission table found, you are likely not connected to a server.")


def calc_unfinished_missions(ctx: SC2Context, unlocks=None):
    unfinished_missions = []
    locations_completed = []

    if not unlocks:
        unlocks = initialize_blank_mission_dict(ctx.mission_req_table)

    available_missions = calc_available_missions(ctx, unlocks)

    for name in available_missions:
        objectives = set(ctx.locations_for_mission(name))
        if objectives:
            objectives_completed = ctx.checked_locations & objectives
            if len(objectives_completed) < len(objectives):
                unfinished_missions.append(name)
                locations_completed.append(objectives_completed)

        else:  # infer that this is the final mission as it has no objectives
            unfinished_missions.append(name)
            locations_completed.append(-1)

    return available_missions, dict(zip(unfinished_missions, locations_completed))


def is_mission_available(ctx: SC2Context, mission_id_to_check):
    unfinished_missions = calc_available_missions(ctx)

    return any(mission_id_to_check == ctx.mission_req_table[mission].id for mission in unfinished_missions)


def mark_up_mission_name(ctx: SC2Context, mission, unlock_table):
    """Checks if the mission is required for game completion and adds '*' to the name to mark that."""

    if ctx.mission_req_table[mission].completion_critical:
        if ctx.ui:
            message = "[color=AF99EF]" + mission + "[/color]"
        else:
            message = "*" + mission + "*"
    else:
        message = mission

    if ctx.ui:
        unlocks = unlock_table[mission]

        if len(unlocks) > 0:
            pre_message = f"[ref={list(ctx.mission_req_table).index(mission)}|Unlocks: "
            pre_message += ", ".join(f"{unlock}({ctx.mission_req_table[unlock].id})" for unlock in unlocks)
            pre_message += f"]"
            message = pre_message + message + "[/ref]"

    return message


def mark_up_objectives(message, ctx, unfinished_locations, mission):
    formatted_message = message

    if ctx.ui:
        locations = unfinished_locations[mission]

        pre_message = f"[ref={list(ctx.mission_req_table).index(mission) + 30}|"
        pre_message += "<br>".join(location for location in locations)
        pre_message += f"]"
        formatted_message = pre_message + message + "[/ref]"

    return formatted_message


def request_available_missions(ctx: SC2Context):
    if ctx.mission_req_table:
        message = "Available Missions: "

        # Initialize mission unlock table
        unlocks = initialize_blank_mission_dict(ctx.mission_req_table)

        missions = calc_available_missions(ctx, unlocks)
        message += \
            ", ".join(f"{mark_up_mission_name(ctx, mission, unlocks)}"
                      f"[{ctx.mission_req_table[mission].id}]"
                      for mission in missions)

        if ctx.ui:
            ctx.ui.log_panels['All'].on_message_markup(message)
            ctx.ui.log_panels['Starcraft2'].on_message_markup(message)
        else:
            sc2_logger.info(message)
    else:
        sc2_logger.warning("No mission table found, you are likely not connected to a server.")


def calc_available_missions(ctx: SC2Context, unlocks=None):
    available_missions = []
    missions_complete = 0

    # Get number of missions completed
    for loc in ctx.checked_locations:
        if loc % victory_modulo == 0:
            missions_complete += 1

    for name in ctx.mission_req_table:
        # Go through the required missions for each mission and fill up unlock table used later for hover-over tooltips
        if unlocks:
            for unlock in ctx.mission_req_table[name].required_world:
                unlocks[list(ctx.mission_req_table)[unlock - 1]].append(name)

        if mission_reqs_completed(ctx, name, missions_complete):
            available_missions.append(name)

    return available_missions


def mission_reqs_completed(ctx: SC2Context, mission_name: str, missions_complete):
    """Returns a bool signifying if the mission has all requirements complete and can be done

    Arguments:
    ctx -- instance of SC2Context
    locations_to_check -- the mission string name to check
    missions_complete -- an int of how many missions have been completed
"""
    if len(ctx.mission_req_table[mission_name].required_world) >= 1:
        # A check for when the requirements are being or'd
        or_success = False

        # Loop through required missions
        for req_mission in ctx.mission_req_table[mission_name].required_world:
            req_success = True

            # Check if required mission has been completed
            if not (ctx.mission_req_table[list(ctx.mission_req_table)[req_mission - 1]].id *
                    victory_modulo + SC2WOL_LOC_ID_OFFSET) in ctx.checked_locations:
                if not ctx.mission_req_table[mission_name].or_requirements:
                    return False
                else:
                    req_success = False

            # Recursively check required mission to see if it's requirements are met, in case !collect has been done
            if not mission_reqs_completed(ctx, list(ctx.mission_req_table)[req_mission - 1], missions_complete):
                if not ctx.mission_req_table[mission_name].or_requirements:
                    return False
                else:
                    req_success = False

            # If requirement check succeeded mark or as satisfied
            if ctx.mission_req_table[mission_name].or_requirements and req_success:
                or_success = True

        if ctx.mission_req_table[mission_name].or_requirements:
            # Return false if or requirements not met
            if not or_success:
                return False

        # Check number of missions
        if missions_complete >= ctx.mission_req_table[mission_name].number:
            return True
        else:
            return False
    else:
        return True


def initialize_blank_mission_dict(location_table):
    unlocks = {}

    for mission in list(location_table):
        unlocks[mission] = []

    return unlocks


def check_game_install_path() -> bool:
    # First thing: go to the default location for ExecuteInfo.
    # An exception for Windows is included because it's very difficult to find ~\Documents if the user moved it.
    if is_windows:
        # The next five lines of utterly inscrutable code are brought to you by copy-paste from Stack Overflow.
        # https://stackoverflow.com/questions/6227590/finding-the-users-my-documents-path/30924555#
        import ctypes.wintypes
        CSIDL_PERSONAL = 5  # My Documents
        SHGFP_TYPE_CURRENT = 0  # Get current, not default value

        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        documentspath = buf.value
        einfo = str(documentspath / Path("StarCraft II\\ExecuteInfo.txt"))
    else:
        einfo = str(sc2.paths.get_home() / Path(sc2.paths.USERPATH[sc2.paths.PF]))

    # Check if the file exists.
    if os.path.isfile(einfo):

        # Open the file and read it, picking out the latest executable's path.
        with open(einfo) as f:
            content = f.read()
        if content:
            base = re.search(r" = (.*)Versions", content).group(1)
            if os.path.exists(base):
                executable = sc2.paths.latest_executeble(Path(base).expanduser() / "Versions")

                # Finally, check the path for an actual executable.
                # If we find one, great. Set up the SC2PATH.
                if os.path.isfile(executable):
                    sc2_logger.info(f"Found an SC2 install at {base}!")
                    sc2_logger.debug(f"Latest executable at {executable}.")
                    os.environ["SC2PATH"] = base
                    sc2_logger.debug(f"SC2PATH set to {base}.")
                    return True
                else:
                    sc2_logger.warning(f"We may have found an SC2 install at {base}, but couldn't find {executable}.")
            else:
                sc2_logger.warning(f"{einfo} pointed to {base}, but we could not find an SC2 install there.")
    else:
        sc2_logger.warning(f"Couldn't find {einfo}. Please run /set_path with your SC2 install directory.")
    return False


def check_mod_install() -> bool:
    # Pull up the SC2PATH if set. If not, encourage the user to manually run /set_path.
    try:
        # Check inside the Mods folder for Archipelago.SC2Mod. If found, tell user. If not, tell user.
        if os.path.isfile(modfile := (os.environ["SC2PATH"] / Path("Mods") / Path("Archipelago.SC2Mod"))):
            sc2_logger.info(f"Archipelago mod found at {modfile}.")
            return True
        else:
            sc2_logger.warning(f"Archipelago mod could not be found at {modfile}. Please install the mod file there.")
    except KeyError:
        sc2_logger.warning(f"SC2PATH isn't set. Please run /set_path with the path to your SC2 install.")
    return False


class DllDirectory:
    # Credit to Black Sliver for this code.
    # More info: https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setdlldirectoryw
    _old: typing.Optional[str] = None
    _new: typing.Optional[str] = None

    def __init__(self, new: typing.Optional[str]):
        self._new = new

    def __enter__(self):
        old = self.get()
        if self.set(self._new):
            self._old = old

    def __exit__(self, *args):
        if self._old is not None:
            self.set(self._old)

    @staticmethod
    def get() -> typing.Optional[str]:
        if sys.platform == "win32":
            n = ctypes.windll.kernel32.GetDllDirectoryW(0, None)
            buf = ctypes.create_unicode_buffer(n)
            ctypes.windll.kernel32.GetDllDirectoryW(n, buf)
            return buf.value
        # NOTE: other OS may support os.environ["LD_LIBRARY_PATH"], but this fix is windows-specific
        return None

    @staticmethod
    def set(s: typing.Optional[str]) -> bool:
        if sys.platform == "win32":
            return ctypes.windll.kernel32.SetDllDirectoryW(s) != 0
        # NOTE: other OS may support os.environ["LD_LIBRARY_PATH"], but this fix is windows-specific
        return False


if __name__ == '__main__':
    colorama.init()
    asyncio.run(main())
    colorama.deinit()
