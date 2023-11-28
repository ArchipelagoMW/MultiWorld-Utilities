from typing import Dict
from Options import AssembleOptions, Choice, Range, Toggle

class Goal(Choice):
    """Choose the end goal.
    Nap: Complete the climb to the top of Hawk Peak and take a nap"""
    display_name = "Goal"
    option_nap = 0
    default = 0

class ShowGoldenChests(Toggle):
    """Turns chests that contain items required for progression into golden chests."""
    display_name = "Progression Items in Golden Chests"
    default = True

class SkipCutscenes(Toggle):
    """Skip major cutscenes."""
    display_name = "Skip Cutscenes"
    default = True

class CoinsInShops(Toggle):
    """When enabled, the randomizer can place coins into locations that are purchased, such as shops."""
    display_name = "Coins in Purchaseable Locations"
    default = False

class GoldenFeathers(Range):
    """Number of Golden Feathers in the item pool."""
    display_name = "Golden Feathers"
    range_start = 0
    range_end = 20
    default = 20

class SilverFeathers(Range):
    """Number of Silver Feathers in the item pool."""
    display_name = "Silver Feathers"
    range_start = 0
    range_end = 20
    default = 2

class Buckets(Range):
    """Number of Buckets in the item pool."""
    display_name = "Buckets"
    range_start = 0
    range_end = 2
    default = 2

class GoldenFeatherProgression(Choice):
    """Determines which locations are considered in logic based on the required amount of golden feathers to reach them.
    Easy: Locations will be considered inaccessible until the player has enough golden feathers to easily reach them
    Normal: Locations will be considered inaccessible until the player has the minimum possible number of golden feathers to reach them
    Hard: Removes the requirement of golden feathers for progression entirely, and glitches may need to be used to progress"""
    display_name = "Golden Feather Progression"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1

short_hike_options: Dict[str, AssembleOptions] = {
    "goal": Goal,
    "show_golden_chests": ShowGoldenChests,
    "skip_cutscenes": SkipCutscenes,
    "coins_in_shops": CoinsInShops,
    "golden_feathers": GoldenFeathers,
    "silver_feathers": SilverFeathers,
    "buckets": Buckets,
    "golden_feather_progression": GoldenFeatherProgression,
}