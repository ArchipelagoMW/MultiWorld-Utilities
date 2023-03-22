from BaseClasses import MultiWorld
from typing import List, Set

from ..generic import Rules as GenericRules
from . import Locations


holy_mountain_regions: List[str] = [
    "Holy Mountain 1 (To Coal Pits)",
    "Holy Mountain 2 (To Snowy Depths)",
    "Holy Mountain 3 (To Hiisi Base)",
    "Holy Mountain 4 (To Underground Jungle)",
    "Holy Mountain 5 (To The Vault)",
    "Holy Mountain 6 (To Temple of the Art)",
    "Holy Mountain 7 (To The Laboratory)",
]

wand_tiers: List[str] = [
    "Wand (Tier 1)",    # Coal Pits
    "Wand (Tier 2)",    # Snowy Depths
    "Wand (Tier 3)",    # Hiisi Base
    "Wand (Tier 4)",    # Underground Jungle
    "Wand (Tier 5)",    # The Vault
    "Wand (Tier 6)",    # Temple of the Art
]

items_hidden_from_shops: Set[str] = {"Gold (10)", "Gold (50)", "Gold (200)", "Gold (1000)", "Potion", "Random Potion",
                                     "Secret Potion", "Chaos Die", "Greed Die", "Kammi", "Refreshing Gourd", "Sadekivi",
                                     "Broken Wand", "Powder Pouch"}


def forbid_items_at_location(world: MultiWorld, location_name: str, items: Set[str], player: int):
    location = world.get_location(location_name, player)
    GenericRules.forbid_items_for_player(location, items, player)


def create_all_rules(world: MultiWorld, player: int) -> None:

    # Prevent gold and potions from appearing as purchasable items in shops
    for location_name in Locations.location_name_to_id.keys():
        if "Shop Item" not in location_name: continue
        forbid_items_at_location(world, location_name, items_hidden_from_shops, player)

    # Prevent high tier wands from appearing in early Holy Mountain shops
    for i, region_name in enumerate(holy_mountain_regions):
        wands_to_forbid = wand_tiers[i+1:]

        locations_in_region = Locations.location_region_mapping[region_name].keys()
        for location_name in locations_in_region:
            forbid_items_at_location(world, location_name, wands_to_forbid, player)

    # Prevent high tier wands from appearing in the Secret shop
    wands_to_forbid = wand_tiers[3:]
    locations_in_region = Locations.location_region_mapping["Secret Shop"].keys()
    for location_name in locations_in_region:
        forbid_items_at_location(world, location_name, wands_to_forbid, player)

    # Prevent the Map perk from being on Toveri
    if world.bosses_as_checks[player].value >= 3:
        for location_name in Locations.location_name_to_id.keys():
            if "Toveri" not in location_name: continue
            forbid_items_at_location(world, location_name, {"Perk (Spatial Awareness)"}, player)
