
from Options import Choice, Toggle, DefaultOnToggle, Range, OptionList
from .Characters import all_chars


class DLC(Choice):
    """Which DLC packs to include content from. Amplified includes 4 characters, Zone 5, and new items. Synchrony includes 3 characters, new items, and balance fixes."""
    display_name = "DLC Packs"
    option_both = 0
    option_amplified = 1
    option_synchrony = 2
    option_none = 3


class Characters(OptionList):
    """Characters which contain checks. Each will be represented at least once."""
    display_name = "Available Characters"
    valid_keys = frozenset(all_chars)
    default = ['Cadence', 'Bard']


class StartingChar(Choice):
    """The initial starting character, unlocked from the start. Strongly recommended not to blindly randomize this, since Coda is an option."""
    display_name = "Starting Character"
    option_cadence = 0
    option_melody = 1
    option_aria = 2
    option_dorian = 3
    option_eli = 4
    option_monk = 5
    option_dove = 6
    option_coda = 7
    option_bolt = 8
    option_bard = 9
    option_nocturna = 10
    option_diamond = 11
    option_mary = 12
    option_tempo = 13
    option_klarinetta = 14
    option_chaunter = 15
    option_suzu = 16


class KeepInventory(Toggle):
    """Keeps your previous items when you die in a run. Makes the game significantly easier."""
    display_name = "Keep Inventory on Death"


class ReduceStartingItems(Toggle):
    """Normally, all diamond-unlocked items are restricted. If this is turned on, almost all item types are initially restricted."""
    display_name = "Reduce Starting Available Items"


class SplitWeapons(Toggle):
    """Normally, all weapons of a given type are unlocked by one item. If this is turned on, different material types will be unlocked by separate items."""
    display_name = "Split Weapon Unlocks"


class ReduceLogic(Toggle):
    """If this is turned on, the randomizer will not guarantee weapons, armor, rings, and spells for later zones, and may expect low-equipment clears."""
    display_name = "Reduce Logical Requirements"


class RandomizeFlawless(Toggle):
    """Flawless boss chests will additionally contain AP sendable items. Flawlessing bosses can be difficult, though!"""
    display_name = "Randomize Boss Flawless Chests"


class FreeSamples(Toggle):
    """Receive a free copy of an item type when received, if the current character can use it."""
    display_name = "Free Samples"


class PreventBadSamples(DefaultOnToggle):
    """Don't receive free copies of items with potentially negative effects: Karate Gi, Crown of Thorns, Glass Jaw, Sunglasses, Boots of Pain, Ring of Pain, Ring of Becoming, Ring of Shadows."""
    display_name = "Prevent Bad Samples"


class TrapPercentage(Range):
    """Percentage chance for a junk item to be a negative trap."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


cotnd_options = {
    'dlc':                      DLC,
    'available_characters':     Characters,
    'starting_character':       StartingChar,
    'randomize_flawless':       RandomizeFlawless,
    'keep_inventory_on_death':  KeepInventory,
    'reduce_starting_items':    ReduceStartingItems,
    'split_weapons':            SplitWeapons,
    'reduce_logic':             ReduceLogic,
    'free_samples':             FreeSamples,
    'prevent_bad_samples':      PreventBadSamples,
    'trap_percentage':          TrapPercentage,
}
