"""
Author: Louis M
Date: Fri, 03 May 2024 14:07:35 +0000
Description: Unit test used to test that no progression items can be put in Energy Temple when option enabled
"""

from . import AquariaTestBase
from BaseClasses import ItemClassification


class NoProgressionEnergyTempleTest(AquariaTestBase):
    """Unit test used to test that no progression items can be put in Energy Temple when option enabled"""
    options = {
        "no_progression_energy_temple": True
    }

    unfillable_locations = [
        "Energy Temple first area, beating the Energy Statue",
        "Energy Temple first area, bulb in the bottom room blocked by a rock",
        "Energy Temple first area, Energy Idol",
        "Energy Temple second area, bulb under the rock",
        "Energy Temple bottom entrance, Krotite Armor",
        "Energy Temple third area, bulb in the bottom path",
        "Energy Temple boss area, Fallen God Tooth",
        "Energy Temple blaster room, Blaster Egg",
    ]

    def test_no_progression_energy_temple(self) -> None:
        """
            Unit test used to test that no progression items can be put in Energy Temple when option enabled
        """
        for location in self.unfillable_locations:
            for item_name in self.world.item_names:
                item = self.get_item_by_name(item_name)
                if item.classification == ItemClassification.progression:
                    self.assertFalse(
                        self.world.get_location(location).can_fill(self.multiworld.state, item, False),
                        "The location \"" + location + "\" can be filled with \"" + item_name + "\"")
                else:
                    self.assertTrue(
                        self.world.get_location(location).can_fill(self.multiworld.state, item, False),
                        "The location \"" + location + "\" cannot be filled with \"" + item_name + "\"")

