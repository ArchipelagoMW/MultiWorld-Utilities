
from typing import Dict, List
from BaseClasses import Item, MultiWorld
from ..AutoWorld import World
#from .Rules import TimespinnerLogic
from .Items import item_table, starter_melee_weapons, starter_spells, starter_progression_items, filler_items
from .Locations import get_location_table, starter_progression_locations
from .Regions import create_regions
from .Options import is_option_enabled, timespinner_options
from .PyramidKeys import get_pyramid_keys_unlock

#TODO 
# use options without world properties
# check if create_item is used at all

class TimespinnerWorld(World):
    options = timespinner_options
    game = "Timespinner"
    topology_present = True
    data_version = 1

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in get_location_table(None, None).items()} 

    def generate_early(self):
        self.pyramid_keys_unlock = get_pyramid_keys_unlock(self.world, self.player)
        self.item_name_groups = get_item_name_groups()

    def create_regions(self):
        create_regions(self.world, self.player, get_location_table(self.world, self.player), self.pyramid_keys_unlock)

    #def create_item(self, name: str) -> Item:
    #    item_data = item_table[name]
    #    return Item(name, item_data.progression, item_data.code, self.player)

    def set_rules(self):
        self.world.completion_condition[self.player] = lambda state: state.can_reach('Ancient Pyramid (left)', 'Region', self.player)

    def generate_basic(self):
        excluded_items = get_excluded_items_based_on_options(self.world, self.player)
        locked_locations = []

        assign_starter_items(self.world, self.player, excluded_items, locked_locations)

        if not is_option_enabled(self.world, self.player, "QuickSeed") or not is_option_enabled(self.world, self.player, "Inverted"):
            place_first_progression_item(self.world, self.player, excluded_items, locked_locations)

        pool = get_item_pool(self.world, self.player, excluded_items)
        pool = fill_item_pool_with_dummy_items(self.world, self.player, locked_locations, pool)

        self.world.itempool += pool

    def fill_slot_data(self) -> Dict:
        slot_data = {}

        for option_name in timespinner_options:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = int(option.value)

        slot_data["StinkyMaw"] = 1
        slot_data["ProgressiveVerticalMovement"] = 0
        slot_data["ProgressiveKeycards"] = 0
        slot_data["PyramidKeysGate"] = self.pyramid_keys_unlock

        return slot_data

class TimespinnerWorldItem(Item):
    game = "Timespinner"

    def __init__(self, name: str, player: int = None):
        item_data = item_table[name]
        super(TimespinnerWorldItem, self).__init__(name, item_data.progression, item_data.code, player)

def get_excluded_items_based_on_options(world: MultiWorld, player: int) -> List[str]:
    excluded_items = []

    if is_option_enabled(world, player, "StartWithJewelryBox"):
        excluded_items.append('Jewelry Box')
    if is_option_enabled(world, player, "StartWithMeyef"):
        excluded_items.append('Meyef')
    if is_option_enabled(world, player, "QuickSeed"):
        excluded_items.append('Talaria Attachment')
    
    return excluded_items

def assign_starter_items(world: MultiWorld, player: int, excluded_items: List[str], locked_locations: List[str]):
    melee_weapon = world.random.choice(starter_melee_weapons)
    spell = world.random.choice(starter_spells)

    excluded_items.append(melee_weapon)
    excluded_items.append(spell)

    melee_weapon_item = TimespinnerWorldItem(melee_weapon, player)
    spell_item = TimespinnerWorldItem(spell, player)
    
    world.get_location('Yo Momma 1', player).place_locked_item(melee_weapon_item)
    world.get_location('Yo Momma 2', player).place_locked_item(spell_item)

    locked_locations.append('Yo Momma 1')
    locked_locations.append('Yo Momma 2')

def get_item_pool(world: MultiWorld, player: int, excluded_items: List[str]) -> List[TimespinnerWorldItem]:
    pool = []

    for name, data in item_table.items():
        if not name in excluded_items:
            for _ in range(data.count):
                item = update_progressive_state_based_flags(world, player, name, TimespinnerWorldItem(name, player))
                pool.append(item)

    return pool

def fill_item_pool_with_dummy_items(world: MultiWorld, player: int, locked_locations: List[str], pool: List[TimespinnerWorldItem]) -> List[TimespinnerWorldItem]:
    for _ in range(len(get_location_table(None, None)) - len(locked_locations) - len(pool)):
        item = TimespinnerWorldItem(world.random.choice(filler_items), player)
        pool.append(item)

    return pool

def place_first_progression_item(world: MultiWorld, player: int, excluded_items: List[str], locked_locations: List[str]):
    progression_item = world.random.choice(starter_progression_items)
    location =  world.random.choice(starter_progression_locations)

    excluded_items.append(progression_item)
    locked_locations.append(location)
    
    item = TimespinnerWorldItem(progression_item, player)

    world.get_location(location, player).place_locked_item(item)
 
def update_progressive_state_based_flags(world: MultiWorld, player: int, name: str, data: TimespinnerWorldItem) -> TimespinnerWorldItem:
    if not data.advancement:
        return data

    if (name == 'Tablet' or name == 'Library Keycard V') and not is_option_enabled(world, player, "DownloadableItems"):
        data.advancement = False
    if name == 'Oculus Ring' and not is_option_enabled(world, player, "FacebookMode"):
        data.advancement = False

    return data

def get_item_name_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = {}

    for name, data in item_table.items():
        groups[data.category] = [ name ] if data.category not in groups else groups[data.category] + [ name ]

    return groups