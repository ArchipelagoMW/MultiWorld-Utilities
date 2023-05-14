from BaseClasses import ItemClassification
from . import MessengerTestBase


class HardLogicTest(MessengerTestBase):
    options = {
        "logic_level": "hard",
    }

    def testVertical(self) -> None:
        """Test the locations that still require wingsuit or rope dart."""
        locations = [
            # tower of time
            "Tower of Time Seal - Time Waster", "Tower of Time Seal - Lantern Climb",
            "Tower of Time Seal - Arcane Orbs",
            # ninja village
            "Ninja Village - Candle", "Ninja Village - Astral Seed", "Ninja Village Seal - Tree House",
            # autumn hills
            "Autumn Hills - Climbing Claws", "Autumn Hills - Key of Hope", "Autumn Hills - Leaf Golem",
            "Autumn Hills Seal - Trip Saws", "Autumn Hills Seal - Double Swing Saws",
            "Autumn Hills Seal - Spike Ball Swing", "Autumn Hills Seal - Spike Ball Darts",
            # forlorn temple
            "Forlorn Temple - Demon King",
            "Forlorn Temple Seal - Rocket Maze", "Forlorn Temple Seal - Rocket Sunset",
            # catacombs
            "Catacombs - Necro", "Catacombs - Ruxxtin's Amulet", "Catacombs - Ruxxtin",
            "Catacombs Seal - Triple Spike Crushers", "Catacombs Seal - Crusher Gauntlet", "Catacombs Seal - Dirty Pond",
            # bamboo creek
            "Bamboo Creek - Claustro",
            "Bamboo Creek Seal - Spike Crushers and Doors", "Bamboo Creek Seal - Spike Ball Pits",
            "Bamboo Creek Seal - Spike Crushers and Doors v2",
            # howling grotto
            "Howling Grotto - Emerald Golem", "Howling Grotto Seal - Crushing Pits", "Howling Grotto Seal - Crushing Pits",
            # searing crags
            "Searing Crags - Astral Tea Leaves",
            # glacial peak
            "Glacial Peak Seal - Ice Climbers",
            # cloud ruins
            "Cloud Ruins - Acro", "Cloud Ruins Seal - Ghost Pit",
            "Cloud Ruins Seal - Toothbrush Alley", "Cloud Ruins Seal - Saw Pit", "Cloud Ruins Seal - Money Farm Room",
            # underworld
            "Underworld Seal - Rising Fanta", "Underworld Seal - Sharp and Windy Climb",
            # elemental skylands
            "Elemental Skylands Seal - Air",
            # phantom
            "Rescue Phantom",
        ]
        items = [["Wingsuit", "Rope Dart"]]
        self.assertAccessDependency(locations, items)

    def testWindmill(self) -> None:
        """Windmill Shuriken isn't progression on normal difficulty, so test it's marked correctly and required."""
        self.assertEqual(ItemClassification.progression, self.get_item_by_name("Windmill Shuriken").classification)
        windmill_locs = [
            "Searing Crags - Key of Strength",
            "Elemental Skylands - Key of Symbiosis",
            "Underworld Seal - Fireball Wave",
        ]
        for loc in windmill_locs:
            with self.subTest("can't reach location with nothing", location=loc):
                self.assertFalse(self.can_reach_location(loc))

        items = self.get_items_by_name(["Windmill Shuriken", "Lightfoot Tabi", "Magic Firefly"])
        self.collect(items)
        for loc in windmill_locs:
            with self.subTest("can reach with Windmill", location=loc):
                self.assertTrue(self.can_reach_location(loc))

        special_loc = "Autumn Hills Seal - Spike Ball Darts"
        item = self.get_item_by_name("Wingsuit")
        self.collect(item)
        self.assertTrue(self.can_reach_location(special_loc))
        self.remove(item)

        item = self.get_item_by_name("Rope Dart")
        self.collect(item)
        self.assertTrue(self.can_reach_location(special_loc))


class ChallengingLogicTest(MessengerTestBase):
    options = {
        "shuffle_seals": "false",
        "logic_level": "challenging",
    }
