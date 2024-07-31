"""
Author: Louis M
Date: Fri, 03 May 2024 14:07:35 +0000
Description: Unit test used to test that progression items can be put in Frozen Veil area when option enabled
"""

from . import AquariaTestBase
from BaseClasses import ItemClassification


class ProgressionFrozenVeilTest(AquariaTestBase):
    """Unit test used to test that progression items can be put in Frozen Veil area when option enabled"""
    options = {
        "no_progression_frozen_veil": False
    }

    unfillable_locations = [
        "Ice Cavern, bulb in the room to the right",
        "Ice Cavern, first bulb in the top exit room",
        "Ice Cavern, second bulb in the top exit room",
        "Ice Cavern, third bulb in the top exit room",
        "Ice Cavern, bulb in the left room",
        "Bubble Cave, bulb in the left cave wall",
        "Bubble Cave, bulb in the right cave wall (behind the ice crystal)",
        "Bubble Cave, Verse Egg",
    ]

    def test_progression_frozen_veil(self) -> None:
        """
            Unit test used to test that progression items can be put in Frozen Veil area when option enabled
        """
        for location in self.unfillable_locations:
            for item_name in self.world.item_names:
                item = self.get_item_by_name(item_name)
                self.assertTrue(
                    self.world.get_location(location).can_fill(self.multiworld.state, item, False),
                    "The location \"" + location + "\" cannot be filled with \"" + item_name + "\"")