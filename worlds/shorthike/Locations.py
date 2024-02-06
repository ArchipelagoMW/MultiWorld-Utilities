from typing import List, TypedDict

class LocationInfo(TypedDict):
    name: str
    id: int
    inGameId: str
    needsShovel: bool
    purchase: bool
    chestAngle: int
    minGoldenFeathers: int
    minGoldenFeathersEasy: int
    minGoldenFeathersBucket: int

base_id = 83000

location_table: List[LocationInfo] = [
    # Original Seashell Locations
    {"name": "Start Beach Seashell", 
        "id": base_id + 1, 
        "inGameId": "PickUps.3", 
        "needsShovel": False, "purchase": False, "chestAngle": 120,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Beach Hut Seashell",
        "id": base_id + 2,
        "inGameId": "PickUps.2",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Beach Umbrella Seashell",
        "id": base_id + 3,
        "inGameId": "PickUps.8",
        "needsShovel": False, "purchase": False, "chestAngle": 160,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Sid Beach Mound Seashell",
        "id": base_id + 4,
        "inGameId": "PickUps.12",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Sid Beach Seashell",
        "id": base_id + 5,
        "inGameId": "PickUps.11",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Shirley's Point Beach Seashell",
        "id": base_id + 6,
        "inGameId": "PickUps.18",
        "needsShovel": False, "purchase": False, "chestAngle": 240,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Shirley's Point Rock Seashell",
        "id": base_id + 7,
        "inGameId": "PickUps.17",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Visitor's Center Beach Seashell",
        "id": base_id + 8,
        "inGameId": "PickUps.19",
        "needsShovel": False, "purchase": False, "chestAngle": 300,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "West River Seashell",
        "id": base_id + 9,
        "inGameId": "PickUps.10",
        "needsShovel": False, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "West Riverbank Seashell",
        "id": base_id + 10,
        "inGameId": "PickUps.4",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Stone Tower Riverbank Seashell",
        "id": base_id + 11,
        "inGameId": "PickUps.23",
        "needsShovel": False, "purchase": False, "chestAngle": 240,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "North Beach Seashell",
        "id": base_id + 12,
        "inGameId": "PickUps.6",
        "needsShovel": False, "purchase": False, "chestAngle": 310,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "North Coast Seashell",
        "id": base_id + 13,
        "inGameId": "PickUps.7",
        "needsShovel": False, "purchase": False, "chestAngle": 80,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Boat Cliff Seashell",
        "id": base_id + 14,
        "inGameId": "PickUps.14",
        "needsShovel": False, "purchase": False, "chestAngle": 40,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Boat Isle Mound Seashell",
        "id": base_id + 15,
        "inGameId": "PickUps.22",
        "needsShovel": False, "purchase": False, "chestAngle": 20,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "East Coast Seashell",
        "id": base_id + 16,
        "inGameId": "PickUps.21",
        "needsShovel": False, "purchase": False, "chestAngle": 120,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "House North Beach Seashell",
        "id": base_id + 17,
        "inGameId": "PickUps.16",
        "needsShovel": False, "purchase": False, "chestAngle": 160,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Airstream Island North Seashell",
        "id": base_id + 18,
        "inGameId": "PickUps.13",
        "needsShovel": False, "purchase": False, "chestAngle": 60,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Airstream Island South Seashell",
        "id": base_id + 19,
        "inGameId": "PickUps.15",
        "needsShovel": False, "purchase": False, "chestAngle": 180,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Secret Island Beach Seashell",
        "id": base_id + 20,
        "inGameId": "PickUps.1",
        "needsShovel": False, "purchase": False, "chestAngle": 310,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Meteor Lake Seashell",
        "id": base_id + 126,
        "inGameId": "PickUps.20",
        "needsShovel": False, "purchase": False, "chestAngle": 160,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Good Creek Path Seashell",
        "id": base_id + 127,
        "inGameId": "PickUps.9",
        "needsShovel": False, "purchase": False, "chestAngle": 110,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},

    # Visitor's Center Shop
    {"name": "Visitor's Center Shop Golden Feather 1",
        "id": base_id + 21,
        "inGameId": "CampRangerNPC[0]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Visitor's Center Shop Golden Feather 2",
        "id": base_id + 22,
        "inGameId": "CampRangerNPC[1]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Visitor's Center Shop Hat",
        "id": base_id + 23,
        "inGameId": "CampRangerNPC[9]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Tough Bird Salesman
    {"name": "Tough Bird Salesman Golden Feather 1",
        "id": base_id + 24,
        "inGameId": "ToughBirdNPC (1)[0]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Tough Bird Salesman Golden Feather 2",
        "id": base_id + 25,
        "inGameId": "ToughBirdNPC (1)[1]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Tough Bird Salesman Golden Feather 3",
        "id": base_id + 26,
        "inGameId": "ToughBirdNPC (1)[2]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Tough Bird Salesman Golden Feather 4",
        "id": base_id + 27,
        "inGameId": "ToughBirdNPC (1)[3]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Tough Bird Salesman (400 Coins)",
        "id": base_id + 28,
        "inGameId": "ToughBirdNPC (1)[9]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},

    # Beachstickball
    {"name": "Beachstickball (10 Hits)",
        "id": base_id + 29,
        "inGameId": "VolleyballOpponent[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Beachstickball (20 Hits)",
        "id": base_id + 30,
        "inGameId": "VolleyballOpponent[1]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Beachstickball (30 Hits)",
        "id": base_id + 31,
        "inGameId": "VolleyballOpponent[2]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Misc Item Locations
    {"name": "Shovel Kid Trade",
        "id": base_id + 32,
        "inGameId": "Frog_StandingNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Compass Guy",
        "id": base_id + 33,
        "inGameId": "Fox_WalkingNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Hawk Peak Bucket Rock",
        "id": base_id + 34,
        "inGameId": "Tools.23",
        "needsShovel": False, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Orange Islands Bucket Rock",
        "id": base_id + 35,
        "inGameId": "Tools.42",
        "needsShovel": False, "purchase": False, "chestAngle": 10,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Bill the Walrus Fisherman",
        "id": base_id + 36,
        "inGameId": "SittingNPC (1)[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Catch 3 Fish Reward",
        "id": base_id + 37,
        "inGameId": "FishBuyer[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Catch All Fish Reward",
        "id": base_id + 38,
        "inGameId": "FishBuyer[1]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 7, "minGoldenFeathersEasy": 9, "minGoldenFeathersBucket": 7},
    {"name": "Permit Guy Bribe",
        "id": base_id + 39,
        "inGameId": "CamperNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Catch Fish with Permit",
        "id": base_id + 129,
        "inGameId": "Player[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Return Camping Permit",
        "id": base_id + 130,
        "inGameId": "CamperNPC[1]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},

    # Original Pickaxe Locations
    {"name": "Blocked Mine Pickaxe 1",
        "id": base_id + 40,
        "inGameId": "Tools.31",
        "needsShovel": False, "purchase": False, "chestAngle": 350,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Blocked Mine Pickaxe 2",
        "id": base_id + 41,
        "inGameId": "Tools.32",
        "needsShovel": False, "purchase": False, "chestAngle": 80,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Blocked Mine Pickaxe 3",
        "id": base_id + 42,
        "inGameId": "Tools.33",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Original Toy Shovel Locations
    {"name": "Blackwood Trail Lookout Toy Shovel",
        "id": base_id + 43,
        "inGameId": "PickUps.27",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Shirley's Point Beach Toy Shovel",
        "id": base_id + 44,
        "inGameId": "PickUps.30",
        "needsShovel": False, "purchase": False, "chestAngle": 300,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Visitor's Center Beach Toy Shovel",
        "id": base_id + 45,
        "inGameId": "PickUps.29",
        "needsShovel": False, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Blackwood Trail Rock Toy Shovel",
        "id": base_id + 46,
        "inGameId": "PickUps.26",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Beach Hut Cliff Toy Shovel",
        "id": base_id + 128,
        "inGameId": "PickUps.28",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Original Stick Locations
    {"name": "Secret Island Beach Trail Stick",
        "id": base_id + 47,
        "inGameId": "PickUps.25",
        "needsShovel": False, "purchase": False, "chestAngle": 240,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Below Lighthouse Walkway Stick",
        "id": base_id + 48,
        "inGameId": "Tools.3",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Beach Hut Rocky Pool Sand Stick",
        "id": base_id + 49,
        "inGameId": "Tools.0",
        "needsShovel": False, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Cliff Overlooking West River Waterfall Stick",
        "id": base_id + 50,
        "inGameId": "Tools.2",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 2, "minGoldenFeathersBucket": 0},
    {"name": "Trail to Tough Bird Salesman Stick",
        "id": base_id + 51,
        "inGameId": "Tools.8",
        "needsShovel": False, "purchase": False, "chestAngle": 180,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "North Beach Stick",
        "id": base_id + 52,
        "inGameId": "Tools.4",
        "needsShovel": False, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Beachstickball Court Stick",
        "id": base_id + 53,
        "inGameId": "VolleyballMinigame.4",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Stick Under Sid Beach Umbrella",
        "id": base_id + 54,
        "inGameId": "Tools.1",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Boating
    {"name": "Boat Rental",
        "id": base_id + 55,
        "inGameId": "DadDeer[0]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Boat Challenge Reward",
        "id": base_id + 56,
        "inGameId": "DeerKidBoat[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Not a location for now, corresponding with the Boating Manual
    # {"name": "Receive Boating Manual",
    #   "id": base_id + 133,
    #   "inGameId": "DadDeer[1]",
    #   "needsShovel": False, "purchase": False, "chestAngle": 0,
	#	"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Original Map Locations
    {"name": "Outlook Point Dog Gift",
        "id": base_id + 57,
        "inGameId": "Dog_WalkingNPC_BlueEyed[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},

    # Original Clothes Locations
    {"name": "Collect 15 Seashells",
        "id": base_id + 58,
        "inGameId": "LittleKidNPCVariant (1)[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Return to Shell Kid",
        "id": base_id + 132,
        "inGameId": "LittleKidNPCVariant (1)[1]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Taylor the Turtle Headband Gift",
        "id": base_id + 59,
        "inGameId": "Turtle_WalkingNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Sue the Rabbit Shoes Reward",
        "id": base_id + 60,
        "inGameId": "Bunny_WalkingNPC (1)[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Purchase Sunhat",
        "id": base_id + 61,
        "inGameId": "SittingNPC[0]",
        "needsShovel": False, "purchase": True, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Original Golden Feather Locations
    {"name": "Blackwood Forest Golden Feather",
        "id": base_id + 62,
        "inGameId": "Feathers.3",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Ranger May Shell Necklace Golden Feather",
        "id": base_id + 63,
        "inGameId": "AuntMayNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Sand Castle Golden Feather",
        "id": base_id + 64,
        "inGameId": "SandProvince.3",
        "needsShovel": False, "purchase": False, "chestAngle": 270,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
    {"name": "Artist Golden Feather",
        "id": base_id + 65,
        "inGameId": "StandingNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Visitor Camp Rock Golden Feather",
        "id": base_id + 66,
        "inGameId": "Feathers.8",
        "needsShovel": False, "purchase": False, "chestAngle": 220,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Outlook Cliff Golden Feather",
        "id": base_id + 67,
        "inGameId": "Feathers.2",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Meteor Lake Cliff Golden Feather",
        "id": base_id + 68,
        "inGameId": "Feathers.7",
        "needsShovel": False, "purchase": False, "chestAngle": 130,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 0},

    # Original Silver Feather Locations
    {"name": "Secret Island Peak",
        "id": base_id + 69,
        "inGameId": "PickUps.24",
        "needsShovel": False, "purchase": False, "chestAngle": 150,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 5},
    {"name": "Wristwatch Trade",
        "id": base_id + 70,
        "inGameId": "Goat_StandingNPC[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},

    # Golden Chests
    {"name": "Lighthouse Golden Chest",
        "id": base_id + 71,
        "inGameId": "Feathers.0",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 2, "minGoldenFeathersEasy": 3, "minGoldenFeathersBucket": 0},
    {"name": "Outlook Golden Chest",
        "id": base_id + 72,
        "inGameId": "Feathers.6",
        "needsShovel": False, "purchase": False, "chestAngle": 200,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "Stone Tower Golden Chest",
        "id": base_id + 73,
        "inGameId": "Feathers.5",
        "needsShovel": False, "purchase": False, "chestAngle": 220,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0},
    {"name": "North Cliff Golden Chest",
        "id": base_id + 74,
        "inGameId": "Feathers.4",
        "needsShovel": False, "purchase": False, "chestAngle": 280,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 10, "minGoldenFeathersBucket": 10},

    # Chests
    {"name": "Blackwood Cliff Chest",
        "id": base_id + 75,
        "inGameId": "Coins.22",
        "needsShovel": False, "purchase": False, "chestAngle": 180,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "White Coast Trail Chest",
        "id": base_id + 76,
        "inGameId": "Coins.6",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Sid Beach Chest",
        "id": base_id + 77,
        "inGameId": "Coins.7",
        "needsShovel": False, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Sid Beach Buried Treasure Chest",
        "id": base_id + 78,
        "inGameId": "Coins.46",
        "needsShovel": True, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Sid Beach Cliff Chest",
        "id": base_id + 79,
        "inGameId": "Coins.9",
        "needsShovel": False, "purchase": False, "chestAngle": 170,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Visitor's Center Buried Chest",
        "id": base_id + 80,
        "inGameId": "Coins.94",
        "needsShovel": True, "purchase": False, "chestAngle": 250,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Visitor's Center Hidden Chest",
        "id": base_id + 81,
        "inGameId": "Coins.42",
        "needsShovel": False, "purchase": False, "chestAngle": 350,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Shirley's Point Chest",
        "id": base_id + 82,
        "inGameId": "Coins.10",
        "needsShovel": False, "purchase": False, "chestAngle": 170,
		"minGoldenFeathers": 1, "minGoldenFeathersEasy": 2, "minGoldenFeathersBucket": 2}, 
    {"name": "Caravan Cliff Chest",
        "id": base_id + 83,
        "inGameId": "Coins.12",
        "needsShovel": False, "purchase": False, "chestAngle": 250,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Caravan Arch Chest",
        "id": base_id + 84,
        "inGameId": "Coins.11",
        "needsShovel": False, "purchase": False, "chestAngle": 270,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "King Buried Treasure Chest",
        "id": base_id + 85,
        "inGameId": "Coins.41",
        "needsShovel": True, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Good Creek Path Buried Chest",
        "id": base_id + 86,
        "inGameId": "Coins.48",
        "needsShovel": True, "purchase": False, "chestAngle": 170,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Good Creek Path West Chest",
        "id": base_id + 87,
        "inGameId": "Coins.33",
        "needsShovel": False, "purchase": False, "chestAngle": 160,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Good Creek Path East Chest",
        "id": base_id + 88,
        "inGameId": "Coins.62",
        "needsShovel": False, "purchase": False, "chestAngle": 160,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "West Waterfall Chest",
        "id": base_id + 89,
        "inGameId": "Coins.20",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Stone Tower West Cliff Chest",
        "id": base_id + 90,
        "inGameId": "PickUps.0",
        "needsShovel": False, "purchase": False, "chestAngle": 120,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Bucket Path Chest",
        "id": base_id + 91,
        "inGameId": "Coins.50",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Bucket Cliff Chest",
        "id": base_id + 92,
        "inGameId": "Coins.49",
        "needsShovel": False, "purchase": False, "chestAngle": 120,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 5}, 
    {"name": "In Her Shadow Buried Treasure Chest",
        "id": base_id + 93,
        "inGameId": "Feathers.9",
        "needsShovel": True, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Meteor Lake Buried Chest",
        "id": base_id + 94,
        "inGameId": "Coins.86",
        "needsShovel": True, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Meteor Lake Chest",
        "id": base_id + 95,
        "inGameId": "Coins.64",
        "needsShovel": False, "purchase": False, "chestAngle": 280,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "House North Beach Chest",
        "id": base_id + 96,
        "inGameId": "Coins.65",
        "needsShovel": False, "purchase": False, "chestAngle": 100,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "East Coast Chest",
        "id": base_id + 97,
        "inGameId": "Coins.98",
        "needsShovel": False, "purchase": False, "chestAngle": 70,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Fisherman's Boat Chest 1",
        "id": base_id + 99,
        "inGameId": "Boat.0",
        "needsShovel": False, "purchase": False, "chestAngle": 20,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Fisherman's Boat Chest 2",
        "id": base_id + 100,
        "inGameId": "Boat.7",
        "needsShovel": False, "purchase": False, "chestAngle": 130,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Airstream Island Chest",
        "id": base_id + 101,
        "inGameId": "Coins.31",
        "needsShovel": False, "purchase": False, "chestAngle": 100,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "West River Waterfall Head Chest",
        "id": base_id + 102,
        "inGameId": "Coins.34",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Old Building Chest",
        "id": base_id + 103,
        "inGameId": "Coins.104",
        "needsShovel": False, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Old Building West Chest",
        "id": base_id + 104,
        "inGameId": "Coins.109",
        "needsShovel": False, "purchase": False, "chestAngle": 310,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Old Building East Chest",
        "id": base_id + 105,
        "inGameId": "Coins.8",
        "needsShovel": False, "purchase": False, "chestAngle": 260,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Hawk Peak West Chest",
        "id": base_id + 106,
        "inGameId": "Coins.21",
        "needsShovel": False, "purchase": False, "chestAngle": 220,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 5}, 
    {"name": "Hawk Peak East Buried Chest",
        "id": base_id + 107,
        "inGameId": "Coins.76",
        "needsShovel": True, "purchase": False, "chestAngle": 50,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 5}, 
    {"name": "Hawk Peak Northeast Chest",
        "id": base_id + 108,
        "inGameId": "Coins.79",
        "needsShovel": False, "purchase": False, "chestAngle": 60,
		"minGoldenFeathers": 3, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 5}, 
    {"name": "Northern East Coast Chest",
        "id": base_id + 109,
        "inGameId": "Coins.45",
        "needsShovel": False, "purchase": False, "chestAngle": 20,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 2, "minGoldenFeathersBucket": 0}, 
    {"name": "North Coast Chest",
        "id": base_id + 110,
        "inGameId": "Coins.28",
        "needsShovel": False, "purchase": False, "chestAngle": 50,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "North Coast Buried Chest",
        "id": base_id + 111,
        "inGameId": "Coins.47",
        "needsShovel": True, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Small South Island Buried Chest",
        "id": base_id + 112,
        "inGameId": "Coins.87",
        "needsShovel": True, "purchase": False, "chestAngle": 190,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Secret Island Bottom Chest",
        "id": base_id + 113,
        "inGameId": "Coins.88",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Secret Island Treehouse Chest",
        "id": base_id + 114,
        "inGameId": "Coins.89",
        "needsShovel": False, "purchase": False, "chestAngle": 230,
		"minGoldenFeathers": 1, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 1}, 
    {"name": "Sunhat Island Buried Chest",
        "id": base_id + 115,
        "inGameId": "Coins.112",
        "needsShovel": True, "purchase": False, "chestAngle": 50,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands South Buried Chest",
        "id": base_id + 116,
        "inGameId": "Coins.119",
        "needsShovel": True, "purchase": False, "chestAngle": 350,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands West Chest",
        "id": base_id + 117,
        "inGameId": "Coins.121",
        "needsShovel": False, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands North Buried Chest",
        "id": base_id + 118,
        "inGameId": "Coins.117",
        "needsShovel": True, "purchase": False, "chestAngle": 20,
		"minGoldenFeathers": 1, "minGoldenFeathersEasy": 1, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands East Chest",
        "id": base_id + 119,
        "inGameId": "Coins.120",
        "needsShovel": False, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands South Hidden Chest",
        "id": base_id + 120,
        "inGameId": "Coins.124",
        "needsShovel": False, "purchase": False, "chestAngle": 170,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "A Stormy View Buried Treasure Chest",
        "id": base_id + 121,
        "inGameId": "Coins.113",
        "needsShovel": True, "purchase": False, "chestAngle": 330,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0}, 
    {"name": "Orange Islands Ruins Buried Chest",
        "id": base_id + 122,
        "inGameId": "Coins.118",
        "needsShovel": True, "purchase": False, "chestAngle": 20,
		"minGoldenFeathers": 2, "minGoldenFeathersEasy": 4, "minGoldenFeathersBucket": 0}, 

    # Race Rewards
    {"name": "Lighthouse Race Reward",
        "id": base_id + 123,
        "inGameId": "RaceOpponent[0]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 2, "minGoldenFeathersEasy": 3, "minGoldenFeathersBucket": 1},
    {"name": "Old Building Race Reward",
        "id": base_id + 124,
        "inGameId": "RaceOpponent[1]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 1, "minGoldenFeathersEasy": 5, "minGoldenFeathersBucket": 0},
    {"name": "Hawk Peak Race Reward",
        "id": base_id + 125,
        "inGameId": "RaceOpponent[2]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 7, "minGoldenFeathersEasy": 9, "minGoldenFeathersBucket": 7},
    {"name": "Lose Race Gift",
        "id": base_id + 131,
        "inGameId": "RaceOpponent[9]",
        "needsShovel": False, "purchase": False, "chestAngle": 0,
		"minGoldenFeathers": 0, "minGoldenFeathersEasy": 0, "minGoldenFeathersBucket": 0},
]
