from typing import Dict, Set, List

REGIONS: Dict[str, List[str]] = {
    "Menu": [],
    "Tower HQ": [],
    "The Shop": [],
    "Tower of Time": [],
    "Ninja Village": ["Ninja Village - Candle", "Ninja Village - Astral Seed"],
    "Autumn Hills": ["Autumn Hills - Climbing Claws", "Autumn Hills - Key of Hope", "Autumn Hills - Leaf Golem"],
    "Forlorn Temple": ["Forlorn Temple - Demon King"],
    "Catacombs": ["Catacombs - Necro", "Catacombs - Ruxxtin's Amulet", "Catacombs - Ruxxtin"],
    "Bamboo Creek": ["Bamboo Creek - Claustro"],
    "Howling Grotto": ["Howling Grotto - Wingsuit", "Howling Grotto - Emerald Golem"],
    "Quillshroom Marsh": ["Quillshroom Marsh - Seashell", "Quillshroom Marsh - Queen of Quills"],
    "Searing Crags": ["Searing Crags - Rope Dart"],
    "Searing Crags Upper": ["Searing Crags - Power Thistle", "Searing Crags - Key of Strength",
                            "Searing Crags - Astral Tea Leaves"],
    "Glacial Peak": [],
    "Cloud Ruins": [],
    "Cloud Ruins Right": ["Cloud Ruins - Acro"],
    "Underworld": ["Searing Crags - Pyro", "Underworld - Key of Chaos"],
    "Dark Cave": [],
    "Riviere Turquoise Entrance": [],
    "Riviere Turquoise": ["Riviere Turquoise - Butterfly Matriarch"],
    "Sunken Shrine": ["Sunken Shrine - Lightfoot Tabi", "Sunken Shrine - Sun Crest", "Sunken Shrine - Moon Crest",
                      "Sunken Shrine - Key of Love"],
    "Elemental Skylands": ["Elemental Skylands - Key of Symbiosis"],
    "Corrupted Future": ["Corrupted Future - Key of Courage"],
    "Music Box": ["Rescue Phantom"],
}
"""seal locations have the region in their name and may not need to be created so skip them here"""

SEALS: Dict[str, List[str]] = {
    "Ninja Village": ["Ninja Village Seal - Tree House"],
    "Autumn Hills": ["Autumn Hills Seal - Trip Saws", "Autumn Hills Seal - Double Swing Saws",
                     "Autumn Hills Seal - Spike Ball Swing", "Autumn Hills Seal - Spike Ball Darts"],
    "Catacombs": ["Catacombs Seal - Triple Spike Crushers", "Catacombs Seal - Crusher Gauntlet",
                  "Catacombs Seal - Dirty Pond"],
    "Bamboo Creek": ["Bamboo Creek Seal - Spike Crushers and Doors", "Bamboo Creek Seal - Spike Ball Pits",
                     "Bamboo Creek Seal - Spike Crushers and Doors v2"],
    "Howling Grotto": ["Howling Grotto Seal - Windy Saws and Balls", "Howling Grotto Seal - Crushing Pits",
                       "Howling Grotto Seal - Breezy Crushers"],
    "Quillshroom Marsh": ["Quillshroom Marsh Seal - Spikey Window", "Quillshroom Marsh Seal - Sand Trap",
                          "Quillshroom Marsh Seal - Do the Spike Wave"],
    "Searing Crags": ["Searing Crags Seal - Triple Ball Spinner"],
    "Searing Crags Upper": ["Searing Crags Seal - Raining Rocks", "Searing Crags Seal - Rhythm Rocks"],
    "Glacial Peak": ["Glacial Peak Seal - Ice Climbers", "Glacial Peak Seal - Projectile Spike Pit",
                     "Glacial Peak Seal - Glacial Air Swag"],
    "Tower of Time": ["Tower of Time Seal - Time Waster", "Tower of Time Seal - Lantern Climb",
                      "Tower of Time Seal - Arcane Orbs"],
    "Cloud Ruins Right": ["Cloud Ruins Seal - Ghost Pit", "Cloud Ruins Seal - Toothbrush Alley",
                          "Cloud Ruins Seal - Saw Pit", "Cloud Ruins Seal - Money Farm Room"],
    "Underworld": ["Underworld Seal - Sharp and Windy Climb", "Underworld Seal - Spike Wall",
                   "Underworld Seal - Fireball Wave", "Underworld Seal - Rising Fanta"],
    "Forlorn Temple": ["Forlorn Temple Seal - Rocket Maze", "Forlorn Temple Seal - Rocket Sunset"],
    "Sunken Shrine": ["Sunken Shrine Seal - Ultra Lifeguard", "Sunken Shrine Seal - Waterfall Paradise",
                      "Sunken Shrine Seal - Tabi Gauntlet"],
    "Riviere Turquoise Entrance": ["Riviere Turquoise Seal - Bounces and Balls"],
    "Riviere Turquoise": ["Riviere Turquoise Seal - Launch of Faith", "Riviere Turquoise Seal - Flower Power"],
    "Elemental Skylands": ["Elemental Skylands Seal - Air", "Elemental Skylands Seal - Water",
                           "Elemental Skylands Seal - Fire"]
}

