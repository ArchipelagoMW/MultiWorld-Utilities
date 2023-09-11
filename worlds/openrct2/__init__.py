from typing import NamedTuple, Union
import logging
import json
from .Options import *
from .Constants import *
from .Items import *
from .Locations import *

from BaseClasses import Item, Tutorial, ItemClassification, Region, Entrance

from ..AutoWorld import World, WebWorld
from NetUtils import SlotType


class OpenRCT2WebWorld(WebWorld):
    tutorials = []

class OpenRCT2Location(Location):
    game = "OpenRCT2"

class OpenRCT2World(World):
    """
    OpenRCT2 is an awesome game! Blow up roller coasters!
    """

    game = "OpenRCT2"
    
    option_definitions = openRCT2_options  # options the player can set
    topology_present = True  # show path to required location checks in spoiler
    item_name_to_id = {name: id for id, name in enumerate(openRCT2_items, base_id)}
    location_name_to_id = {name: id for id, name in enumerate(openRCT2_locations, base_id)}
    
    print("Here's the location_name_to_id dictionary:")
    print(location_name_to_id)

    print("Monopoly Mode is enabled?")
    # print(self.multiworld.monopoly_mode[self.player])
    # if self.multiworld.monopoly_mode[self.player]:
    #     item_frequency["Land Discount"] = 20
    #     item_frequency["Construction Rights Discount"] = 20

    create_locations()

    def create_items(self) -> None:
        # for item in item_table:
        #     count = 0
        #     while count != item_frequency[item]:
        #         item_name_to_id.append(self.create_item(item))
        #         count += 1


        print("The item tabel is this long:")
        print(len(item_table))
        print(item_frequency)
        for item in item_table:
            count = 0
            while count != item_frequency[item]:
                self.multiworld.itempool.append(self.create_item(item))
                count += 1

        print("Here's the multiworld item pool:")
        print(self.multiworld.itempool)

    def create_regions(self) -> None:
        # Add regions to the multiworld. "Menu" is the required starting point.
        # Arguments to Region() are name, player, world, and optionally hint_text
        r = Region("Menu", self.player, self.multiworld)
        # Set Region.exits to a list of entrances that are reachable from region
        r.exits = [Entrance(self.player, "New Game", r)]  # or use r.exits.append
        # Append region to MultiWorld's regions
        self.multiworld.regions.append(r)  # or use += [r...]
        
        s = Region("Unlock Shop", self.player, self.multiworld)
        # Add main location. All unlocks come from here
        s.locations = []
        s.exits = [Entrance(self.player, "No Prereqs", s)]#, Entrance(self.player, "Category Prereq", r), Entrance(self.player, "Ride Prereq", r)]
        self.multiworld.regions.append(s)
        
        t = Region("No Prereqs", self.player, self.multiworld)
        # Add unlocks that are just prices traced back to location 0. Anything with a ride requirement or after an item with a ride requirement won't appear here
        NoPrereqs = []
        for index, item in enumerate(openRCT2_items):
        #if self.Options["difficulty"] == 0:
            NoPrereqs.append(OpenRCT2Location(self.player,"OpenRCT2_" + str(index),self.location_name_to_id["OpenRCT2_" + str(index)],t))
        
        print("Here's the NoPrereqs list:")
        print(NoPrereqs)

        t.locations = NoPrereqs
        self.multiworld.regions.append(t)

        # If entrances are not randomized, they should be connected here, otherwise
        # they can also be connected at a later stage.
        self.multiworld.get_entrance("New Game", self.player).connect(self.multiworld.get_region("Unlock Shop", self.player))
        self.multiworld.get_entrance("No Prereqs", self.player).connect(self.multiworld.get_region("No Prereqs", self.player))
        #self.multiworld.get_entrance("Category ", self.player).connect(self.multiworld.get_region("No Prereqs", self.player))

        


    def create_item(self, name:str) -> OpenRCT2Item:
        return OpenRCT2Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
