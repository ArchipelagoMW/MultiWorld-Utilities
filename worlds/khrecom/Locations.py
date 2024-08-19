from typing import Dict, NamedTuple, Optional
import typing


from BaseClasses import Location


class KHRECOMLocation(Location):
    game: str = "Kingdom Hearts Chain of Memories"


class KHRECOMLocationData(NamedTuple):
    category: str
    code: int


def get_locations_by_category(category: str) -> Dict[str, KHRECOMLocationData]:
    location_dict: Dict[str, KHRECOMLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, KHRECOMLocationData] = {
    "Starting Checks (Attack Cards Kingdom Key)":                        KHRECOMLocationData("Starting"         , 269_0001),
    "Agrabah Field (Attack Cards Three Wishes)":                         KHRECOMLocationData("Agrabah"          , 269_0002),
    "Atlantica Field (Attack Cards Crabclaw)":                           KHRECOMLocationData("Atlantica"        , 269_0003),
    "Halloween Town Field (Attack Cards Pumpkinhead)":                   KHRECOMLocationData("Halloween Town"   , 269_0004),
    "Neverland Field (Attack Cards Fairy Harp)":                         KHRECOMLocationData("Neverland"        , 269_0005),
    "Monstro Field (Attack Cards Wishing Star)":                         KHRECOMLocationData("Monstro"          , 269_0006),
    "100 Acre Wood Tigger's Playground (Attack Cards Spellbinder)":      KHRECOMLocationData("100 Acre Wood"    , 269_0007),
    "Olympus Coliseum Room of Rewards (Attack Cards Metal Chocobo)":     KHRECOMLocationData("Olympus Coliseum" , 269_0008),
    "Olympus Coliseum Field (Attack Card Olympia)":                      KHRECOMLocationData("Olympus Coliseum" , 269_0009),
    "Traverse Town Room of Rewards (Attack Cards Lionheart)":            KHRECOMLocationData("Traverse Town"    , 269_0010),
    "Wonderland Field (Attack Cards Lady Luck)":                         KHRECOMLocationData("Wonderland"       , 269_0011),
    "Hollow Bastion Field (Attack Cards Divine Rose)":                   KHRECOMLocationData("Hollow Bastion"   , 269_0012),
    "Destiny Islands Room of Guidance (Attack Cards Oathkeeper)":        KHRECOMLocationData("Destiny Islands"  , 269_0013),
    "12F Exit Hall Larxene II (Attack Cards Oblivion)":                  KHRECOMLocationData("Exit Halls"       , 269_0014),
    "Castle Oblivion Room of Rewards (Attack Cards Star Seeker)":        KHRECOMLocationData("Castle Oblivion"  , 269_0018), # Days Location
    "Olympus Coliseum Room of Rewards (Attack Cards Total Eclipse)":     KHRECOMLocationData("Olympus Coliseum" , 269_0019), # Days Location
    "Neverland Room of Rewards (Attack Cards Midnight Roar)":            KHRECOMLocationData("Neverland"        , 269_0020), # Days Location
    "Traverse Town Bounty (Attack Cards Maverick Flare)":                KHRECOMLocationData("Traverse Town"    , 269_0021), # Days Location
    "Destiny Islands Room of Rewards (Attack Cards Two Become One)":     KHRECOMLocationData("Destiny Islands"  , 269_0022), # Days Location
    "Halloween Town Room of Rewards (Attack Cards Bond of Flame)":       KHRECOMLocationData("Halloween Town"   , 269_0023), # Days Location
    "01F Exit Hall Axel I (Magic Cards Fire)":                           KHRECOMLocationData("Exit Halls"       , 269_0024),
    "Starting Checks (Magic Cards Blizzard)":                            KHRECOMLocationData("Starting"         , 269_0025),
    "06F Exit Hall Larxene I (Magic Cards Thunder)":                     KHRECOMLocationData("Exit Halls"       , 269_0026),
    "Starting Checks (Magic Cards Cure)":                                KHRECOMLocationData("Starting"         , 269_0027),
    "Agrabah Bounty (Magic Cards Gravity)":                              KHRECOMLocationData("Agrabah"          , 269_0028),
    "Wonderland Bounty (Magic Cards Stop)":                              KHRECOMLocationData("Wonderland"       , 269_0029),
    "07F Exit Hall Riku I (Magic Cards Aero)":                           KHRECOMLocationData("Exit Halls"       , 269_0030),
    "Traverse Town Room of Beginnings (Summon Cards Simba)":             KHRECOMLocationData("Traverse Town"    , 269_0031),
    "Agrabah Room of Truth (Summon Cards Genie)":                        KHRECOMLocationData("Agrabah"          , 269_0032),
    "100 Acre Wood Clear (Summon Cards Bambi)":                          KHRECOMLocationData("100 Acre"         , 269_0033),
    "Monstro Room of Truth (Summon Cards Dumbo)":                        KHRECOMLocationData("Monstro"          , 269_0034),
    "Neverland Room of Truth (Summon Cards Tinker Bell)":                KHRECOMLocationData("Neverland"        , 269_0035),
    "Hollow Bastion Room of Rewards (Summon Cards Mushu)":               KHRECOMLocationData("Hollow Bastion"   , 269_0036),
    "Olympus Coliseum Room of Truth (Summon Cards Cloud)":               KHRECOMLocationData("Olympus Coliseum" , 269_0037),
    "Starting Checks (Item Cards Potion)":                               KHRECOMLocationData("Starting"         , 269_0038),
    "Olympus Coliseum Room of Guidance (Item Cards Hi-Potion)":          KHRECOMLocationData("Olympus Coliseum" , 269_0039),
    "11F Exit Hall Riku III (Item Cards Mega-Potion)":                   KHRECOMLocationData("Exit Halls"       , 269_0040),
    "Agrabah Room of Guidance (Item Cards Ether)":                       KHRECOMLocationData("Agrabah"          , 269_0041),
    "100 Acre Wood Whirlwind Plunge (Item Cards Mega-Ether)":            KHRECOMLocationData("100 Acre Wood"    , 269_0042),
    "100 Acre Wood Bumble Rumble (Item Cards Elixir)":                   KHRECOMLocationData("100 Acre Wood"    , 269_0043),
    "Destiny Islands Room of Rewards (Item Cards Megalixir)":            KHRECOMLocationData("Destiny Islands"  , 269_0044),
    "Traverse Town Room of Truth (Enemy Cards Guard Armor)":             KHRECOMLocationData("Traverse Town"    , 269_0083),
    "Olympus Coliseum Room of Truth (Enemy Cards Hades)":                KHRECOMLocationData("Olympus Coliseum" , 269_0084),
    "Wonderland Room of Truth (Enemy Cards Trickmaster)":                KHRECOMLocationData("Wonderland"       , 269_0085),
    "Agrabah Room of Truth (Enemy Cards Jafar)":                         KHRECOMLocationData("Agrabah"          , 269_0086),
    "Atlantica Room of Truth (Enemy Cards Ursula)":                      KHRECOMLocationData("Atlantica"        , 269_0087),
    "Halloween Town Room of Truth (Enemy Cards Oogie Boogie)":           KHRECOMLocationData("Halloween Town"   , 269_0088),
    "Monstro Room of Guidance (Enemy Cards Parasite Cage)":              KHRECOMLocationData("Monstro"          , 269_0089),
    "Neverland Room of Truth (Enemy Cards Hook)":                        KHRECOMLocationData("Neverland"        , 269_0090),
    "Hollow Bastion Room of Truth (Enemy Cards Dragon Maleficent)":      KHRECOMLocationData("Hollow Bastion"   , 269_0091),
    "Destiny Islands Room of Guidance (Enemy Cards Darkside)":           KHRECOMLocationData("Destiny Islands"  , 269_0092),
    "12F Exit Hall Riku IV (Enemy Cards Riku)":                          KHRECOMLocationData("Exit Halls"       , 269_0093),
    "Wonderland Room of Beginnings (Enemy Cards Card Soldier)":          KHRECOMLocationData("Wonderland"       , 269_0094),
   #"Twilight Town Bounty (Enemy Cards Ansem)":                          KHRECOMLocationData("Twilight Town"    , 269_0095), # RR
    "Wonderland Room of Rewards (Enemy Cards Xemnas)":                   KHRECOMLocationData("Wonderland"       , 269_0096), # Days Location
    "Hollow Bastion Room of Rewards (Enemy Cards Xigbar)":               KHRECOMLocationData("Hollow Bastion"   , 269_0097), # Days Location
    "Monstro Room of Rewards (Enemy Cards Xaldin)":                      KHRECOMLocationData("Monstro"          , 269_0098), # Days Location
    "Twilight Town Room of Beginnings (Enemy Cards Vexen)":              KHRECOMLocationData("Twilight Town"    , 269_0099),
   #"Castle Oblivion Bounty (Enemy Cards Lexaeus)":                      KHRECOMLocationData("Castle Oblivion"  , 269_0100), # RR
   #"Destiny Islands Bounty (Enemy Cards Zexion)":                       KHRECOMLocationData("Destiny Islands"  , 269_0101), # RR
    "Traverse Town Room of Rewards (Enemy Cards Saix)":                  KHRECOMLocationData("Traverse Town"    , 269_0102), # Days Location
    "Castle Oblivion Room of Beginnings (Enemy Cards Axel)":             KHRECOMLocationData("Castle Oblivion"  , 269_0103),
    "Atlantica Room of Rewards (Enemy Cards Demyx)":                     KHRECOMLocationData("Atlantica"        , 269_0104), # Days Location
    "Agrabah Room of Rewards (Enemy Cards Luxord)":                      KHRECOMLocationData("Agrabah"          , 269_0105), # Days Location
    "Castle Oblivion Field Marluxia":                                    KHRECOMLocationData("Castle Oblivion"  , 269_0106),
    "12F Exit Hall Larxene II (Enemy Cards Larxene)":                    KHRECOMLocationData("Exit Halls"       , 269_0107),
    "Twilight Town Room of Rewards (Enemy Cards Roxas)":                 KHRECOMLocationData("Twilight Town"    , 269_0108), # Days Location
    
    "Traverse Town Room of Beginnings":                                  KHRECOMLocationData("Traverse Town"    , 269_1011),
    "Traverse Town Room of Guidance":                                    KHRECOMLocationData("Traverse Town"    , 269_1012),
    "Traverse Town Room of Truth":                                       KHRECOMLocationData("Traverse Town"    , 269_1013),
    "Agrabah Room of Beginnings":                                        KHRECOMLocationData("Agrabah"          , 269_1021),
    "Agrabah Room of Guidance":                                          KHRECOMLocationData("Agrabah"          , 269_1022),
    "Agrabah Room of Truth":                                             KHRECOMLocationData("Agrabah"          , 269_1023),
    "Olympus Coliseum Room of Beginnings":                               KHRECOMLocationData("Olympus Coliseum" , 269_1031),
    "Olympus Coliseum Room of Guidance":                                 KHRECOMLocationData("Olympus Coliseum" , 269_1032),
    "Olympus Coliseum Room of Truth":                                    KHRECOMLocationData("Olympus Coliseum" , 269_1033),
    "Wonderland Room of Beginnings":                                     KHRECOMLocationData("Wonderland"       , 269_1041),
    "Wonderland Room of Guidance":                                       KHRECOMLocationData("Wonderland"       , 269_1042),
    "Wonderland Room of Truth":                                          KHRECOMLocationData("Wonderland"       , 269_1043),
    "Monstro Room of Beginnings":                                        KHRECOMLocationData("Monstro"          , 269_1051),
    "Monstro Room of Guidance":                                          KHRECOMLocationData("Monstro"          , 269_1052),
    "Monstro Room of Truth":                                             KHRECOMLocationData("Monstro"          , 269_1053),
    "Halloween Town Room of Beginnings":                                 KHRECOMLocationData("Halloween Town"   , 269_1061),
    "Halloween Town Room of Guidance":                                   KHRECOMLocationData("Halloween Town"   , 269_1062),
    "Halloween Town Room of Truth":                                      KHRECOMLocationData("Halloween Town"   , 269_1063),
    "Atlantica Room of Beginnings":                                      KHRECOMLocationData("Atlantica"        , 269_1071),
    "Atlantica Room of Guidance":                                        KHRECOMLocationData("Atlantica"        , 269_1072),
    "Atlantica Room of Truth":                                           KHRECOMLocationData("Atlantica"        , 269_1073),
    "Neverland Room of Beginnings":                                      KHRECOMLocationData("Neverland"        , 269_1081),
    "Neverland Room of Guidance":                                        KHRECOMLocationData("Neverland"        , 269_1082),
    "Neverland Room of Truth":                                           KHRECOMLocationData("Neverland"        , 269_1083),
    "Hollow Bastion Room of Beginnings":                                 KHRECOMLocationData("Hollow Bastion"   , 269_1091),
    "Hollow Bastion Room of Guidance":                                   KHRECOMLocationData("Hollow Bastion"   , 269_1092),
    "Hollow Bastion Room of Truth":                                      KHRECOMLocationData("Hollow Bastion"   , 269_1093),
    "Twilight Town Room of Beginnings":                                  KHRECOMLocationData("Twilight Town"    , 269_1111),
    "Destiny Islands Room of Beginnings":                                KHRECOMLocationData("Destiny Islands"  , 269_1121),
    "Destiny Islands Room of Guidance":                                  KHRECOMLocationData("Destiny Islands"  , 269_1122),
    "Castle Oblivion Room of Beginnings":                                KHRECOMLocationData("Castle Oblivion"  , 269_1131),
    
    "Defeat 1 Heartless Shadow":                                         KHRECOMLocationData("Heartless1"       , 269_1201),
    "Defeat 1 Heartless Soldier":                                        KHRECOMLocationData("Heartless1"       , 269_1202),
    "Defeat 1 Heartless Large Body":                                     KHRECOMLocationData("Heartless1"       , 269_1203),
    "Defeat 1 Heartless Red Nocturne":                                   KHRECOMLocationData("Heartless1"       , 269_1204),
    "Defeat 1 Heartless Blue Rhapsody":                                  KHRECOMLocationData("Heartless1"       , 269_1205),
    "Defeat 1 Heartless Yellow Opera":                                   KHRECOMLocationData("Heartless1"       , 269_1206),
    "Defeat 1 Heartless Green Requiem":                                  KHRECOMLocationData("Heartless1"       , 269_1207),
    "Defeat 1 Heartless Powerwild":                                      KHRECOMLocationData("Heartless1"       , 269_1208),
    "Defeat 1 Heartless Bouncywild":                                     KHRECOMLocationData("Heartless1"       , 269_1209),
    "Defeat 1 Heartless Air Soldier":                                    KHRECOMLocationData("Heartless1"       , 269_1210),
    "Defeat 1 Heartless Bandit":                                         KHRECOMLocationData("Heartless1"       , 269_1211),
    "Defeat 1 Heartless Fat Bandit":                                     KHRECOMLocationData("Heartless1"       , 269_1212),
    "Defeat 1 Heartless Barrel Spider":                                  KHRECOMLocationData("Heartless1"       , 269_1213),
    "Defeat 1 Heartless Search Ghost":                                   KHRECOMLocationData("Heartless1"       , 269_1214),
    "Defeat 1 Heartless Sea Neon":                                       KHRECOMLocationData("Heartless1"       , 269_1215),
    "Defeat 1 Heartless Screwdiver":                                     KHRECOMLocationData("Heartless1"       , 269_1216),
    "Defeat 1 Heartless Aquatank":                                       KHRECOMLocationData("Heartless1"       , 269_1217),
    "Defeat 1 Heartless Wight Knight":                                   KHRECOMLocationData("Heartless1"       , 269_1218),
    "Defeat 1 Heartless Gargoyle":                                       KHRECOMLocationData("Heartless1"       , 269_1219),
    "Defeat 1 Heartless Pirate":                                         KHRECOMLocationData("Heartless1"       , 269_1220),
    "Defeat 1 Heartless Air Pirate":                                     KHRECOMLocationData("Heartless1"       , 269_1221),
    "Defeat 1 Heartless Darkball":                                       KHRECOMLocationData("Heartless1"       , 269_1222),
    "Defeat 1 Heartless Defender":                                       KHRECOMLocationData("Heartless1"       , 269_1223),
    "Defeat 1 Heartless Wyvern":                                         KHRECOMLocationData("Heartless1"       , 269_1224),
    "Defeat 1 Heartless Wizard":                                         KHRECOMLocationData("Heartless1"       , 269_1225),
    "Defeat 1 Heartless Neoshadow":                                      KHRECOMLocationData("Heartless1"       , 269_1226),
    "Defeat 1 Heartless White Mushroom":                                 KHRECOMLocationData("Heartless1"       , 269_1227),
    "Defeat 1 Heartless Black Fungus":                                   KHRECOMLocationData("Heartless1"       , 269_1228),
    "Defeat 1 Heartless Creeper Plant":                                  KHRECOMLocationData("Heartless1"       , 269_1229),
    "Defeat 1 Heartless Tornado Step":                                   KHRECOMLocationData("Heartless1"       , 269_1230),
    "Defeat 1 Heartless Crescendo":                                      KHRECOMLocationData("Heartless1"       , 269_1231),
    
    "Defeat 2 Heartless Shadow":                                         KHRECOMLocationData("Heartless2"       , 269_1301),
    "Defeat 2 Heartless Soldier":                                        KHRECOMLocationData("Heartless2"       , 269_1302),
    "Defeat 2 Heartless Large Body":                                     KHRECOMLocationData("Heartless2"       , 269_1303),
    "Defeat 2 Heartless Red Nocturne":                                   KHRECOMLocationData("Heartless2"       , 269_1304),
    "Defeat 2 Heartless Blue Rhapsody":                                  KHRECOMLocationData("Heartless2"       , 269_1305),
    "Defeat 2 Heartless Yellow Opera":                                   KHRECOMLocationData("Heartless2"       , 269_1306),
    "Defeat 2 Heartless Green Requiem":                                  KHRECOMLocationData("Heartless2"       , 269_1307),
    "Defeat 2 Heartless Powerwild":                                      KHRECOMLocationData("Heartless2"       , 269_1308),
    "Defeat 2 Heartless Bouncywild":                                     KHRECOMLocationData("Heartless2"       , 269_1309),
    "Defeat 2 Heartless Air Soldier":                                    KHRECOMLocationData("Heartless2"       , 269_1310),
    "Defeat 2 Heartless Bandit":                                         KHRECOMLocationData("Heartless2"       , 269_1311),
    "Defeat 2 Heartless Fat Bandit":                                     KHRECOMLocationData("Heartless2"       , 269_1312),
    "Defeat 2 Heartless Barrel Spider":                                  KHRECOMLocationData("Heartless2"       , 269_1313),
    "Defeat 2 Heartless Search Ghost":                                   KHRECOMLocationData("Heartless2"       , 269_1314),
    "Defeat 2 Heartless Sea Neon":                                       KHRECOMLocationData("Heartless2"       , 269_1315),
    "Defeat 2 Heartless Screwdiver":                                     KHRECOMLocationData("Heartless2"       , 269_1316),
    "Defeat 2 Heartless Aquatank":                                       KHRECOMLocationData("Heartless2"       , 269_1317),
    "Defeat 2 Heartless Wight Knight":                                   KHRECOMLocationData("Heartless2"       , 269_1318),
    "Defeat 2 Heartless Gargoyle":                                       KHRECOMLocationData("Heartless2"       , 269_1319),
    "Defeat 2 Heartless Pirate":                                         KHRECOMLocationData("Heartless2"       , 269_1320),
    "Defeat 2 Heartless Air Pirate":                                     KHRECOMLocationData("Heartless2"       , 269_1321),
    "Defeat 2 Heartless Darkball":                                       KHRECOMLocationData("Heartless2"       , 269_1322),
    "Defeat 2 Heartless Defender":                                       KHRECOMLocationData("Heartless2"       , 269_1323),
    "Defeat 2 Heartless Wyvern":                                         KHRECOMLocationData("Heartless2"       , 269_1324),
    "Defeat 2 Heartless Wizard":                                         KHRECOMLocationData("Heartless2"       , 269_1325),
    "Defeat 2 Heartless Neoshadow":                                      KHRECOMLocationData("Heartless2"       , 269_1326),
    "Defeat 2 Heartless White Mushroom":                                 KHRECOMLocationData("Heartless2"       , 269_1327),
    "Defeat 2 Heartless Black Fungus":                                   KHRECOMLocationData("Heartless2"       , 269_1328),
    "Defeat 2 Heartless Creeper Plant":                                  KHRECOMLocationData("Heartless2"       , 269_1329),
    "Defeat 2 Heartless Tornado Step":                                   KHRECOMLocationData("Heartless2"       , 269_1330),
    "Defeat 2 Heartless Crescendo":                                      KHRECOMLocationData("Heartless2"       , 269_1331),
    
    "Defeat 3 Heartless Shadow":                                         KHRECOMLocationData("Heartless3"       , 269_1401),
    "Defeat 3 Heartless Soldier":                                        KHRECOMLocationData("Heartless3"       , 269_1402),
    "Defeat 3 Heartless Large Body":                                     KHRECOMLocationData("Heartless3"       , 269_1403),
    "Defeat 3 Heartless Red Nocturne":                                   KHRECOMLocationData("Heartless3"       , 269_1404),
    "Defeat 3 Heartless Blue Rhapsody":                                  KHRECOMLocationData("Heartless3"       , 269_1405),
    "Defeat 3 Heartless Yellow Opera":                                   KHRECOMLocationData("Heartless3"       , 269_1406),
    "Defeat 3 Heartless Green Requiem":                                  KHRECOMLocationData("Heartless3"       , 269_1407),
    "Defeat 3 Heartless Powerwild":                                      KHRECOMLocationData("Heartless3"       , 269_1408),
    "Defeat 3 Heartless Bouncywild":                                     KHRECOMLocationData("Heartless3"       , 269_1409),
    "Defeat 3 Heartless Air Soldier":                                    KHRECOMLocationData("Heartless3"       , 269_1410),
    "Defeat 3 Heartless Bandit":                                         KHRECOMLocationData("Heartless3"       , 269_1411),
    "Defeat 3 Heartless Fat Bandit":                                     KHRECOMLocationData("Heartless3"       , 269_1412),
    "Defeat 3 Heartless Barrel Spider":                                  KHRECOMLocationData("Heartless3"       , 269_1413),
    "Defeat 3 Heartless Search Ghost":                                   KHRECOMLocationData("Heartless3"       , 269_1414),
    "Defeat 3 Heartless Sea Neon":                                       KHRECOMLocationData("Heartless3"       , 269_1415),
    "Defeat 3 Heartless Screwdiver":                                     KHRECOMLocationData("Heartless3"       , 269_1416),
    "Defeat 3 Heartless Aquatank":                                       KHRECOMLocationData("Heartless3"       , 269_1417),
    "Defeat 3 Heartless Wight Knight":                                   KHRECOMLocationData("Heartless3"       , 269_1418),
    "Defeat 3 Heartless Gargoyle":                                       KHRECOMLocationData("Heartless3"       , 269_1419),
    "Defeat 3 Heartless Pirate":                                         KHRECOMLocationData("Heartless3"       , 269_1420),
    "Defeat 3 Heartless Air Pirate":                                     KHRECOMLocationData("Heartless3"       , 269_1421),
    "Defeat 3 Heartless Darkball":                                       KHRECOMLocationData("Heartless3"       , 269_1422),
    "Defeat 3 Heartless Defender":                                       KHRECOMLocationData("Heartless3"       , 269_1423),
    "Defeat 3 Heartless Wyvern":                                         KHRECOMLocationData("Heartless3"       , 269_1424),
    "Defeat 3 Heartless Wizard":                                         KHRECOMLocationData("Heartless3"       , 269_1425),
    "Defeat 3 Heartless Neoshadow":                                      KHRECOMLocationData("Heartless3"       , 269_1426),
    "Defeat 3 Heartless White Mushroom":                                 KHRECOMLocationData("Heartless3"       , 269_1427),
    "Defeat 3 Heartless Black Fungus":                                   KHRECOMLocationData("Heartless3"       , 269_1428),
    "Defeat 3 Heartless Creeper Plant":                                  KHRECOMLocationData("Heartless3"       , 269_1429),
    "Defeat 3 Heartless Tornado Step":                                   KHRECOMLocationData("Heartless3"       , 269_1430),
    "Defeat 3 Heartless Crescendo":                                      KHRECOMLocationData("Heartless3"       , 269_1431),
    
    "Level 02 (Sleight Sliding Dash)":                                   KHRECOMLocationData("Levels"           , 269_2001),
    "Level 17 (Sleight Blitz)":                                          KHRECOMLocationData("Levels"           , 269_2002),
    "Level 07 (Sleight Stun Impact)":                                    KHRECOMLocationData("Levels"           , 269_2003),
    "Level 22 (Sleight Zantetsuken)":                                    KHRECOMLocationData("Levels"           , 269_2004),
    "Level 12 (Sleight Strike Raid)":                                    KHRECOMLocationData("Levels"           , 269_2005),
    "Level 27 (Sleight Sonic Blade)":                                    KHRECOMLocationData("Levels"           , 269_2006),
    "Level 42 (Sleight Ars Arcanum)":                                    KHRECOMLocationData("Levels"           , 269_2007),
    "Level 52 (Sleight Ragnarok)":                                       KHRECOMLocationData("Levels"           , 269_2008),
    "Castle Oblivion Entrance (Sleight Trinity Limit)":                  KHRECOMLocationData("Castle Oblivion"  , 269_2009),
    "01F Exit Hall Axel I (Sleight Fira)":                               KHRECOMLocationData("Exit Halls"       , 269_2010),
    "Starting Checks (Sleight Blizzara)":                                KHRECOMLocationData("Starting"         , 269_2011),
    "06F Exit Hall Larxene I (Sleight Thundara)":                        KHRECOMLocationData("Exit Halls"       , 269_2012),
    "Starting Checks (Sleight Cura)":                                    KHRECOMLocationData("Starting"         , 269_2013),
    "Agrabah Bounty (Sleight Gravira)":                                  KHRECOMLocationData("Agrabah"          , 269_2014),
    "Wonderland Bounty (Sleight Stopra)":                                KHRECOMLocationData("Wonderland"       , 269_2015),
    "07F Exit Hall Riku I (Sleight Aerora)":                             KHRECOMLocationData("Exit Halls"       , 269_2016),
    "01F Exit Hall Axel I (Sleight Firaga)":                             KHRECOMLocationData("Exit Halls"       , 269_2017),
    "Starting Checks (Sleight Blizzaga)":                                KHRECOMLocationData("Starting"         , 269_2018),
    "06F Exit Hall Larxene I (Sleight Thundaga)":                        KHRECOMLocationData("Exit Halls"       , 269_2019),
    "Starting Checks (Sleight Curaga)":                                  KHRECOMLocationData("Starting"         , 269_2020),
    "Agrabah Bounty (Sleight Graviga)":                                  KHRECOMLocationData("Agrabah"          , 269_2021),
    "Wonderland Bounty (Sleight Stopga)":                                KHRECOMLocationData("Wonderland"       , 269_2022),
    "07F Exit Hall Riku I (Sleight Aeroga)":                             KHRECOMLocationData("Exit Halls"       , 269_2023),
    "Monstro Bounty (Sleight Fire Raid)":                                KHRECOMLocationData("Monstro"          , 269_2024),
    "Olympus Coliseum Bounty (Sleight Blizzard Raid)":                   KHRECOMLocationData("Olympus Coliseum" , 269_2025),
    "Neverland Room of Rewards (Sleight Thunder Raid)":                  KHRECOMLocationData("Neverland"        , 269_2026),
    "Hollow Bastion Bounty (Sleight Reflect Raid)":                      KHRECOMLocationData("Hollow Bastion"   , 269_2027),
    "Destiny Islands Bounty (Sleight Judgment)":                         KHRECOMLocationData("Destiny Islands"  , 269_2028),
    "100 Acre Wood Balloon Glider (Sleight Firaga Burst)":               KHRECOMLocationData("100 Acre Wood "   , 269_2029),
    "Castle Oblivion Bounty (Sleight Raging Storm)":                     KHRECOMLocationData("Castle Oblivion"  , 269_2030),
    "Level 57 (Sleight Mega Flare)":                                     KHRECOMLocationData("Levels"           , 269_2031),
    "10F Exit Hall Vexen I (Sleight Freeze)":                            KHRECOMLocationData("Exit Halls"       , 269_2032),
    "Atlantica Bounty (Sleight Homing Blizzara)":                        KHRECOMLocationData("Atlantica"        , 269_2033),
    "Monstro Room of Rewards (Sleight Aqua Splash)":                     KHRECOMLocationData("Monstro"          , 269_2034),
    "08F Exit Hall Riku II (Sleight Magnet Spiral)":                     KHRECOMLocationData("Exit Halls"       , 269_2035),
    "Level 32 (Sleight Lethal Frame)":                                   KHRECOMLocationData("Levels"           , 269_2036),
    "Atlantica Bounty (Sleight Shock Impact)":                           KHRECOMLocationData("Atlantica"        , 269_2037),
    "Level 37 (Sleight Tornado)":                                        KHRECOMLocationData("Levels"           , 269_2038),
    "Atlantica Room of Rewards (Sleight Quake)":                         KHRECOMLocationData("Atlantica"        , 269_2039),
    "Twilight Town Bounty (Sleight Warpinator)":                         KHRECOMLocationData("Twilight Town"    , 269_2040),
    "Agrabah Room of Rewards (Sleight Warp)":                            KHRECOMLocationData("Agrabah"          , 269_2041),
    "Halloween Town Room of Rewards (Sleight Bind)":                     KHRECOMLocationData("Halloween Town"   , 269_2042),
    "100 Acre Wood Piglet (Sleight Confuse)":                            KHRECOMLocationData("100 Acre Wood"    , 269_2043),
    "Halloween Town Ally (Sleight Terror)":                              KHRECOMLocationData("Halloween Town"   , 269_2044),
    "Wonderland Room of Rewards (Sleight Synchro)":                      KHRECOMLocationData("Wonderland"       , 269_2045),
    "Halloween Town Bounty (Sleight Gifted Miracle)":                    KHRECOMLocationData("Halloween Town"   , 269_2046),
    "Neverland Bounty (Sleight Teleport)":                               KHRECOMLocationData("Neverland"        , 269_2047),
    "Level 47 (Sleight Holy)":                                           KHRECOMLocationData("Levels"           , 269_2048),
    "Traverse Town Room of Beginnings (Sleight Proud Roar LV2)":         KHRECOMLocationData("Traverse Town"    , 269_2049),
    "Traverse Town Room of Beginnings (Sleight Proud Roar LV3)":         KHRECOMLocationData("Traverse Town"    , 269_2050),
    "Monstro Room of Truth (Sleight Splash LV2)":                        KHRECOMLocationData("Monstro"          , 269_2051),
    "Monstro Room of Truth (Sleight Splash LV3)":                        KHRECOMLocationData("Monstro"          , 269_2052),
    "100 Acre Wood Clear (Sleight Paradise LV2)":                        KHRECOMLocationData("100 Acre Wood"    , 269_2053),
    "100 Acre Wood Clear (Sleight Paradise LV3)":                        KHRECOMLocationData("100 Acre Wood"    , 269_2054),
    "100 Acre Wood Jump-a-Thon (Sleight Idyll Romp)":                    KHRECOMLocationData("100 Acre Wood"    , 269_2055),
    "Hollow Bastion Room of Rewards (Sleight Flare Breath LV2)":         KHRECOMLocationData("Hollow Bastion"   , 269_2056),
    "Hollow Bastion Room of Rewards (Sleight Flare Breath LV3)":         KHRECOMLocationData("Hollow Bastion"   , 269_2057),
    "Agrabah Room of Truth (Sleight Showtime LV2)":                      KHRECOMLocationData("Agrabah"          , 269_2058),
    "Agrabah Room of Truth (Sleight Showtime LV3)":                      KHRECOMLocationData("Agrabah"          , 269_2059),
    "Neverland Room of Truth (Sleight Twinkle LV2)":                     KHRECOMLocationData("Neverland"        , 269_2060),
    "Neverland Room of Truth (Sleight Twinkle LV3)":                     KHRECOMLocationData("Neverland"        , 269_2061),
    "Olympus Coliseum Room of Truth (Sleight Cross-slash)":              KHRECOMLocationData("Olympus Coliseum" , 269_2062),
    "Olympus Coliseum Room of Truth (Sleight Omnislash)":                KHRECOMLocationData("Olympus Coliseum" , 269_2063),
    "100 Acre Wood Veggie Panic (Sleight Cross-slash+)":                 KHRECOMLocationData("100 Acre Wood"    , 269_2064),
    "Pick Up Donald In Battle (Sleight Magic LV2)":                      KHRECOMLocationData("Traverse Town"    , 269_2065),
    "Pick Up Donald In Battle (Sleight Magic LV3)":                      KHRECOMLocationData("Traverse Town"    , 269_2066),
    "Twilight Town Room of Rewards (Sleight Stardust Blitz)":            KHRECOMLocationData("Twilight Town"    , 269_2067),
    "Pick Up Goofy In Battle (Sleight Goofy Tornado LV2)":               KHRECOMLocationData("Traverse Town"    , 269_2068),
    "Pick Up Goofy In Battle (Sleight Goofy Tornado LV3)":               KHRECOMLocationData("Traverse Town"    , 269_2069),
    "Pick Up Goofy In Battle (Sleight Goofy Smash)":                     KHRECOMLocationData("Traverse Town"    , 269_2070),
    "Pick Up Goofy In Battle (Sleight Wild Crush)":                      KHRECOMLocationData("Traverse Town"    , 269_2071),
    "Agrabah Ally (Sleight Sandstorm LV2)":                              KHRECOMLocationData("Agrabah"          , 269_2072),
    "Agrabah Ally (Sleight Sandstorm LV3)":                              KHRECOMLocationData("Agrabah"          , 269_2073),
    "Halloween Town Ally (Sleight Surprise! LV2)":                       KHRECOMLocationData("Halloween Town"   , 269_2074),
    "Halloween Town Ally (Sleight Surprise! LV3)":                       KHRECOMLocationData("Halloween Town"   , 269_2075),
    "Atlantica Ally (Sleight Spiral Wave LV2)":                          KHRECOMLocationData("Atlantica"        , 269_2076),
    "Atlantica Ally (Sleight Spiral Wave LV3)":                          KHRECOMLocationData("Atlantica"        , 269_2077),
    "Neverland Ally (Sleight Hummingbird LV2)":                          KHRECOMLocationData("Atlantica"        , 269_2078),
    "Neverland Ally (Sleight Hummingbird LV3)":                          KHRECOMLocationData("Atlantica"        , 269_2079),
    "Hollow Bastion Ally (Sleight Furious Volley LV2)":                  KHRECOMLocationData("Hollow Bastion"   , 269_2080),
    "Hollow Bastion Ally (Sleight Furious Volley LV3)":                  KHRECOMLocationData("Hollow Bastion"   , 269_2081),
    "Pick Up Pluto In Battle (Sleight Lucky Bounty LV2)":                KHRECOMLocationData("Traverse Town"    , 269_2082),
    "Pick Up Pluto In Battle (Sleight Lucky Bounty LV3)":                KHRECOMLocationData("Traverse Town"    , 269_2083),

    "Final Marluxia":                                                    KHRECOMLocationData("Final"            , 269_9999),
}

event_location_table: Dict[str, KHRECOMLocationData] = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}
