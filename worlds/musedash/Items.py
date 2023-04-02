from typing import NamedTuple, Optional, Union
from BaseClasses import Item, ItemClassification


class SongData(NamedTuple):
    """Special data continer to contain the metadata of each song to make filtering work."""

    code: Optional[int]
    song_is_free: bool
    streamer_mode: bool
    easy: str = Optional[int]
    hard: int = Optional[int]
    master: int = Optional[int]
    secret: int = Optional[int] #Note: Secret diffs can be Harder, but it can also just be "different". (See Heracles and Super Battleworm Insomniac for "different")


class AlbumData(NamedTuple):
    """Special data continer to contain the metadata of each album to make filtering work. Currently not used."""

    code: Optional[int]


class MuseDashSongItem(Item):
    game: str = "Muse Dash"

    def __init__(self, name: str, player: int, data: Union[SongData, AlbumData]) -> None:
        super().__init__(name, ItemClassification.progression, data.code, player)


class MuseDashFixedItem(Item):
    game: str = "Muse Dash"

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int) -> None:
        super().__init__(name, classification, code, player)
