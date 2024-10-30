import unittest

from Fill import distribute_items_restrictive
from NetUtils import encode
from worlds.AutoWorld import AutoWorldRegister, call_all
from worlds import failed_world_loads
from . import setup_solo_multiworld


class TestImplemented(unittest.TestCase):
    def test_completion_condition(self):
        """Ensure a completion condition is set that has requirements."""
        for game_name, world_type in AutoWorldRegister.world_types.items():
            if not world_type.hidden and game_name not in {"Sudoku"}:
                with self.subTest(game_name):
                    multiworld = setup_solo_multiworld(world_type)
                    self.assertFalse(multiworld.completion_condition[1](multiworld.state))

    def test_entrance_parents(self):
        """Tests that the parents of created Entrances match the exiting Region."""
        for game_name, world_type in AutoWorldRegister.world_types.items():
            if not world_type.hidden:
                with self.subTest(game_name):
                    multiworld = setup_solo_multiworld(world_type)
                    for region in multiworld.regions:
                        for exit in region.exits:
                            self.assertEqual(exit.parent_region, region)

    def test_stage_methods(self):
        """Tests that worlds don't try to implement certain steps that are only ever called as stage."""
        for game_name, world_type in AutoWorldRegister.world_types.items():
            if not world_type.hidden:
                with self.subTest(game_name):
                    for method in ("assert_generate",):
                        self.assertFalse(hasattr(world_type, method),
                                         f"{method} must be implemented as a @classmethod named stage_{method}.")

    def test_slot_data(self):
        """Tests that if a world creates slot data, it's json serializable."""
        for game_name, world_type in AutoWorldRegister.world_types.items():
            # has an await for generate_output which isn't being called
            if game_name in {"Ocarina of Time", "Zillion"}:
                continue
            multiworld = setup_solo_multiworld(world_type)
            with self.subTest(game=game_name, seed=multiworld.seed):
                distribute_items_restrictive(multiworld)
                call_all(multiworld, "post_fill")
                for key, data in multiworld.worlds[1].fill_slot_data().items():
                    self.assertIsInstance(key, str, "keys in slot data must be a string")
                    self.assertIsInstance(encode(data), str, f"object {type(data).__name__} not serializable.")

    def test_no_failed_world_loads(self):
        if failed_world_loads:
            self.fail(f"The following worlds failed to load: {failed_world_loads}")

    def test_prefill_items(self):
        """Test that every world can reach every location from allstate before pre_fill."""
        for gamename, world_type in AutoWorldRegister.world_types.items():
            if gamename not in ("Archipelago", "Sudoku", "Final Fantasy", "Test Game"):
                with self.subTest(gamename):
                    multiworld = setup_solo_multiworld(world_type, ("generate_early", "create_regions", "create_items",
                                                                    "set_rules", "generate_basic"))
                    allstate = multiworld.get_all_state(False)
                    locations = multiworld.get_locations()
                    reachable = multiworld.get_reachable_locations(allstate)
                    unreachable = [location for location in locations if location not in reachable]

                    self.assertTrue(not unreachable,
                                    f"Locations were not reachable with all state before prefill: "
                                    f"{unreachable}")
