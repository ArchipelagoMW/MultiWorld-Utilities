from typing import Dict, NamedTuple, List, Tuple
from enum import IntEnum


class Portal(NamedTuple):
    name: str  # human-readable name
    region: str  # AP region
    destination: str  # vanilla destination scene and tag

    def scene(self) -> str:  # the actual scene name in Tunic
        return tunic_er_regions[self.region].game_scene

    def scene_destination(self) -> str:  # full, nonchanging name to interpret by the mod
        return self.scene() + ", " + self.destination


portal_mapping: List[Portal] = [
    Portal(name="Stick House Entrance", region="Overworld",
           destination="Sword Cave_"),
    Portal(name="Windmill Entrance", region="Overworld",
           destination="Windmill_"),
    Portal(name="Well Ladder Entrance", region="Overworld Well Ladder",
           destination="Sewer_entrance"),
    Portal(name="Entrance to Well from Well Rail", region="Overworld Well to Furnace Rail",
           destination="Sewer_west_aqueduct"),
    Portal(name="Old House Door Entrance", region="Overworld Old House Door",
           destination="Overworld Interiors_house"),
    Portal(name="Old House Waterfall Entrance", region="Overworld",
           destination="Overworld Interiors_under_checkpoint"),
    Portal(name="Entrance to Furnace from Well Rail", region="Overworld Well to Furnace Rail",
           destination="Furnace_gyro_upper_north"),
    Portal(name="Entrance to Furnace under Windmill", region="Overworld",
           destination="Furnace_gyro_upper_east"),
    Portal(name="Entrance to Furnace near West Garden", region="Overworld to West Garden from Furnace",
           destination="Furnace_gyro_west"),
    Portal(name="Entrance to Furnace from Beach", region="Overworld",
           destination="Furnace_gyro_lower"),
    Portal(name="Caustic Light Cave Entrance", region="Overworld Swamp Lower Entry",
           destination="Overworld Cave_"),
    Portal(name="Swamp Upper Entrance", region="Overworld Swamp Upper Entry",
           destination="Swamp Redux 2_wall"),
    Portal(name="Swamp Lower Entrance", region="Overworld Swamp Lower Entry",
           destination="Swamp Redux 2_conduit"),
    Portal(name="Ruined Passage Not-Door Entrance", region="After Ruined Passage",
           destination="Ruins Passage_east"),
    Portal(name="Ruined Passage Door Entrance", region="Overworld Ruined Passage Door",
           destination="Ruins Passage_west"),
    Portal(name="Atoll Upper Entrance", region="Overworld to Atoll Upper",
           destination="Atoll Redux_upper"),
    Portal(name="Atoll Lower Entrance", region="Overworld Beach",
           destination="Atoll Redux_lower"),
    Portal(name="Special Shop Entrance", region="Overworld Special Shop Entry",
           destination="ShopSpecial_"),
    Portal(name="Maze Cave Entrance", region="Overworld Beach",
           destination="Maze Room_"),
    Portal(name="West Garden Entrance near Belltower", region="Overworld to West Garden Upper",
           destination="Archipelagos Redux_upper"),
    Portal(name="West Garden Entrance from Furnace", region="Overworld to West Garden from Furnace",
           destination="Archipelagos Redux_lower"),
    Portal(name="West Garden Laurels Entrance", region="Overworld West Garden Laurels Entry",
           destination="Archipelagos Redux_lowest"),
    Portal(name="Temple Door Entrance", region="Overworld Temple Door",
           destination="Temple_main"),
    Portal(name="Temple Rafters Entrance", region="Upper Overworld",
           destination="Temple_rafters"),
    Portal(name="Ruined Shop Entrance", region="Overworld",
           destination="Ruined Shop_"),
    Portal(name="Patrol Cave Entrance", region="Overworld at Patrol Cave",
           destination="PatrolCave_"),
    Portal(name="Hourglass Cave Entrance", region="Overworld Beach",
           destination="Town Basement_beach"),
    Portal(name="Changing Room Entrance", region="Overworld",
           destination="Changing Room_"),
    Portal(name="Cube Cave Entrance", region="Overworld",
           destination="CubeRoom_"),
    Portal(name="Stairs from Overworld to Mountain", region="Upper Overworld",
           destination="Mountain_"),
    Portal(name="Overworld to Fortress", region="East Overworld",
           destination="Fortress Courtyard_"),
    Portal(name="Fountain HC Door Entrance", region="Overworld Fountain Cross Door",
           destination="Town_FiligreeRoom_"),
    Portal(name="Southeast HC Door Entrance", region="Overworld Southeast Cross Door",
           destination="EastFiligreeCache_"),
    Portal(name="Overworld to Quarry Connector", region="Overworld Quarry Entry",
           destination="Darkwoods Tunnel_"),
    Portal(name="Dark Tomb Main Entrance", region="Overworld",
           destination="Crypt Redux_"),
    Portal(name="Overworld to Forest Belltower", region="East Overworld",
           destination="Forest Belltower_"),
    Portal(name="Town to Far Shore", region="Overworld Town Portal",
           destination="Transit_teleporter_town"),
    Portal(name="Spawn to Far Shore", region="Overworld Spawn Portal",
           destination="Transit_teleporter_starting island"),
    Portal(name="Secret Gathering Place Entrance", region="Overworld",
           destination="Waterfall_"),
    
    Portal(name="Secret Gathering Place Exit", region="Secret Gathering Place",
           destination="Overworld Redux_"),
    
    Portal(name="Windmill Exit", region="Windmill",
           destination="Overworld Redux_"),
    Portal(name="Windmill Shop", region="Windmill",
           destination="Shop_"),
    
    Portal(name="Old House Door Exit", region="Old House Front",
           destination="Overworld Redux_house"),
    Portal(name="Old House to Glyph Tower", region="Old House Front",
           destination="g_elements_"),
    Portal(name="Old House Waterfall Exit", region="Old House Back",
           destination="Overworld Redux_under_checkpoint"),
    
    Portal(name="Glyph Tower Exit", region="Relic Tower",
           destination="Overworld Interiors_"),
    
    Portal(name="Changing Room Exit", region="Changing Room",
           destination="Overworld Redux_"),
    
    Portal(name="Fountain HC Room Exit", region="Fountain Cross Room",
           destination="Overworld Redux_"),
    
    Portal(name="Cube Cave Exit", region="Cube Cave",
           destination="Overworld Redux_"),
    
    Portal(name="Guard Patrol Cave Exit", region="Patrol Cave",
           destination="Overworld Redux_"),
    
    Portal(name="Ruined Shop Exit", region="Ruined Shop",
           destination="Overworld Redux_"),
    
    Portal(name="Furnace Exit towards Well", region="Furnace Fuse",
           destination="Overworld Redux_gyro_upper_north"),
    Portal(name="Furnace Exit to Dark Tomb", region="Furnace Walking Path",
           destination="Crypt Redux_"),
    Portal(name="Furnace Exit towards West Garden", region="Furnace Walking Path",
           destination="Overworld Redux_gyro_west"),
    Portal(name="Furnace Exit to Beach", region="Furnace Ladder Area",
           destination="Overworld Redux_gyro_lower"),
    Portal(name="Furnace Exit under Windmill", region="Furnace Ladder Area",
           destination="Overworld Redux_gyro_upper_east"),
    
    Portal(name="Stick House Exit", region="Stick House",
           destination="Overworld Redux_"),
    
    Portal(name="Ruined Passage Not-Door Exit", region="Ruined Passage",
           destination="Overworld Redux_east"),
    Portal(name="Ruined Passage Door Exit", region="Ruined Passage",
           destination="Overworld Redux_west"),
    
    Portal(name="Southeast HC Room Exit", region="Southeast Cross Room",
           destination="Overworld Redux_"),
    
    Portal(name="Caustic Light Cave Exit", region="Caustic Light Cave",
           destination="Overworld Redux_"),
    
    Portal(name="Maze Cave Exit", region="Maze Cave",
           destination="Overworld Redux_"),
    
    Portal(name="Hourglass Cave Exit", region="Hourglass Cave",
           destination="Overworld Redux_beach"),
    
    Portal(name="Special Shop Exit", region="Special Shop",
           destination="Overworld Redux_"),
    
    Portal(name="Temple Rafters Exit", region="Sealed Temple Rafters",
           destination="Overworld Redux_rafters"),
    Portal(name="Temple Door Exit", region="Sealed Temple",
           destination="Overworld Redux_main"),
    
    Portal(name="Well Ladder Exit", region="Beneath the Well Ladder Exit",
           destination="Overworld Redux_entrance"),
    Portal(name="Well to Well Boss", region="Beneath the Well Back",
           destination="Sewer_Boss_"),
    Portal(name="Well Exit towards Furnace", region="Beneath the Well Back",
           destination="Overworld Redux_west_aqueduct"),
    
    Portal(name="Well Boss to Well", region="Well Boss",
           destination="Sewer_"),
    Portal(name="Checkpoint to Dark Tomb", region="Dark Tomb Checkpoint",
           destination="Crypt Redux_"),
    
    Portal(name="Dark Tomb to Overworld", region="Dark Tomb Entry Point",
           destination="Overworld Redux_"),
    Portal(name="Dark Tomb to Furnace", region="Dark Tomb Dark Exit",
           destination="Furnace_"),
    Portal(name="Dark Tomb to Checkpoint", region="Dark Tomb Entry Point",
           destination="Sewer_Boss_"),
    
    Portal(name="West Garden Exit near Hero's Grave", region="West Garden",
           destination="Overworld Redux_lower"),
    Portal(name="West Garden to Magic Dagger House", region="West Garden",
           destination="archipelagos_house_"),
    Portal(name="West Garden Exit after Boss", region="West Garden after Boss",
           destination="Overworld Redux_upper"),
    Portal(name="West Garden Shop", region="West Garden",
           destination="Shop_"),
    Portal(name="West Garden Laurels Exit", region="West Garden Laurels Exit Region",
           destination="Overworld Redux_lowest"),
    Portal(name="West Garden Hero's Grave", region="West Garden Hero's Grave Region",
           destination="RelicVoid_teleporter_relic plinth"),
    Portal(name="West Garden to Far Shore", region="West Garden Portal",
           destination="Transit_teleporter_archipelagos_teleporter"),
    
    Portal(name="Magic Dagger House Exit", region="Magic Dagger House",
           destination="Archipelagos Redux_"),
    
    Portal(name="Atoll Upper Exit", region="Ruined Atoll",
           destination="Overworld Redux_upper"),
    Portal(name="Atoll Lower Exit", region="Ruined Atoll Lower Entry Area",
           destination="Overworld Redux_lower"),
    Portal(name="Atoll Shop", region="Ruined Atoll",
           destination="Shop_"),
    Portal(name="Atoll to Far Shore", region="Ruined Atoll Portal",
           destination="Transit_teleporter_atoll"),
    Portal(name="Atoll Statue Teleporter", region="Ruined Atoll Statue",
           destination="Library Exterior_"),
    Portal(name="Frog Stairs Eye Entrance", region="Ruined Atoll Frog Eye",
           destination="Frog Stairs_eye"),
    Portal(name="Frog Stairs Mouth Entrance", region="Ruined Atoll Frog Mouth",
           destination="Frog Stairs_mouth"),
    
    Portal(name="Frog Stairs Eye Exit", region="Frog Stairs Eye Exit",
           destination="Atoll Redux_eye"),
    Portal(name="Frog Stairs Mouth Exit", region="Frog Stairs Upper",
           destination="Atoll Redux_mouth"),
    Portal(name="Frog Stairs to Frog's Domain's Entrance", region="Frog Stairs to Frog's Domain",
           destination="frog cave main_Entrance"),
    Portal(name="Frog Stairs to Frog's Domain's Exit", region="Frog Stairs Lower",
           destination="frog cave main_Exit"),
    
    Portal(name="Frog's Domain Ladder Exit", region="Frog's Domain",
           destination="Frog Stairs_Entrance"),
    Portal(name="Frog's Domain Orb Exit", region="Frog's Domain Back",
           destination="Frog Stairs_Exit"),
    
    Portal(name="Library Exterior Tree", region="Library Exterior Tree Region",
           destination="Atoll Redux_"),
    Portal(name="Library Exterior Ladder", region="Library Exterior Ladder Region",
           destination="Library Hall_"),
    
    Portal(name="Library Hall Bookshelf Exit", region="Library Hall",
           destination="Library Exterior_"),
    Portal(name="Library Hero's Grave", region="Library Hero's Grave Region",
           destination="RelicVoid_teleporter_relic plinth"),
    Portal(name="Library Hall to Rotunda", region="Library Hall",
           destination="Library Rotunda_"),
    
    Portal(name="Library Rotunda Lower Exit", region="Library Rotunda",
           destination="Library Hall_"),
    Portal(name="Library Rotunda Upper Exit", region="Library Rotunda",
           destination="Library Lab_"),
    
    Portal(name="Library Lab to Rotunda", region="Library Lab Lower",
           destination="Library Rotunda_"),
    Portal(name="Library to Far Shore", region="Library Portal",
           destination="Transit_teleporter_library teleporter"),
    Portal(name="Library Lab to Librarian Arena", region="Library Lab",
           destination="Library Arena_"),
    
    Portal(name="Librarian Arena Exit", region="Library Arena",
           destination="Library Lab_"),
    
    Portal(name="Forest to Belltower", region="East Forest",
           destination="Forest Belltower_"),
    Portal(name="Forest Guard House 1 Lower Entrance", region="East Forest",
           destination="East Forest Redux Laddercave_lower"),
    Portal(name="Forest Guard House 1 Gate Entrance", region="East Forest",
           destination="East Forest Redux Laddercave_gate"),
    Portal(name="Forest Dance Fox Outside Doorway", region="East Forest Dance Fox Spot",
           destination="East Forest Redux Laddercave_upper"),
    Portal(name="Forest to Far Shore", region="East Forest Portal",
           destination="Transit_teleporter_forest teleporter"),
    Portal(name="Forest Guard House 2 Lower Entrance", region="Lower Forest",
           destination="East Forest Redux Interior_lower"),
    Portal(name="Forest Guard House 2 Upper Entrance", region="East Forest",
           destination="East Forest Redux Interior_upper"),
    Portal(name="Forest Grave Path Lower Entrance", region="East Forest",
           destination="Sword Access_lower"),
    Portal(name="Forest Grave Path Upper Entrance", region="East Forest",
           destination="Sword Access_upper"),
    
    Portal(name="Guard House 1 Dance Fox Exit", region="Guard House 1 West",
           destination="East Forest Redux_upper"),
    Portal(name="Guard House 1 Lower Exit", region="Guard House 1 West",
           destination="East Forest Redux_lower"),
    Portal(name="Guard House 1 Upper Forest Exit", region="Guard House 1 East",
           destination="East Forest Redux_gate"),
    Portal(name="Guard House 1 to Guard Captain Room", region="Guard House 1 East",
           destination="Forest Boss Room_"),
    
    Portal(name="Forest Grave Path Upper Exit", region="Forest Grave Path Upper",
           destination="East Forest Redux_upper"),
    Portal(name="Forest Grave Path Lower Exit", region="Forest Grave Path Main",
           destination="East Forest Redux_lower"),
    Portal(name="East Forest Hero's Grave", region="Forest Hero's Grave",
           destination="RelicVoid_teleporter_relic plinth"),
    
    Portal(name="Guard House 2 Lower Exit", region="Guard House 2 Lower",
           destination="East Forest Redux_lower"),
    Portal(name="Guard House 2 Upper Exit", region="Guard House 2 Upper",
           destination="East Forest Redux_upper"),
    
    Portal(name="Guard Captain Room Non-Gate Exit", region="Forest Boss Room",
           destination="East Forest Redux Laddercave_"),
    Portal(name="Guard Captain Room Gate Exit", region="Forest Boss Room",
           destination="Forest Belltower_"),
    
    Portal(name="Forest Belltower to Fortress", region="Forest Belltower Main",
           destination="Fortress Courtyard_"),
    Portal(name="Forest Belltower to Forest", region="Forest Belltower Lower",
           destination="East Forest Redux_"),
    Portal(name="Forest Belltower to Overworld", region="Forest Belltower Main",
           destination="Overworld Redux_"),
    Portal(name="Forest Belltower to Guard Captain Room", region="Forest Belltower Upper",
           destination="Forest Boss Room_"),
    
    Portal(name="Fortress Courtyard to Fortress Grave Path Lower", region="Fortress Courtyard",
           destination="Fortress Reliquary_Lower"),
    Portal(name="Fortress Courtyard to Fortress Grave Path Upper", region="Fortress Courtyard Upper",
           destination="Fortress Reliquary_Upper"),
    Portal(name="Fortress Courtyard to Fortress Interior", region="Fortress Courtyard",
           destination="Fortress Main_Big Door"),
    Portal(name="Fortress Courtyard to East Fortress", region="Fortress Courtyard Upper",
           destination="Fortress East_"),
    Portal(name="Fortress Courtyard to Beneath the Earth", region="Fortress Exterior near cave",
           destination="Fortress Basement_"),
    Portal(name="Fortress Courtyard to Forest Belltower", region="Fortress Exterior from East Forest",
           destination="Forest Belltower_"),
    Portal(name="Fortress Courtyard to Overworld", region="Fortress Exterior from Overworld",
           destination="Overworld Redux_"),
    Portal(name="Fortress Courtyard Shop", region="Fortress Exterior near cave",
           destination="Shop_"),
    
    Portal(name="Beneath the Earth to Fortress Interior", region="Beneath the Vault Back",
           destination="Fortress Main_"),
    Portal(name="Beneath the Earth to Fortress Courtyard", region="Beneath the Vault Front",
           destination="Fortress Courtyard_"),
    
    Portal(name="Fortress Interior Main Exit", region="Eastern Vault Fortress",
           destination="Fortress Courtyard_Big Door"),
    Portal(name="Fortress Interior to Beneath the Earth", region="Eastern Vault Fortress",
           destination="Fortress Basement_"),
    Portal(name="Fortress Interior to Siege Engine Arena", region="Eastern Vault Fortress Gold Door",
           destination="Fortress Arena_"),
    Portal(name="Fortress Interior Shop", region="Eastern Vault Fortress",
           destination="Shop_"),
    Portal(name="Fortress Interior to East Fortress Upper", region="Eastern Vault Fortress",
           destination="Fortress East_upper"),
    Portal(name="Fortress Interior to East Fortress Lower", region="Eastern Vault Fortress",
           destination="Fortress East_lower"),
    
    Portal(name="East Fortress to Interior Lower", region="Fortress East Shortcut Lower",
           destination="Fortress Main_lower"),
    Portal(name="East Fortress to Courtyard", region="Fortress East Shortcut Upper",
           destination="Fortress Courtyard_"),
    Portal(name="East Fortress to Interior Upper", region="Fortress East Shortcut Upper",
           destination="Fortress Main_upper"),
    
    Portal(name="Fortress Grave Path Lower Exit", region="Fortress Grave Path",
           destination="Fortress Courtyard_Lower"),
    Portal(name="Fortress Hero's Grave", region="Fortress Hero's Grave Region",
           destination="RelicVoid_teleporter_relic plinth"),
    Portal(name="Fortress Grave Path Upper Exit", region="Fortress Grave Path Upper",
           destination="Fortress Courtyard_Upper"),
    Portal(name="Fortress Grave Path Dusty Entrance", region="Fortress Grave Path Dusty Entrance Region",
           destination="Dusty_"),

    Portal(name="Dusty Exit", region="Fortress Leaf Piles",
           destination="Fortress Reliquary_"),
    
    Portal(name="Siege Engine Arena to Fortress", region="Fortress Arena",
           destination="Fortress Main_"),
    Portal(name="Fortress to Far Shore", region="Fortress Arena Portal",
           destination="Transit_teleporter_spidertank"),
    
    Portal(name="Stairs to Top of the Mountain", region="Lower Mountain Stairs",
           destination="Mountaintop_"),
    Portal(name="Mountain to Quarry", region="Lower Mountain",
           destination="Quarry Redux_"),
    Portal(name="Mountain to Overworld", region="Lower Mountain",
           destination="Overworld Redux_"),
    
    Portal(name="Top of the Mountain Exit", region="Top of the Mountain",
           destination="Mountain_"),
    
    Portal(name="Quarry Connector to Overworld", region="Quarry Connector",
           destination="Overworld Redux_"),
    Portal(name="Quarry Connector to Quarry", region="Quarry Connector",
           destination="Quarry Redux_"),
    
    Portal(name="Quarry to Overworld Exit", region="Quarry Entry",
           destination="Darkwoods Tunnel_"),
    Portal(name="Quarry Shop", region="Quarry Entry",
           destination="Shop_"),
    Portal(name="Quarry to Monastery Front", region="Quarry Monastery Entry",
           destination="Monastery_front"),
    Portal(name="Quarry to Monastery Back", region="Monastery Rope",
           destination="Monastery_back"),
    Portal(name="Quarry to Mountain", region="Quarry Back",
           destination="Mountain_"),
    Portal(name="Quarry to Ziggurat", region="Lower Quarry Zig Door",
           destination="ziggurat2020_0_"),
    Portal(name="Quarry to Far Shore", region="Quarry Portal",
           destination="Transit_teleporter_quarry teleporter"),
    
    Portal(name="Monastery Rear Exit", region="Monastery Back",
           destination="Quarry Redux_back"),
    Portal(name="Monastery Front Exit", region="Monastery Front",
           destination="Quarry Redux_front"),
    Portal(name="Monastery Hero's Grave", region="Monastery Hero's Grave Region",
           destination="RelicVoid_teleporter_relic plinth"),
    
    Portal(name="Ziggurat Entry Hallway to Ziggurat Upper", region="Rooted Ziggurat Entry",
           destination="ziggurat2020_1_"),
    Portal(name="Ziggurat Entry Hallway to Quarry", region="Rooted Ziggurat Entry",
           destination="Quarry Redux_"),
    
    Portal(name="Ziggurat Upper to Ziggurat Entry Hallway", region="Rooted Ziggurat Upper Entry",
           destination="ziggurat2020_0_"),
    Portal(name="Ziggurat Upper to Ziggurat Tower", region="Rooted Ziggurat Upper Back",
           destination="ziggurat2020_2_"),
    
    Portal(name="Ziggurat Tower to Ziggurat Upper", region="Rooted Ziggurat Middle Top",
           destination="ziggurat2020_1_"),
    Portal(name="Ziggurat Tower to Ziggurat Lower", region="Rooted Ziggurat Middle Bottom",
           destination="ziggurat2020_3_"),
    
    Portal(name="Ziggurat Lower to Ziggurat Tower", region="Rooted Ziggurat Lower Front",
           destination="ziggurat2020_2_"),
    Portal(name="Ziggurat Portal Room Entrance", region="Rooted Ziggurat Portal Room Entrance",
           destination="ziggurat2020_FTRoom_"),
    
    Portal(name="Ziggurat Portal Room Exit", region="Rooted Ziggurat Portal Room Exit",
           destination="ziggurat2020_3_"),
    Portal(name="Ziggurat to Far Shore", region="Rooted Ziggurat Portal",
           destination="Transit_teleporter_ziggurat teleporter"),
    
    Portal(name="Swamp Lower Exit", region="Swamp Front",
           destination="Overworld Redux_conduit"),
    Portal(name="Swamp to Cathedral Main Entrance", region="Swamp to Cathedral Main Entrance Region",
           destination="Cathedral Redux_main"),
    Portal(name="Swamp to Cathedral Secret Legend Room Entrance", region="Swamp to Cathedral Treasure Room",
           destination="Cathedral Redux_secret"),
    Portal(name="Swamp to Gauntlet", region="Back of Swamp",
           destination="Cathedral Arena_"),
    Portal(name="Swamp Shop", region="Swamp Front",
           destination="Shop_"),
    Portal(name="Swamp Upper Exit", region="Back of Swamp Laurels Area",
           destination="Overworld Redux_wall"),
    Portal(name="Swamp Hero's Grave", region="Swamp Hero's Grave Region",
           destination="RelicVoid_teleporter_relic plinth"),
    
    Portal(name="Cathedral Main Exit", region="Cathedral",
           destination="Swamp Redux 2_main"),
    Portal(name="Cathedral Elevator", region="Cathedral",
           destination="Cathedral Arena_"),
    Portal(name="Cathedral Secret Legend Room Exit", region="Cathedral Secret Legend Room",
           destination="Swamp Redux 2_secret"),
    
    Portal(name="Gauntlet to Swamp", region="Cathedral Gauntlet Exit",
           destination="Swamp Redux 2_"),
    Portal(name="Gauntlet Elevator", region="Cathedral Gauntlet Checkpoint",
           destination="Cathedral Redux_"),
    Portal(name="Gauntlet Shop", region="Cathedral Gauntlet Checkpoint",
           destination="Shop_"),
    
    Portal(name="Hero's Grave to Fortress", region="Hero Relic - Fortress",
           destination="Fortress Reliquary_teleporter_relic plinth"),
    Portal(name="Hero's Grave to Monastery", region="Hero Relic - Quarry",
           destination="Monastery_teleporter_relic plinth"),
    Portal(name="Hero's Grave to West Garden", region="Hero Relic - West Garden",
           destination="Archipelagos Redux_teleporter_relic plinth"),
    Portal(name="Hero's Grave to East Forest", region="Hero Relic - East Forest",
           destination="Sword Access_teleporter_relic plinth"),
    Portal(name="Hero's Grave to Library", region="Hero Relic - Library",
           destination="Library Hall_teleporter_relic plinth"),
    Portal(name="Hero's Grave to Swamp", region="Hero Relic - Swamp",
           destination="Swamp Redux 2_teleporter_relic plinth"),
    
    Portal(name="Far Shore to West Garden", region="Far Shore to West Garden Region",
           destination="Archipelagos Redux_teleporter_archipelagos_teleporter"),
    Portal(name="Far Shore to Library", region="Far Shore to Library Region",
           destination="Library Lab_teleporter_library teleporter"),
    Portal(name="Far Shore to Quarry", region="Far Shore to Quarry Region",
           destination="Quarry Redux_teleporter_quarry teleporter"),
    Portal(name="Far Shore to East Forest", region="Far Shore to East Forest Region",
           destination="East Forest Redux_teleporter_forest teleporter"),
    Portal(name="Far Shore to Fortress", region="Far Shore to Fortress Region",
           destination="Fortress Arena_teleporter_spidertank"),
    Portal(name="Far Shore to Atoll", region="Far Shore",
           destination="Atoll Redux_teleporter_atoll"),
    Portal(name="Far Shore to Ziggurat", region="Far Shore",
           destination="ziggurat2020_FTRoom_teleporter_ziggurat teleporter"),
    Portal(name="Far Shore to Heir", region="Far Shore",
           destination="Spirit Arena_teleporter_spirit arena"),
    Portal(name="Far Shore to Town", region="Far Shore",
           destination="Overworld Redux_teleporter_town"),
    Portal(name="Far Shore to Spawn", region="Far Shore to Spawn Region",
           destination="Overworld Redux_teleporter_starting island"),
    
    Portal(name="Heir Arena Exit", region="Spirit Arena",
           destination="Transit_teleporter_spirit arena"),
    
    Portal(name="Purgatory Bottom Exit", region="Purgatory",
           destination="Purgatory_bottom"),
    Portal(name="Purgatory Top Exit", region="Purgatory",
           destination="Purgatory_top"),
]