MEGA_SHARDS: Dict[str, List[str]] = {
    "Autumn Hills": ["Autumn Hills Mega Shard", "Hidden Entrance Mega Shard"],
    "Catacombs": ["Catacombs Mega Shard"],
    "Bamboo Creek": ["Above Entrance Mega Shard", "Abandoned Mega Shard", "Time Loop Mega Shard"],
    "Howling Grotto": ["Bottom Left Mega Shard", "Near Portal Mega Shard", "Pie in the Sky Mega Shard"],
    "Quillshroom Marsh": ["Quillshroom Marsh Mega Shard"],
    "Searing Crags Upper": ["Searing Crags Mega Shard"],
    "Glacial Peak": ["Glacial Peak Mega Shard"],
    "Tower of Time": [],
    "Cloud Ruins": ["Cloud Entrance Mega Shard", "Time Warp Mega Shard"],
    "Cloud Ruins Right": ["Money Farm Room Mega Shard 1", "Money Farm Room Mega Shard 2"],
    "Underworld": ["Under Entrance Mega Shard", "Hot Tub Mega Shard", "Projectile Pit Mega Shard"],
    "Forlorn Temple": ["Sunny Day Mega Shard", "Down Under Mega Shard"],
    "Sunken Shrine": ["Mega Shard of the Moon", "Beginner's Mega Shard", "Mega Shard of the Stars", "Mega Shard of the Sun"],
    "RIviere Turquoise Entrance": ["Waterfall Mega Shard"],
    "Riviere Turquoise": ["Quick Restock Mega Shard 1", "Quick Restock Mega Shard 2"],
    "Elemental Skylands": ["Earth Mega Shard", "Water Mega Shard"],
}


REGION_CONNECTIONS: Dict[str, Set[str]] = {
    "Menu": {"Tower HQ"},
    "Tower HQ": {"Autumn Hills", "Howling Grotto", "Searing Crags", "Glacial Peak", "Tower of Time",
                 "Riviere Turquoise Entrance", "Sunken Shrine", "Corrupted Future", "The Shop", "Music Box"},
    "Tower of Time": set(),
    "Ninja Village": set(),
    "Autumn Hills": {"Ninja Village", "Forlorn Temple", "Catacombs"},
    "Forlorn Temple": {"Catacombs", "Bamboo Creek"},
    "Catacombs": {"Autumn Hills", "Bamboo Creek", "Dark Cave"},
    "Bamboo Creek": {"Catacombs", "Howling Grotto"},
    "Howling Grotto": {"Bamboo Creek", "Quillshroom Marsh", "Sunken Shrine"},
    "Quillshroom Marsh": {"Howling Grotto", "Searing Crags"},
    "Searing Crags": {"Searing Crags Upper", "Quillshroom Marsh", "Underworld"},
    "Searing Crags Upper": {"Searing Crags", "Glacial Peak"},
    "Glacial Peak": {"Searing Crags Upper", "Tower HQ", "Cloud Ruins", "Elemental Skylands"},
    "Cloud Ruins": {"Cloud Ruins Right"},
    "Cloud Ruins Right": {"Underworld"},
    "Underworld": set(),
    "Dark Cave": {"Catacombs", "Riviere Turquoise Entrance"},
    "Riviere Turquoise Entrance": {"Riviere Turquoise"},
    "Riviere Turquoise": set(),
    "Sunken Shrine": {"Howling Grotto"},
    "Elemental Skylands": set(),
}
"""Vanilla layout mapping with all Tower HQ portals open. from -> to"""
