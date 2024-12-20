import typing
from typing import NamedTuple

from BaseClasses import Entrance
from worlds.generic.Rules import CollectionRule


class LoonylandEntrance(Entrance):
    game = "Loonyland"


class LL_Entrance(NamedTuple):
    source_region: str
    target_region: str
    is_real_loading_zone: bool
    # rule: typing.Callable[[player, state], bool]
    rule: CollectionRule = lambda state: True