class RegionInfo(NamedTuple):
    game_scene: str  # the name of the scene in the actual game
    dead_end: int = 0  # if a region has only one exit
    hint: int = 0  # what kind of hint text you should have


class DeadEnd(IntEnum):
    free = 0  # not a dead end
    all_cats = 1  # dead end in every logic category
    restricted = 2  # dead end only in restricted
    # there's no dead ends that are only in unrestricted


# key is the AP region name. "Fake" in region info just means the mod won't receive that info at all
tunic_er_regions: Dict[str, RegionInfo] = {
    "Menu": RegionInfo("Fake", dead_end=DeadEnd.all_cats),
    "Overworld": RegionInfo("Overworld Redux"),
    "Overworld Holy Cross": RegionInfo("Fake", dead_end=DeadEnd.all_cats),
    "Overworld Belltower": RegionInfo("Overworld Redux"),  # the area with the belltower and chest
    "Overworld Belltower at Bell": RegionInfo("Overworld Redux"),  # the belltower itself, being able to ring it
    "Overworld Swamp Upper Entry": RegionInfo("Overworld Redux"),  # upper swamp entry spot
    "Overworld Swamp Lower Entry": RegionInfo("Overworld Redux"),  # lower swamp entrance, rotating lights
    "After Ruined Passage": RegionInfo("Overworld Redux"),  # just the door and chest
    "Above Ruined Passage": RegionInfo("Overworld Redux"),  # one ladder up, just the chest in the trees
    "East Overworld": RegionInfo("Overworld Redux"),  # where the east forest and fortress entrances are
    "Overworld Special Shop Entry": RegionInfo("Overworld Redux"),  # special shop entry spot
    "Upper Overworld": RegionInfo("Overworld Redux"),  # where the mountain stairs are
    "Overworld above Quarry Entrance": RegionInfo("Overworld Redux"),  # top of the ladder where the chest is
    "Overworld after Temple Rafters": RegionInfo("Overworld Redux"),  # the ledge after the rafter exit, before ladder
    "Overworld Quarry Entry": RegionInfo("Overworld Redux"),  # at the top of the ladder to darkwoods
    "Overworld above Patrol Cave": RegionInfo("Overworld Redux"),  # where the hook is, and one ladder up from patrol
    "Overworld at Patrol Cave": RegionInfo("Overworld Redux"),  # right at the patrol cave entrance
    "Overworld West Garden Laurels Entry": RegionInfo("Overworld Redux"),  # west garden laurels entry
    "Overworld to West Garden Upper": RegionInfo("Overworld Redux"),  # usually leads to garden knight
    "Overworld to West Garden from Furnace": RegionInfo("Overworld Redux"),
    "Overworld Well Ladder": RegionInfo("Overworld Redux"),  # just the ladder entrance
    "Overworld Beach": RegionInfo("Overworld Redux"),
    "Overworld to Atoll Upper": RegionInfo("Overworld Redux"),
    "Overworld Well to Furnace Rail": RegionInfo("Overworld Redux"),  # the tiny rail passageway
    "Overworld Ruined Passage Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Old House Door": RegionInfo("Overworld Redux"),  # the too-small space between the door and the portal
    "Overworld Southeast Cross Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Fountain Cross Door": RegionInfo("Overworld Redux"),
    "Overworld Temple Door": RegionInfo("Overworld Redux"),  # the small space betweeen the door and the portal
    "Overworld Town Portal": RegionInfo("Overworld Redux"),
    "Overworld Spawn Portal": RegionInfo("Overworld Redux"),
    "Stick House": RegionInfo("Sword Cave", dead_end=DeadEnd.all_cats),
    "Windmill": RegionInfo("Windmill"),
    "Old House Back": RegionInfo("Overworld Interiors"),  # part with the hc door
    "Old House Front": RegionInfo("Overworld Interiors"),  # part with the bedroom
    "Relic Tower": RegionInfo("g_elements", dead_end=DeadEnd.all_cats),
    "Furnace Fuse": RegionInfo("Furnace"),  # top of the furnace
    "Furnace Ladder Area": RegionInfo("Furnace"),  # the two portals accessible by the ladder
    "Furnace Walking Path": RegionInfo("Furnace"),  # dark tomb to west garden
    "Secret Gathering Place": RegionInfo("Waterfall", dead_end=DeadEnd.all_cats),
    "Changing Room": RegionInfo("Changing Room", dead_end=DeadEnd.all_cats),
    "Patrol Cave": RegionInfo("PatrolCave", dead_end=DeadEnd.all_cats),
    "Ruined Shop": RegionInfo("Ruined Shop", dead_end=DeadEnd.all_cats),
    "Ruined Passage": RegionInfo("Ruins Passage"),
    "Special Shop": RegionInfo("ShopSpecial", dead_end=DeadEnd.all_cats),
    "Caustic Light Cave": RegionInfo("Overworld Cave", dead_end=DeadEnd.all_cats),
    "Maze Cave": RegionInfo("Maze Room", dead_end=DeadEnd.all_cats),
    "Cube Cave": RegionInfo("CubeRoom", dead_end=DeadEnd.all_cats),
    "Southeast Cross Room": RegionInfo("EastFiligreeCache", dead_end=DeadEnd.all_cats),
    "Fountain Cross Room": RegionInfo("Town_FiligreeRoom", dead_end=DeadEnd.all_cats),
    "Hourglass Cave": RegionInfo("Town Basement", dead_end=DeadEnd.all_cats),
    "Hourglass Cave Tower": RegionInfo("Town Basement", dead_end=DeadEnd.all_cats),  # top of the tower
    "Sealed Temple": RegionInfo("Temple"),
    "Sealed Temple Rafters": RegionInfo("Temple"),
    "Forest Belltower Upper": RegionInfo("Forest Belltower"),
    "Forest Belltower Main": RegionInfo("Forest Belltower"),
    "Forest Belltower Lower": RegionInfo("Forest Belltower"),
    "East Forest": RegionInfo("East Forest Redux"),
    "East Forest Dance Fox Spot": RegionInfo("East Forest Redux"),
    "East Forest Portal": RegionInfo("East Forest Redux"),
    "Lower Forest": RegionInfo("East Forest Redux"),  # bottom of the forest
    "Guard House 1 East": RegionInfo("East Forest Redux Laddercave"),
    "Guard House 1 West": RegionInfo("East Forest Redux Laddercave"),
    "Guard House 2 Upper": RegionInfo("East Forest Redux Interior"),
    "Guard House 2 Lower": RegionInfo("East Forest Redux Interior"),
    "Forest Boss Room": RegionInfo("Forest Boss Room"),
    "Forest Grave Path Main": RegionInfo("Sword Access"),
    "Forest Grave Path Upper": RegionInfo("Sword Access"),
    "Forest Grave Path by Grave": RegionInfo("Sword Access"),
    "Forest Hero's Grave": RegionInfo("Sword Access"),
    "Dark Tomb Entry Point": RegionInfo("Crypt Redux"),  # both upper exits
    "Dark Tomb Upper": RegionInfo("Crypt Redux"),  # the part with the casket and the top of the ladder
    "Dark Tomb Main": RegionInfo("Crypt Redux"),
    "Dark Tomb Dark Exit": RegionInfo("Crypt Redux"),
    "Dark Tomb Checkpoint": RegionInfo("Sewer_Boss"),  # can laurels backwards
    "Well Boss": RegionInfo("Sewer_Boss"),  # can walk through (with bombs at least)
    "Beneath the Well Ladder Exit": RegionInfo("Sewer"),  # just the ladder
    "Beneath the Well Front": RegionInfo("Sewer"),  # the front, to separate it from the weapon requirement in the mid
    "Beneath the Well Main": RegionInfo("Sewer"),  # the main section of it, requires a weapon
    "Beneath the Well Back": RegionInfo("Sewer"),  # the back two portals, and all 4 upper chests
    "West Garden": RegionInfo("Archipelagos Redux"),
    "Magic Dagger House": RegionInfo("archipelagos_house", dead_end=DeadEnd.all_cats),
    "West Garden Portal": RegionInfo("Archipelagos Redux", dead_end=DeadEnd.restricted),
    "West Garden Portal Item": RegionInfo("Archipelagos Redux", dead_end=DeadEnd.restricted),
    "West Garden Laurels Exit Region": RegionInfo("Archipelagos Redux"),
    "West Garden after Boss": RegionInfo("Archipelagos Redux"),
    "West Garden Hero's Grave Region": RegionInfo("Archipelagos Redux"),
    "Ruined Atoll": RegionInfo("Atoll Redux"),
    "Ruined Atoll Lower Entry Area": RegionInfo("Atoll Redux"),
    "Ruined Atoll Ladder Tops": RegionInfo("Atoll Redux"),  # at the top of the 5 ladders in south Atoll
    "Ruined Atoll Frog Mouth": RegionInfo("Atoll Redux"),
    "Ruined Atoll Frog Eye": RegionInfo("Atoll Redux"),
    "Ruined Atoll Portal": RegionInfo("Atoll Redux"),
    "Ruined Atoll Statue": RegionInfo("Atoll Redux"),
    "Frog Stairs Eye Exit": RegionInfo("Frog Stairs"),
    "Frog Stairs Upper": RegionInfo("Frog Stairs"),
    "Frog Stairs Lower": RegionInfo("Frog Stairs"),
    "Frog Stairs to Frog's Domain": RegionInfo("Frog Stairs"),
    "Frog's Domain": RegionInfo("frog cave main"),
    "Frog's Domain Back": RegionInfo("frog cave main"),
    "Library Exterior Tree Region": RegionInfo("Library Exterior"),
    "Library Exterior Ladder Region": RegionInfo("Library Exterior"),
    "Library Hall": RegionInfo("Library Hall"),
    "Library Hero's Grave Region": RegionInfo("Library Hall"),
    "Library Rotunda": RegionInfo("Library Rotunda"),
    "Library Lab": RegionInfo("Library Lab"),
    "Library Lab Lower": RegionInfo("Library Lab"),
    "Library Portal": RegionInfo("Library Lab"),
    "Library Arena": RegionInfo("Library Arena", dead_end=DeadEnd.all_cats),
    "Fortress Exterior from East Forest": RegionInfo("Fortress Courtyard"),
    "Fortress Exterior from Overworld": RegionInfo("Fortress Courtyard"),
    "Fortress Exterior near cave": RegionInfo("Fortress Courtyard"),  # where the shop and beneath the earth entry are
    "Fortress Courtyard": RegionInfo("Fortress Courtyard"),
    "Fortress Courtyard Upper": RegionInfo("Fortress Courtyard"),
    "Beneath the Vault Front": RegionInfo("Fortress Basement"),  # the vanilla entry point
    "Beneath the Vault Back": RegionInfo("Fortress Basement"),  # the vanilla exit point
    "Eastern Vault Fortress": RegionInfo("Fortress Main"),
    "Eastern Vault Fortress Gold Door": RegionInfo("Fortress Main"),
    "Fortress East Shortcut Upper": RegionInfo("Fortress East"),
    "Fortress East Shortcut Lower": RegionInfo("Fortress East"),
    "Fortress Grave Path": RegionInfo("Fortress Reliquary"),
    "Fortress Grave Path Upper": RegionInfo("Fortress Reliquary", dead_end=DeadEnd.restricted),
    "Fortress Grave Path Dusty Entrance Region": RegionInfo("Fortress Reliquary"),
    "Fortress Hero's Grave Region": RegionInfo("Fortress Reliquary"),
    "Fortress Leaf Piles": RegionInfo("Dusty", dead_end=DeadEnd.all_cats),
    "Fortress Arena": RegionInfo("Fortress Arena"),
    "Fortress Arena Portal": RegionInfo("Fortress Arena"),
    "Lower Mountain": RegionInfo("Mountain"),
    "Lower Mountain Stairs": RegionInfo("Mountain"),
    "Top of the Mountain": RegionInfo("Mountaintop", dead_end=DeadEnd.all_cats),
    "Quarry Connector": RegionInfo("Darkwoods Tunnel"),
    "Quarry Entry": RegionInfo("Quarry Redux"),
    "Quarry": RegionInfo("Quarry Redux"),
    "Quarry Portal": RegionInfo("Quarry Redux"),
    "Quarry Back": RegionInfo("Quarry Redux"),
    "Quarry Monastery Entry": RegionInfo("Quarry Redux"),
    "Monastery Front": RegionInfo("Monastery"),
    "Monastery Back": RegionInfo("Monastery"),
    "Monastery Hero's Grave Region": RegionInfo("Monastery"),
    "Monastery Rope": RegionInfo("Quarry Redux"),
    "Lower Quarry": RegionInfo("Quarry Redux"),
    "Lower Quarry Zig Door": RegionInfo("Quarry Redux"),
    "Rooted Ziggurat Entry": RegionInfo("ziggurat2020_0"),
    "Rooted Ziggurat Upper Entry": RegionInfo("ziggurat2020_1"),
    "Rooted Ziggurat Upper Front": RegionInfo("ziggurat2020_1"),
    "Rooted Ziggurat Upper Back": RegionInfo("ziggurat2020_1"),  # after the administrator
    "Rooted Ziggurat Middle Top": RegionInfo("ziggurat2020_2"),
    "Rooted Ziggurat Middle Bottom": RegionInfo("ziggurat2020_2"),
    "Rooted Ziggurat Lower Front": RegionInfo("ziggurat2020_3"),  # the vanilla entry point side
    "Rooted Ziggurat Lower Back": RegionInfo("ziggurat2020_3"),  # the boss side
    "Rooted Ziggurat Portal Room Entrance": RegionInfo("ziggurat2020_3"),  # the door itself on the zig 3 side
    "Rooted Ziggurat Portal": RegionInfo("ziggurat2020_FTRoom"),
    "Rooted Ziggurat Portal Room Exit": RegionInfo("ziggurat2020_FTRoom"),
    "Swamp Front": RegionInfo("Swamp Redux 2"),  # from the main entry to the top of the ladder after south
    "Swamp Mid": RegionInfo("Swamp Redux 2"),  # from the bottom of the ladder to the cathedral door
    "Swamp Ledge under Cathedral Door": RegionInfo("Swamp Redux 2"),  # the ledge with the chest and secret door
    "Swamp to Cathedral Treasure Room": RegionInfo("Swamp Redux 2"),  # just the door
    "Swamp to Cathedral Main Entrance Region": RegionInfo("Swamp Redux 2"),  # just the door
    "Back of Swamp": RegionInfo("Swamp Redux 2"),  # the area with hero grave and gauntlet entrance
    "Swamp Hero's Grave Region": RegionInfo("Swamp Redux 2"),
    "Back of Swamp Laurels Area": RegionInfo("Swamp Redux 2"),  # the spots you need laurels to traverse
    "Cathedral": RegionInfo("Cathedral Redux"),
    "Cathedral Secret Legend Room": RegionInfo("Cathedral Redux", dead_end=DeadEnd.all_cats),
    "Cathedral Gauntlet Checkpoint": RegionInfo("Cathedral Arena"),
    "Cathedral Gauntlet": RegionInfo("Cathedral Arena"),
    "Cathedral Gauntlet Exit": RegionInfo("Cathedral Arena"),
    "Far Shore": RegionInfo("Transit"),
    "Far Shore to Spawn Region": RegionInfo("Transit"),
    "Far Shore to East Forest Region": RegionInfo("Transit"),
    "Far Shore to Quarry Region": RegionInfo("Transit"),
    "Far Shore to Fortress Region": RegionInfo("Transit"),
    "Far Shore to Library Region": RegionInfo("Transit"),
    "Far Shore to West Garden Region": RegionInfo("Transit"),
    "Hero Relic - Fortress": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Hero Relic - Quarry": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Hero Relic - West Garden": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Hero Relic - East Forest": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Hero Relic - Library": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Hero Relic - Swamp": RegionInfo("RelicVoid", dead_end=DeadEnd.all_cats),
    "Purgatory": RegionInfo("Purgatory"),
    "Shop Entrance 1": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop Entrance 2": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop Entrance 3": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop Entrance 4": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop Entrance 5": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop Entrance 6": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Shop": RegionInfo("Shop", dead_end=DeadEnd.all_cats),
    "Spirit Arena": RegionInfo("Spirit Arena", dead_end=DeadEnd.all_cats),
    "Spirit Arena Victory": RegionInfo("Spirit Arena", dead_end=DeadEnd.all_cats)
}


