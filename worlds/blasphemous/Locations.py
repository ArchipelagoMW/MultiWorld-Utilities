from typing import List, TypedDict


class LocationDict(TypedDict):
    name: str
    region: str
    game_id: str
    room: str


location_table: List[LocationDict] = [
    # Albero (35)
    {'name': "Albero: Sick house",
        'region': "albero",
        'game_id': "RB01",
        'room': "D01Z02S02"},
    {'name': "Albero: Outside ossuary",
        'region': "albero",
        'game_id': "CO43",
        'room': "D01Z02S04"},
    {'name': "Albero: Graveyard",
        'region': "albero",
        'game_id': "CO16",
        'room': "D01Z02S05"},
    {'name': "Albero: Warp room",
        'region': "albero",
        'game_id': "QI65",
        'room': "D01Z02S07"},
    {'name': "Albero: Elevator cherub",
        'region': "albero",
        'game_id': "RESCUED_CHERUB_08",
        'room': "D01Z02S03"},
    {'name': "Albero: Bless cloth",
        'region': "albero",
        'game_id': "RE04",
        'room': "D01Z02S01"},
    {'name': "Albero: Bless egg",
        'region': "albero",
        'game_id': "RE10",
        'room': "D01Z02S01"},
    {'name': "Albero: Bless hand",
        'region': "albero",
        'game_id': "RE02",
        'room': "D01Z02S01"},
    {'name': "Albero: Cleofas gift initial",
        'region': "albero",
        'game_id': "QI01",
        'room': "D01Z02S03"},
    {'name': "Albero: Cleofas gift final",
        'region': "albero",
        'game_id': "PR11",
        'room': "D01Z02S03"},
    {'name': "Albero: Tirso reward 1",
        'region': "albero",
        'game_id': "QI66",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward 2",
        'region': "albero",
        'game_id': "Tirso[500]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward 3",
        'region': "albero",
        'game_id': "Tirso[1000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward 4",
        'region': "albero",
        'game_id': "Tirso[2000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward 5",
        'region': "albero",
        'game_id': "Tirso[5000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward 6",
        'region': "albero",
        'game_id': "Tirso[10000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso reward final",
        'region': "albero",
        'game_id': "QI56",
        'room': "D01Z02S02"},
    {'name': "Albero: Tentudia reward 1",
        'region': "albero",
        'game_id': "Lvdovico[500]",
        'room': "D01Z02S03"},
    {'name': "Albero: Tentudia reward 2",
        'region': "albero",
        'game_id': "Lvdovico[1000]",
        'room': "D01Z02S03"},
    {'name': "Albero: Tentudia reward 3",
        'region': "albero",
        'game_id': "PR03",
        'room': "D01Z02S03"},
    {'name': "Ossuary: Isidora reward main",
        'region': "albero",
        'game_id': "QI201",
        'room': "D01BZ08S01"},
    {'name': "Albero: Sword room",
        'region': "albero",
        'game_id': "Sword[D01Z02S06]",
        'room': "D01Z02S06"},
    {'name': "Albero: Church donation 1",
        'region': "albero",
        'game_id': "RB104",
        'room': "D01BZ04S01"},
    {'name': "Albero: Church donation 2",
        'region': "albero",
        'game_id': "RB105",
        'room': "D01BZ04S01"},
    {'name': "Ossuary: Reward 1",
        'region': "albero",
        'game_id': "Undertaker[250]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 2",
        'region': "albero",
        'game_id': "Undertaker[500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 3",
        'region': "albero",
        'game_id': "Undertaker[750]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 4",
        'region': "albero",
        'game_id': "Undertaker[1000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 5",
        'region': "albero",
        'game_id': "Undertaker[1250]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 6",
        'region': "albero",
        'game_id': "Undertaker[1500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 7",
        'region': "albero",
        'game_id': "Undertaker[1750]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 8",
        'region': "albero",
        'game_id': "Undertaker[2000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 9",
        'region': "albero",
        'game_id': "Undertaker[2500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 10",
        'region': "albero",
        'game_id': "Undertaker[3000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: Reward 11",
        'region': "albero",
        'game_id': "Undertaker[5000]",
        'room': "D01BZ06S01"},
    
    # All the Tears of the Sea (1)
    {'name': "AtTotS: Miriam gift",
        'region': "attots",
        'game_id': "PR201",
        'room': "D04Z04S02"},

    # Archcathedral Rooftops (11)
    {'name': "AR: Bridge fight 1",
        'region': "ar",
        'game_id': "QI02",
        'room': "D06Z01S03"},
    {'name': "AR: Bridge fight 2",
        'region': "ar",
        'game_id': "QI03",
        'room': "D06Z01S06"},
    {'name': "AR: Bridge fight 3",
        'region': "ar",
        'game_id': "QI04",
        'room': "D06Z01S21"},
    {'name': "AR: Western shaft ledge",
        'region': "ar",
        'game_id': "CO06",
        'room': "D06Z01S12"},
    {'name': "AR: Western shaft cherub",
        'region': "ar",
        'game_id': "RESCUED_CHERUB_36",
        'room': "D06Z01S12"},
    {'name': "AR: Western shaft chest",
        'region': "ar",
        'game_id': "PR12",
        'room': "D06Z01S12"},
    {'name': "AR: MoM east entrance",
        'region': "ar",
        'game_id': "HE04",
        'room': "D06Z01S22"},
    {'name': "AR: Lady room",
        'region': "ar",
        'game_id': "Lady[D06Z01S24]",
        'room': "D06Z01S24"},
    {'name': "AR: Second checkpoint ledge",
        'region': "ar",
        'game_id': "CO40",
        'room': "D06Z01S15"},
    {'name': "AR: Sword room",
        'region': "ar",
        'game_id': "Sword[D06Z01S11]",
        'room': "D06Z01S11"},
    {'name': "AR: Crisanta",
        'region': "ar",
        'game_id': "BS16",
        'room': "D06Z01S25"},

    # Bridge of the Three Cavalries (3)
    {'name': "BotTC: Esdras",
        'region': "bottc",
        'game_id': "BS12",
        'room': "D08Z01S01"},
    {'name': "BotTC: Esdras gift initial",
        'region': "bottc",
        'game_id': "PR09",
        'room': "D08Z01S01"},
    {'name': "BotTC: Amanecida core",
        'region': "bottc",
        'game_id': "HE101",
        'room': "D08Z01S02"},

    # Brotherhood of the Silent Sorrow (11)
    {'name': "BotSS: Beginning gift",
        'region': "botss",
        'game_id': "QI106",
        'room': "D17Z01S01"},
    {'name': "BotSS: Initial room cherub",
        'region': "botss",
        'game_id': "RESCUED_CHERUB_06",
        'room': "D17Z01S01"},
    {'name': "BotSS: Initial room ledge",
        'region': "botss",
        'game_id': "RB204",
        'room': "D17Z01S01"},
    {'name': "BotSS: Elder Brother's room",
        'region': "botss",
        'game_id': "RE01",
        'room': "D17BZ01S01[relic]"},
    {'name': "BotSS: Sword room",
        'region': "botss",
        'game_id': "Sword[D17Z01S08]",
        'room': "D17Z01S08"},
    {'name': "BotSS: Spike gauntlet exit",
        'region': "botss",
        'game_id': "CO25",
        'room': "D17Z01S04"},
    {'name': "BotSS: Blue candle",
        'region': "botss",
        'game_id': "RB25",
        'room': "D17Z01S04"},
    {'name': "BotSS: Church entrance",
        'region': "botss",
        'game_id': "PR203",
        'room': "D17Z01S14"},
    {'name': "BotSS: Esdras gift final",
        'region': "botss",
        'game_id': "QI204",
        'room': "D17Z01S15"},
    {'name': "BotSS: Crisanta gift",
        'region': "botss",
        'game_id': "QI301",
        'room': "D17Z01S15"},
    {'name': "BotSS: Warden of the Silent Sorrow",
        'region': "botss",
        'game_id': "BS13",
        'room': "D17Z01S11"},
    
    # Convent of Our Lady of the Charred Visage (13)
    {'name': "CoOLotCV: Blood platform ledge",
        'region': "coolotcv",
        'game_id': "CO05",
        'room': "D02Z03S03"},
    {'name': "CoOLotCV: Ghost death room",
        'region': "coolotcv",
        'game_id': "CO15",
        'room': "D02Z03S07"},
    {'name': "CoOLotCV: Central lung room",
        'region': "coolotcv",
        'game_id': "RB08",
        'room': "D02Z03S05"},
    {'name': "CoOLotCV: Southwest lung room",
        'region': "coolotcv",
        'game_id': "HE03",
        'room': "D02Z03S12"},
    {'name': "CoOLotCV: Lady room",
        'region': "coolotcv",
        'game_id': "Lady[D02Z03S15]",
        'room': "D02Z03S15"},
    {'name': "CoOLotCV: Sword room",
        'region': "coolotcv",
        'game_id': "Sword[D02Z03S13]",
        'room': "D02Z03S13"},
    {'name': "CoOLotCV: Red candle",
        'region': "coolotcv",
        'game_id': "RB18",
        'room': "D02Z03S06"},
    {'name': "CoOLotCV: Blue candle",
        'region': "coolotcv",
        'game_id': "RB24",
        'room': "D02Z03S17"},
    {'name': "CoOLotCV: Outside area",
        'region': "coolotcv",
        'game_id': "RB107",
        'room': "D02Z03S23"},
    {'name': "CoOLotCV: Burning oil fountain",
        'region': "coolotcv",
        'game_id': "QI57",
        'room': "D02Z03S21"},
    {'name': "CoOLotCV: Our Lady of the Charred Visage",
        'region': "coolotcv",
        'game_id': "BS03",
        'room': "D02Z03S20"},
    {'name': "CoOLotCV: Holy Visage gift",
        'region': "coolotcv",
        'game_id': "QI40",
        'room': "D02Z03S21"},
    {'name': "CoOLotCV: Mask room",
        'region': "coolotcv",
        'game_id': "QI61",
        'room': "D02Z03S19"},

    # Deambulatory of His Holiness (3)
    {'name': "DoHH: Viridiana gift",
        'region': "dohh",
        'game_id': "PR08",
        'room': "D07Z01S01"},
    {'name': "DoHH: Complete Penitence 1",
        'region': "dohh",
        'game_id': "RB101",
        'room': "D07Z01S03"},
    {'name': "DoHH: Complete Penitence 2",
        'region': "dohh",
        'game_id': "RB102",
        'room': "D07Z01S03"},
    {'name': "DoHH: Complete Penitence 3",
        'region': "dohh",
        'game_id': "RB103",
        'room': "D07Z01S03"},

    # Desecrated Cistern (20)
    {'name': "DC: MeD lady room",
        'region': "dc",
        'game_id': "Lady[D01Z05S22]",
        'room': "D01Z05S22"},
    {'name': "DC: MeD entrance",
        'region': "dc",
        'game_id': "CO41",
        'room': "D01Z05S15"},
    {'name': "DC: Water room cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_11",
        'room': "D01Z05S14"},
    {'name': "DC: Eastern lower tunnel chest",
        'region': "dc",
        'game_id': "QI45",
        'room': "D01Z05S11"},
    {'name': "DC: Eastern upper tunnel chest",
        'region': "dc",
        'game_id': "PR16",
        'room': "D01Z05S06"},
    {'name': "DC: Eastern upper tunnel cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_13",
        'room': "D01Z05S06"},
    {'name': "DC: Hidden hand room",
        'region': "dc",
        'game_id': "QI67",
        'room': "D01Z05S05"},
    {'name': "DC: WaBC entrance",
        'region': "dc",
        'game_id': "CO09",
        'room': "D01Z05S05"},
    {'name': "DC: Oil room",
        'region': "dc",
        'game_id': "Oil[D01Z05S07]",
        'room': "D01Z05S07"},
    {'name': "DC: Veil room cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_14",
        'room': "D01Z05S08"},
    {'name': "DC: Veil room ledge",
        'region': "dc",
        'game_id': "QI12",
        'room': "D01Z05S08"},
    {'name': "DC: Lung tunnel cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_12",
        'room': "D01Z05S13"},
    {'name': "DC: Lung tunnel ledge",
        'region': "dc",
        'game_id': "CO32",
        'room': "D01Z05S17"},
    {'name': "DC: Shroud puzzle",
        'region': "dc",
        'game_id': "RB03",
        'room': "D01Z05S21"},
    {'name': "DC: Chalice room",
        'region': "dc",
        'game_id': "QI75",
        'room': "D01Z05S23"},
    {'name': "DC: Sword room",
        'region': "dc",
        'game_id': "Sword[D01Z05S24]",
        'room': "D01Z05S24"},
    {'name': "DC: GrA lady room",
        'region': "dc",
        'game_id': "Lady[D01Z05S26]",
        'room': "D01Z05S26"},
    {'name': "DC: Elevator exit cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_15",
        'room': "D01Z05S20"},
    {'name': "DC: Elevator shaft cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_22",
        'room': "D01Z05S25"},
    {'name': "DC: Elevator shaft ledge",
        'region': "dc",
        'game_id': "CO44",
        'room': "D01Z05S25"},

    # Echoes of Salt (2)
    {'name': "EoS: MoED entrance",
        'region': "eos",
        'game_id': "RB108",
        'room': "D20Z01S02"},
    {'name': "EoS: Near elevator shaft",
        'region': "eos",
        'game_id': "RB202",
        'room': "D20Z01S09"},
    
    # Graveyard of the Peaks (21)
    {'name': "GotP: Shop cave cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_31",
        'room': "D02Z02S08"},
    {'name': "GotP: Shop cave hole",
        'region': "gotp",
        'game_id': "CO42",
        'room': "D02Z02S08"},
    {'name': "GotP: Shop left",
        'region': "gotp",
        'game_id': "QI11",
        'room': "D02BZ01S01"},
    {'name': "GotP: Shop middle",
        'region': "gotp",
        'game_id': "RB37",
        'room': "D02BZ01S01"},
    {'name': "GotP: Shop right",
        'region': "gotp",
        'game_id': "RB02",
        'room': "D02BZ01S01"},
    {'name': "GotP: Guilt room",
        'region': "gotp",
        'game_id': "RB38",
        'room': "D02Z02S06"},
    {'name': "GotP: Elevator shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_26",
        'room': "D02Z02S11"},
    {'name': "GotP: Elevator shaft ledge",
        'region': "gotp",
        'game_id': "QI53",
        'room': "D02Z02S11"},
    {'name': "GotP: Lady room",
        'region': "gotp",
        'game_id': "Lady[D02Z02S12]",
        'room': "D02Z02S12"},
    {'name': "GotP: Bleed room",
        'region': "gotp",
        'game_id': "HE11",
        'room': "D02Z02S13"},
    {'name': "GotP: Eastern shaft lower",
        'region': "gotp",
        'game_id': "QI46",
        'room': "D02Z02S03"},
    {'name': "GotP: Eastern shaft middle",
        'region': "gotp",
        'game_id': "CO29",
        'room': "D02Z02S03"},
    {'name': "GotP: Eastern shaft upper",
        'region': "gotp",
        'game_id': "QI08",
        'room': "D02Z02S03"},
    {'name': "GotP: Amanecida ledge",
        'region': "gotp",
        'game_id': "RB106",
        'room': "D02Z02S14"},
    {'name': "GotP: Western shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_25",
        'room': "D02Z02S04"},
    {'name': "GotP: Western shaft lower",
        'region': "gotp",
        'game_id': "RB32",
        'room': "D02Z02S04"},
    {'name': "GotP: Western shaft upper",
        'region': "gotp",
        'game_id': "CO01",
        'room': "D02Z02S04"},
    {'name': "GotP: Center shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_24",
        'room': "D02Z02S02"},
    {'name': "GotP: Center shaft ledge",
        'region': "gotp",
        'game_id': "RB15",
        'room': "D02Z02S05"},
    {'name': "GotP: Oil room",
        'region': "gotp",
        'game_id': "Oil[D02Z02S10]",
        'room': "D02Z02S10"},
    {'name': "GotP: Bow Amanecida",
        'region': "gotp",
        'game_id': "D02Z02S14[18000]",
        'room': "D02Z02S14"},
    
    # Grievance Ascends (12)
    {'name': "GA: Western lung ledge",
        'region': "ga",
        'game_id': "QI44",
        'room': "D03Z03S02"},
    {'name': "GA: Lung room upper",
        'region': "ga",
        'game_id': "RE07",
        'room': "D03Z03S06"},
    {'name': "GA: Lung room cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_19",
        'room': "D03Z03S06"},
    {'name': "GA: Lung room lower",
        'region': "ga",
        'game_id': "CO12",
        'room': "D03Z03S06"},
    {'name': "GA: Oil room",
        'region': "ga",
        'game_id': "Oil[D03Z03S13]",
        'room': "D03Z03S13"},
    {'name': "GA: Blood tunnel ledge",
        'region': "ga",
        'game_id': "QI10",
        'room': "D03Z03S08"},
    {'name': "GA: Blood tunnel cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_21",
        'room': "D03Z03S08"},
    {'name': "GA: Altasgracias cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_20",
        'room': "D03Z03S09"},
    {'name': "GA: Altasgracias gift",
        'region': "ga",
        'game_id': "QI13",
        'room': "D03Z03S10"},
    {'name': "GA: Altasgracias cacoon",
        'region': "ga",
        'game_id': "RB06",
        'room': "D03Z03S10"},
    {'name': "GA: Tres Angustias",
        'region': "ga",
        'game_id': "BS04",
        'room': "D03Z03S15"},
    {'name': "GA: Holy Visage gift",
        'region': "ga",
        'game_id': "QI39",
        'room': "D03Z03S16"},
    
    # Hall of the Dawning (2)
    {'name': "HotD: Mirror room",
        'region': "hotd",
        'game_id': "QI105",
        'room': "D08Z02S01"},
    {'name': "HotD: Laudes",
        'region': "hotd",
        'game_id': "LaudesBossTrigger[30000]",
        'room': "D08Z02S03"},
    
    # Jondo (13)
    {'name': "Jondo: Eastern entrance ledge",
        'region': "jondo",
        'game_id': "CO08",
        'room': "D03Z03S01"},
    {'name': "Jondo: Eastern entrance chest",
        'region': "jondo",
        'game_id': "PR10",
        'room': "D03Z03S01"},
    {'name': "Jondo: Eastern shaft bell chargers",
        'region': "jondo",
        'game_id': "CO33",
        'room': "D03Z03S04"},
    {'name': "Jondo: Eastern shaft bell trap",
        'region': "jondo",
        'game_id': "QI19",
        'room': "D03Z03S06"},
    {'name': "Jondo: Eastern shaft cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_18",
        'room': "D03Z03S05"},
    {'name': "Jondo: Spike tunnel cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_37",
        'room': "D03Z03S11"},
    {'name': "Jondo: Spike tunnel ledge",
        'region': "jondo",
        'game_id': "HE06",
        'room': "D03Z03S11"},
    {'name': "Jondo: EcS entrance",
        'region': "jondo",
        'game_id': "QI103",
        'room': "D03Z03S15"},
    {'name': "Jondo: Western shaft lower slide",
        'region': "jondo",
        'game_id': "CO07",
        'room': "D03Z03S07"},
    {'name': "Jondo: Western shaft bell trap",
        'region': "jondo",
        'game_id': "QI41",
        'room': "D03Z03S08"},
    {'name': "Jondo: Western shaft bell puzzle",
        'region': "jondo",
        'game_id': "QI52",
        'room': "D03Z03S12"},
    {'name': "Jondo: Western shaft root puzzle",
        'region': "jondo",
        'game_id': "RB28",
        'room': "D03Z03S13"},
    {'name': "Jondo: Western shaft cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_17",
        'room': "D03Z03S10"},
    
    # Knot of the Three Words (1)
    {'name': "KotTW: Fourth Visage gift",
        'region': "kottw",
        'game_id': "HE201",
        'room': "D04Z03S02"},
    
    # Library of the Negated Words (18)
    {'name': "LotNW: Platform room cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_01",
        'room': "D05Z01S04"},
    {'name': "LotNW: Platform room ledge",
        'region': "lotnw",
        'game_id': "CO18",
        'room': "D05Z01S04"},
    {'name': "LotNW: Upper cathedral ledge",
        'region': "lotnw",
        'game_id': "CO22",
        'room': "D05Z01S05"},
    {'name': "LotNW: Hidden floor",
        'region': "lotnw",
        'game_id': "QI50",
        'room': "D05Z01S05"},
    {'name': "LotNW: Lung ambush chest",
        'region': "lotnw",
        'game_id': "RB31",
        'room': "D05Z01S06"},
    {'name': "LotNW: Lady room",
        'region': "lotnw",
        'game_id': "Lady[D05Z01S14]",
        'room': "D05Z01S14"},
    {'name': "LotNW: Bone puzzle",
        'region': "lotnw",
        'game_id': "PR15",
        'room': "D05Z01S18"},
    {'name': "LotNW: Diosdado ledge",
        'region': "lotnw",
        'game_id': "CO28",
        'room': "D05Z01S11"},
    {'name': "LotNW: Platform puzzle chest",
        'region': "lotnw",
        'game_id': "PR07",
        'room': "D05Z01S10"},
    {'name': "LotNW: Final shaft ledge",
        'region': "lotnw",
        'game_id': "RB30",
        'room': "D05Z01S11"},
    {'name': "LotNW: Final shaft cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_02",
        'room': "D05Z01S11"},
    {'name': "LotNW: Oil room",
        'region': "lotnw",
        'game_id': "Oil[D05Z01S19]",
        'room': "D05Z01S19"},
    {'name': "LotNW: Elevator cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_32",
        'room': "D05Z01S21"},
    {'name': "LotNW: Mask room",
        'region': "lotnw",
        'game_id': "QI62",
        'room': "D05Z01S15"},
    {'name': "LotNW: Sword room",
        'region': "lotnw",
        'game_id': "Sword[D05Z01S13]",
        'room': "D05Z01S13"},
    {'name': "LotNW: Red candle",
        'region': "lotnw",
        'game_id': "RB19",
        'room': "D05Z01S02"},
    {'name': "LotNW: Diosdado gift",
        'region': "lotnw",
        'game_id': "RB203",
        'room': "D05Z01S11"}, # ?
    {'name': "LotNW: Fourth Visage hidden wall",
        'region': "lotnw",
        'game_id': "RB301",
        'room': "D05BZ01S01"},

    # Mercy Dreams (15)
    {'name': "MD: First section hidden wall",
        'region': "md",
        'game_id': "CO30",
        'room': "D01Z04S05"},
    {'name': "MD: Second section ghost ambush",
        'region': "md",
        'game_id': "PR01",
        'room': "D01Z04S07"},
    {'name': "MD: Second section ledge",
        'region': "md",
        'game_id': "CO03",
        'room': "D01Z04S06"},
    {'name': "MD: Second section cherub",
        'region': "md",
        'game_id': "RESCUED_CHERUB_09",
        'room': "D01Z04S06"},
    {'name': "MD: Red candle",
        'region': "md",
        'game_id': "RB17",
        'room': "D01Z04S08"},
    {'name': "MD: Shop left",
        'region': "md",
        'game_id': "QI58",
        'room': "D01BZ02S01"},
    {'name': "MD: Shop middle",
        'region': "md",
        'game_id': "RB05",
        'room': "D01BZ02S01"},
    {'name': "MD: Shop right",
        'region': "md",
        'game_id': "RB09",
        'room': "D01BZ02S01"},
    {'name': "MD: Third section hidden wall",
        'region': "md",
        'game_id': "QI48",
        'room': "D01Z04S11"},
    {'name': "MD: Third section lower corridor",
        'region': "md",
        'game_id': "CO38",
        'room': "D01Z04S14"},
    {'name': "MD: Ten Piedad",
        'region': "md",
        'game_id': "BS01",
        'room': "D01Z04S18"},
    {'name': "MD: Holy Visage gift",
        'region': "md",
        'game_id': "QI38",
        'room': "D01Z04S19"},
    {'name': "MD: Blue candle",
        'region': "md",
        'game_id': "RB26",
        'room': "D01Z04S16"},
    {'name': "MD: SlC entrance cherub",
        'region': "md",
        'game_id': "RESCUED_CHERUB_33",
        'room': "D01Z04S16"}, 
    {'name': "MD: SlC entrance ledge",
        'region': "md",
        'game_id': "CO03",
        'room': "D01Z04S13"},

    # Mother of Mothers (14)
    {'name': "MoM: Oil room",
        'region': "mom",
        'game_id': "Oil[D04Z02S14]",
        'room': "D04Z02S14"},
    {'name': "MoM: Eastern room upper",
        'region': "mom",
        'game_id': "RB33",
        'room': "D04Z02S07"},
    {'name': "MoM: Eastern room lower",
        'region': "mom",
        'game_id': "CO35",
        'room': "D04Z02S"},
    {'name': "MoM: Western room cherub",
        'region': "mom",
        'game_id': "RESCUED_CHERUB_30",
        'room': ""},
    {'name': "MoM: Western room ledge",
        'region': "mom",
        'game_id': "CO17",
        'room': "D04Z02S02"},
    {'name': "MoM: Redento prayer room",
        'region': "mom",
        'game_id': "RE03",
        'room': "D04BZ02S01"},
    {'name': "MoM: Redento corpse",
        'region': "mom",
        'game_id': "QI54",
        'room': "D04BZ02S01"},
    {'name': "MoM: Blood incense shaft",
        'region': "mom",
        'game_id': "HE01",
        'room': "D04Z02S16"},
    {'name': "MoM: Outside Cleofas room",
        'region': "mom",
        'game_id': "CO34",
        'room': "D04Z02S06"},
    {'name': "MoM: Center room ledge",
        'region': "mom",
        'game_id': "CO20",
        'room': "D04Z02S11"},
    {'name': "MoM: Center room cherub",
        'region': "mom",
        'game_id': "RESCUED_CHERUB_29",
        'room': ""},
    {'name': "MoM: Sword room",
        'region': "mom",
        'game_id': "Sword[D04Z02S12]",
        'room': "D04Z02S12"},
    {'name': "MoM: Melquiades",
        'region': "mom",
        'game_id': "BS05",
        'room': "D04Z02S22"},
    {'name': "MoM: Mask room",
        'region': "mom",
        'game_id': "QI60",
        'room': "D04Z02S15"},

    # Mountains of the Endless Dusk (8)
    {'name': "MotED: DeC entrance",
        'region': "moted",
        'game_id': "CO13",
        'room': "D03Z01S01"},
    {'name': "MotED: Perpetua gift",
        'region': "moted",
        'game_id': "RB13",
        'room': "D03Z01S06"},
    {'name': "MotED: Bell gap cherub",
        'region': "moted",
        'game_id': "RESCUED_CHERUB_16",
        'room': "D03Z01S03"},
    {'name': "MotED: Bell gap ledge",
        'region': "moted",
        'game_id': "QI47",
        'room': "D03Z01S03"},
    {'name': "MotED: Redento meeting 1",
        'region': "moted",
        'game_id': "RB22",
        'room': "D03Z01S03"},
    {'name': "MotED: Blood platform",
        'region': "moted",
        'game_id': "QI63",
        'room': "D03Z01S04"},
    {'name': "MotED: Egg hatching",
        'region': "moted",
        'game_id': "QI14",
        'room': "D03Z01S06"},
    {'name': "MotED: Axe Amanecida",
        'region': "moted",
        'game_id': "D03Z01S03[18000]",
        'room': "D03Z01S03"},

    # Mourning and Havoc (4)
    {'name': "MaH: Western chest",
        'region': "mah",
        'game_id': "PR202",
        'room': "D20Z02S11"},
    {'name': "MaH: Eastern chest",
        'region': "mah",
        'game_id': "RB201",
        'room': "D20Z02S02"},
    {'name': "MaH: Sierpes reward",
        'region': "mah",
        'game_id': "QI202",
        'room': "D20Z02S08"},
    {'name': "MaH: Sierpes",
        'region': "mah",
        'game_id': "BossTrigger[5000]",
        'room': "D20Z02S08"},
    
    # Patio of the Silent Steps (9)
    {'name': "PotSS: Garden 1 cherub",
        'region': "potss",
        'game_id': "RESCUED_CHERUB_35",
        'room': "D04Z01S01"},
    {'name': "PotSS: Garden 1 ledge",
        'region': "potss",
        'game_id': "CO23",
        'room': "D04Z01S01"},
    {'name': "PotSS: Garden 2 ledge",
        'region': "potss",
        'game_id': "RB14",
        'room': "D04Z01S02"},
    {'name': "PotSS: Garden 3 cherub",
        'region': "potss",
        'game_id': "RESCUED_CHERUB_28",
        'room': "D04Z01S03"},
    {'name': "PotSS: Garden 3 lower ledge",
        'region': "potss",
        'game_id': "QI37",
        'room': "D04Z01S03"},
    {'name': "PotSS: Garden 3 upper ledge",
        'region': "potss",
        'game_id': "CO39",
        'room': "D04Z01S03"},
    {'name': "PotSS: Northern shaft",
        'region': "potss",
        'game_id': "QI102",
        'room': "D04Z01S05"},
    {'name': "PotSS: Redento meeting 4",
        'region': "potss",
        'game_id': "RB21",
        'room': "D04Z01S01"},
    {'name': "PotSS: Falcata Amanecida",
        'region': "potss",
        'game_id': "D04Z01S04[18000]",
        'room': "D04Z01S04"},

    # Petrous (1)
    {'name': "Petrous: Entrance room",
        'region': "petrous",
        'game_id': "QI101",
        'room': "D01Z06S01"},

    # The Resting Place of the Sister (1)
    {'name': "TRPotS: Perpetua shrine",
        'region': "trpots",
        'game_id': "QI203",
        'room': "D20Z03S01"},
    
    # The Sleeping Canvases (10)
    {'name': "TSC: Herb shaft",
        'region': "tsc",
        'game_id': "QI64",
        'room': "D05Z02S02"},
    {'name': "TSC: Wax bleed puzzle",
        'region': "tsc",
        'game_id': "HE07",
        'room': "D05Z02S08"},
    {'name': "TSC: Shop left",
        'region': "tsc",
        'game_id': "RB12",
        'room': "D05BZ02S01"},
    {'name': "TSC: Shop middle",
        'region': "tsc",
        'game_id': "QI49",
        'room': "D05BZ02S01"},
    {'name': "TSC: Shop right",
        'region': "tsc",
        'game_id': "QI71",
        'room': "D05BZ02S01"},
    {'name': "TSC: Low tunnel blade trap",
        'region': "tsc",
        'game_id': "QI104",
        'room': "D05Z02S15"},
    {'name': "TSC: Exposito",
        'region': "tsc",
        'game_id': "BS06",
        'room': "D05Z02S14"},
    {'name': "TSC: Linen drop room",
        'region': "tsc",
        'game_id': "CO31",
        'room': "D05Z02S11"},
    {'name': "TSC: Jocinero gift initial",
        'region': "tsc",
        'game_id': "RE05",
        'room': "D05Z02S10"}, # ?
    {'name': "TSC: Jocinero gift final",
        'region': "tsc",
        'game_id': "PR05",
        'room': "D05Z02S10"}, # ?

    # The Holy Line (6)
    {'name': "THL: Deosgracias gift",
        'region': "thl",
        'game_id': "QI31",
        'room': "D01Z01S07"},
    {'name': "THL: Mud ledge lower",
        'region': "thl",
        'game_id': "PR14",
        'room': "D01Z01S02"},
    {'name': "THL: Mud ledge upper",
        'region': "thl",
        'game_id': "RB07",
        'room': "D01Z01S02"},
    {'name': "THL: Mud cherub",
        'region': "thl",
        'game_id': "RESCUED_CHERUB_07",
        'room': "D01Z01S03"},
    {'name': "THL: Cave ledge",
        'region': "thl",
        'game_id': "CO04",
        'room': "D01Z01S03"},
    {'name': "THL: Cave chest",
        'region': "thl",
        'game_id': "QI55",
        'room': "D01Z01S03"},

    # Wall of the Holy Prohibitions (19)
    {'name': "WotHP: Q1 lift puzzle",
        'region': "wothp",
        'game_id': "RB11",
        'room': "D09Z01S02"},
    {'name': "WotHP: Q1 drop room upper",
        'region': "wothp",
        'game_id': "CO10",
        'room': "D09BZ01S01[Cell22]"},
    {'name': "WotHP: Q1 drop room lower",
        'region': "wothp",
        'game_id': "QI69",
        'room': "D09BZ01S01[Cell22]"},
    {'name': "WotHP: Q1 upper bronze door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_03",
        'room': "D09BZ01S01[Cell1]"},
    {'name': "WotHP: Q1 upper silver door",
        'region': "wothp",
        'game_id': "CO24",
        'room': "D09BZ01S01[Cell6]"},
    {'name': "WotHP: Q1 middle gold door",
        'region': "wothp",
        'game_id': "QI51",
        'room': "D09Z01S02"},
    {'name': "WotHP: Q2 middle gold door",
        'region': "wothp",
        'game_id': "CO26",
        'room': "D09BZ01S01[Cell16]"},
    {'name': "WotHP: Q3 lower gold door",
        'region': "wothp",
        'game_id': "CO02",
        'room': "D09BZ01S01[Cell21]"},
    {'name': "WotHP: Q3 upper silver door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_34",
        'room': "D09BZ01S01[Cell17~18]"}, # ?
    {'name': "WotHP: Q3 upper ledge",
        'region': "wothp",
        'game_id': "RB16",
        'room': "D09BZ01S01[Cell24]"},
    {'name': "WotHP: Q4 hidden ledge",
        'region': "wothp",
        'game_id': "CO27",
        'room': "D09Z01S10"},
    {'name': "WotHP: Q4 lower silver door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_04",
        'room': "D09BZ01S01[Cell11]"},
    {'name': "WotHP: Q4 upper bronze door",
        'region': "wothp",
        'game_id': "QI70",
        'room': "D09Z01S10"},
    {'name': "WotHP: Q4 upper silver door",
        'region': "wothp",
        'game_id': "CO37",
        'room': "D09BZ01S01[Cell10]"},
    {'name': "WotHP: CoLCV entrance",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_05",
        'room': "D09Z01S06"},
    {'name': "WotHP: Oil room",
        'region': "wothp",
        'game_id': "Oil[D09Z01S12]",
        'room': "D09Z01S12"},
    {'name': "WotHP: Quirce",
        'region': "wothp",
        'game_id': "BS14",
        'room': "D09Z01S03"},
    {'name': "WotHP: Quirce room",
        'region': "wothp",
        'game_id': "QI72",
        'room': "D09Z01S08"},
    {'name': "WotHP: Lance Amanecida",
        'region': "wothp",
        'game_id': "D09Z01S01[18000]",
        'room': "D09Z01S01"},

    # Wasteland of the Buried Churches (8)
    {'name': "WotBC: Lower tree path",
        'region': "wotbc",
        'game_id': "RB04",
        'room': "D01Z03S01"},
    {'name': "WotBC: Building slide",
        'region': "wotbc",
        'game_id': "CO14",
        'room': "D01Z03S02"},
    {'name': "WotBC: Exterior ledge",
        'region': "wotbc",
        'game_id': "CO36",
        'room': "D01Z03S03"},
    {'name': "WotBC: Exterior cherub",
        'region': "wotbc",
        'game_id': "RESCUED_CHERUB_10",
        'room': "D01Z03S03"},
    {'name': "WotBC: Underneath MeD bridge",
        'region': "wotbc",
        'game_id': "QI06",
        'room': "D01Z03S05"},
    {'name': "WotBC: Cliffside ledge",
        'region': "wotbc",
        'game_id': "HE02",
        'room': "D01Z03S07"},
    {'name': "WotBC: Cliffside cherub",
        'region': "wotbc",
        'game_id': "RESCUED_CHERUB_38",
        'room': "D01Z03S07"},
    {'name': "WotBC: Redento meeting 3",
        'region': "wotbc",
        'game_id': "RB20",
        'room': "D01Z03S01"}, # ?
    
    # Where Olive Trees Wither (11)
    {'name': "WOTW: WaBC entrance",
        'region': "wotw",
        'game_id': "CO11",
        'room': "D02Z01S01"},
    {'name': "WOTW: Healing cave",
        'region': "wotw",
        'game_id': "QI20",
        'room': "D02Z01S04"},
    {'name': "WOTW: White lady flower",
        'region': "wotw",
        'game_id': "QI68",
        'room': "D02Z01S"},
    {'name': "WOTW: White lady tomb",
        'region': "wotw",
        'game_id': "PR04",
        'room': "D02Z01S08"},
    {'name': "WOTW: White lady cave cherub",
        'region': "wotw",
        'game_id': "RESCUED_CHERUB_17",
        'room': "D02Z01S06"},
    {'name': "WOTW: White lady cave ledge",
        'region': "wotw",
        'game_id': "CO19",
        'room': "D02Z01S06"},
    {'name': "WOTW: Eastern root cherub",
        'region': "wotw",
        'game_id': "RESCUED_CHERUB_23",
        'room': "D02Z01S09"},
    {'name': "WOTW: Eastern root ledge",
        'region': "wotw",
        'game_id': "HE05",
        'room': "D02Z01S09"},
    {'name': "WOTW: Death run",
        'region': "wotw",
        'game_id': "QI07",
        'room': "D02Z01S05"},
    {'name': "WOTW: Gemino gift initial",
        'region': "wotw",
        'game_id': "QI59",
        'room': "D02Z01S01"},
    {'name': "WOTW: Gemino gift final",
        'region': "wotw",
        'game_id': "RB10",
        'room': "D02Z01S01"},

    # Various (20)
    {'name': "Guilt arena 1 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[1000]",
        'room': "dungeon"},
    {'name': "Guilt arena 1 main",
        'region': "dungeon",
        'game_id': "QI32",
        'room': "dungeon"},
    {'name': "Guilt arena 2 extra",
        'region': "dungeon",
        'game_id': "HE10",
        'room': "dungeon"},
    {'name': "Guilt arena 2 main",
        'region': "dungeon",
        'game_id': "QI33",
        'room': "dungeon"},
    {'name': "Guilt arena 3 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[3000]",
        'room': "dungeon"},
    {'name': "Guilt arena 3 main",
        'region': "dungeon",
        'game_id': "QI34",
        'room': "dungeon"},
    {'name': "Guilt arena 4 extra",
        'region': "dungeon",
        'game_id': "RB34",
        'room': "dungeon"},
    {'name': "Guilt arena 4 main",
        'region': "dungeon",
        'game_id': "QI35",
        'room': "dungeon"},
    {'name': "Guilt arena 5 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[5000]",
        'room': "dungeon"},
    {'name': "Guilt arena 5 main",
        'region': "dungeon",
        'game_id': "QI79",
        'room': "dungeon"},
    {'name': "Guilt arena 6 extra",
        'region': "dungeon",
        'game_id': "RB35",
        'room': "dungeon"},
    {'name': "Guilt arena 6 main",
        'region': "dungeon",
        'game_id': "QI80",
        'room': "dungeon"},
    {'name': "Guilt arena 7 extra",
        'region': "dungeon",
        'game_id': "RB36",
        'room': "dungeon"},
    {'name': "Guilt arena 7 main",
        'region': "dungeon",
        'game_id': "QI81",
        'room': "dungeon"},
    {'name': "Amanecida 1",
        'region': "dungeon",
        'game_id': "QI107",
        'room': "dungeon"},
    {'name': "Amanecida 2",
        'region': "dungeon",
        'game_id': "QI108",
        'room': "dungeon"},
    {'name': "Amanecida 3",
        'region': "dungeon",
        'game_id': "QI109",
        'room': "dungeon"},
    {'name': "Amanecida 4",
        'region': "dungeon",
        'game_id': "QI110",
        'room': "dungeon"},
    {'name': "All amanecidas reward",
        'region': "dungeon",
        'game_id': "PR101",
        'room': "dungeon"}
]