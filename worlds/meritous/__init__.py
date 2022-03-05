# Copyright (c) 2022 FelicitusNeko
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from BaseClasses import Item, MultiWorld
from Fill import fill_restrictive
from .Items import item_table, item_groups, MeritousItem
from .Locations import location_table, MeritousLocation
from .Options import meritous_options
from .Regions import create_regions
from .Rules import set_rules
from ..AutoWorld import World

client_version = 1


class MeritousWorld(World):
    # NOTE: Remember to put in an actual description before going live
    """Insert some sort of description here"""

    game: str = "Meritous"
    topology_present: False

    item_name_to_id = item_table
    location_name_to_id = location_table
    item_name_groups = item_groups

    data_version = 1
    forced_auto_forfeit = False

    options = meritous_options

    def __init__(self, world: MultiWorld, player: int):
        super(MeritousWorld, self).__init__(world, player)
        self.goal = 0
        self.include_evolution_traps = False
        self.include_psi_keys = False
        self.death_link = False

    @staticmethod
    def _is_progression(name):
        return "PSI Key" in name or name in ["Cursed Seal", "Agate Knife"]

    def create_item(self, name: str) -> Item:
        return MeritousItem(name, self._is_progression(
            name), item_table[name], self.player)

    def create_event(self, event: str):
        event = MeritousItem(event, True, None, self.player)
        event.type = "Victory"
        return event

    def _create_item_in_quantities(self, name: str, qty: int) -> [Item]:
        return [self.create_item(name) for _ in range(0, qty)]

    def _make_crystals(self, qty: int) -> [MeritousItem]:
        crystal_pool = []

        for _ in range(0, qty):
            rand_crystals = self.world.random.randrange(0, 32)
            if rand_crystals < 16:
                crystal_pool += [self.create_item("Crystals x500")]
            elif rand_crystals < 28:
                crystal_pool += [self.create_item("Crystals x1000")]
            else:
                crystal_pool += [self.create_item("Crystals x2000")]

        return crystal_pool

    def generate_early(self):
        self.goal = self.world.goal[self.player].value
        self.include_evolution_traps = self.world.include_evolution_traps[self.player].value
        self.include_psi_keys = self.world.include_psi_keys[self.player].value
        self.death_link = self.world.death_link[self.player].value

    def create_regions(self):
        create_regions(self.world, self.player)

    def create_items(self):
        frequencies = [0, 25, 23, 22, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3]
        location_count = len(location_table) - 2
        item_pool = []

        if not self.include_psi_keys:
            location_count -= 3
            for i in range(3):
                frequencies[i + 12] = 0

        if not self.include_evolution_traps:
            frequencies[17] = 0
            location_count -= 3

        for i, name in enumerate(item_table):
            if i < len(frequencies):
                item_pool += self._create_item_in_quantities(
                    name, frequencies[i])

        if len(item_pool) < location_count:
            item_pool += self._make_crystals(location_count - len(item_pool))

        self.world.itempool += item_pool

    def set_rules(self):
        set_rules(self.world, self.player)

    def generate_basic(self):
        self.world.get_location("Place of Power", self.player).place_locked_item(
            self.create_item("Cursed Seal"))
        self.world.get_location("The Last Place You'll Look", self.player).place_locked_item(
            self.create_item("Agate Knife"))
        self.world.get_location("Wervyn Anixil", self.player).place_locked_item(
            self.create_event("Victory"))
        self.world.get_location("Wervyn Anixil?", self.player).place_locked_item(
            self.create_event("Full Victory"))
        for boss in ["Meridian", "Ataraxia", "Merodach"]:
            self.world.get_location(f"{boss} Defeat", self.player).place_locked_item(
                self.create_event(f"{boss} Defeated"))

        if not self.include_psi_keys:
            psi_keys = []
            psi_key_storage = []
            for i in range(0, 3):
                psi_keys += [self.create_item(f"PSI Key {i + 1}")]
                psi_key_storage += [self.world.get_location(
                    f"PSI Key Storage {i + 1}", self.player)]

            fill_restrictive(self.world, self.world.get_all_state(
                False), psi_key_storage, psi_keys)

        if not self.include_evolution_traps:
            for boss in ["Meridian", "Ataraxia", "Merodach"]:
                self.world.get_location(boss, self.player).place_locked_item(
                    self.create_item("Evolution Trap"))

        if self.goal == 0:
            self.world.completion_condition[self.player] = lambda state: state.has_any(
                ["Victory", "Full Victory"], self.player)
        else:
            self.world.completion_condition[self.player] = lambda state: state.has(
                "Full Victory", self.player)

    def get_required_client_version(self) -> tuple:
        # NOTE: Remember to change this before this game goes live
        return max((0, 2, 4), super(MeritousWorld, self).get_required_client_version())

    def fill_slot_data(self) -> dict:
        return {
            "goal": self.goal,
            "death_link": self.death_link
        }