# the key is the region you have, the value is the regions you get for having that region
# this is mostly so we don't have to do something overly complex to get this information
dependent_regions_restricted: Dict[Tuple[str, ...], List[str]] = {
    ("Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
     "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Southeast Cross Door",
     "Overworld Temple Door", "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
     "Overworld Swamp Lower Entry", "After Ruined Passage", "Above Ruined Passage", "East Overworld", "Upper Overworld",
     "Overworld after Temple Rafters", "Overworld Quarry Entry", "Overworld above Patrol Cave",
     "Overworld at Patrol Cave", "Overworld to West Garden Upper", "Overworld Well Ladder", "Overworld Beach",
     "Overworld to Atoll Upper", "Overworld above Quarry Entrance"):
         ["Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
          "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Ruined Passage Door",
          "Overworld Southeast Cross Door", "Overworld Old House Door", "Overworld Temple Door",
          "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
          "Overworld Swamp Lower Entry", "After Ruined Passage", "Above Ruined Passage", "East Overworld",
          "Upper Overworld", "Overworld after Temple Rafters", "Overworld Quarry Entry", "Overworld above Patrol Cave",
          "Overworld at Patrol Cave", "Overworld to West Garden Upper", "Overworld Well Ladder", "Overworld Beach",
          "Overworld to Atoll Upper", "Overworld Temple Door", "Overworld above Quarry Entrance"],
    ("Hourglass Cave",):
        ["Hourglass Cave", "Hourglass Cave Tower"],
    ("Old House Front",):
        ["Old House Front", "Old House Back"],
    ("Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"):
        ["Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"],
    ("Sealed Temple", "Sealed Temple Rafters"): ["Sealed Temple", "Sealed Temple Rafters"],
    ("Forest Belltower Upper",):
        ["Forest Belltower Upper", "Forest Belltower Main", "Forest Belltower Lower"],
    ("Forest Belltower Main",):
        ["Forest Belltower Main", "Forest Belltower Lower"],
    ("East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"):
        ["East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"],
    ("Guard House 1 East", "Guard House 1 West"):
        ["Guard House 1 East", "Guard House 1 West"],
    ("Guard House 2 Upper", "Guard House 2 Lower"):
        ["Guard House 2 Upper", "Guard House 2 Lower"],
    ("Forest Grave Path Main", "Forest Grave Path Upper"):
        ["Forest Grave Path Main", "Forest Grave Path Upper", "Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Forest Grave Path by Grave", "Forest Hero's Grave"):
        ["Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"):
        ["Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"],
    ("Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"):
        ["Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"],
    ("Well Boss",):
        ["Dark Tomb Checkpoint", "Well Boss"],
    ("West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region"):
        ["West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region"],
    ("West Garden Portal", "West Garden Portal Item"): ["West Garden Portal", "West Garden Portal Item"],
    ("Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
     "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"):
        ["Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
         "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"],
    ("Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"):
        ["Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"],
    ("Frog's Domain",):
        ["Frog's Domain", "Frog's Domain Back"],
    ("Library Exterior Ladder Region", "Library Exterior Tree Region"):
        ["Library Exterior Ladder Region", "Library Exterior Tree Region"],
    ("Library Hall", "Library Hero's Grave Region"):
        ["Library Hall", "Library Hero's Grave Region"],
    ("Library Lab", "Library Lab Lower", "Library Portal"):
        ["Library Lab", "Library Lab Lower", "Library Portal"],
    ("Fortress Courtyard Upper",):
        ["Fortress Courtyard Upper", "Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard"],
    ("Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
     "Fortress Exterior near cave", "Fortress Courtyard"):
        ["Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard"],
    ("Beneath the Vault Front", "Beneath the Vault Back"):
        ["Beneath the Vault Front", "Beneath the Vault Back"],
    ("Fortress East Shortcut Upper",):
        ["Fortress East Shortcut Upper", "Fortress East Shortcut Lower"],
    ("Eastern Vault Fortress",):
        ["Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"],
    ("Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"):
        ["Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"],
    ("Fortress Arena", "Fortress Arena Portal"):
        ["Fortress Arena", "Fortress Arena Portal"],
    ("Lower Mountain", "Lower Mountain Stairs"):
        ["Lower Mountain", "Lower Mountain Stairs"],
    ("Monastery Front",):
        ["Monastery Front", "Monastery Back", "Monastery Hero's Grave Region"],
    ("Monastery Back", "Monastery Hero's Grave Region"):
        ["Monastery Back", "Monastery Hero's Grave Region"],
    ("Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry"):
        ["Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry",
         "Lower Quarry Zig Door"],
    ("Monastery Rope",): ["Monastery Rope", "Quarry", "Quarry Entry", "Quarry Back", "Quarry Portal", "Lower Quarry",
                          "Lower Quarry Zig Door"],
    ("Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front"):
        ["Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front", "Rooted Ziggurat Upper Back"],
    ("Rooted Ziggurat Middle Top",):
        ["Rooted Ziggurat Middle Top", "Rooted Ziggurat Middle Bottom"],
    ("Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"):
        ["Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"],
    ("Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"):
        ["Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"],
    ("Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp Ledge under Cathedral Door"):
        ["Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
         "Swamp Ledge under Cathedral Door"],
    ("Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region"):
        ["Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region"],
    ("Cathedral Gauntlet Checkpoint",):
        ["Cathedral Gauntlet Checkpoint", "Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Cathedral Gauntlet Exit",):
        ["Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
     "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"):
        ["Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
         "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"]
}


