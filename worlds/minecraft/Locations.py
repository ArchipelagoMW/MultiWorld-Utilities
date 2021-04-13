from BaseClasses import Region, Entrance, Location, MultiWorld, Item
import typing

class MinecraftAdvancement(Location): 
    game: str = "Minecraft"
    def __init__(self, player: int, name: str, address: int, parent):
        super().__init__(player, name, address, parent)

advancement_table = {
    "Who is Cutting Onions?": 42000,
    "Oh Shiny": 42001,
    "Suit Up": 42002,
    "Very Very Frightening": 42003,
    "Hot Stuff": 42004,
    "Free the End": 42005,
    "A Furious Cocktail": 42006,
    "Best Friends Forever": 42007,
    "Bring Home the Beacon": 42008,
    "Not Today, Thank You": 42009,
    "Isn't It Iron Pick": 42010,
    "Local Brewery": 42011,
    "The Next Generation": 42012,
    "Fishy Business": 42013,
    "Hot Tourist Destinations": 42014,
    "This Boat Has Legs": 42015,
    "Sniper Duel": 42016,
    "Nether": 42017,
    "Great View From Up Here": 42018,
    "How Did We Get Here?": 42019,
    "Bullseye": 42020,
    "Spooky Scary Skeleton": 42021,
    "Two by Two": 42022,
    "Stone Age": 42023,
    "Two Birds, One Arrow": 42024,
    "We Need to Go Deeper": 42025,
    "Who's the Pillager Now?": 42026,
    "Getting an Upgrade": 42027,
    "Tactical Fishing": 42028,
    "Zombie Doctor": 42029,
    "The City at the End of the Game": 42030,
    "Ice Bucket Challenge": 42031,
    "Remote Getaway": 42032,
    "Into Fire": 42033,
    "War Pigs": 42034,
    "Take Aim": 42035,
    "Total Beelocation": 42036,
    "Arbalistic": 42037,    
    "The End... Again...": 42038,
    "Acquire Hardware": 42039,
    "Not Quite \"Nine\" Lives": 42040,
    "Cover Me With Diamonds": 42041,
    "Sky's the Limit": 42042,
    "Hired Help": 42043,
    "Return to Sender": 42044,
    "Sweet Dreams": 42045,
    "You Need a Mint": 42046,
    "Adventure": 42047,
    "Monsters Hunted": 42048,
    "Enchanter": 42049,
    "Voluntary Exile": 42050,
    "Eye Spy": 42051,
    "The End": 42052,
    "Serious Dedication": 42053,
    "Postmortal": 42054,
    "Monster Hunter": 42055,
    "Adventuring Time": 42056,
    "A Seedy Place": 42057,
    "Those Were the Days": 42058,
    "Hero of the Village": 42059,
    "Hidden in the Depths": 42060,
    "Beaconator": 42061,
    "Withering Heights": 42062,
    "A Balanced Diet": 42063,
    "Subspace Bubble": 42064,
    "Husbandry": 42065,
    "Country Lode, Take Me Home": 42066,
    "Bee Our Guest": 42067,
    "What a Deal!": 42068,
    "Uneasy Alliance": 42069,
    "Diamonds!": 42070,
    "A Terrible Fortress": 42071,
    "A Throwaway Joke": 42072,
    "Minecraft": 42073,
    "Sticky Situation": 42074,
    "Ol' Betsy": 42075,
    "Cover Me in Debris": 42076,
    "The End?": 42077,
    "The Parrots and the Bats": 42078,
    "A Complete Catalogue": 42079
}

exclusion_table = {
    "hard": {
        "Very Very Frightening": "50 XP",
        "Two by Two": "100 XP",
        "Two Birds, One Arrow": "50 XP",
        "Arbalistic": "100 XP",
        "Beaconator": "50 XP",
        "A Balanced Diet": "100 XP",
        "Uneasy Alliance": "100 XP",
        "Cover Me in Debris": "100 XP",
        "A Complete Catalogue": "50 XP"
    }, 
    "insane": {
        "How Did We Get Here?": "500 XP",
        "Adventuring Time": "500 XP"
    },
    "postgame": {
        "The Next Generation": "50 XP",
        "The End... Again...": "50 XP",
        "You Need a Mint": "50 XP", 
        "Monsters Hunted": "100 XP"
    }
}


lookup_id_to_name: typing.Dict[int, str] = {loc_id: loc_name for loc_name, loc_id in advancement_table.items()}
