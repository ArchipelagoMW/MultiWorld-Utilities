from typing import Dict, List, Tuple
from BaseClasses import Location

from .MetroidPrimeInterface import MetroidPrimeLevel

METROID_PRIME_LOCATION_BASE = 5031100


class MetroidPrimeLocation(Location):
    game: str = "Metroid Prime"


chozo_location_table = {
    "Chozo Ruins: Main Plaza - Half-Pipe": 5031100,
    "Chozo Ruins: Main Plaza - Grapple Ledge": 5031101,
    "Chozo Ruins: Main Plaza - Tree": 5031102,
    "Chozo Ruins: Main Plaza - Locked Door": 5031103,
    "Chozo Ruins: Ruined Fountain": 5031104,
    "Chozo Ruins: Ruined Shrine - Plated Beetle": 5031105,
    "Chozo Ruins: Ruined Shrine - Half-Pipe": 5031106,
    "Chozo Ruins: Ruined Shrine - Lower Tunnel": 5031107,
    "Chozo Ruins: Vault": 5031108,
    "Chozo Ruins: Training Chamber": 5031109,
    "Chozo Ruins: Ruined Nursery": 5031110,
    "Chozo Ruins: Training Chamber Access": 5031111,
    "Chozo Ruins: Magma Pool": 5031112,
    "Chozo Ruins: Tower of Light": 5031113,
    "Chozo Ruins: Tower Chamber": 5031114,
    "Chozo Ruins: Ruined Gallery - Missile Wall": 5031115,
    "Chozo Ruins: Ruined Gallery - Tunnel": 5031116,
    "Chozo Ruins: Transport Access North": 5031117,
    "Chozo Ruins: Gathering Hall": 5031118,
    "Chozo Ruins: Hive Totem": 5031119,
    "Chozo Ruins: Sunchamber - Flaahgra": 5031120,
    "Chozo Ruins: Sunchamber - Ghosts": 5031121,
    "Chozo Ruins: Watery Hall Access": 5031122,
    "Chozo Ruins: Watery Hall - Scan Puzzle": 5031123,
    "Chozo Ruins: Watery Hall - Underwater": 5031124,
    "Chozo Ruins: Dynamo - Lower": 5031125,
    "Chozo Ruins: Dynamo - Spider Track": 5031126,
    "Chozo Ruins: Burn Dome - Missile": 5031127,
    "Chozo Ruins: Burn Dome - Incinerator Drone": 5031128,
    "Chozo Ruins: Furnace - Spider Tracks": 5031129,
    "Chozo Ruins: Furnace - Inside Furnace": 5031130,
    "Chozo Ruins: Hall of the Elders": 5031131,
    "Chozo Ruins: Crossway": 5031132,
    "Chozo Ruins: Elder Chamber": 5031133,
    "Chozo Ruins: Antechamber": 5031134,
}

phen_location_table = {
    "Phendrana Drifts: Phendrana Shorelines - Behind Ice": 5031135,
    "Phendrana Drifts: Phendrana Shorelines - Spider Track": 5031136,
    "Phendrana Drifts: Chozo Ice Temple": 5031137,
    "Phendrana Drifts: Ice Ruins West": 5031138,
    "Phendrana Drifts: Ice Ruins East - Behind Ice": 5031139,
    "Phendrana Drifts: Ice Ruins East - Spider Track": 5031140,
    "Phendrana Drifts: Chapel of the Elders": 5031141,
    "Phendrana Drifts: Ruined Courtyard": 5031142,
    "Phendrana Drifts: Phendrana Canyon": 5031143,
    "Phendrana Drifts: Quarantine Cave": 5031144,
    "Phendrana Drifts: Research Lab Hydra": 5031145,
    "Phendrana Drifts: Quarantine Monitor": 5031146,
    "Phendrana Drifts: Observatory": 5031147,
    "Phendrana Drifts: Transport Access": 5031148,
    "Phendrana Drifts: Control Tower": 5031149,
    "Phendrana Drifts: Research Core": 5031150,
    "Phendrana Drifts: Frost Cave": 5031151,
    "Phendrana Drifts: Research Lab Aether - Tank": 5031152,
    "Phendrana Drifts: Research Lab Aether - Morph Track": 5031153,
    "Phendrana Drifts: Gravity Chamber - Underwater": 5031154,
    "Phendrana Drifts: Gravity Chamber - Grapple Ledge": 5031155,
    "Phendrana Drifts: Storage Cave": 5031156,
    "Phendrana Drifts: Security Cave": 5031157,
}

