from typing import TextIO
import os
import threading
from copy import deepcopy

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, LocationProgressType
from Fill import fill_restrictive, FillError, sweep_from_pool
from ..AutoWorld import World, WebWorld
from ..generic.Rules import add_item_rule
from .items import item_table, item_groups
from .locations import location_data, PokemonRBLocation
from .regions import create_regions
from .options import pokemon_rb_options
from .rom_addresses import rom_addresses
from .text import encode_text
from .rom import generate_output, get_base_rom_bytes, get_base_rom_path
from .pokemon import process_pokemon_data, process_move_data
from .encounters import process_pokemon_locations, process_trainer_data
from .rules import set_rules
from .level_scaling import level_scaling
from . import logic
from . import poke_data

class PokemonWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pokemon Red and Blue with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Alchav"]
    )]


class PokemonRedBlueWorld(World):
    """Pokémon Red and Pokémon Blue are the original monster-collecting turn-based RPGs.  Explore the Kanto region with
    your Pokémon, catch more than 150 unique creatures, earn badges from the region's Gym Leaders, and challenge the
    Elite Four to become the champion!"""
    # -MuffinJets#4559
    game = "Pokemon Red and Blue"
    option_definitions = pokemon_rb_options

    data_version = 0
    required_client_version = (0, 3, 9)

    topology_present = True

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {location.name: location.address for location in location_data if location.type == "Item"
                           and location.address is not None}
    item_name_groups = item_groups

    web = PokemonWebWorld()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.fly_map = None
        self.fly_map_code = None
        self.town_map_fly_map = None
        self.town_map_fly_map_code = None
        self.extra_badges = {}
        self.type_chart = None
        self.local_poke_data = None
        self.local_move_data = None
        self.local_tms = None
        self.learnsets = None
        self.trainer_name = None
        self.rival_name = None
        self.type_chart = None
        self.traps = None
        self.trade_mons = {}
        self.finished_level_scaling = threading.Event()
        self.dexsanity_table = []

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld):
        versions = set()
        for player in multiworld.player_ids:
            if multiworld.worlds[player].game == "Pokemon Red and Blue":
                versions.add(multiworld.game_version[player].current_key)
        for version in versions:
            if not os.path.exists(get_base_rom_path(version)):
                raise FileNotFoundError(get_base_rom_path(version))

    def generate_early(self):
        def encode_name(name, t):
            try:
                if len(encode_text(name)) > 7:
                    raise IndexError(f"{t} name too long for player {self.multiworld.player_name[self.player]}. Must be 7 characters or fewer.")
                return encode_text(name, length=8, whitespace="@", safety=True)
            except KeyError as e:
                raise KeyError(f"Invalid character(s) in {t} name for player {self.multiworld.player_name[self.player]}") from e
        if self.multiworld.trainer_name[self.player] == "choose_in_game":
            self.trainer_name = "choose_in_game"
        else:
            self.trainer_name = encode_name(self.multiworld.trainer_name[self.player].value, "Player")
        if self.multiworld.rival_name[self.player] == "choose_in_game":
            self.rival_name = "choose_in_game"
        else:
            self.rival_name = encode_name(self.multiworld.rival_name[self.player].value, "Rival")

        if len(self.multiworld.player_name[self.player].encode()) > 16:
            raise Exception(f"Player name too long for {self.multiworld.get_player_name(self.player)}. Player name cannot exceed 16 bytes for Pokémon Red and Blue.")

        if self.multiworld.key_items_only[self.player]:
            self.multiworld.trainersanity[self.player] = self.multiworld.trainersanity[self.player].from_text("off")
            self.multiworld.dexsanity[self.player] = self.multiworld.dexsanity[self.player].from_text("off")
            self.multiworld.randomize_hidden_items[self.player] = \
                self.multiworld.randomize_hidden_items[self.player].from_text("off")

        if self.multiworld.badges_needed_for_hm_moves[self.player].value >= 2:
            badges_to_add = ["Marsh Badge", "Volcano Badge", "Earth Badge"]
            if self.multiworld.badges_needed_for_hm_moves[self.player].value == 3:
                badges = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Marsh Badge",
                          "Soul Badge", "Volcano Badge", "Earth Badge"]
                self.multiworld.random.shuffle(badges)
                badges_to_add += [badges.pop(), badges.pop()]
            hm_moves = ["Cut", "Fly", "Surf", "Strength", "Flash"]
            self.multiworld.random.shuffle(hm_moves)
            self.extra_badges = {}
            for badge in badges_to_add:
                self.extra_badges[hm_moves.pop()] = badge

        process_move_data(self)
        process_pokemon_data(self)

        if self.multiworld.randomize_type_chart[self.player] == "vanilla":
            chart = deepcopy(poke_data.type_chart)
        elif self.multiworld.randomize_type_chart[self.player] == "randomize":
            types = poke_data.type_names.values()
            matchups = []
            for type1 in types:
                for type2 in types:
                    matchups.append([type1, type2])
            self.multiworld.random.shuffle(matchups)
            immunities = self.multiworld.immunity_matchups[self.player].value
            super_effectives = self.multiworld.super_effective_matchups[self.player].value
            not_very_effectives = self.multiworld.not_very_effective_matchups[self.player].value
            normals = self.multiworld.normal_matchups[self.player].value
            while super_effectives + not_very_effectives + normals < 225 - immunities:
                if super_effectives == not_very_effectives == normals == 0:
                    super_effectives = 225
                    not_very_effectives = 225
                    normals = 225
                else:
                    super_effectives += self.multiworld.super_effective_matchups[self.player].value
                    not_very_effectives += self.multiworld.not_very_effective_matchups[self.player].value
                    normals += self.multiworld.normal_matchups[self.player].value
            if super_effectives + not_very_effectives + normals > 225 - immunities:
                total = super_effectives + not_very_effectives + normals
                excess = total - (225 - immunities)
                subtract_amounts = (
                    int((excess / (super_effectives + not_very_effectives + normals)) * super_effectives),
                    int((excess / (super_effectives + not_very_effectives + normals)) * not_very_effectives),
                    int((excess / (super_effectives + not_very_effectives + normals)) * normals))
                super_effectives -= subtract_amounts[0]
                not_very_effectives -= subtract_amounts[1]
                normals -= subtract_amounts[2]
                while super_effectives + not_very_effectives + normals > 225 - immunities:
                    r = self.multiworld.random.randint(0, 2)
                    if r == 0:
                        super_effectives -= 1
                    elif r == 1:
                        not_very_effectives -= 1
                    else:
                        normals -= 1
            chart = []
            for matchup_list, matchup_value in zip([immunities, normals, super_effectives, not_very_effectives],
                                                   [0, 10, 20, 5]):
                for _ in range(matchup_list):
                    matchup = matchups.pop()
                    matchup.append(matchup_value)
                    chart.append(matchup)
        elif self.multiworld.randomize_type_chart[self.player] == "chaos":
            types = poke_data.type_names.values()
            matchups = []
            for type1 in types:
                for type2 in types:
                    matchups.append([type1, type2])
            chart = []
            values = list(range(21))
            self.multiworld.random.shuffle(matchups)
            self.multiworld.random.shuffle(values)
            for matchup in matchups:
                value = values.pop(0)
                values.append(value)
                matchup.append(value)
                chart.append(matchup)
        # sort so that super-effective matchups occur first, to prevent dual "not very effective" / "super effective"
        # matchups from leading to damage being ultimately divided by 2 and then multiplied by 2, which can lead to
        # damage being reduced by 1 which leads to a "not very effective" message appearing due to my changes
        # to the way effectiveness messages are generated.
        self.type_chart = sorted(chart, key=lambda matchup: -matchup[2])

        self.dexsanity_table = [
            *[True for _ in range(round(self.multiworld.dexsanity[self.player].value * 1.51))],
            *[False for _ in range(151 - round(self.multiworld.dexsanity[self.player].value * 1.51))]
        ]
        self.multiworld.random.shuffle(self.dexsanity_table)

    def create_items(self) -> None:
        start_inventory = self.multiworld.start_inventory[self.player].value.copy()
        if self.multiworld.randomize_pokedex[self.player] == "start_with":
            start_inventory["Pokedex"] = 1
            self.multiworld.push_precollected(self.create_item("Pokedex"))
        if self.multiworld.exp_all[self.player] == "start_with":
            start_inventory["Exp. All"] = 1
            self.multiworld.push_precollected(self.create_item("Exp. All"))

        locations = [location for location in location_data if location.type in ("Item", "Trainer Parties")]
        item_pool = []
        combined_traps = (self.multiworld.poison_trap_weight[self.player].value
                          + self.multiworld.fire_trap_weight[self.player].value
                          + self.multiworld.paralyze_trap_weight[self.player].value
                          + self.multiworld.ice_trap_weight[self.player].value)
        stones = ["Moon Stone", "Fire Stone", "Water Stone", "Thunder Stone", "Leaf Stone"]
        for location in locations:
            event = location.event
            if not location.inclusion(self.multiworld, self.player):
                continue

            if location.original_item is None:
                item = self.create_filler()
            elif location.original_item == "Exp. All" and self.multiworld.exp_all[self.player] == "remove":
                item = self.create_filler()
            elif location.original_item == "Pokedex":
                if self.multiworld.randomize_pokedex[self.player] == "vanilla":
                    self.multiworld.get_location(location.name, self.player).event = True
                    event = True
                item = self.create_item("Pokedex")
            elif location.original_item == "Moon Stone" and self.multiworld.stonesanity[self.player]:
                stone = stones.pop()
                item = self.create_item(stone)
            elif location.original_item.startswith("TM"):
                if self.multiworld.randomize_tm_moves[self.player]:
                    item = self.create_item(location.original_item.split(" ")[0])
                else:
                    item = self.create_item(location.original_item)
            elif location.original_item == "Card Key" and self.multiworld.split_card_key[self.player] == "on":
                item = self.create_item("Card Key 3F")
            elif "Card Key" in location.original_item and self.multiworld.split_card_key[self.player] == "progressive":
                item = self.create_item("Progressive Card Key")
            else:
                item = self.create_item(location.original_item)
                if (item.classification == ItemClassification.filler and self.multiworld.random.randint(1, 100)
                        <= self.multiworld.trap_percentage[self.player].value and combined_traps != 0):
                    item = self.create_item(self.select_trap())

            if not location.event and (self.multiworld.key_items_only[self.player] and (item.classification not in
                                       (ItemClassification.progression, ItemClassification.progression_skip_balancing,
                                        ItemClassification.useful) or item.name.startswith("TM"))):
                continue

            if item.name in start_inventory and start_inventory[item.name] > 0 and \
                    location.original_item in item_groups["Unique"]:
                start_inventory[location.original_item] -= 1
                item = self.create_filler()

            if event:
                loc = self.multiworld.get_location(location.name, self.player)
                loc.place_locked_item(item)
                if location.type == "Trainer Parties":
                    # loc.item.classification = ItemClassification.filler
                    loc.party_data = deepcopy(location.party_data)
            elif "Badge" not in item.name or self.multiworld.badgesanity[self.player].value:
                item_pool.append(item)

        self.multiworld.random.shuffle(item_pool)
        advancement_items = [item.name for item in item_pool if item.advancement] \
            + [item.name for item in self.multiworld.precollected_items[self.player] if item.advancement]
        total_advancement_items = len(
            # The stonesanity items are not checekd for here and instead just always added as the `+ 4`
            # They will always exist, but if stonesanity is off, then only as events.
            # We don't want to just add 4 if stonesanity is off while still putting them in this list in case
            # the player puts stones in their start inventory, in which case they would be double-counted here.
            [item for item in ["Bicycle", "Silph Scope", "Item Finder", "Super Rod", "Good Rod",
                               "Old Rod", "Lift Key", "Card Key", "Town Map", "Coin Case", "S.S. Ticket",
                               "Secret Key", "Poke Flute", "Mansion Key", "Safari Pass", "Plant Key",
                               "Hideout Key", "Card Key 2F", "Card Key 3F", "Card Key 4F", "Card Key 5F",
                               "Card Key 6F", "Card Key 7F", "Card Key 8F", "Card Key 9F", "Card Key 10F",
                               "Card Key 11F", "Exp. All", "Moon Stone"] if item in advancement_items]) + 4
        if "Progressive Card Key" in advancement_items:
            total_advancement_items += 10

        self.multiworld.cerulean_cave_key_items_condition[self.player].total = round((total_advancement_items / 100)
            * self.multiworld.cerulean_cave_key_items_condition[self.player].value)

        self.multiworld.elite_four_key_items_condition[self.player].total = round((total_advancement_items / 100)
            * self.multiworld.elite_four_key_items_condition[self.player].value)


        self.multiworld.itempool += item_pool

    def pre_fill(self) -> None:
        process_pokemon_locations(self)
        process_trainer_data(self)
        locs = [location.name for location in location_data if location.type != "Item"]
        for location in self.multiworld.get_locations(self.player):
            if location.name in locs:
                location.show_in_spoiler = False

        def intervene(move, test_state):
            if self.multiworld.randomize_wild_pokemon[self.player]:
                accessible_slots = [loc for loc in self.multiworld.get_reachable_locations(test_state, self.player) if
                                    loc.type == "Wild Encounter"]

                def number_of_zones(mon):
                    zones = set()
                    for loc in [slot for slot in accessible_slots if slot.item.name == mon]:
                        zones.add(loc.name.split(" - ")[0])
                    return len(zones)

                move_bit = pow(2, poke_data.hm_moves.index(move) + 2)
                viable_mons = [mon for mon in self.local_poke_data if self.local_poke_data[mon]["tms"][6] & move_bit]
                placed_mons = [slot.item.name for slot in accessible_slots]

                if self.multiworld.area_1_to_1_mapping[self.player]:
                    placed_mons.sort(key=lambda i: number_of_zones(i))
                else:
                    # this sort method doesn't work if you reference the same list being sorted in the lambda
                    placed_mons_copy = placed_mons.copy()
                    placed_mons.sort(key=lambda i: placed_mons_copy.count(i))

                placed_mon = placed_mons.pop()
                replace_mon = self.multiworld.random.choice(viable_mons)
                replace_slot = self.multiworld.random.choice([slot for slot in accessible_slots if slot.item.name
                                                              == placed_mon])
                if self.multiworld.area_1_to_1_mapping[self.player]:
                    zone = " - ".join(replace_slot.name.split(" - ")[:-1])
                    replace_slots = [slot for slot in accessible_slots if slot.name.startswith(zone) and slot.item.name
                                     == placed_mon]
                    for replace_slot in replace_slots:
                        replace_slot.item = self.create_item(replace_mon)
                else:
                    replace_slot.item = self.create_item(replace_mon)
            else:
                tms_hms = self.local_tms + poke_data.hm_moves
                flag = tms_hms.index(move)
                mon_list = [mon for mon in poke_data.pokemon_data.keys() if test_state.has(mon, self.player)]
                self.multiworld.random.shuffle(mon_list)
                mon_list.sort(key=lambda mon: self.local_move_data[move]["type"] not in
                              [self.local_poke_data[mon]["type1"], self.local_poke_data[mon]["type2"]])
                for mon in mon_list:
                    if test_state.has(mon, self.player):
                        self.local_poke_data[mon]["tms"][int(flag / 8)] |= 1 << (flag % 8)
                        break

        last_intervene = None
        while True:
            intervene_move = None
            test_state = self.multiworld.get_all_state(False)
            if not logic.can_surf(test_state, self.player):
                intervene_move = "Surf"
            elif not logic.can_strength(test_state, self.player):
                intervene_move = "Strength"
            # cut may not be needed if accessibility is minimal, unless you need all 8 badges and badgesanity is off,
            # as you will require cut to access celadon gyn
            elif ((not logic.can_cut(test_state, self.player)) and
                    (self.multiworld.accessibility[self.player] != "minimal" or ((not
                    self.multiworld.badgesanity[self.player]) and max(
                    self.multiworld.elite_four_badges_condition[self.player],
                    self.multiworld.route_22_gate_condition[self.player],
                    self.multiworld.victory_road_condition[self.player])
                    > 7) or (self.multiworld.door_shuffle[self.player] not in ("off", "simple")))):
                intervene_move = "Cut"
            elif ((not logic.can_flash(test_state, self.player)) and self.multiworld.dark_rock_tunnel_logic[self.player]
                    and (((self.multiworld.accessibility[self.player] != "minimal" and
                    (self.multiworld.trainersanity[self.player] or self.multiworld.extra_key_items[self.player])) or
                    self.multiworld.door_shuffle[self.player]))):
                intervene_move = "Flash"
            # If no Pokémon can learn Fly, then during door shuffle it would simply not treat the free fly maps
            # as reachable, and if on no door shuffle or simple, fly is simply never necessary.
            # We only intervene if a Pokémon is able to learn fly but none are reachable, as that would have been
            # considered in door shuffle.
            elif ((not logic.can_fly(test_state, self.player)) and logic.can_learn_hm(test_state, "Fly", self.player)
                    and self.multiworld.door_shuffle[self.player] not in
                    ("none", "simple") and [self.fly_map, self.town_map_fly_map] != ["Pallet Town", "Pallet Town"]):
                intervene_move = "Fly"
            if intervene_move:
                # if not self.multiworld.badgesanity[self.player]:
                #     test_state.collect(self.create_item(["Cascade Badge", "Thunder Badge", "Soul Badge",
                #                        "Rainbow Badge", "Boulder Badge"][poke_data.hm_moves.index(intervene_move)]))
                if intervene_move == last_intervene:
                    raise Exception(f"Caught in infinite loop attempting to ensure {intervene_move} is available to player {self.player}")
                intervene(intervene_move, test_state)
                last_intervene = intervene_move
            else:
                break

        # Delete evolution events for Pokémon that are not in logic in an all_state so that accessibility check does not
        # fail. Re-use test_state from previous final loop.
        evolutions_region = self.multiworld.get_region("Evolution", self.player)
        clear_cache = False
        for location in evolutions_region.locations.copy():
            if not test_state.can_reach(location, player=self.player):
                evolutions_region.locations.remove(location)
                clear_cache = True
        if clear_cache:
            self.multiworld.clear_location_cache()

        tms = [item for item in self.multiworld.itempool if item.player == self.player and item.name.startswith("TM")]
        if len(tms) > 7:
            for gym_leader in (("Pewter Gym", "Brock"), ("Cerulean Gym", "Misty"), ("Vermilion Gym", "Lt. Surge"),
                                ("Celadon Gym-C", "Erika"), ("Fuchsia Gym", "Koga"), ("Saffron Gym-C", "Sabrina"),
                                ("Cinnabar Gym", "Blaine"), ("Viridian Gym", "Giovanni")):
                for party in self.multiworld.get_location(gym_leader[0] + " - Trainer Parties", self.player).party_data:
                    if party["party_address"] == f"Trainer_Party_{gym_leader[1].replace('. ', '').replace('Giovanni', 'Viridian_Gym_Giovanni')}_A":
                        mon = party["party"][-1]
                        learnable_tms = [tm for tm in tms if self.local_poke_data[mon]["tms"][
                            int((int(tm.name[2:4]) - 1) / 8)] & 1 << ((int(tm.name[2:4]) - 1) % 8)]
                        if not learnable_tms:
                            learnable_tms = tms
                        tm = self.multiworld.random.choice(learnable_tms)
                        self.multiworld.get_location(f"{gym_leader[0].split('-')[0]} - {gym_leader[1]} TM",
                                                     self.player).place_locked_item(tm)
                        tms.remove(tm)
                        self.multiworld.itempool.remove(tm)
                        break
                else:
                    raise Exception("Missing Gym Leader data")

        if self.multiworld.old_man[self.player] == "early_parcel":
            self.multiworld.local_early_items[self.player]["Oak's Parcel"] = 1
            if self.multiworld.dexsanity[self.player]:
                for location in [self.multiworld.get_location(f"Pokedex - {mon}", self.player)
                                 for mon in poke_data.pokemon_data.keys()]:
                    add_item_rule(location, lambda item: item.name != "Oak's Parcel" or item.player != self.player)

        if not self.multiworld.badgesanity[self.player]:
            self.multiworld.non_local_items[self.player].value -= self.item_name_groups["Badges"]
            # Door Shuffle options besides Simple place badges during door shuffling
            if not self.multiworld.door_shuffle[self.player] not in ("none", "simple"):
                for _ in range(5):
                    badges = []
                    badgelocs = []
                    for badge in ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge",
                                  "Marsh Badge", "Volcano Badge", "Earth Badge"]:
                        badges.append(self.create_item(badge))
                    for loc in ["Pewter Gym - Brock Prize", "Cerulean Gym - Misty Prize", "Vermilion Gym - Lt. Surge Prize",
                                "Celadon Gym - Erika Prize", "Fuchsia Gym - Koga Prize", "Saffron Gym - Sabrina Prize",
                                "Cinnabar Gym - Blaine Prize", "Viridian Gym - Giovanni Prize"]:
                        badgelocs.append(self.multiworld.get_location(loc, self.player))
                    state = self.multiworld.get_all_state(False)
                    self.multiworld.random.shuffle(badges)
                    self.multiworld.random.shuffle(badgelocs)
                    badgelocs_copy = badgelocs.copy()
                    # allow_partial so that unplaced badges aren't lost, for debugging purposes
                    fill_restrictive(self.multiworld, state, badgelocs_copy, badges, True, True, allow_partial=True)
                    if badges:
                        for location in badgelocs:
                            location.item = None
                        continue
                    break
                else:
                    raise FillError(f"Failed to place badges for player {self.player}")

        # Place local items in some locations to prevent save-scumming. Also Oak's PC to prevent an "AP Item" from
        # entering the player's inventory.

        locs = {self.multiworld.get_location("Fossil - Choice A", self.player),
                self.multiworld.get_location("Fossil - Choice B", self.player)}

        for mon in ([" ".join(self.multiworld.get_location(
                f"Oak's Lab - Starter {i}", self.player).item.name.split(" ")[1:]) for i in range(1, 4)]
                + [" ".join(self.multiworld.get_location(
                f"Saffron Fighting Dojo - Gift {i}", self.player).item.name.split(" ")[1:]) for i in range(1, 3)]):
            try:
                loc = self.multiworld.get_location(f"Pokedex - {mon}", self.player)
                if loc.item is None:
                    locs.add(loc)
            except KeyError:
                pass

        try:
            loc = self.multiworld.get_location("Player's House 2F - Player's PC", self.player)
            if loc.item is None:
                locs.add(loc)
        except KeyError:
            pass

        for loc in sorted(locs):
            unplaced_items = []
            if loc.name in self.multiworld.priority_locations[self.player].value:
                add_item_rule(loc, lambda i: i.advancement)
            add_item_rule(loc, lambda i: i.player == self.player)
            if self.multiworld.old_man[self.player] == "early_parcel":
                add_item_rule(loc, lambda i: i.name != "Oak's Parcel")
            for item in self.multiworld.itempool.copy():
                if item.player == self.player and loc.can_fill(self.multiworld.state, item, False):
                    self.multiworld.itempool.remove(item)
                    if item.advancement:
                        state = sweep_from_pool(self.multiworld.state, self.multiworld.itempool + unplaced_items)
                    if (not item.advancement) or state.can_reach(loc, "Location", self.player):
                        self.multiworld.push_item(loc, item, False)
                        loc.event = item.advancement
                        break
                    else:
                        unplaced_items.append(item)
            self.multiworld.itempool += unplaced_items

        all_state = self.multiworld.get_all_state(False)

        reachable_mons = set()
        for mon in poke_data.pokemon_data:
            if all_state.has(mon, self.player) or all_state.has(f"Static {mon}", self.player):
                reachable_mons.add(mon)
        self.multiworld.elite_four_pokedex_condition[self.player].total = \
            int((len(reachable_mons) / 100) * self.multiworld.elite_four_pokedex_condition[self.player].value)

        if self.multiworld.accessibility[self.player] == "locations":
            balls = [self.create_item(ball) for ball in ["Poke Ball", "Great Ball", "Ultra Ball"]]
            traps = [self.create_item(trap) for trap in item_groups["Traps"]]
            locations = [location for location in self.multiworld.get_locations(self.player) if "Pokedex - " in
                         location.name]
            pokedex = self.multiworld.get_region("Pokedex", self.player)
            remove_items = 0

            for location in locations:
                if not location.can_reach(all_state):
                    pokedex.locations.remove(location)
                    remove_items += 1

            for _ in range(remove_items - 5):
                balls.append(balls.pop(0))
                for ball in balls:
                    try:
                        self.multiworld.itempool.remove(ball)
                    except ValueError:
                        continue
                    else:
                        break
                else:
                    self.multiworld.random.shuffle(traps)
                    for trap in traps:
                        try:
                            self.multiworld.itempool.remove(trap)
                        except ValueError:
                            continue
                        else:
                            break
                    else:
                        raise Exception("Failed to remove corresponding item while deleting unreachable Dexsanity location")

            self.multiworld._recache()

        if self.multiworld.door_shuffle[self.player] == "decoupled":
            swept_state = self.multiworld.state.copy()
            swept_state.sweep_for_events(player=self.player)
            locations = [location for location in
                         self.multiworld.get_reachable_locations(swept_state, self.player) if location.item is
                         None]
            self.multiworld.random.shuffle(locations)
            while len(locations) > 10:
                location = locations.pop()
                location.progress_type = LocationProgressType.EXCLUDED

    def create_regions(self):
        if (self.multiworld.old_man[self.player] == "vanilla" or
                self.multiworld.door_shuffle[self.player] in ("full", "insanity")):
            fly_map_codes = self.multiworld.random.sample(range(2, 11), 2)
        elif (self.multiworld.door_shuffle[self.player] == "simple" or
                self.multiworld.route_3_condition[self.player] == "boulder_badge" or
              (self.multiworld.route_3_condition[self.player] == "any_badge" and
               self.multiworld.badgesanity[self.player])):
            fly_map_codes = self.multiworld.random.sample(range(3, 11), 2)

        else:
            fly_map_codes = self.multiworld.random.sample([4, 6, 7, 8, 9, 10], 2)
        if self.multiworld.free_fly_location[self.player]:
            fly_map_code = fly_map_codes[0]
        else:
            fly_map_code = 0
        if self.multiworld.town_map_fly_location[self.player]:
            town_map_fly_map_code = fly_map_codes[1]
        else:
            town_map_fly_map_code = 0
        fly_maps = ["Pallet Town", "Viridian City", "Pewter City", "Cerulean City", "Lavender Town",
                    "Vermilion City", "Celadon City", "Fuchsia City", "Cinnabar Island", "Indigo Plateau",
                    "Saffron City"]
        self.fly_map = fly_maps[fly_map_code]
        self.town_map_fly_map = fly_maps[town_map_fly_map_code]
        self.fly_map_code = fly_map_code
        self.town_map_fly_map_code = town_map_fly_map_code

        create_regions(self)
        self.multiworld.completion_condition[self.player] = lambda state, player=self.player: state.has("Become Champion", player=player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return PokemonRBItem(name, self.player)

    @classmethod
    def stage_generate_output(cls, multiworld, output_directory):
        level_scaling(multiworld)

    def generate_output(self, output_directory: str):
        generate_output(self, output_directory)

    def write_spoiler_header(self, spoiler_handle: TextIO):
        spoiler_handle.write(f"Cerulean Cave Total Key Items:   {self.multiworld.cerulean_cave_key_items_condition[self.player].total}\n")
        spoiler_handle.write(f"Elite Four Total Key Items:      {self.multiworld.elite_four_key_items_condition[self.player].total}\n")
        spoiler_handle.write(f"Elite Four Total Pokemon:        {self.multiworld.elite_four_pokedex_condition[self.player].total}\n")
        if self.multiworld.free_fly_location[self.player]:
            spoiler_handle.write(f"Free Fly Location:               {self.fly_map}\n")
        if self.multiworld.town_map_fly_location[self.player]:
            spoiler_handle.write(f"Town Map Fly Location:           {self.town_map_fly_map}\n")
        if self.extra_badges:
            for hm_move, badge in self.extra_badges.items():
                spoiler_handle.write(hm_move + " enabled by: " + (" " * 20)[:20 - len(hm_move)] + badge + "\n")

    def write_spoiler(self, spoiler_handle):
        if self.multiworld.randomize_type_chart[self.player].value:
            spoiler_handle.write(f"\n\nType matchups ({self.multiworld.player_name[self.player]}):\n\n")
            for matchup in self.type_chart:
                spoiler_handle.write(f"{matchup[0]} deals {matchup[2] * 10}% damage to {matchup[1]}\n")
        spoiler_handle.write(f"\n\nPokémon locations ({self.multiworld.player_name[self.player]}):\n\n")
        pokemon_locs = [location.name for location in location_data if location.type not in ("Item", "Trainer Parties")]
        for location in self.multiworld.get_locations(self.player):
            if location.name in pokemon_locs:
                spoiler_handle.write(location.name + ": " + location.item.name + "\n")

    def get_filler_item_name(self) -> str:
        combined_traps = (self.multiworld.poison_trap_weight[self.player].value
                          + self.multiworld.fire_trap_weight[self.player].value
                          + self.multiworld.paralyze_trap_weight[self.player].value
                          + self.multiworld.ice_trap_weight[self.player].value
                          + self.multiworld.sleep_trap_weight[self.player].value)
        if (combined_traps > 0 and
                self.multiworld.random.randint(1, 100) <= self.multiworld.trap_percentage[self.player].value):
            return self.select_trap()

        return self.multiworld.random.choice([item for item in item_table if item_table[item].id and item_table[
            item].classification == ItemClassification.filler and item not in item_groups["Vending Machine Drinks"] +
                                              item_groups["Unique"]])

    def select_trap(self):
        if self.traps is None:
            self.traps = []
            self.traps += ["Poison Trap"] * self.multiworld.poison_trap_weight[self.player].value
            self.traps += ["Fire Trap"] * self.multiworld.fire_trap_weight[self.player].value
            self.traps += ["Paralyze Trap"] * self.multiworld.paralyze_trap_weight[self.player].value
            self.traps += ["Ice Trap"] * self.multiworld.ice_trap_weight[self.player].value
            self.traps += ["Sleep Trap"] * self.multiworld.sleep_trap_weight[self.player].value
        return self.multiworld.random.choice(self.traps)

    def extend_hint_information(self, hint_data):
        if self.multiworld.dexsanity[self.player] or self.multiworld.door_shuffle[self.player]:
            hint_data[self.player] = {}
        if self.multiworld.dexsanity[self.player]:
            mon_locations = {mon: set() for mon in poke_data.pokemon_data.keys()}
            for loc in location_data:
                if loc.type in ["Wild Encounter", "Static Pokemon", "Legendary Pokemon", "Missable Pokemon"]:
                    mon = self.multiworld.get_location(loc.name, self.player).item.name
                    if mon.startswith("Static ") or mon.startswith("Missable "):
                        mon = " ".join(mon.split(" ")[1:])
                    mon_locations[mon].add(loc.name.split(" -")[0])
            for mon in mon_locations:
                if mon_locations[mon]:
                    try:
                        hint_data[self.player][self.multiworld.get_location(f"Pokedex - {mon}", self.player).address] =\
                            ", ".join(mon_locations[mon])
                    except KeyError:
                        pass
        if self.multiworld.door_shuffle[self.player]:
            for location in self.multiworld.get_locations(self.player):
                if location.parent_region.entrance_hint and location.address:
                    hint_data[self.player][location.address] = location.parent_region.entrance_hint

    def fill_slot_data(self) -> dict:
        return {
            "second_fossil_check_condition": self.multiworld.second_fossil_check_condition[self.player].value,
            "require_item_finder": self.multiworld.require_item_finder[self.player].value,
            "randomize_hidden_items": self.multiworld.randomize_hidden_items[self.player].value,
            "badges_needed_for_hm_moves": self.multiworld.badges_needed_for_hm_moves[self.player].value,
            "oaks_aide_rt_2": self.multiworld.oaks_aide_rt_2[self.player].value,
            "oaks_aide_rt_11": self.multiworld.oaks_aide_rt_11[self.player].value,
            "oaks_aide_rt_15": self.multiworld.oaks_aide_rt_15[self.player].value,
            "extra_key_items": self.multiworld.extra_key_items[self.player].value,
            "extra_strength_boulders": self.multiworld.extra_strength_boulders[self.player].value,
            "tea": self.multiworld.tea[self.player].value,
            "old_man": self.multiworld.old_man[self.player].value,
            "elite_four_badges_condition": self.multiworld.elite_four_badges_condition[self.player].value,
            "elite_four_key_items_condition": self.multiworld.elite_four_key_items_condition[self.player].total,
            "elite_four_pokedex_condition": self.multiworld.elite_four_pokedex_condition[self.player].total,
            "victory_road_condition": self.multiworld.victory_road_condition[self.player].value,
            "route_22_gate_condition": self.multiworld.route_22_gate_condition[self.player].value,
            "route_3_condition": self.multiworld.route_3_condition[self.player].value,
            "robbed_house_officer": self.multiworld.robbed_house_officer[self.player].value,
            "viridian_gym_condition": self.multiworld.viridian_gym_condition[self.player].value,
            "cerulean_cave_badges_condition": self.multiworld.cerulean_cave_badges_condition[self.player].value,
            "cerulean_cave_key_items_condition": self.multiworld.cerulean_cave_key_items_condition[self.player].total,
            "free_fly_map": self.fly_map_code,
            "town_map_fly_map": self.town_map_fly_map_code,
            "extra_badges": self.extra_badges,
            "type_chart": self.type_chart,
            "randomize_pokedex": self.multiworld.randomize_pokedex[self.player].value,
            "trainersanity": self.multiworld.trainersanity[self.player].value,
            "death_link": self.multiworld.death_link[self.player].value,
            "prizesanity": self.multiworld.prizesanity[self.player].value,
            "key_items_only": self.multiworld.key_items_only[self.player].value,
        }


class PokemonRBItem(Item):
    game = "Pokemon Red and Blue"
    type = None

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(PokemonRBItem, self).__init__(
            name,
            item_data.classification,
            item_data.id, player
        )