from typing import Dict, Set, List

REGIONS: Dict[str, List[str]] = {
    "Menu": [],
    "Tower HQ": [],
    "The Shop": [],
    "Tower of Time": [],
    "Ninja Village": ["Candle", "Astral Seed"],
    "Autumn Hills": ["Climbing Claws", "Key of Hope", "Leaf Golem"],
    "Forlorn Temple": ["Demon King Crown"],
    "Catacombs": ["Necro", "Ruxxtin's Amulet", "Ruxxtin"],
    "Bamboo Creek": ["Claustro"],
    "Howling Grotto": ["Wingsuit", "Emerald Golem"],
    "Quillshroom Marsh": ["Seashell", "Queen of Quills"],
    "Searing Crags": ["Rope Dart"],
    "Searing Crags Upper": ["Power Thistle", "Key of Strength", "Astral Tea Leaves"],
    "Glacial Peak": [],
    "Cloud Ruins": [],
    "Cloud Ruins Right": ["Acro"],
    "Underworld": ["Pyro", "Key of Chaos"],
    "Dark Cave": [],
    "Riviere Turquoise": ["Fairy Bottle"],
    "Sunken Shrine": ["Ninja Tabi", "Sun Crest", "Moon Crest", "Key of Love"],
    "Elemental Skylands": ["Key of Symbiosis"],
    "Corrupted Future": ["Key of Courage"],
    "Music Box": ["Rescue Phantom"]
}
"""seal locations have the region in their name and may not need to be created so skip them here"""

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
    "Riviere Turquoise": ["Waterfall Mega Shard", "Quick Restock Mega Shard 1", "Quick Restock Mega Shard 2"],
    "Elemental Skylands": [],
}


REGION_CONNECTIONS: Dict[str, Set[str]] = {
    "Menu": {"Tower HQ"},
    "Tower HQ": {"Autumn Hills", "Howling Grotto", "Searing Crags", "Glacial Peak", "Tower of Time", "Riviere Turquoise",
                 "Sunken Shrine", "Corrupted Future", "The Shop", "Music Box"},
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
    "Dark Cave": {"Catacombs", "Riviere Turquoise"},
    "Riviere Turquoise": set(),
    "Sunken Shrine": {"Howling Grotto"},
    "Elemental Skylands": set()
}
"""Vanilla layout mapping with all Tower HQ portals open. from -> to"""
