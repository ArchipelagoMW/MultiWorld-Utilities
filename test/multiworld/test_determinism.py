from typing import TypedDict
from unittest import TestCase

import worlds
from BaseClasses import (
    Location, MultiWorld, Item, Entrance, Region, ItemClassification, LocationProgressType,
)
from Fill import distribute_items_restrictive
from Options import Removed
from worlds.AutoWorld import AutoWorldRegister, call_all
from ..general import setup_multiworld


# TypedDicts for passing generated multiworld data between processes
class ItemData(TypedDict):
    name: str
    player: int
    code: int | None
    classification: ItemClassification


class LocationData(TypedDict):
    name: str
    address: int | None
    progress_type: LocationProgressType
    item: ItemData | None


class EntranceData(TypedDict):
    name: str
    parent_region: str | None
    connected_region: str | None


class RegionData(TypedDict):
    name: str
    locations: list[str]


class TestDeterministicGeneration(TestCase):
    @staticmethod
    def _test_determinism_multiworld_to_basic_data(item_pool_copy: list[Item], multiworld: MultiWorld) -> tuple[
        list[ItemData], dict[int, list[RegionData]], dict[int, list[EntranceData]], dict[int, list[LocationData]], dict[int, list[LocationData]], dict[int, list[ItemData]], dict[int, list[dict[str, str]]]
    ]:
        def item_to_basic_data(item: Item) -> ItemData:
            return {"name": item.name, "player": item.player, "code": item.code, "classification": item.classification}

        def location_to_basic_data(loc: Location, include_items: bool = False) -> LocationData:
            item = loc.item
            if include_items and item is not None:
                item_data = item_to_basic_data(item)
            else:
                item_data = None

            # ALttP does not play by the rules and sets some location addresses to `list[int]` instead of `int | None`.
            address = loc.address
            if address is not None and type(address) is not int:
                address = None
            return {"name": loc.name, "address": address, "progress_type": loc.progress_type, "item": item_data}

        def entrance_to_basic_data(ent: Entrance) -> EntranceData:
            parent_region = ent.parent_region
            parent_region_name = parent_region.name if parent_region is not None else None
            connected_region = ent.connected_region
            connected_region_name = connected_region.name if connected_region is not None else None
            return {"name": ent.name, "parent_region": parent_region_name, "connected_region": connected_region_name}

        def region_to_basic_data(reg: Region) -> RegionData:
            return {"name": reg.name, "locations": [loc.name for loc in reg.locations]}

        def dump_options(multiworld: MultiWorld) -> dict[int, list[dict[str, str]]]:
            all_options = {}
            for player in multiworld.player_ids:
                output = []
                world = multiworld.worlds[player]
                player_output = {
                    "Game": multiworld.game[player],
                    "Name": multiworld.get_player_name(player),
                }
                for option_key, option in world.options_dataclass.type_hints.items():
                    if issubclass(Removed, option):
                        continue
                    display_name = getattr(option, "display_name", option_key)
                    player_output[display_name] = getattr(world.options, option_key).current_option_name
                output.append(player_output)
                all_options[player] = output
            return all_options

        item_pool_before_main_fill = list(map(item_to_basic_data, item_pool_copy))
        # The order that regions and entrances are added to the multiworld is not considered important, so sort them by
        # name.
        regions = {player: sorted(map(region_to_basic_data, regions.values()), key=lambda reg: reg["name"])
                   for player, regions in multiworld.regions.region_cache.items()}
        entrances = {player: sorted(map(entrance_to_basic_data, entrances.values()), key=lambda ent: ent["name"])
                     for player, entrances in multiworld.regions.entrance_cache.items()}
        locations = {player: list(map(location_to_basic_data, locations.values()))
                     for player, locations in multiworld.regions.location_cache.items()}
        # Locations with the items placed at them, to compare the results of filling the multiworld.
        placements = {player: list(map(location_to_basic_data, locations.values(), (True,) * len(locations)))
                                for player, locations in multiworld.regions.location_cache.items()}
        precollected_items = {player: list(map(item_to_basic_data, items))
                              for player, items in multiworld.precollected_items.items()}

        return item_pool_before_main_fill, regions, entrances, locations, placements, precollected_items, dump_options(multiworld)

    @staticmethod
    def _test_determinism_world_setup(world_type_name: str, seed: int):
        world_type = worlds.AutoWorldRegister.world_types[world_type_name]
        multiworld = setup_multiworld(world_type, seed=seed)
        item_pool_copy = multiworld.itempool.copy()
        distribute_items_restrictive(multiworld)
        call_all(multiworld, "post_fill")
        return TestDeterministicGeneration._test_determinism_multiworld_to_basic_data(item_pool_copy, multiworld)

    @staticmethod
    def _hash_check():
        return hash("hash check")

    def test_determinism(self) -> None:
        from concurrent.futures import ProcessPoolExecutor, Future
        import multiprocessing

        hash_check = TestDeterministicGeneration._hash_check()

        # ProcessPoolExecutor is used so that we don't have to mess around with setting up communication between the new
        # process as well as exception handling and more.
        # The new process must be spawned so that the new process gets a different hashseed, resulting in different
        # ordering within `set` objects.
        with ProcessPoolExecutor(max_workers=1, mp_context=multiprocessing.get_context("spawn")) as ppe:
            # Starting up the process takes a while (6 or more seconds), so give it a generous timeout.
            # This opportunity is also used to check that the new process (most likely) has a different hashseed set.
            other_hash = ppe.submit(TestDeterministicGeneration._hash_check).result(timeout=20.0)
            # if other_hash == hash_check:
            #     self.skipTest("spawned process produced the same hash as the current process")
            self.assertNotEqual(other_hash, hash_check, "Different hashes should be produced by the current"
                                                        " process and the spawned process, but they were the same")
            for world_type_name, world_type in AutoWorldRegister.world_types.items():
                self.multiworld = setup_multiworld(world_type)
                with self.subTest(game=world_type.game, seed=self.multiworld.seed):
                    future: Future = ppe.submit(TestDeterministicGeneration._test_determinism_world_setup, world_type_name, self.multiworld.seed)
                    item_pool_copy = self.multiworld.itempool.copy()
                    distribute_items_restrictive(self.multiworld)
                    call_all(self.multiworld, "post_fill")
                    # Get our data first in-case we break something, so we get better exception tracebacks.
                    data_from_current_process = TestDeterministicGeneration._test_determinism_multiworld_to_basic_data(item_pool_copy, self.multiworld)
                    data_from_other_process = future.result(timeout=10.0)
                    for data_current, data_other, name in zip(data_from_current_process, data_from_other_process, ["item_pool", "regions", "entrances", "locations", "locations_with_items", "start_inventory", "options"], strict=True):
                        with self.subTest(name):
                            if name == "locations_with_items":
                                for player, current_locations_data in data_current.items():
                                    other_locations_data = data_other.get(player, [])
                                    current_locations_dict = {(loc["name"], loc["address"]): (loc["progress_type"], loc["item"]) for loc in current_locations_data}
                                    self.assertEqual(len(current_locations_dict), len(current_locations_data), "Duplicate locations were found (current process)")
                                    other_locations_dict = {(loc["name"], loc["address"]): (loc["progress_type"], loc["item"]) for loc in other_locations_data}
                                    self.assertEqual(len(other_locations_dict), len(other_locations_data), "Duplicate locations were found (other process)")
                                    self.assertEqual(current_locations_dict.keys(), other_locations_dict.keys(), "the names and IDs of the locations existing in the multiworld did not match")
                                    for loc_key, loc_value in current_locations_dict.items():
                                        other_loc_value = other_locations_dict[loc_key]
                                        self.assertEqual(other_loc_value, loc_value, f"location data for {loc_key} did not match")
                            else:
                                self.assertEqual(data_current, data_other)

