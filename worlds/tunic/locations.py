from typing import Dict, NamedTuple, Set, Optional


class TunicLocationData(NamedTuple):
    region: str
    er_region: str  # entrance rando region
    ladder_region: Optional[str] = None
    location_group: Optional[str] = None

    def ladders_region(self) -> str:
        return self.ladder_region or self.region


location_base_id = 509342400

location_table: Dict[str, TunicLocationData] = {
    "Beneath the Well - [Powered Secret Room] Chest": TunicLocationData("Beneath the Well", "Beneath the Well Back"),
    "Beneath the Well - [Entryway] Chest": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Third Room] Beneath Platform Chest": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Third Room] Tentacle Chest": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Entryway] Obscured Behind Waterfall": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Save Room] Upper Floor Chest 1": TunicLocationData("Beneath the Well", "Beneath the Well Back"),
    "Beneath the Well - [Save Room] Upper Floor Chest 2": TunicLocationData("Beneath the Well", "Beneath the Well Back"),
    "Beneath the Well - [Second Room] Underwater Chest": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Back Corridor] Right Secret": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Back Corridor] Left Secret": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Second Room] Obscured Behind Waterfall": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Side Room] Chest By Pots": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Beneath the Well - [Side Room] Chest By Phrends": TunicLocationData("Beneath the Well", "Beneath the Well Back"),
    "Beneath the Well - [Second Room] Page": TunicLocationData("Beneath the Well", "Beneath the Well Main"),
    "Dark Tomb Checkpoint - [Passage To Dark Tomb] Page Pickup": TunicLocationData("Overworld", "Dark Tomb Checkpoint"),
    "Cathedral - [1F] Guarded By Lasers": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [1F] Near Spikes": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [2F] Bird Room": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [2F] Entryway Upper Walkway": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [1F] Library": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [2F] Library": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [2F] Guarded By Lasers": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [2F] Bird Room Secret": TunicLocationData("Cathedral", "Cathedral"),
    "Cathedral - [1F] Library Secret": TunicLocationData("Cathedral", "Cathedral"),
    "Dark Tomb - Spike Maze Near Exit": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Dark Tomb - 2nd Laser Room": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Dark Tomb - 1st Laser Room": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Dark Tomb - Spike Maze Upper Walkway": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Dark Tomb - Skulls Chest": TunicLocationData("Dark Tomb", "Dark Tomb Upper", ladder_region="Dark Tomb Front"),
    "Dark Tomb - Spike Maze Near Stairs": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Dark Tomb - 1st Laser Room Obscured": TunicLocationData("Dark Tomb", "Dark Tomb Main"),
    "Guardhouse 2 - Upper Floor": TunicLocationData("East Forest", "Guard House 2 Upper"),
    "Guardhouse 2 - Bottom Floor Secret": TunicLocationData("East Forest", "Guard House 2 Lower", ladder_region="Lower Forest"),
    "Guardhouse 1 - Upper Floor Obscured": TunicLocationData("East Forest", "Guard House 1 East"),
    "Guardhouse 1 - Upper Floor": TunicLocationData("East Forest", "Guard House 1 East"),
    "East Forest - Dancing Fox Spirit Holy Cross": TunicLocationData("East Forest", "East Forest Dance Fox Spot", location_group="holy cross"),
    "East Forest - Golden Obelisk Holy Cross": TunicLocationData("East Forest", "Lower Forest", ladder_region="Lower Forest", location_group="holy cross"),
    "East Forest - Ice Rod Grapple Chest": TunicLocationData("East Forest", "East Forest"),
    "East Forest - Above Save Point": TunicLocationData("East Forest", "East Forest"),
    "East Forest - Above Save Point Obscured": TunicLocationData("East Forest", "East Forest"),
    "East Forest - From Guardhouse 1 Chest": TunicLocationData("East Forest", "East Forest Dance Fox Spot"),
    "East Forest - Near Save Point": TunicLocationData("East Forest", "East Forest"),
    "East Forest - Beneath Spider Chest": TunicLocationData("East Forest", "Lower Forest", ladder_region="Lower Forest"),
    "East Forest - Near Telescope": TunicLocationData("East Forest", "East Forest"),
    "East Forest - Spider Chest": TunicLocationData("East Forest", "Lower Forest", ladder_region="Lower Forest"),
    "East Forest - Lower Dash Chest": TunicLocationData("East Forest", "Lower Forest", ladder_region="Lower Forest"),
    "East Forest - Lower Grapple Chest": TunicLocationData("East Forest", "Lower Forest", ladder_region="Lower Forest"),
    "East Forest - Bombable Wall": TunicLocationData("East Forest", "East Forest"),
    "East Forest - Page On Teleporter": TunicLocationData("East Forest", "East Forest"),
    "Forest Belltower - Near Save Point": TunicLocationData("East Forest", "Forest Belltower Lower"),
    "Forest Belltower - After Guard Captain": TunicLocationData("East Forest", "Forest Belltower Upper"),
    "Forest Belltower - Obscured Near Bell Top Floor": TunicLocationData("East Forest", "Forest Belltower Upper"),
    "Forest Belltower - Obscured Beneath Bell Bottom Floor": TunicLocationData("East Forest", "Forest Belltower Main"),
    "Forest Belltower - Page Pickup": TunicLocationData("East Forest", "Forest Belltower Main"),
    "Forest Grave Path - Holy Cross Code by Grave": TunicLocationData("East Forest", "Forest Grave Path by Grave", location_group="holy cross"),
    "Forest Grave Path - Above Gate": TunicLocationData("East Forest", "Forest Grave Path Main"),
    "Forest Grave Path - Obscured Chest": TunicLocationData("East Forest", "Forest Grave Path Main"),
    "Forest Grave Path - Upper Walkway": TunicLocationData("East Forest", "Forest Grave Path Upper"),
    "Forest Grave Path - Sword Pickup": TunicLocationData("East Forest", "Forest Grave Path by Grave"),
    "Hero's Grave - Tooth Relic": TunicLocationData("East Forest", "Hero Relic - East Forest", location_group="hero relic"),
    "Fortress Courtyard - From East Belltower": TunicLocationData("East Forest", "Fortress Exterior from East Forest"),
    "Fortress Leaf Piles - Secret Chest": TunicLocationData("Eastern Vault Fortress", "Fortress Leaf Piles"),
    "Fortress Arena - Hexagon Red": TunicLocationData("Eastern Vault Fortress", "Fortress Arena"),
    "Fortress Arena - Siege Engine/Vault Key Pickup": TunicLocationData("Eastern Vault Fortress", "Fortress Arena", location_group="bosses"),
    "Fortress East Shortcut - Chest Near Slimes": TunicLocationData("Eastern Vault Fortress", "Fortress East Shortcut Lower"),
    "Eastern Vault Fortress - [West Wing] Candles Holy Cross": TunicLocationData("Eastern Vault Fortress", "Eastern Vault Fortress", location_group="holy cross"),
    "Eastern Vault Fortress - [West Wing] Dark Room Chest 1": TunicLocationData("Eastern Vault Fortress", "Eastern Vault Fortress"),
    "Eastern Vault Fortress - [West Wing] Dark Room Chest 2": TunicLocationData("Eastern Vault Fortress", "Eastern Vault Fortress"),
    "Eastern Vault Fortress - [East Wing] Bombable Wall": TunicLocationData("Eastern Vault Fortress", "Eastern Vault Fortress"),
    "Eastern Vault Fortress - [West Wing] Page Pickup": TunicLocationData("Eastern Vault Fortress", "Eastern Vault Fortress"),
    "Fortress Grave Path - Upper Walkway": TunicLocationData("Eastern Vault Fortress", "Fortress Grave Path Upper"),
    "Fortress Grave Path - Chest Right of Grave": TunicLocationData("Eastern Vault Fortress", "Fortress Grave Path"),
    "Fortress Grave Path - Obscured Chest Left of Grave": TunicLocationData("Eastern Vault Fortress", "Fortress Grave Path"),
    "Hero's Grave - Flowers Relic": TunicLocationData("Eastern Vault Fortress", "Hero Relic - Fortress", location_group="hero relic"),
    "Beneath the Fortress - Bridge": TunicLocationData("Beneath the Vault", "Beneath the Vault Back"),
    "Beneath the Fortress - Cell Chest 1": TunicLocationData("Beneath the Vault", "Beneath the Vault Back"),
    "Beneath the Fortress - Obscured Behind Waterfall": TunicLocationData("Beneath the Vault", "Beneath the Vault Front"),
    "Beneath the Fortress - Back Room Chest": TunicLocationData("Beneath the Vault", "Beneath the Vault Back"),
    "Beneath the Fortress - Cell Chest 2": TunicLocationData("Beneath the Vault", "Beneath the Vault Back"),
    "Frog's Domain - Near Vault": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Slorm Room": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Escape Chest": TunicLocationData("Frog's Domain", "Frog's Domain Back"),
    "Frog's Domain - Grapple Above Hot Tub": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Above Vault": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Main Room Top Floor": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Main Room Bottom Floor": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Side Room Secret Passage": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Side Room Chest": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Side Room Grapple Secret": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Frog's Domain - Magic Orb Pickup": TunicLocationData("Frog's Domain", "Frog's Domain"),
    "Librarian - Hexagon Green": TunicLocationData("Library", "Library Arena", location_group="bosses"),
    "Library Hall - Holy Cross Chest": TunicLocationData("Library", "Library Hall", location_group="holy cross"),
    "Library Lab - Chest By Shrine 2": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Chest By Shrine 1": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Chest By Shrine 3": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Behind Chalkboard by Fuse": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Page 3": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Page 1": TunicLocationData("Library", "Library Lab"),
    "Library Lab - Page 2": TunicLocationData("Library", "Library Lab"),
    "Hero's Grave - Mushroom Relic": TunicLocationData("Library", "Hero Relic - Library", location_group="hero relic"),
    "Lower Mountain - Page Before Door": TunicLocationData("Overworld", "Lower Mountain", ladder_region="Upper Overworld"),
    "Changing Room - Normal Chest": TunicLocationData("Overworld", "Changing Room"),
    "Fortress Courtyard - Chest Near Cave": TunicLocationData("Overworld", "Fortress Exterior near cave", ladder_region="East Overworld"),
    "Fortress Courtyard - Near Fuse": TunicLocationData("Overworld", "Fortress Exterior from Overworld", ladder_region="East Overworld"),
    "Fortress Courtyard - Below Walkway": TunicLocationData("Overworld", "Fortress Exterior from Overworld", ladder_region="East Overworld"),
    "Fortress Courtyard - Page Near Cave": TunicLocationData("Overworld", "Fortress Exterior near cave", ladder_region="East Overworld"),
    "West Furnace - Lantern Pickup": TunicLocationData("Overworld", "Furnace Fuse", ladder_region="Beneath the Well Back"),
    "Maze Cave - Maze Room Chest": TunicLocationData("Overworld", "Maze Cave", ladder_region="Overworld Beach"),
    "Old House - Normal Chest": TunicLocationData("Overworld", "Old House Front"),
    "Old House - Shield Pickup": TunicLocationData("Overworld", "Old House Front"),
    "Overworld - [West] Obscured Behind Windmill": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [South] Beach Chest": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [West] Obscured Near Well": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Central] Bombable Wall": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Chest Near Turret": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [East] Chest Near Pots": TunicLocationData("Overworld", "East Overworld", ladder_region="East Overworld"),
    "Overworld - [Northwest] Chest Near Golden Obelisk": TunicLocationData("Overworld", "Overworld above Quarry Entrance"),
    "Overworld - [Southwest] South Chest Near Guard": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Southwest] West Beach Guarded By Turret": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [Southwest] Chest Guarded By Turret": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Shadowy Corner Chest": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Southwest] Obscured In Tunnel To Beach": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Southwest] Grapple Chest Over Walkway": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Chest Beneath Quarry Gate": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Southeast] Chest Near Swamp": TunicLocationData("Overworld", "Overworld Swamp Lower Entry", ladder_region="Swamp"),
    "Overworld - [Southwest] From West Garden": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [East] Grapple Chest": TunicLocationData("Overworld", "Overworld above Patrol Cave"),
    "Overworld - [Southwest] West Beach Guarded By Turret 2": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [Southwest] Beach Chest Near Flowers": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [Southwest] Bombable Wall Near Fountain": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [West] Chest After Bell": TunicLocationData("Overworld", "Overworld Belltower"),
    "Overworld - [Southwest] Tunnel Guarded By Turret": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [East] Between Ladders Near Ruined Passage": TunicLocationData("Overworld", "After Ruined Passage"),
    "Overworld - [Northeast] Chest Above Patrol Cave": TunicLocationData("Overworld", "Upper Overworld", ladder_region="Upper Overworld"),
    "Overworld - [Southwest] Beach Chest Beneath Guard": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [Central] Chest Across From Well": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Chest Near Quarry Gate": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [East] Chest In Trees": TunicLocationData("Overworld", "Above Ruined Passage"),
    "Overworld - [West] Chest Behind Moss Wall": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [South] Beach Page": TunicLocationData("Overworld", "Overworld Beach", ladder_region="Overworld Beach"),
    "Overworld - [Southeast] Page on Pillar by Swamp": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Southwest] Key Pickup": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [West] Key Pickup": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [East] Page Near Secret Shop": TunicLocationData("Overworld", "East Overworld", ladder_region="East Overworld"),
    "Overworld - [Southwest] Fountain Page": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Page on Pillar by Dark Tomb": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Fire Wand Pickup": TunicLocationData("Overworld", "Upper Overworld", ladder_region="Upper Overworld"),
    "Overworld - [West] Page On Teleporter": TunicLocationData("Overworld", "Overworld"),
    "Overworld - [Northwest] Page By Well": TunicLocationData("Overworld", "Overworld"),
    "Patrol Cave - Normal Chest": TunicLocationData("Overworld", "Patrol Cave"),
    "Ruined Shop - Chest 1": TunicLocationData("Overworld", "Ruined Shop"),
    "Ruined Shop - Chest 2": TunicLocationData("Overworld", "Ruined Shop"),
    "Ruined Shop - Chest 3": TunicLocationData("Overworld", "Ruined Shop"),
    "Ruined Passage - Page Pickup": TunicLocationData("Overworld", "Ruined Passage"),
    "Shop - Potion 1": TunicLocationData("Overworld", "Shop", location_group="shop"),
    "Shop - Potion 2": TunicLocationData("Overworld", "Shop", location_group="shop"),
    "Shop - Coin 1": TunicLocationData("Overworld", "Shop", location_group="shop"),
    "Shop - Coin 2": TunicLocationData("Overworld", "Shop", location_group="shop"),
    "Special Shop - Secret Page Pickup": TunicLocationData("Overworld", "Special Shop", ladder_region="East Overworld"),
    "Stick House - Stick Chest": TunicLocationData("Overworld", "Stick House"),
    "Sealed Temple - Page Pickup": TunicLocationData("Overworld", "Sealed Temple", ladder_region="Sealed Temple"),
    "Hourglass Cave - Hourglass Chest": TunicLocationData("Overworld", "Hourglass Cave", ladder_region="Overworld Beach"),
    "Far Shore - Secret Chest": TunicLocationData("Overworld", "Far Shore"),
    "Far Shore - Page Pickup": TunicLocationData("Overworld", "Far Shore to Spawn Region"),
    "Coins in the Well - 10 Coins": TunicLocationData("Overworld", "Overworld", location_group="well"),
    "Coins in the Well - 15 Coins": TunicLocationData("Overworld", "Overworld", location_group="well"),
    "Coins in the Well - 3 Coins": TunicLocationData("Overworld", "Overworld", location_group="well"),
    "Coins in the Well - 6 Coins": TunicLocationData("Overworld", "Overworld", location_group="well"),
    "Secret Gathering Place - 20 Fairy Reward": TunicLocationData("Overworld", "Secret Gathering Place", location_group="fairies"),
    "Secret Gathering Place - 10 Fairy Reward": TunicLocationData("Overworld", "Secret Gathering Place", location_group="fairies"),
    "Overworld - [West] Moss Wall Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Holy Cross", location_group="holy cross"),
    "Overworld - [Southwest] Flowers Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Beach", ladder_region="Overworld Beach", location_group="holy cross"),
    "Overworld - [Southwest] Fountain Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Holy Cross", location_group="holy cross"),
    "Overworld - [Northeast] Flowers Holy Cross": TunicLocationData("Overworld Holy Cross", "East Overworld", ladder_region="East Overworld", location_group="holy cross"),
    "Overworld - [East] Weathervane Holy Cross": TunicLocationData("Overworld Holy Cross", "East Overworld", ladder_region="East Overworld", location_group="holy cross"),
    "Overworld - [West] Windmill Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Holy Cross", location_group="holy cross"),
    "Overworld - [Southwest] Haiku Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Beach", ladder_region="Overworld Beach", location_group="holy cross"),
    "Overworld - [West] Windchimes Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Holy Cross", location_group="holy cross"),
    "Overworld - [South] Starting Platform Holy Cross": TunicLocationData("Overworld Holy Cross", "Overworld Holy Cross", location_group="holy cross"),
    "Overworld - [Northwest] Golden Obelisk Page": TunicLocationData("Overworld Holy Cross", "Upper Overworld", ladder_region="Upper Overworld", location_group="holy cross"),
    "Old House - Holy Cross Door Page": TunicLocationData("Overworld Holy Cross", "Old House Back", location_group="holy cross"),
    "Cube Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Cube Cave", location_group="holy cross"),
    "Southeast Cross Door - Chest 3": TunicLocationData("Overworld Holy Cross", "Southeast Cross Room", location_group="holy cross"),
    "Southeast Cross Door - Chest 2": TunicLocationData("Overworld Holy Cross", "Southeast Cross Room", location_group="holy cross"),
    "Southeast Cross Door - Chest 1": TunicLocationData("Overworld Holy Cross", "Southeast Cross Room", location_group="holy cross"),
    "Maze Cave - Maze Room Holy Cross": TunicLocationData("Overworld Holy Cross", "Maze Cave", ladder_region="Overworld Beach", location_group="holy cross"),
    "Caustic Light Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Caustic Light Cave", ladder_region="Swamp", location_group="holy cross"),
    "Old House - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Old House Front", location_group="holy cross"),
    "Patrol Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Patrol Cave", location_group="holy cross"),
    "Ruined Passage - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Ruined Passage", ladder_region="Overworld", location_group="holy cross"),
    "Hourglass Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Hourglass Cave Tower", ladder_region="Overworld Beach", location_group="holy cross"),
    "Sealed Temple - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Sealed Temple", ladder_region="Sealed Temple", location_group="holy cross"),
    "Fountain Cross Door - Page Pickup": TunicLocationData("Overworld Holy Cross", "Fountain Cross Room", location_group="holy cross"),
    "Secret Gathering Place - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "Secret Gathering Place", location_group="holy cross"),
    "Top of the Mountain - Page At The Peak": TunicLocationData("Overworld Holy Cross", "Top of the Mountain", ladder_region="Upper Overworld", location_group="holy cross"),
    "Monastery - Monastery Chest": TunicLocationData("Quarry", "Monastery Back"),
    "Quarry - [Back Entrance] Bushes Holy Cross": TunicLocationData("Quarry Back", "Quarry Back", location_group="holy cross"),
    "Quarry - [Back Entrance] Chest": TunicLocationData("Quarry Back", "Quarry Back"),
    "Quarry - [Central] Near Shortcut Ladder": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Near Telescope": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Upper Floor": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [Central] Below Entry Walkway": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Obscured Near Winding Staircase": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Obscured Beneath Scaffolding": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Obscured Near Telescope": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [Back Entrance] Obscured Behind Wall": TunicLocationData("Quarry Back", "Quarry Back"),
    "Quarry - [Central] Obscured Below Entry Walkway": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [Central] Top Floor Overhang": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [East] Near Bridge": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [Central] Above Ladder": TunicLocationData("Quarry", "Quarry Monastery Entry"),
    "Quarry - [Central] Obscured Behind Staircase": TunicLocationData("Quarry", "Quarry"),
    "Quarry - [Central] Above Ladder Dash Chest": TunicLocationData("Quarry", "Quarry Monastery Entry"),
    "Quarry - [West] Upper Area Bombable Wall": TunicLocationData("Quarry Back", "Quarry Back"),
    "Quarry - [East] Bombable Wall": TunicLocationData("Quarry", "Quarry"),
    "Hero's Grave - Ash Relic": TunicLocationData("Quarry", "Hero Relic - Quarry", location_group="hero relics"),
    "Quarry - [West] Shooting Range Secret Path": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Near Shooting Range": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Below Shooting Range": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [Lowlands] Below Broken Ladder": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Upper Area Near Waterfall": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [Lowlands] Upper Walkway": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Lower Area Below Bridge": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Lower Area Isolated Chest": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [Lowlands] Near Elevator": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Quarry - [West] Lower Area After Bridge": TunicLocationData("Lower Quarry", "Lower Quarry"),
    "Rooted Ziggurat Upper - Near Bridge Switch": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Upper Front"),
    "Rooted Ziggurat Upper - Beneath Bridge To Administrator": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Upper Back"),
    "Rooted Ziggurat Tower - Inside Tower": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Middle Top"),
    "Rooted Ziggurat Lower - Near Corpses": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - Spider Ambush": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - Left Of Checkpoint Before Fuse": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - After Guarded Fuse": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - Guarded By Double Turrets": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - After 2nd Double Turret Chest": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - Guarded By Double Turrets 2": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Front"),
    "Rooted Ziggurat Lower - Hexagon Blue": TunicLocationData("Rooted Ziggurat", "Rooted Ziggurat Lower Back", location_group="bosses"),
    "Ruined Atoll - [West] Near Kevin Block": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [South] Upper Floor On Power Line": TunicLocationData("Ruined Atoll", "Ruined Atoll Ladder Tops"),
    "Ruined Atoll - [South] Chest Near Big Crabs": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [North] Guarded By Bird": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Northeast] Chest Beneath Brick Walkway": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Northwest] Bombable Wall": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [North] Obscured Beneath Bridge": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [South] Upper Floor On Bricks": TunicLocationData("Ruined Atoll", "Ruined Atoll Ladder Tops"),
    "Ruined Atoll - [South] Near Birds": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Northwest] Behind Envoy": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Southwest] Obscured Behind Fuse": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [East] Locked Room Upper Chest": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [North] From Lower Overworld Entrance": TunicLocationData("Ruined Atoll", "Ruined Atoll Lower Entry Area"),
    "Ruined Atoll - [East] Locked Room Lower Chest": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Northeast] Chest On Brick Walkway": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Ruined Atoll - [Southeast] Chest Near Fuse": TunicLocationData("Ruined Atoll", "Ruined Atoll Ladder Tops"),
    "Ruined Atoll - [Northeast] Key Pickup": TunicLocationData("Ruined Atoll", "Ruined Atoll"),
    "Cathedral Gauntlet - Gauntlet Reward": TunicLocationData("Swamp", "Cathedral Gauntlet", ladder_region="Back of Swamp"),
    "Cathedral - Secret Legend Trophy Chest": TunicLocationData("Swamp", "Cathedral Secret Legend Room", ladder_region="Swamp Middle"),
    "Swamp - [Upper Graveyard] Obscured Behind Hill": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] 4 Orange Skulls": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Central] Near Ramps Up": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [Upper Graveyard] Near Shield Fleemers": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] Obscured Behind Ridge": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] Obscured Beneath Telescope": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Entrance] Above Entryway": TunicLocationData("Swamp", "Back of Swamp Laurels Area", ladder_region="Back of Swamp"),
    "Swamp - [Central] South Secret Passage": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] Upper Walkway On Pedestal": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [South Graveyard] Guarded By Tentacles": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Upper Graveyard] Near Telescope": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [Outside Cathedral] Near Moonlight Bridge Door": TunicLocationData("Swamp", "Swamp Ledge under Cathedral Door", ladder_region="Swamp Middle"),
    "Swamp - [Entrance] Obscured Inside Watchtower": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Entrance] South Near Fence": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [South Graveyard] Guarded By Big Skeleton": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [South Graveyard] Chest Near Graves": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Entrance] North Small Island": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Outside Cathedral] Obscured Behind Memorial": TunicLocationData("Swamp", "Back of Swamp", ladder_region="Back of Swamp"),
    "Swamp - [Central] Obscured Behind Northern Mountain": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] Upper Walkway Dash Chest": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Swamp - [South Graveyard] Above Big Skeleton": TunicLocationData("Swamp", "Swamp Front"),
    "Swamp - [Central] Beneath Memorial": TunicLocationData("Swamp", "Swamp Mid", ladder_region="Swamp Middle"),
    "Hero's Grave - Feathers Relic": TunicLocationData("Swamp", "Hero Relic - Swamp", location_group="hero relic"),
    "West Furnace - Chest": TunicLocationData("West Garden", "Furnace Walking Path"),
    "Overworld - [West] Near West Garden Entrance": TunicLocationData("West Garden", "Overworld to West Garden from Furnace"),
    "West Garden - [Central Highlands] Holy Cross (Blue Lines)": TunicLocationData("West Garden", "West Garden", location_group="holy cross"),
    "West Garden - [West Lowlands] Tree Holy Cross Chest": TunicLocationData("West Garden", "West Garden", location_group="holy cross"),
    "West Garden - [Southeast Lowlands] Outside Cave": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Lowlands] Chest Beneath Faeries": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [North] Behind Holy Cross Door": TunicLocationData("West Garden", "West Garden", location_group="holy cross"),
    "West Garden - [Central Highlands] Top of Ladder Before Boss": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Lowlands] Passage Beneath Bridge": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [North] Across From Page Pickup": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Lowlands] Below Left Walkway": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [West] In Flooded Walkway": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [West] Past Flooded Walkway": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [North] Obscured Beneath Hero's Memorial": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Lowlands] Chest Near Shortcut Bridge": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [West Highlands] Upper Left Walkway": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Lowlands] Chest Beneath Save Point": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Highlands] Behind Guard Captain": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [Central Highlands] After Garden Knight": TunicLocationData("Overworld", "West Garden after Boss", location_group="bosses"),
    "West Garden - [South Highlands] Secret Chest Beneath Fuse": TunicLocationData("West Garden", "West Garden"),
    "West Garden - [East Lowlands] Page Behind Ice Dagger House": TunicLocationData("West Garden", "West Garden Portal Item"),
    "West Garden - [North] Page Pickup": TunicLocationData("West Garden", "West Garden"),
    "West Garden House - [Southeast Lowlands] Ice Dagger Pickup": TunicLocationData("West Garden", "Magic Dagger House"),
    "Hero's Grave - Effigy Relic": TunicLocationData("West Garden", "Hero Relic - West Garden", location_group="hero relic"),
}

hexagon_locations: Dict[str, str] = {
    "Red Questagon": "Fortress Arena - Siege Engine/Vault Key Pickup",
    "Green Questagon": "Librarian - Hexagon Green",
    "Blue Questagon": "Rooted Ziggurat Lower - Hexagon Blue",
}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        if loc_data.location_group not in location_name_groups.keys():
            location_name_groups[loc_data.location_group] = set()
        location_name_groups[loc_data.location_group].add(loc_name)
