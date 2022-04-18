import string

from BaseClasses import Item, MultiWorld, Region, Location, Entrance
from .Items import item_table, item_pool, event_item_pairs
from .Locations import location_table
from .Regions import create_regions
from .Rules import set_rules
from ..AutoWorld import World
from .Options import spire_options


class SpireWorld(World):
    options = spire_options
    game = "Slay the Spire"
    topology_present = False
    data_version = 1

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    forced_auto_forfeit = True

    def _get_slot_data(self):
        return {
            'seed': "".join(self.world.slot_seeds[self.player].choice(string.ascii_letters) for i in range(16)),
            'character': self.world.character[self.player],
            'ascension': self.world.ascension[self.player],
            'heart_run': self.world.heart_run[self.player]
        }

    def generate_basic(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool = []
        for name, data in item_table.items():
            if not data.event:
                if name in item_pool:
                    card_draw = 0
                    for amount in range(item_pool[name]):
                        item = SpireItem(name, self.player)

                        # This feels wrong but it makes our failure rate drop dramatically
                        # makes all but 7 basic card draws trash fill
                        if item.name == "Card Draw":
                            card_draw += 1
                            if card_draw > 7:
                                item.advancement = False

                        pool.append(item)
                else:
                    item = SpireItem(name, self.player)
                    pool.append(item)

        self.world.itempool += pool

        # Pair up our event locations with our event items
        for event, item in event_item_pairs.items():
            event_item = SpireItem(item, self.player)
            self.world.get_location(event, self.player).place_locked_item(event_item)

        if self.world.logic[self.player] != 'no logic':
            self.world.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


    def set_rules(self):
        set_rules(self.world, self.player)

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        return Item(name, item_data.progression, item_data.code, self.player)

    def create_regions(self):
        create_regions(self.world, self.player)

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        for option_name in spire_options:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = int(option.value)
        return slot_data

    def get_filler_item_name(self) -> str:
        return self.world.random.choice(["Card Draw", "Card Draw", "Card Draw", "Relic", "Relic"])


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, None, name, player)
    ret.world = world
    if locations:
        for location in locations:
            loc_id = location_table.get(location, 0)
            location = SpireLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret


class SpireLocation(Location):
    game: str = "Slay the Spire"

    def __init__(self, player: int, name: str, address=None, parent=None):
        super(SpireLocation, self).__init__(player, name, address, parent)
        if address is None:
            self.event = True
            self.locked = True


class SpireItem(Item):
    game = "Slay the Spire"

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(SpireItem, self).__init__(name, item_data.progression, item_data.code, player)
