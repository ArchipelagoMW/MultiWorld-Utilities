import typing, os, json
from BaseClasses import Item, ItemClassification, Region, Entrance, Location
from .Locations import JakAndDaxterLocation, location_table
from .Options import JakAndDaxterOptions
from .Regions import JakAndDaxterLevel, JakAndDaxterSubLevel, JakAndDaxterRegion, level_table, subLevel_table, create_regions
from .Rules import set_rules
from .Items import JakAndDaxterItem, item_table, generic_item_table, special_item_table
from ..AutoWorld import World

from Utils import visualize_regions


class JakAndDaxterWorld(World):
    game: str = "Jak and Daxter: The Precursor Legacy"
    game_id = 74680000 # All IDs will be offset by this number.

    # Stored as {ID: Name} pairs, these must now be swapped to {Name: ID} pairs.
    item_name_to_id = {item_table[k]: 74680000 + k for k in item_table}
    location_name_to_id = {location_table[k]: 74680000 + k for k in location_table}

    options_dataclass = JakAndDaxterOptions

    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        if name == "Power Cell":
            classification = ItemClassification.progression_skip_balancing
        elif name == "Scout Fly":
            classification = ItemClassification.progression_skip_balancing
        elif name == "Precursor Orb":
            classification = ItemClassification.filler # TODO
        else:
            classification = ItemClassification.progression

        item = JakAndDaxterItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        self.multiworld.itempool += [self.create_item(item_table[0]) for k in range(0, 100)]
        self.multiworld.itempool += [self.create_item(item_table[101]) for k in range(101, 212)]
        self.multiworld.itempool += [self.create_item(item_table[k]) for k in special_item_table]
