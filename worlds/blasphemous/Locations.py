from typing import List, TypedDict


class LocationDict(TypedDict):
    name: str
    region: str


location_table: List[LocationDict] = [
    # Albero (35)
    {'name': "Albero: Sick house",
        'region': "albero"},
    {'name': "Albero: Outside ossuary",
        'region': "albero"},
    {'name': "Albero: Graveyard",
        'region': "albero"},
    {'name': "Albero: Warp room",
        'region': "albero"},
    {'name': "Albero: Elevator cherub",
        'region': "albero"},
    {'name': "Albero: Bless cloth",
        'region': "albero"},
    {'name': "Albero: Bless egg",
        'region': "albero"},
    {'name': "Albero: Bless hand",
        'region': "albero"},
    {'name': "Albero: Cleofas gift initial",
        'region': "albero"},
    {'name': "Albero: Cleofas gift final",
        'region': "albero"},
    {'name': "Albero: Tirso reward 1",
        'region': "albero"},
    {'name': "Albero: Tirso reward 2",
        'region': "albero"},
    {'name': "Albero: Tirso reward 3",
        'region': "albero"},
    {'name': "Albero: Tirso reward 4",
        'region': "albero"},
    {'name': "Albero: Tirso reward 5",
        'region': "albero"},
    {'name': "Albero: Tirso reward 6",
        'region': "albero"},
    {'name': "Albero: Tirso reward final",
        'region': "albero"},
    {'name': "Albero: Tentudia reward 1",
        'region': "albero"},
    {'name': "Albero: Tentudia reward 2",
        'region': "albero"},
    {'name': "Albero: Tentudia reward 3",
        'region': "albero"},
    {'name': "Ossuary: Isidora reward main",
        'region': "albero"},
    {'name': "Albero: Sword room",
        'region': "albero"},
    {'name': "Albero: Church donation 1",
        'region': "albero"},
    {'name': "Albero: Church donation 2",
        'region': "albero"},
    {'name': "Ossuary: Reward 1",
        'region': "albero"},
    {'name': "Ossuary: Reward 2",
        'region': "albero"},
    {'name': "Ossuary: Reward 3",
        'region': "albero"},
    {'name': "Ossuary: Reward 4",
        'region': "albero"},
    {'name': "Ossuary: Reward 5",
        'region': "albero"},
    {'name': "Ossuary: Reward 6",
        'region': "albero"},
    {'name': "Ossuary: Reward 7",
        'region': "albero"},
    {'name': "Ossuary: Reward 8",
        'region': "albero"},
    {'name': "Ossuary: Reward 9",
        'region': "albero"},
    {'name': "Ossuary: Reward 10",
        'region': "albero"},
    {'name': "Ossuary: Reward 11",
        'region': "albero"},
    
    # All the Tears of the Sea (1)
    {'name': "AtTotS: Miriam gift",
        'region': "attots"},

    # Archcathedral Rooftops (11)
    {'name': "AR: Bridge fight 1",
        'region': "ar"},
    {'name': "AR: Bridge fight 2",
        'region': "ar"},
    {'name': "AR: Bridge fight 3",
        'region': "ar"},
    {'name': "AR: Western shaft ledge",
        'region': "ar"},
    {'name': "AR: Western shaft cherub",
        'region': "ar"},
    {'name': "AR: Western shaft chest",
        'region': "ar"},
    {'name': "AR: MoM east entrance",
        'region': "ar"},
    {'name': "AR: Lady room",
        'region': "ar"},
    {'name': "AR: Second checkpoint ledge",
        'region': "ar"},
    {'name': "AR: Sword room",
        'region': "ar"},
    {'name': "AR: Crisanta",
        'region': "ar"},

    # Bridge of the Three Cavalries (3)
    {'name': "BotTC: Esdras",
        'region': "bottc"},
    {'name': "BotTC: Esdras gift initial",
        'region': "bottc"},
    {'name': "BotTC: Amanecida core",
        'region': "bottc"},

    # Brotherhood of the Silent Sorrow (11)
    {'name': "BotSS: Beginning gift",
        'region': "botss"},
    {'name': "BotSS: Initial room cherub",
        'region': "botss"},
    {'name': "BotSS: Initial room ledge",
        'region': "botss"},
    {'name': "BotSS: Elder Brother's room",
        'region': "botss"},
    {'name': "BotSS: Sword room",
        'region': "botss"},
    {'name': "BotSS: Spike gauntlet exit",
        'region': "botss"},
    {'name': "BotSS: Blue candle",
        'region': "botss"},
    {'name': "BotSS: Church entrance",
        'region': "botss"},
    {'name': "BotSS: Esdras gift final",
        'region': "botss"},
    {'name': "BotSS: Crisanta gift",
        'region': "botss"},
    {'name': "BotSS: Warden of the Silent Sorrow",
        'region': "botss"},
    
    # Convent of Our Lady of the Charred Visage (13)
    {'name': "CoOLotCV: Blood platform ledge",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Ghost death room",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Central lung room",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Southwest lung room",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Lady room",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Sword room",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Red candle",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Blue candle",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Outside area",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Burning oil fountain",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Our Lady of the Charred Visage",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Holy Visage gift",
        'region': "coolotcv"},
    {'name': "CoOLotCV: Mask room",
        'region': "coolotcv"},

    # Deambulatory of His Holiness (3)
    {'name': "DoHH: Complete Penitence 1",
        'region': "dohh"},
    {'name': "DoHH: Complete Penitence 2",
        'region': "dohh"},
    {'name': "DoHH: Complete Penitence 3",
        'region': "dohh"},

    # Desecrated Cistern (20)
    {'name': "DC: MeD lady room",
        'region': "dc"},
    {'name': "DC: MeD entrance",
        'region': "dc"},
    {'name': "DC: Water room cherub",
        'region': "dc"},
    {'name': "DC: Eastern lower tunnel chest",
        'region': "dc"},
    {'name': "DC: Eastern upper tunnel chest",
        'region': "dc"},
    {'name': "DC: Eastern upper tunnel cherub",
        'region': "dc"},
    {'name': "DC: Hidden hand room",
        'region': "dc"},
    {'name': "DC: WaBC entrance",
        'region': "dc"},
    {'name': "DC: Oil room",
        'region': "dc"},
    {'name': "DC: Veil room cherub",
        'region': "dc"},
    {'name': "DC: Veil room ledge",
        'region': "dc"},
    {'name': "DC: Lung tunnel cherub",
        'region': "dc"},
    {'name': "DC: Lung tunnel ledge",
        'region': "dc"},
    {'name': "DC: Shroud puzzle",
        'region': "dc"},
    {'name': "DC: Chalice room",
        'region': "dc"},
    {'name': "DC: Sword room",
        'region': "dc"},
    {'name': "DC: GrA lady room",
        'region': "dc"},
    {'name': "DC: Elevator exit cherub",
        'region': "dc"},
    {'name': "DC: Elevator shaft cherub",
        'region': "dc"},
    {'name': "DC: Elevator shaft ledge",
        'region': "dc"},

    # Echoes of Salt (2)
    {'name': "EoS: MoED entrance",
        'region': "eos"},
    {'name': "EoS: Near elevator shaft",
        'region': "eos"},
    
    # Graveyard of the Peaks (21)
    {'name': "GotP: Shop cave cherub",
        'region': "gotp"},
    {'name': "GotP: Shop cave hole",
        'region': "gotp"},
    {'name': "GotP: Shop left",
        'region': "gotp"},
    {'name': "GotP: Shop middle",
        'region': "gotp"},
    {'name': "GotP: Shop right",
        'region': "gotp"},
    {'name': "GotP: Guilt room",
        'region': "gotp"},
    {'name': "GotP: Elevator shaft cherub",
        'region': "gotp"},
    {'name': "GotP: Elevator shaft ledge",
        'region': "gotp"},
    {'name': "GotP: Lady room",
        'region': "gotp"},
    {'name': "GotP: Bleed room",
        'region': "gotp"},
    {'name': "GotP: Eastern shaft lower",
        'region': "gotp"},
    {'name': "GotP: Eastern shaft middle",
        'region': "gotp"},
    {'name': "GotP: Eastern shaft upper",
        'region': "gotp"},
    {'name': "GotP: Amanecida ledge",
        'region': "gotp"},
    {'name': "GotP: Western shaft cherub",
        'region': "gotp"},
    {'name': "GotP: Western shaft lower",
        'region': "gotp"},
    {'name': "GotP: Western shaft middle",
        'region': "gotp"},
    {'name': "GotP: Western shaft upper",
        'region': "gotp"},
    {'name': "GotP: Center shaft cherub",
        'region': "gotp"},
    {'name': "GotP: Center shaft ledge",
        'region': "gotp"},
    {'name': "GotP: Oil room",
        'region': "gotp"},
    {'name': "GotP: Bow Amanecida",
        'region': "gotp"},
    
    # Grievance Ascends (12)
    {'name': "GA: Western lung ledge",
        'region': "ga"},
    {'name': "GA: Lung room upper",
        'region': "ga"},
    {'name': "GA: Lung room cherub",
        'region': "ga"},
    {'name': "GA: Lung room lower",
        'region': "ga"},
    {'name': "GA: Oil room",
        'region': "ga"},
    {'name': "GA: Blood tunnel ledge",
        'region': "ga"},
    {'name': "GA: Blood tunnel cherub",
        'region': "ga"},
    {'name': "GA: Altasgracias cherub",
        'region': "ga"},
    {'name': "GA: Altasgracias gift",
        'region': "ga"},
    {'name': "GA: Altasgracias cocoon",
        'region': "ga"},
    {'name': "GA: Tres Angustias",
        'region': "ga"},
    {'name': "GA: Holy Visage gift",
        'region': "ga"},
    
    # Hall of the Dawning (2)
    {'name': "HotD: Mirror room",
        'region': "hotd"},
    {'name': "HotD: Laudes",
        'region': "hotd"},
    
    # Jondo (13)
    {'name': "Jondo: Eastern entrance ledge",
        'region': "jondo"},
    {'name': "Jondo: Eastern entrance chest",
        'region': "jondo"},
    {'name': "Jondo: Eastern shaft bell chargers",
        'region': "jondo"},
    {'name': "Jondo: Eastern shaft bell trap",
        'region': "jondo"},
    {'name': "Jondo: Eastern shaft cherub",
        'region': "jondo"},
    {'name': "Jondo: Spike tunnel cherub",
        'region': "jondo"},
    {'name': "Jondo: Spike tunnel ledge",
        'region': "jondo"},
    {'name': "Jondo: EcS entrance",
        'region': "jondo"},
    {'name': "Jondo: Western shaft lower slide",
        'region': "jondo"},
    {'name': "Jondo: Western shaft bell trap",
        'region': "jondo"},
    {'name': "Jondo: Western shaft bell puzzle",
        'region': "jondo"},
    {'name': "Jondo: Western shaft root puzzle",
        'region': "jondo"},
    {'name': "Jondo: Western shaft cherub",
        'region': "jondo"},
    
    # Knot of the Three Words (1)
    {'name': "KotTW: Fourth Visage gift",
        'region': "kottw"},
    
    # Library of the Negated Words (18)
    {'name': "LotNW: Platform room cherub",
        'region': "lotnw"},
    {'name': "LotNW: Platform room ledge",
        'region': "lotnw"},
    {'name': "LotNW: Upper cathedral ledge",
        'region': "lotnw"},
    {'name': "LotNW: Hidden floor",
        'region': "lotnw"},
    {'name': "LotNW: Lung ambush chest",
        'region': "lotnw"},
    {'name': "LotNW: Lady room",
        'region': "lotnw"},
    {'name': "LotNW: Bone puzzle",
        'region': "lotnw"},
    {'name': "LotNW: Diosdado ledge",
        'region': "lotnw"},
    {'name': "LotNW: Platform puzzle chest",
        'region': "lotnw"},
    {'name': "LotNW: Final shaft ledge",
        'region': "lotnw"},
    {'name': "LotNW: Final shaft cherub",
        'region': "lotnw"},
    {'name': "LotNW: Oil room",
        'region': "lotnw"},
    {'name': "LotNW: Elevator cherub",
        'region': "lotnw"},
    {'name': "LotNW: Mask room",
        'region': "lotnw"},
    {'name': "LotNW: Sword room",
        'region': "lotnw"},
    {'name': "LotNW: Red candle",
        'region': "lotnw"},
    {'name': "LotNW: Diosdado gift",
        'region': "lotnw"},
    {'name': "LotNW: Fourth Visage hidden wall",
        'region': "lotnw"},

    # Mercy Dreams (15)
    {'name': "MD: First section hidden wall",
        'region': "md"},
    {'name': "MD: Second section ghost ambush",
        'region': "md"},
    {'name': "MD: Second section ledge",
        'region': "md"},
    {'name': "MD: Second section cherub",
        'region': "md"},
    {'name': "MD: Red candle",
        'region': "md"},
    {'name': "MD: Shop left",
        'region': "md"},
    {'name': "MD: Shop middle",
        'region': "md"},
    {'name': "MD: Shop right",
        'region': "md"},
    {'name': "MD: Third section hidden wall",
        'region': "md"},
    {'name': "MD: Third section lower corridor",
        'region': "md"},
    {'name': "MD: Ten Piedad",
        'region': "md"},
    {'name': "MD: Holy Visage gift",
        'region': "md"},
    {'name': "MD: Blue candle",
        'region': "md"},
    {'name': "MD: SlC entrance cherub",
        'region': "md"},
    {'name': "MD: SlC entrance ledge",
        'region': "md"},

    # Mother of Mothers (14)
    {'name': "MoM: Oil room",
        'region': "mom"},
    {'name': "MoM: Eastern room upper",
        'region': "mom"},
    {'name': "MoM: Eastern room lower",
        'region': "mom"},
    {'name': "MoM: Western room cherub",
        'region': "mom"},
    {'name': "MoM: Western room ledge",
        'region': "mom"},
    {'name': "MoM: Redento prayer room",
        'region': "mom"},
    {'name': "MoM: Redento corpse",
        'region': "mom"},
    {'name': "MoM: Blood incense shaft",
        'region': "mom"},
    {'name': "MoM: Outside Cleofas room",
        'region': "mom"},
    {'name': "MoM: Center room ledge",
        'region': "mom"},
    {'name': "MoM: Center room cherub",
        'region': "mom"},
    {'name': "MoM: Sword room",
        'region': "mom"},
    {'name': "MoM: Melquiades",
        'region': "mom"},
    {'name': "MoM: Mask room",
        'region': "mom"},

    # Mountains of the Endless Dusk (8)
    {'name': "MotED: DeC entrance",
        'region': "moted"},
    {'name': "MotED: Petpetua gift",
        'region': "moted"},
    {'name': "MotED: Bell gap cherub",
        'region': "moted"},
    {'name': "MotED: Bell gap ledge",
        'region': "moted"},
    {'name': "MotED: Redento meeting 1",
        'region': "moted"},
    {'name': "MotED: Blood platform",
        'region': "moted"},
    {'name': "MotED: Egg hatching",
        'region': "moted"},
    {'name': "MotED: Axe Amanecida",
        'region': "moted"},

    # Mourning and Havoc (4)
    {'name': "MaH: Western chest",
        'region': "mah"},
    {'name': "MaH: Eastern chest",
        'region': "mah"},
    {'name': "MaH: Sierpes reward",
        'region': "mah"},
    {'name': "MaH: Sierpes",
        'region': "mah"},
    
    # Patio of the Silent Steps (9)
    {'name': "PotSS: Garden 1 cherub",
        'region': "potss"},
    {'name': "PotSS: Garden 1 ledge",
        'region': "potss"},
    {'name': "PotSS: Garden 2 ledge",
        'region': "potss"},
    {'name': "PotSS: Garden 3 cherub",
        'region': "potss"},
    {'name': "PotSS: Garden 3 lower ledge",
        'region': "potss"},
    {'name': "PotSS: Garden 3 upper ledge",
        'region': "potss"},
    {'name': "PotSS: Northern shaft",
        'region': "potss"},
    {'name': "PotSS: Redento meeting 4",
        'region': "potss"},
    {'name': "PotSS: Falcata Amanecida",
        'region': "potss"},

    # Petrous (1)
    {'name': "Petrous: Entrance room",
        'region': "petrous"},

    # The Resting Place of the Sister (1)
    {'name': "TRPotS: Perpetua shrine",
        'region': "trpots"},
    
    # The Sleeping Canvases (10)
    {'name': "TSC: Herb shaft",
        'region': "tsc"},
    {'name': "TSC: Wax bleed puzzle",
        'region': "tsc"},
    {'name': "TSC: Shop left",
        'region': "tsc"},
    {'name': "TSC: Shop middle",
        'region': "tsc"},
    {'name': "TSC: Shop right",
        'region': "tsc"},
    {'name': "TSC: Low tunnel blade trap",
        'region': "tsc"},
    {'name': "TSC: Exposito",
        'region': "tsc"},
    {'name': "TSC: Linen drop room",
        'region': "tsc"},
    {'name': "TSC: Jocinero gift initial",
        'region': "tsc"},
    {'name': "TSC: Jocinero gift final",
        'region': "tsc"},

    # The Holy Line (6)
    {'name': "THL: Deosgracias gift",
        'region': "thl"},
    {'name': "THL: Mud ledge lower",
        'region': "thl"},
    {'name': "THL: Mud ledge upper",
        'region': "thl"},
    {'name': "THL: Mud cherub",
        'region': "thl"},
    {'name': "THL: Cave ledge",
        'region': "thl"},
    {'name': "THL: Cave chest",
        'region': "thl"},

    # Wall of the Holy Prohibitions (19)
    {'name': "WotHP: Q1 lift puzzle",
        'region': "wothp"},
    {'name': "WotHP: Q1 drop room upper",
        'region': "wothp"},
    {'name': "WotHP: Q1 drop room lower",
        'region': "wothp"},
    {'name': "WotHP: Q1 upper bronze door",
        'region': "wothp"},
    {'name': "WotHP: Q1 upper silver door",
        'region': "wothp"},
    {'name': "WotHP: Q1 middle gold door",
        'region': "wothp"},
    {'name': "WotHP: Q2 middle gold door",
        'region': "wothp"},
    {'name': "WotHP: Q3 lower gold door",
        'region': "wothp"},
    {'name': "WotHP: Q3 upper silver door",
        'region': "wothp"},
    {'name': "WotHP: Q3 upper ledge",
        'region': "wothp"},
    {'name': "WotHP: Q4 hidden ledge",
        'region': "wothp"},
    {'name': "WotHP: Q4 lower silver door",
        'region': "wothp"},
    {'name': "WotHP: Q4 upper bronze door",
        'region': "wothp"},
    {'name': "WotHP: Q4 upper silver door",
        'region': "wothp"},
    {'name': "WotHP: CoLCV entrance",
        'region': "wothp"},
    {'name': "WotHP: Oil room",
        'region': "wothp"},
    {'name': "WotHP: Quirce",
        'region': "wothp"},
    {'name': "WotHP: Quirce room",
        'region': "wothp"},
    {'name': "WotHP: Lance Amanecida",
        'region': "wothp"},

    # Wasteland of the Buried Churches (8)
    {'name': "WotBC: Lower tree path",
        'region': "wotbc"},
    {'name': "WotBC: Building slide",
        'region': "wotbc"},
    {'name': "WotBC: Exterior ledge",
        'region': "wotbc"},
    {'name': "WotBC: Exterior cherub",
        'region': "wotbc"},
    {'name': "WotBC: Underneath MeD bridge",
        'region': "wotbc"},
    {'name': "WotBC: Cliffside ledge",
        'region': "wotbc"},
    {'name': "WotBC: Cliffside cherub",
        'region': "wotbc"},
    {'name': "WotBC: Redento meeting 3",
        'region': "wotbc"},
    
    # Where Olive Trees Wither (11)
    {'name': "WOTW: WaBC entrance",
        'region': "wotw"},
    {'name': "WOTW: Healing cave",
        'region': "wotw"},
    {'name': "WOTW: White lady flower",
        'region': "wotw"},
    {'name': "WOTW: White lady tomb",
        'region': "wotw"},
    {'name': "WOTW: White lady cave cherub",
        'region': "wotw"},
    {'name': "WOTW: White lady cave ledge",
        'region': "wotw"},
    {'name': "WOTW: Eastern root cherub",
        'region': "wotw"},
    {'name': "WOTW: Eastern root ledge",
        'region': "wotw"},
    {'name': "WOTW: Death run",
        'region': "wotw"},
    {'name': "WOTW: Gemino gift initial",
        'region': "wotw"},
    {'name': "WOTW: Gemino gift final",
        'region': "wotw"},

    # Various (20)
    {'name': "Guilt arena 1 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 1 main",
        'region': "dungeon"},
    {'name': "Guilt arena 2 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 2 main",
        'region': "dungeon"},
    {'name': "Guilt arena 3 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 3 main",
        'region': "dungeon"},
    {'name': "Guilt arena 4 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 4 main",
        'region': "dungeon"},
    {'name': "Guilt arena 5 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 5 main",
        'region': "dungeon"},
    {'name': "Guilt arena 6 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 6 main",
        'region': "dungeon"},
    {'name': "Guilt arena 7 extra",
        'region': "dungeon"},
    {'name': "Guilt arena 7 main",
        'region': "dungeon"},
    {'name': "Viridiana gift",
        'region': "ar"},
    {'name': "Amanecida 1",
        'region': "dungeon"},
    {'name': "Amanecida 2",
        'region': "dungeon"},
    {'name': "Amanecida 3",
        'region': "dungeon"},
    {'name': "Amanecida 4",
        'region': "dungeon"},
    {'name': "All amanecidas reward",
        'region': "dungeon"},
]