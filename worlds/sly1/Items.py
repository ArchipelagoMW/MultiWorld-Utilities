from BaseClasses import Item, ItemClassification
from .Types import ItemData, Sly1Item, episode_type_to_name, EpisodeType
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Sly1World

def create_itempool(world: "Sly1World") -> List[Item]:
    itempool: List[Item] = []

    starting_episode = (episode_type_to_name[EpisodeType(world.options.StartingEpisode)])
    del item_table[starting_episode]

    for name in item_table.keys():
        item_type: ItemClassification = item_table.get(name).classification
        item_amount: int = item_table.get(name).count
    
        itempool += create_multiple_items(world, name, item_amount, item_type)
    
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - len(event_item_pairs))
    return itempool

def create_item(world: "Sly1World", name: str) -> Item:
    data = item_table[name]
    return Sly1Item(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "Sly1World", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [Sly1Item(name, item_type, data.ap_code, world.player)]

    return itemlist

def create_junk_items(world: "Sly1World", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    # For now, all junk has equal weights
    for i in range(count):
        junk_pool.append(world.create_item(world.random.choices(list(junk_items.keys()), k=1)[0]))
    return junk_pool

sly_items = {
    # Progressive Moves
    "Progressive Dive Attack": ItemData(10020001, ItemClassification.useful, 2),
    "Progressive Roll": ItemData(10020002, ItemClassification.useful, 2),
    "Progressive Slow Motion": ItemData(10020003, ItemClassification.useful, 3),
    "Progressive Safety": ItemData(10020007, ItemClassification.useful, 2),
    "Progressive Invisibility": ItemData(10020010, ItemClassification.progression_skip_balancing, 2),
    
    # Non-progressive Moves
    "Coin Magnet": ItemData(10020004, ItemClassification.useful),
    "Mine": ItemData(10020005, ItemClassification.useful),
    "Fast": ItemData(10020006, ItemClassification.useful),
    "Decoy": ItemData(10020008, ItemClassification.useful),
    "Hacking": ItemData(10020009, ItemClassification.useful),

    # Blueprints
    "ToT Blueprints": ItemData(10020011, ItemClassification.useful),
    "SSE Blueprints": ItemData(10020012, ItemClassification.useful),
    "VV Blueprints": ItemData(10020013, ItemClassification.useful),
    "FitS Blueprints": ItemData(10020014, ItemClassification.useful),

    # Keys
    "ToT Key": ItemData(10020015, ItemClassification.progression, 7),
    "SSE Key": ItemData(10020016, ItemClassification.progression, 7),
    "VV Key": ItemData(10020017, ItemClassification.progression, 7),
    "FitS Key": ItemData(10020018, ItemClassification.progression, 7)
}

sly_episodes = {
    "Tides of Terror": ItemData(10020021, ItemClassification.progression),
    "Sunset Snake Eyes": ItemData(10020022, ItemClassification.progression),
    "Vicious Voodoo": ItemData(10020023, ItemClassification.progression),
    "Fire in the Sky": ItemData(10020024, ItemClassification.progression)
}

junk_items = {
    # Junk
    "Charm": ItemData(10020019, ItemClassification.filler),
    "1-Up": ItemData(10020020, ItemClassification.filler)

    # Traps - TBI
}

item_table = {
    **sly_items,
    **sly_episodes,
    **junk_items
}

event_item_pairs: Dict[str, str] = {
    "Eye of the Storm": "Beat Raleigh",
    "Last Call": "Beat Muggshot",
    "Deadly Dance": "Beat Mz. Ruby",
    "Flame Fu!": "Beat Panda King",
    "Cold Heart of Hate": "Victory"
}