dependent_regions_nmg: Dict[Tuple[str, ...], List[str]] = {
    ("Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
     "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Southeast Cross Door",
     "Overworld Temple Door", "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
     "Overworld Ruined Passage Door", "Overworld Swamp Lower Entry", "After Ruined Passage", "Above Ruined Passage",
     "East Overworld", "Upper Overworld", "Overworld after Temple Rafters", "Overworld Quarry Entry",
     "Overworld above Patrol Cave", "Overworld at Patrol Cave", "Overworld to West Garden Upper",
     "Overworld Well Ladder", "Overworld Beach", "Overworld to Atoll Upper", "Overworld above Quarry Entrance"):
         ["Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
          "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Ruined Passage Door",
          "Overworld Southeast Cross Door", "Overworld Old House Door", "Overworld Temple Door",
          "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
          "Overworld Swamp Lower Entry", "After Ruined Passage", "Above Ruined Passage", "East Overworld",
          "Upper Overworld", "Overworld after Temple Rafters", "Overworld Quarry Entry", "Overworld above Patrol Cave",
          "Overworld at Patrol Cave", "Overworld to West Garden Upper", "Overworld Well Ladder", "Overworld Beach",
          "Overworld to Atoll Upper", "Overworld above Quarry Entrance"],
    # can laurels through the gate
    ("Old House Front", "Old House Back"):
        ["Old House Front", "Old House Back"],
    ("Hourglass Cave",):
        ["Hourglass Cave", "Hourglass Cave Tower"],
    ("Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"):
        ["Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"],
    ("Sealed Temple", "Sealed Temple Rafters"): ["Sealed Temple", "Sealed Temple Rafters"],
    ("Forest Belltower Upper",):
        ["Forest Belltower Upper", "Forest Belltower Main", "Forest Belltower Lower"],
    ("Forest Belltower Main",):
        ["Forest Belltower Main", "Forest Belltower Lower"],
    ("East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"):
        ["East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"],
    ("Guard House 1 East", "Guard House 1 West"):
        ["Guard House 1 East", "Guard House 1 West"],
    ("Guard House 2 Upper", "Guard House 2 Lower"):
        ["Guard House 2 Upper", "Guard House 2 Lower"],
    ("Forest Grave Path Main", "Forest Grave Path Upper", "Forest Grave Path by Grave", "Forest Hero's Grave"):
        ["Forest Grave Path Main", "Forest Grave Path Upper", "Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"):
        ["Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"],
    ("Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"):
        ["Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"],
    ("Dark Tomb Checkpoint", "Well Boss"):
        ["Dark Tomb Checkpoint", "Well Boss"],
    ("West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region",
     "West Garden Portal", "West Garden Portal Item"):
        ["West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region",
         "West Garden Portal", "West Garden Portal Item"],
    ("Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
     "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"):
        ["Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
         "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"],
    ("Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"):
        ["Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"],
    ("Frog's Domain",):
        ["Frog's Domain", "Frog's Domain Back"],
    ("Library Exterior Ladder Region", "Library Exterior Tree Region"):
        ["Library Exterior Ladder Region", "Library Exterior Tree Region"],
    ("Library Hall", "Library Hero's Grave Region"):
        ["Library Hall", "Library Hero's Grave Region"],
    ("Library Lab", "Library Lab Lower", "Library Portal"):
        ["Library Lab", "Library Lab Lower", "Library Portal"],
    ("Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
     "Fortress Exterior near cave", "Fortress Courtyard", "Fortress Courtyard Upper"):
        ["Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard", "Fortress Courtyard Upper"],
    ("Beneath the Vault Front", "Beneath the Vault Back"):
        ["Beneath the Vault Front", "Beneath the Vault Back"],
    ("Fortress East Shortcut Upper", "Fortress East Shortcut Lower"):
        ["Fortress East Shortcut Upper", "Fortress East Shortcut Lower"],
    ("Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"):
        ["Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"],
    ("Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"):
        ["Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"],
    ("Fortress Grave Path Upper",):
        ["Fortress Grave Path Upper", "Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region",
         "Fortress Hero's Grave Region"],
    ("Fortress Arena", "Fortress Arena Portal"):
        ["Fortress Arena", "Fortress Arena Portal"],
    ("Lower Mountain", "Lower Mountain Stairs"):
        ["Lower Mountain", "Lower Mountain Stairs"],
    ("Monastery Front", "Monastery Back", "Monastery Hero's Grave Region"):
        ["Monastery Front", "Monastery Back", "Monastery Hero's Grave Region"],
    ("Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry"):
        ["Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry",
         "Lower Quarry Zig Door"],
    ("Monastery Rope",): ["Monastery Rope", "Quarry", "Quarry Entry", "Quarry Back", "Quarry Portal", "Lower Quarry",
                          "Lower Quarry Zig Door"], 
    ("Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front"):
        ["Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front", "Rooted Ziggurat Upper Back"],
    ("Rooted Ziggurat Middle Top",):
        ["Rooted Ziggurat Middle Top", "Rooted Ziggurat Middle Bottom"],
    ("Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"):
        ["Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"],
    ("Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"):
        ["Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"],
    ("Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
     "Swamp Ledge under Cathedral Door"):
        ["Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
         "Swamp Ledge under Cathedral Door"],
    ("Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region"):
        ["Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region", "Swamp Front", "Swamp Mid",
         "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
         "Swamp Ledge under Cathedral Door"],
    ("Cathedral Gauntlet Checkpoint",):
        ["Cathedral Gauntlet Checkpoint", "Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Cathedral Gauntlet Exit",):
        ["Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
     "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"):
        ["Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
         "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"]
}