tallon_location_table = {
    "Tallon Overworld: Landing Site": 5031158,
    "Tallon Overworld: Alcove": 5031159,
    "Tallon Overworld: Frigate Crash Site": 5031160,
    "Tallon Overworld: Overgrown Cavern": 5031161,
    "Tallon Overworld: Root Cave": 5031162,
    "Tallon Overworld: Artifact Temple": 5031163,
    "Tallon Overworld: Transport Tunnel B": 5031164,
    "Tallon Overworld: Arbor Chamber": 5031165,
    "Tallon Overworld: Cargo Freight Lift to Deck Gamma": 5031166,
    "Tallon Overworld: Biohazard Containment": 5031167,
    "Tallon Overworld: Hydro Access Tunnel": 5031168,
    "Tallon Overworld: Great Tree Chamber": 5031169,
    "Tallon Overworld: Life Grove Tunnel": 5031170,
    "Tallon Overworld: Life Grove - Start": 5031171,
    "Tallon Overworld: Life Grove - Underwater Spinner": 5031172,
}

mines_location_table = {
    "Phazon Mines: Main Quarry": 5031173,
    "Phazon Mines: Security Access A": 5031174,
    "Phazon Mines: Storage Depot B": 5031175,
    "Phazon Mines: Storage Depot A": 5031176,
    "Phazon Mines: Elite Research - Phazon Elite": 5031177,
    "Phazon Mines: Elite Research - Laser": 5031178,
    "Phazon Mines: Elite Control Access": 5031179,
    "Phazon Mines: Ventilation Shaft": 5031180,
    "Phazon Mines: Phazon Processing Center": 5031181,
    "Phazon Mines: Processing Center Access": 5031182,
    "Phazon Mines: Elite Quarters": 5031183,
    "Phazon Mines: Central Dynamo": 5031184,
    "Phazon Mines: Metroid Quarantine B": 5031185,
    "Phazon Mines: Metroid Quarantine A": 5031186,
    "Phazon Mines: Fungal Hall B": 5031187,
    "Phazon Mines: Phazon Mining Tunnel": 5031188,
    "Phazon Mines: Fungal Hall Access": 5031189,
}

magmoor_location_table = {
    "Magmoor Caverns: Lava Lake": 5031190,
    "Magmoor Caverns: Triclops Pit": 5031191,
    "Magmoor Caverns: Storage Cavern": 5031192,
    "Magmoor Caverns: Transport Tunnel A": 5031193,
    "Magmoor Caverns: Warrior Shrine": 5031194,
    "Magmoor Caverns: Shore Tunnel": 5031195,
    "Magmoor Caverns: Fiery Shores - Morph Track": 5031196,
    "Magmoor Caverns: Fiery Shores - Warrior Shrine Tunnel": 5031197,
    "Magmoor Caverns: Plasma Processing": 5031198,
    "Magmoor Caverns: Magmoor Workstation": 5031199,
}

every_location: Dict[str, int] = {
    **chozo_location_table,
    **phen_location_table,
    **tallon_location_table,
    **mines_location_table,
    **magmoor_location_table,
}

