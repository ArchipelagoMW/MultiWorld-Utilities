
from BaseClasses import MultiWorld, Item
from worlds.AutoWorld import World, CollectionState
from .Items import item_table, create_itempool, create_item
from .Locations import get_location_names
from .Options import Sly1Options
from .Regions import create_regions
from .Types import EpisodeType, episode_type_to_name
from .Rules import set_rules

class Sly1World(World):
    """
    Sly Cooper and the Thievius Raccoonus is a action stealth game.
    Avenge your father and take back the pages from the fiendish five.
    """

    game = "Sly Cooper and the Thievius Raccoonus"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = Sly1Options
    options = Sly1Options

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        
    def generate_early(self):
        starting_espisode = (episode_type_to_name[EpisodeType(self.options.StartingEpisode)])
        print(starting_espisode)
        self.multiworld.push_precollected(self.create_item(starting_espisode))

    def create_regions(self):
        create_regions(self)

        # If needed, can create a boss locations and input a proof of victory item
        # Add them to the correct location here

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)