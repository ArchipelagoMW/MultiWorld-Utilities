from __future__ import annotations

from typing import Dict

from Options import Choice, Option, DefaultOnToggle, DeathLink, Range, Toggle


class EmptyItemCount(Range):
    """How many empty items to allow in a multiworld.

    Increasing this can pull more items into the Adventure world, at
    the cost of giving other worlds 'nothing' in some of their filler locations

    Supported values: 0-8
    Default value: 0
    """
    display_name = "Empty Item Count"
    range_start = 0
    range_end = 8
    default = 0


class ItemRandoType(Choice):
    """Choose how items are placed in the game

    Not yet implemented.  Currently only traditional supported
    Traditional: Adventure items are not in the map until
    they are collected (except local items) and are dropped
    on the player when collected.  Adventure items are not checks.
    Inactive: Every item is placed, but is inactive until collected.
    Each item touched is a check.  The bat ignores inactive items.

    Supported values: traditional, inactive
    Default value: traditional
    """

    display_name = "Item type"
    option_traditional = 0x00
    option_inactive = 0x01
    default = option_traditional


class DragonSlayCheck(DefaultOnToggle):
    """If true, slaying each dragon for the first time is a check
    Not yet implemented
    """
    display_name = "Slay Dragon Checks"


class TrapBatCheck(Choice):
    """
    Locking the bat inside a castle may be a check

    Not yet implemented
    If set to yes, the bat will not start inside a castle.
    Setting with_key requires the matching castle key to also be
    in the castle with the bat, achieved by dropping the key in the
    path of the portcullis as it falls.  This setting is not recommended with the bat use_logic setting

    Supported values: no, yes, with_key
    Default value: yes
    """
    display_name = "Trap bat check"
    option_no_check = 0x0
    option_yes_key_optional = 0x1
    option_with_key = 0x2
    default = option_yes_key_optional


class DragonRandoType(Choice):
    """
    How to randomize the dragon starting locations

    normal: Grundle is in the overworld, Yorgle in the white castle, and Rhindle in the black castle
    shuffle: A random dragon is placed in the overworld, one in the white castle, and one in the black castle
    overworldplus: Dragons can be placed anywhere, but at least one will be in the overworld
    randomized: Dragons can be anywhere


    Supported values: normal, shuffle, overworldplus, randomized
    Default value: shuffle
    """
    display_name = "Dragon Randomization"
    option_normal = 0x0
    option_shuffle = 0x1
    option_overworldplus = 0x2
    option_randomized = 0x3
    default = option_shuffle


class BatLogic(Choice):
    """How the bat is considered for logic

    Not yet implemented, currently the bat ignores AP items
    With cannot_break, the bat cannot pick up an item that starts out-of-logic until the player touches it
    With can_break, the bat is free to pick up local adventure items, even if they are out-of-logic
    With use_logic, the bat itself is placed as an item and can be required for logic for some locations, such
    as the credits room.  This can make the bat required to get certain items, and potentially tedious.  And also
    is not recommended with TrapBatCheck set to with_key

    Supported values: cannot_break, can_break, use_logic
    Default value: can_break
    """
    display_name = "Bat Logic"
    option_cannot_break = 0x0
    option_can_break = 0x1
    option_use_logic = 0x2
    default = option_can_break


class YorgleStartingSpeed(Range):
    """
    Sets Yorgle's initial speed.  Yorgle has a speed of 2 in the original game
    Default value: 2
    """
    display_name = "Yorgle MaxSpeed"
    range_start = 1
    range_end = 9
    default = 2


class YorgleMinimumSpeed(Range):
    """
    Sets Yorgle's speed when all speed reducers are found.  Yorgle has a speed of 2 in the original game
    Default value: 2
    """
    display_name = "Yorgle Min Speed"
    range_start = 1
    range_end = 9
    default = 1


class GrundleStartingSpeed(Range):
    """
    Sets Grundle's initial speed.  Grundle has a speed of 2 in the original game
    Default value: 2
    """
    display_name = "Grundle MaxSpeed"
    range_start = 1
    range_end = 9
    default = 2


class GrundleMinimumSpeed(Range):
    """
    Sets Grundle's speed when all speed reducers are found.  Grundle has a speed of 2 in the original game
    Default value: 2
    """
    display_name = "Grundle Min Speed"
    range_start = 1
    range_end = 9
    default = 1


class RhindleStartingSpeed(Range):
    """
    Sets Rhindle's initial speed.  Rhindle has a speed of 3 in the original game
    Default value: 3
    """
    display_name = "Rhindle MaxSpeed"
    range_start = 1
    range_end = 9
    default = 3


class RhindleMinimumSpeed(Range):
    """
    Sets Rhindle's speed when all speed reducers are found.  Rhindle has a speed of 3 in the original game
    Default value: 2
    """
    display_name = "Rhindle Min Speed"
    range_start = 1
    range_end = 9
    default = 2


class ConnectorMultiSlot(Toggle):
    """If true, the client and lua connector will add lowest 8 bits of the player slot
    to the port number used to connect to each other, to simplify connecting multiple local
    clients to local BizHawks.
    Set in the yaml, since the connector has to read this out of the rom file before connecting.
    """
    display_name = "Connector Multi-Slot"


class DifficultySwitchA(Choice):
    """Set availability of difficulty switch A

    """
    display_name = "Difficulty Switch A"
    option_normal = 0x0
    option_locked_hard = 0x1
    option_hard_with_unlock_item = 0x2
    default = option_hard_with_unlock_item


class DifficultySwitchB(Choice):
    """Set availability of difficulty switch B

    """
    display_name = "Difficulty Switch B"
    option_normal = 0x0
    option_locked_hard = 0x1
    option_hard_with_unlock_item = 0x2
    default = option_hard_with_unlock_item


adventure_option_definitions: Dict[str, type(Option)] = {
    "item_rando_type": ItemRandoType,
    "dragon_slay_check": DragonSlayCheck,
    "trap_bat_check": TrapBatCheck,
    "death_link": DeathLink,
    "bat_logic": BatLogic,
    "empty_item_count": EmptyItemCount,
    "dragon_rando_type": DragonRandoType,
    "connector_multi_slot": ConnectorMultiSlot,
    "yorgle_speed": YorgleStartingSpeed,
    "yorgle_min_speed": YorgleMinimumSpeed,
    "grundle_speed": GrundleStartingSpeed,
    "grundle_min_speed": GrundleMinimumSpeed,
    "rhindle_speed": RhindleStartingSpeed,
    "rhindle_min_speed": RhindleMinimumSpeed,
    "difficulty_switch_a": DifficultySwitchA,
    "difficulty_switch_b": DifficultySwitchB,

}