PICKUP_LOCATIONS: List[Tuple[MetroidPrimeLevel, int]] = [
    (MetroidPrimeLevel.Chozo_Ruins, 0x0002012D),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00020132),
    (MetroidPrimeLevel.Chozo_Ruins, 0x0002006B),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00020159),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00080077),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00090028),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00090069),
    (MetroidPrimeLevel.Chozo_Ruins, 0x0009006E),
    (MetroidPrimeLevel.Chozo_Ruins, 0x000B003E),
    (MetroidPrimeLevel.Chozo_Ruins, 0x000C002D),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00100004),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00120004),
    (MetroidPrimeLevel.Chozo_Ruins, 0x001400EE),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00150336),
    (MetroidPrimeLevel.Chozo_Ruins, 0x001B001A),
    (MetroidPrimeLevel.Chozo_Ruins, 0x001C002F),
    (MetroidPrimeLevel.Chozo_Ruins, 0x001C0061),
    (MetroidPrimeLevel.Chozo_Ruins, 0x001E0173),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00200058),
    (MetroidPrimeLevel.Chozo_Ruins, 0x002401DD),
    (MetroidPrimeLevel.Chozo_Ruins, 0x002528EF),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00253094),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00260009),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00290086),
    (MetroidPrimeLevel.Chozo_Ruins, 0x002927E7),
    (MetroidPrimeLevel.Chozo_Ruins, 0x002D0023),
    (MetroidPrimeLevel.Chozo_Ruins, 0x002D00AE),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00300037),
    (MetroidPrimeLevel.Chozo_Ruins, 0x0030278B),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00310063),
    (MetroidPrimeLevel.Chozo_Ruins, 0x0031000C),
    (MetroidPrimeLevel.Chozo_Ruins, 0x003402DF),
    (MetroidPrimeLevel.Chozo_Ruins, 0x003502C9),
    (MetroidPrimeLevel.Chozo_Ruins, 0x00390004),
    (MetroidPrimeLevel.Chozo_Ruins, 0x003D0004),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x0002016F),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00020177),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00080258),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x000928EE),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x000A00AC),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x000A0192),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x000E0059),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x000F022D),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x001000E3),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x001801CC),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00190514),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x001B0012),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x001E02F7),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x001F00A6),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x002704D0),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x0028011D),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00290188),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x003303E1),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00330412),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x00350021),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x0035012D),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x003600AA),
    (MetroidPrimeLevel.Phendrana_Drifts, 0x0037001A),
    (MetroidPrimeLevel.Tallon_Overworld, 0x00000085),
    (MetroidPrimeLevel.Tallon_Overworld, 0x0004000E),
    (MetroidPrimeLevel.Tallon_Overworld, 0x000801FC),
    (MetroidPrimeLevel.Tallon_Overworld, 0x000D00C7),
    (MetroidPrimeLevel.Tallon_Overworld, 0x000F00FE),
    (MetroidPrimeLevel.Tallon_Overworld, 0x001001D5),
    (MetroidPrimeLevel.Tallon_Overworld, 0x00130137),
    (MetroidPrimeLevel.Tallon_Overworld, 0x00140016),
    (MetroidPrimeLevel.Tallon_Overworld, 0x001B0116),
    (MetroidPrimeLevel.Tallon_Overworld, 0x001E02ED),
    (MetroidPrimeLevel.Tallon_Overworld, 0x00230054),
    (MetroidPrimeLevel.Tallon_Overworld, 0x0025000E),
    (MetroidPrimeLevel.Tallon_Overworld, 0x00270037),
    (MetroidPrimeLevel.Tallon_Overworld, 0x002A0022),
    (MetroidPrimeLevel.Tallon_Overworld, 0x002A0235),
    (MetroidPrimeLevel.Phazon_Mines, 0x00020234),
    (MetroidPrimeLevel.Phazon_Mines, 0x00050188),
    (MetroidPrimeLevel.Phazon_Mines, 0x00090005),
    (MetroidPrimeLevel.Phazon_Mines, 0x000C0027),
    (MetroidPrimeLevel.Phazon_Mines, 0x000D0341),
    (MetroidPrimeLevel.Phazon_Mines, 0x000D04F2),
    (MetroidPrimeLevel.Phazon_Mines, 0x000F008E),
    (MetroidPrimeLevel.Phazon_Mines, 0x0012010E),
    (MetroidPrimeLevel.Phazon_Mines, 0x00130767),
    (MetroidPrimeLevel.Phazon_Mines, 0x001600A8),
    (MetroidPrimeLevel.Phazon_Mines, 0x001A04B9),
    (MetroidPrimeLevel.Phazon_Mines, 0x001B04B2),
    (MetroidPrimeLevel.Phazon_Mines, 0x001F0206),
    (MetroidPrimeLevel.Phazon_Mines, 0x002005EB),
    (MetroidPrimeLevel.Phazon_Mines, 0x00240128),
    (MetroidPrimeLevel.Phazon_Mines, 0x00270080),
    (MetroidPrimeLevel.Phazon_Mines, 0x00280103),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x0004287D),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x0006010D),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x00080010),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x000A0044),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x000B0038),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x000C0029),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x000E01DB),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x000E0240),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x00150020),
    (MetroidPrimeLevel.Magmoor_Caverns, 0x0017028F),
]
