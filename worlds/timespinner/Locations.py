import typing

class LocationData(typing.NamedTuple):
    region: str
    code: int

location_table: typing.Dict[str, LocationData] = {
    # PresentItemLocations
    'Yo Momma 1': LocationData('Tutorial', 1337000),
    'Yo Momma 2': LocationData('Tutorial', 1337001),
    'Starter chest 2': LocationData('Lake desolation' , 1337002),
    'Starter chest 3': LocationData('Lake desolation' , 1337003),
    'Starter chest 1': LocationData('Lake desolation' , 1337004),
    'Timespinner Wheel room': LocationData('Lake desolation' , 1337005),
    'Forget me not chest': LocationData('Lake desolation' , 1337006),
    'Chicken chest': LocationData('Lower lake desolation' , 1337007),
    'Not so secret room': LocationData('Lower lake desolation' , 1337008),
    'Tank chest': LocationData('Lower lake desolation' , 1337009),
    'Oxygen recovery room': LocationData('Upper lake desolation' , 1337010),
    'Lake secret': LocationData('Upper lake desolation' , 1337011),
    'Double jump cave floor': LocationData('Upper lake desolation' , 1337012),
    'Double jump cave platform': LocationData('Upper lake desolation' , 1337013),
    'Fire-Locked sparrow chest': LocationData('Upper lake desolation' , 1337014),
    'Crash site pedestal': LocationData('Upper lake desolation' , 1337015),
    'Crash site chest 1': LocationData('Upper lake desolation' , 1337016),
    'Crash site chest 2': LocationData('Upper lake desolation' , 1337017),
    'Kitty Boss': LocationData('Upper lake desolation' , 1337018),
    'Basement': LocationData('Libary' , 1337019),
    'Consolation': LocationData('Libary' , 1337020),
    'Librarian': LocationData('Libary' , 1337021),
    'Reading nook chest': LocationData('Libary' , 1337022),
    'Storage room chest 1': LocationData('Libary' , 1337023),
    'Storage room chest 2': LocationData('Libary' , 1337024),
    'Storage room chest 3': LocationData('Libary' , 1337025),
    'Backer room chest 5': LocationData('Libary top' , 1337026),
    'Backer room chest 4': LocationData('Libary top' , 1337027),
    'Backer room chest 3': LocationData('Libary top' , 1337028),
    'Backer room chest 2': LocationData('Libary top' , 1337029),
    'Backer room chest 1': LocationData('Libary top' , 1337030),
    'Elevator Key not required': LocationData('Varndagroth tower left' , 1337031),
    'Ye olde Timespinner': LocationData('Varndagroth tower left' , 1337032),
    'C Keycard chest': LocationData('Varndagroth tower left' , 1337033),
    'Left air vents secret': LocationData('Varndagroth tower left' , 1337034),
    'Left elevator chest': LocationData('Varndagroth tower left' , 1337035),
    'Spider heck room': LocationData('Varndagroth tower right (upper)' , 1337036),
    'Right elevator chest': LocationData('Varndagroth tower right (elevator)' , 1337037),
    'Elevator card chest': LocationData('Varndagroth tower right (upper)' , 1337038),
    'Air vents left': LocationData('Varndagroth tower right (upper)' , 1337039),
    'Air Vents right': LocationData('Varndagroth tower right (upper)' , 1337040),
    'Right side bottom floor': LocationData('Varndagroth tower right (lower)' , 1337041),
    'Varndagroth' : LocationData('Varndagroth tower right (elevator)' , 1337042),
    'Varndagroth Spider hell': LocationData('Varndagroth tower right (elevator)' , 1337043),
    'Skeleton': LocationData('Lake desolation' , 1337044), # region changed from 'Sealed Caves (Xarion)' to ease entrance logic
    'Shroom jump room': LocationData('Sealed Caves (Xarion)' , 1337045),
    'Double shroom room': LocationData('Sealed Caves (Xarion)' , 1337046),
    'Mini jackpot room': LocationData('Sealed Caves (Xarion)' , 1337047),
    'Below mini jackpot room': LocationData('Sealed Caves (Xarion)' , 1337048),
    'Sealed cave secret room': LocationData('Sealed Caves (Xarion)' , 1337049),
    'Below Sealed cave secret': LocationData('Sealed Caves (Xarion)' , 1337050),
    'Last chance before Xarion': LocationData('Sealed Caves (Xarion)' , 1337051),
    'Xarion': LocationData('Sealed Caves (Xarion)' , 1337052),
    'Solo siren chest': LocationData('Sealed Caves (Sirens)' , 1337053),
    'Big siren room right': LocationData('Sealed Caves (Sirens)' , 1337054),
    'Big siren Room left': LocationData('Sealed Caves (Sirens)' , 1337055),
    'Room after sirens chest 2': LocationData('Sealed Caves (Sirens)' , 1337056),
    'Room after sirens chest 1': LocationData('Sealed Caves (Sirens)' , 1337057),
    'Militairy Bomber chest': LocationData('Militairy Fortress' , 1337058),
    'Close combat room': LocationData('Militairy Fortress' , 1337059),
    'Bridge full of soldiers': LocationData('Militairy Fortress' , 1337060),
    'Giantess Room': LocationData('Militairy Fortress' , 1337061),
    'Bridge with Giantess': LocationData('Militairy Fortress' , 1337062),
    'Military B door chest 2': LocationData('Militairy Fortress' , 1337063),
    'Military B door chest 1': LocationData('Militairy Fortress' , 1337064),
    'Military pedestal': LocationData('Militairy Fortress' , 1337065),
    'Coffee Break chest': LocationData('The lab' , 1337066),
    'Lower trash right': LocationData('The lab' , 1337067),
    'Lower trash left': LocationData('The lab' , 1337068),
    'Single turret room': LocationData('The lab' , 1337069),
    'Trash jump room': LocationData('The lab (power off)' , 1337070),
    'Dynamo Works': LocationData('The lab (power off)' , 1337071),
    'Blob mom': LocationData('The lab (upper)' , 1337072),
    'Experiment #13': LocationData('The lab (power off)' , 1337073),
    'Download and chest room': LocationData('The lab (upper)' , 1337074),
    'Lab secret': LocationData('The lab (upper)' , 1337075),
    'Lab Spider hell': LocationData('The lab (power off)' , 1337076),
    'Bottom': LocationData('Emperors tower' , 1337077),
    'After Courtyard Floor Secret': LocationData('Emperors tower' , 1337078),
    'Top': LocationData('Emperors tower' , 1337079),
    'Galactic Sage Room': LocationData('Emperors tower' , 1337080),
    'Bottom of Right Tower': LocationData('Emperors tower' , 1337081),
    'Wayyyy up there': LocationData('Emperors tower' , 1337082),
    'Left tower balcony': LocationData('Emperors tower' , 1337083),
    'Dad\'s Chambers chest': LocationData('Emperors tower' , 1337084),
    'Dad\'s Chambers pedestal': LocationData('Emperors tower' , 1337085),

    # PastItemLocations
    'Neliste\'s Bra': LocationData('Refugee Camp' , 1337086),
    'Refugee camp storage chest 3': LocationData('Refugee Camp' , 1337087),
    'Refugee camp storage chest 2': LocationData('Refugee Camp' , 1337088),
    'Refugee camp storage chest 1': LocationData('Refugee Camp' , 1337089),
    'Refugee camp roof': LocationData('Forest' , 1337090),
    'Bat jump chest': LocationData('Forest' , 1337091),
    'Green platform secret': LocationData('Forest' , 1337092),
    'Rats guarded chest': LocationData('Forest' , 1337093),
    'Waterfall chest 1': LocationData('Forest' , 1337094),
    'Waterfall chest 2': LocationData('Forest' , 1337095),
    'Batcave': LocationData('Forest' , 1337096),
    'Bridge Chest': LocationData('Forest' , 1337097),
    'Solitary bat room': LocationData('Forest' , 1337098),
    'Rat nest': LocationData('Upper Lake Sirine' , 1337099),
    'Double jump cave platform (past)': LocationData('Upper Lake Sirine' , 1337100),
    'Double jump cave floor (past)': LocationData('Upper Lake Sirine' , 1337101),
    'West lake serene cave secret': LocationData('Upper Lake Sirine' , 1337102),
    'Chest behind vines': LocationData('Upper Lake Sirine' , 1337103),
    'Pyramid keys room': LocationData('Upper Lake Sirine' , 1337104),
    'Deep dive': LocationData('Upper Lake Sirine' , 1337105),
    'Under the eels': LocationData('Upper Lake Sirine' , 1337106),
    'Water spikes room': LocationData('Upper Lake Sirine' , 1337107),
    'Underwater secret': LocationData('Upper Lake Sirine' , 1337108),
    'T chest': LocationData('Upper Lake Sirine' , 1337109),
    'Past the eels': LocationData('Upper Lake Sirine' , 1337110),
    'Underwater pedestal': LocationData('Upper Lake Sirine' , 1337111),
    'Mushroom double jump': LocationData('Caves of Banishment (Maw)' , 1337112),
    'Caves of banishment secret room': LocationData('Caves of Banishment (Maw)' , 1337113),
    'Below caves of banishment secret': LocationData('Caves of Banishment (Maw)' , 1337114),
    'Single shroom room': LocationData('Caves of Banishment (Maw)' , 1337115),
    'Jackpot room chest 1': LocationData('Caves of Banishment (Maw)' , 1337116),
    'Jackpot room chest 2': LocationData('Caves of Banishment (Maw)' , 1337117),
    'Jackpot room chest 3': LocationData('Caves of Banishment (Maw)' , 1337118),
    'Jackpot room chest 4': LocationData('Caves of Banishment (Maw)' , 1337119),
    'Banishment pedestal': LocationData('Caves of Banishment (Maw)' , 1337120),
    'Last chance before Maw': LocationData('Caves of Banishment (Maw)' , 1337121),
    'Mineshaft': LocationData('Caves of Banishment (Maw)' , 1337122),
    'Wyvern room': LocationData('Caves of Banishment (Sirens)' , 1337123),
    'Above water sirens': LocationData('Caves of Banishment (Sirens)' , 1337124),
    'Underwater sirens left': LocationData('Caves of Banishment (Sirens)' , 1337125),
    'Underwater sirens right': LocationData('Caves of Banishment (Sirens)' , 1337126),
    'Water hook': LocationData('Caves of Banishment (Sirens)' , 1337127),
    'Caste Bomber chest': LocationData('Caste Ramparts' , 1337128),
    'Freeze the engineer': LocationData('Caste Ramparts' , 1337129),
    'Giantess guarded room': LocationData('Caste Ramparts' , 1337130),
    'Knight and archer guarded room': LocationData('Caste Ramparts' , 1337131),
    'Castle pedestal': LocationData('Caste Ramparts' , 1337132),
    'Basement secret pedestal': LocationData('Caste Keep' , 1337133),
    'Break the wall': LocationData('Caste Keep' , 1337134),
    'Yas queen room': LocationData('Caste Keep' , 1337135),
    'Basement hammer': LocationData('Caste Keep' , 1337136),
    'Omelette chest': LocationData('Caste Keep' , 1337137),
    'Just an egg': LocationData('Caste Keep' , 1337138),
    'Out of the way': LocationData('Caste Keep' , 1337139),
    'Twins': LocationData('Caste Keep' , 1337140),
    'Royal guard tiny room': LocationData('Caste Keep' , 1337141),
    'Royal tower floor secret': LocationData('Royal towers (lower)' , 1337142),
    'Above the gap': LocationData('Royal towers' , 1337143),
    'Under the ice mage': LocationData('Royal towers' , 1337144),
    'Next to easy struggle juggle room': LocationData('Royal towers (upper)' , 1337145),
    'Easy struggle juggle': LocationData('Royal towers (upper)' , 1337146),
    'Hard struggle juggle': LocationData('Royal towers (upper)' , 1337147),
    'No sturggle required': LocationData('Royal towers (upper)' , 1337148),
    'Right tower freebie': LocationData('Royal towers' , 1337149),
    'Above the cide mage': LocationData('Royal towers (upper)' , 1337150),
    'Royal guard big room': LocationData('Royal towers (upper)' , 1337151),
    'Before Aelana': LocationData('Royal towers (upper)' , 1337152),
    'Statue room': LocationData('Royal towers (upper)' , 1337153),
    'Aelana\'s pedestal': LocationData('Royal towers (upper)' , 1337154),
    'After Aelana': LocationData('Royal towers (upper)' , 1337155),

    # 1337157 - 1337170 Downloads

    # 1337171 - 1337238 Reserved

    # PyramidItemLocations
    #'Transition chest 1': LocationData('Temporal Gyre' , 1337239),
    #'Transition chest 2': LocationData('Temporal Gyre' , 1337240),
    #'Transition chest 3': LocationData('Temporal Gyre' , 1337241),
    #'Ravenlord pre fight': LocationData('Temporal Gyre' , 1337242),
    #'Ravenlord post fight': LocationData('Temporal Gyre' , 1337243),
    #'Ifrid pre fight': LocationData('Temporal Gyre' , 1337244),
    #'Ifrid post fight': LocationData('Temporal Gyre' , 1337245),
    'Why not it\'s right there': LocationData('Ancient Pyramid (left)' , 1337246),
    'Conviction guarded room': LocationData('Ancient Pyramid (left)' , 1337247),
    'Pit secret room': LocationData('Ancient Pyramid (right)' , 1337248),
    'Regret chest': LocationData('Ancient Pyramid (right)' , 1337249)
}

downloadable_items: typing.Dict[str, LocationData] = {
    # DownloadTerminals
    'Library terminal 1': LocationData('Libary' , 1337157),
    'Library terminal 2': LocationData('Libary' , 1337156),
    'Library terminal 3' : LocationData('Libary' , 1337159),
    'V terminal 1': LocationData('Libary' , 1337160),
    'V terminal 2': LocationData('Libary' , 1337161),
    'V terminal 3': LocationData('Libary' , 1337162),
    'Backer room terminal': LocationData('Libary top' , 1337163),
    'Medbay': LocationData('Varndagroth tower right' , 1337164),
    'Chest and download terminal': LocationData('The lab' , 1337165),
    'Lab terminal middle': LocationData('The lab' , 1337166),
    'Sentry platform terminal': LocationData('The lab' , 1337167),
    'Experiment 13 terminal': LocationData('The lab' , 1337168),
    'Lab terminal left': LocationData('The lab' , 1337169),
    'Lab terminal right': LocationData('The lab' , 1337170)
}

starter_progression_locations = [
    'Starter chest 2',
    'Starter chest 3',
    'Starter chest 1',
    'Timespinner Wheel room'
]

events = [
    "Killed Nightmare"
]