dependent_regions_ur: Dict[Tuple[str, ...], List[str]] = {
    # can use ladder storage to get to the well rail
    ("Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
     "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Southeast Cross Door",
     "Overworld Temple Door", "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
     "Overworld Ruined Passage Door", "Overworld Swamp Lower Entry", "After Ruined Passage", "Above Ruined Passage",
     "East Overworld", "Upper Overworld", "Overworld after Temple Rafters", "Overworld Quarry Entry",
     "Overworld above Patrol Cave", "Overworld at Patrol Cave", "Overworld to West Garden Upper",
     "Overworld Well Ladder", "Overworld Beach", "Overworld to Atoll Upper", "Overworld above Quarry Entrance"):
         ["Overworld", "Overworld Belltower", "Overworld Belltower at Bell", "Overworld Swamp Upper Entry",
          "Overworld Special Shop Entry", "Overworld West Garden Laurels Entry", "Overworld Southeast Cross Door",
          "Overworld Temple Door", "Overworld Fountain Cross Door", "Overworld Town Portal", "Overworld Spawn Portal",
          "Overworld Ruined Passage Door", "Overworld Swamp Lower Entry", "After Ruined Passage",
          "Above Ruined Passage", "East Overworld", "Upper Overworld", "Overworld after Temple Rafters",
          "Overworld Quarry Entry", "Overworld above Patrol Cave", "Overworld at Patrol Cave",
          "Overworld to West Garden Upper", "Overworld Well Ladder", "Overworld Beach", "Overworld to Atoll Upper",
          "Overworld above Quarry Entrance"],
    # can laurels through the gate
    ("Old House Front", "Old House Back"):
        ["Old House Front", "Old House Back"],
    ("Hourglass Cave",):
        ["Hourglass Cave", "Hourglass Cave Tower"],
    ("Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"):
        ["Furnace Fuse", "Furnace Ladder Area", "Furnace Walking Path"],
    ("Sealed Temple", "Sealed Temple Rafters"): ["Sealed Temple", "Sealed Temple Rafters"],
    ("Forest Belltower Upper",):
        ["Forest Belltower Upper", "Forest Belltower Main", "Forest Belltower Lower"],
    ("Forest Belltower Main",):
        ["Forest Belltower Main", "Forest Belltower Lower"],
    ("East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"):
        ["East Forest", "East Forest Dance Fox Spot", "East Forest Portal", "Lower Forest"],
    ("Guard House 1 East", "Guard House 1 West"):
        ["Guard House 1 East", "Guard House 1 West"],
    ("Guard House 2 Upper", "Guard House 2 Lower"):
        ["Guard House 2 Upper", "Guard House 2 Lower"],
    # can use laurels, ice grapple, or ladder storage to traverse
    ("Forest Grave Path Main", "Forest Grave Path Upper", "Forest Grave Path by Grave", "Forest Hero's Grave"):
        ["Forest Grave Path Main", "Forest Grave Path Upper", "Forest Grave Path by Grave", "Forest Hero's Grave"],
    ("Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"):
        ["Beneath the Well Front", "Beneath the Well Main", "Beneath the Well Back", "Beneath the Well Ladder Exit"],
    ("Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"):
        ["Dark Tomb Entry Point", "Dark Tomb Main", "Dark Tomb Dark Exit", "Dark Tomb Upper"],
    ("Dark Tomb Checkpoint", "Well Boss"):
        ["Dark Tomb Checkpoint", "Well Boss"],
    # can ice grapple from portal area to the rest, and vice versa
    ("West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region",
     "West Garden Portal", "West Garden Portal Item"):
        ["West Garden", "West Garden Laurels Exit Region", "West Garden after Boss", "West Garden Hero's Grave Region",
         "West Garden Portal", "West Garden Portal Item"],
    ("Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
     "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"):
        ["Ruined Atoll", "Ruined Atoll Lower Entry Area", "Ruined Atoll Frog Mouth", "Ruined Atoll Portal",
         "Ruined Atoll Statue", "Ruined Atoll Ladder Tops", "Ruined Atoll Frog Eye", "Ruined Atoll Ladder Tops"],
    ("Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"):
        ["Frog Stairs Upper", "Frog Stairs Lower", "Frog Stairs to Frog's Domain"],
    ("Frog's Domain",):
        ["Frog's Domain", "Frog's Domain Back"],
    ("Library Exterior Ladder Region", "Library Exterior Tree Region"):
        ["Library Exterior Ladder Region", "Library Exterior Tree Region"],
    ("Library Hall", "Library Hero's Grave Region"):
        ["Library Hall", "Library Hero's Grave Region"],
    ("Library Lab", "Library Lab Lower", "Library Portal"):
        ["Library Lab", "Library Lab Lower", "Library Portal"],
    # can use ice grapple or ladder storage to get from any ladder to upper
    ("Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
     "Fortress Exterior near cave", "Fortress Courtyard", "Fortress Courtyard Upper"):
        ["Fortress Exterior from East Forest", "Fortress Exterior from Overworld",
         "Fortress Exterior near cave", "Fortress Courtyard", "Fortress Courtyard Upper"],
    ("Beneath the Vault Front", "Beneath the Vault Back"):
        ["Beneath the Vault Front", "Beneath the Vault Back"],
    # can ice grapple up
    ("Fortress East Shortcut Upper", "Fortress East Shortcut Lower"):
        ["Fortress East Shortcut Upper", "Fortress East Shortcut Lower"],
    ("Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"):
        ["Eastern Vault Fortress", "Eastern Vault Fortress Gold Door"],
    ("Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"):
        ["Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region", "Fortress Hero's Grave Region"],
    # can ice grapple down
    ("Fortress Grave Path Upper",):
        ["Fortress Grave Path Upper", "Fortress Grave Path", "Fortress Grave Path Dusty Entrance Region",
         "Fortress Hero's Grave Region"],
    ("Fortress Arena", "Fortress Arena Portal"):
        ["Fortress Arena", "Fortress Arena Portal"],
    ("Lower Mountain", "Lower Mountain Stairs"):
        ["Lower Mountain", "Lower Mountain Stairs"],
    ("Monastery Front", "Monastery Back", "Monastery Hero's Grave Region"):
        ["Monastery Front", "Monastery Back", "Monastery Hero's Grave Region"],
    # can use ladder storage at any of the Quarry ladders to get to Monastery Rope
    ("Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry",
     "Monastery Rope"):
        ["Quarry", "Quarry Portal", "Lower Quarry", "Quarry Entry", "Quarry Back", "Quarry Monastery Entry",
         "Monastery Rope", "Lower Quarry Zig Door"],
    ("Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front"):
        ["Rooted Ziggurat Upper Entry", "Rooted Ziggurat Upper Front", "Rooted Ziggurat Upper Back"],
    ("Rooted Ziggurat Middle Top",):
        ["Rooted Ziggurat Middle Top", "Rooted Ziggurat Middle Bottom"],
    ("Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"):
        ["Rooted Ziggurat Lower Front", "Rooted Ziggurat Lower Back", "Rooted Ziggurat Portal Room Entrance"],
    ("Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"):
        ["Rooted Ziggurat Portal", "Rooted Ziggurat Portal Room Exit"],
    ("Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
     "Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region", "Swamp Ledge under Cathedral Door"):
        ["Swamp Front", "Swamp Mid", "Swamp to Cathedral Treasure Room", "Swamp to Cathedral Main Entrance Region",
         "Back of Swamp", "Back of Swamp Laurels Area", "Swamp Hero's Grave Region",
         "Swamp Ledge under Cathedral Door"],
    ("Cathedral Gauntlet Checkpoint",):
        ["Cathedral Gauntlet Checkpoint", "Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Cathedral Gauntlet Exit",):
        ["Cathedral Gauntlet Exit", "Cathedral Gauntlet"],
    ("Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
     "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"):
        ["Far Shore", "Far Shore to Spawn Region", "Far Shore to East Forest Region", "Far Shore to Quarry Region",
         "Far Shore to Fortress Region", "Far Shore to Library Region", "Far Shore to West Garden Region"]
}
