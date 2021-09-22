from typing import Set, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import is_option_enabled

class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True

def get_locations(world: MultiWorld, player: int):
    location_table: Set[LocationData] = {
        # PresentItemLocations
        LocationData('Tutorial', 'Yo Momma 1',  1337000),
        LocationData('Tutorial', 'Yo Momma 2',  1337001),
        LocationData('Lake desolation', 'Starter chest 2',  1337002),
        LocationData('Lake desolation', 'Starter chest 3',  1337003),
        LocationData('Lake desolation', 'Starter chest 1',  1337004),
        LocationData('Lake desolation', 'Timespinner Wheel room',  1337005),
        LocationData('Upper lake desolation', 'Forget me not chest',  1337006),
        LocationData('Lower lake desolation', 'Chicken chest',  1337007, lambda state: state._timespinner_has_timestop(world, player)),
        LocationData('Lower lake desolation', 'Not so secret room',  1337008, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Lower lake desolation', 'Tank chest',  1337009, lambda state: state._timespinner_has_timestop(world, player)),
        LocationData('Upper lake desolation', 'Oxygen recovery room',  1337010),
        LocationData('Upper lake desolation', 'Lake secret',  1337011, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Upper lake desolation', 'Double jump cave floor',  1337012, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Upper lake desolation', 'Double jump cave platform',  1337013),
        LocationData('Upper lake desolation', 'Fire-Locked sparrow chest',  1337014),
        LocationData('Upper lake desolation', 'Crash site pedestal',  1337015),
        LocationData('Upper lake desolation', 'Crash site chest 1',  1337016, lambda state: state.has_all(['Killed Maw', 'Gas Mask'], player)),
        LocationData('Upper lake desolation', 'Crash site chest 2',  1337017, lambda state: state.has_all(['Killed Maw', 'Gas Mask'], player)),
        LocationData('Upper lake desolation', 'Kitty Boss',  1337018),
        LocationData('Libary', 'Basement',  1337019),
        LocationData('Libary', 'Consolation',  1337020),
        LocationData('Libary', 'Librarian',  1337021),
        LocationData('Libary', 'Reading nook chest',  1337022),
        LocationData('Libary', 'Storage room chest 1',  1337023, lambda state: state._timespinner_has_keycard_D(world, player)),
        LocationData('Libary', 'Storage room chest 2',  1337024, lambda state: state._timespinner_has_keycard_D(world, player)),
        LocationData('Libary', 'Storage room chest 3',  1337025, lambda state: state._timespinner_has_keycard_D(world, player)),
        LocationData('Libary top', 'Backer room chest 5',  1337026),
        LocationData('Libary top', 'Backer room chest 4',  1337027),
        LocationData('Libary top', 'Backer room chest 3',  1337028),
        LocationData('Libary top', 'Backer room chest 2',  1337029),
        LocationData('Libary top', 'Backer room chest 1',  1337030),
        LocationData('Varndagroth tower left', 'Elevator Key not required',  1337031),
        LocationData('Varndagroth tower left', 'Ye olde Timespinner',  1337032),
        LocationData('Varndagroth tower left', 'C Keycard chest',  1337033, lambda state: state._timespinner_has_keycard_C(world, player)),
        LocationData('Varndagroth tower left', 'Left air vents secret',  1337034, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Varndagroth tower left', 'Left elevator chest',  1337035, lambda state: state.has('Elevator Keycard', player)),
        LocationData('Varndagroth tower right (upper)', 'Spider heck room',  1337036),
        LocationData('Varndagroth tower right (elevator)', 'Right elevator chest',  1337037),
        LocationData('Varndagroth tower right (upper)', 'Elevator card chest',  1337038, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        LocationData('Varndagroth tower right (upper)', 'Air vents left',  1337039, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        LocationData('Varndagroth tower right (upper)', 'Air Vents right',  1337040, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        LocationData('Varndagroth tower right (lower)', 'Right side bottom floor',  1337041),
        LocationData('Varndagroth tower right (elevator)', 'Varndagroth',  1337042, lambda state: state._timespinner_has_keycard_C(world, player)),
        LocationData('Varndagroth tower right (elevator)', 'Varndagroth Spider hell',  1337043, lambda state: state._timespinner_has_keycard_A(world, player)),
        LocationData('Lake desolation', 'Skeleton',  1337044, lambda state: state._timespinner_has_doublejump(world, player)), # region changed from 'Sealed Caves (Xarion)' to ease entrance logic
        LocationData('Sealed Caves (Xarion)', 'Shroom jump room',  1337045, lambda state: state._timespinner_has_timestop(world, player)),
        LocationData('Sealed Caves (Xarion)', 'Double shroom room',  1337046),
        LocationData('Sealed Caves (Xarion)', 'Mini jackpot room',  1337047, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Sealed Caves (Xarion)', 'Below mini jackpot room',  1337048),
        LocationData('Sealed Caves (Xarion)', 'Sealed cave secret room',  1337049, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Sealed Caves (Xarion)', 'Below Sealed cave secret',  1337050),
        LocationData('Sealed Caves (Xarion)', 'Last chance before Xarion',  1337051, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Sealed Caves (Xarion)', 'Xarion',  1337052),
        LocationData('Sealed Caves (Sirens)', 'Solo siren chest',  1337053, lambda state: state.has('Water Mask', player)),
        LocationData('Sealed Caves (Sirens)', 'Big siren room right',  1337054, lambda state: state.has('Water Mask', player)),
        LocationData('Sealed Caves (Sirens)', 'Big siren Room left',  1337055, lambda state: state.has('Water Mask', player)),
        LocationData('Sealed Caves (Sirens)', 'Room after sirens chest 2',  1337056),
        LocationData('Sealed Caves (Sirens)', 'Room after sirens chest 1',  1337057),
        LocationData('Militairy Fortress', 'Militairy Bomber chest',  1337058, lambda state: state.has('Timespinner Wheel', player) and state._timespinner_has_doublejump_of_npc(world, player)),
        LocationData('Militairy Fortress', 'Close combat room',  1337059),
        LocationData('Militairy Fortress', 'Bridge full of soldiers',  1337060),
        LocationData('Militairy Fortress', 'Giantess Room',  1337061),
        LocationData('Militairy Fortress', 'Bridge with Giantess',  1337062),
        LocationData('Militairy Fortress', 'Military B door chest 2',  1337063, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_has_keycard_B(world, player)),
        LocationData('Militairy Fortress', 'Military B door chest 1',  1337064, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_has_keycard_B(world, player)),
        LocationData('Militairy Fortress', 'Military pedestal',  1337065, lambda state: state._timespinner_has_doublejump(world, player) and (state._timespinner_has_doublejump_of_npc(world, player) or state._timespinner_has_forwarddash_doublejump(world, player))),
        LocationData('The lab', 'Coffee Break chest',  1337066),
        LocationData('The lab', 'Lower trash right',  1337067, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('The lab', 'Lower trash left',  1337068, lambda state: state._timespinner_has_upwarddash(world, player)),
        LocationData('The lab', 'Single turret room',  1337069, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('The lab (power off)', 'Trash jump room',  1337070),
        LocationData('The lab (power off)', 'Dynamo Works',  1337071),
        LocationData('The lab (upper)', 'Blob mom',  1337072),
        LocationData('The lab (power off)', 'Experiment #13',  1337073),
        LocationData('The lab (upper)', 'Download and chest room',  1337074),
        LocationData('The lab (upper)', 'Lab secret',  1337075, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('The lab (power off)', 'Lab Spider hell',  1337076, lambda state: state._timespinner_has_keycard_A(world, player)),
        LocationData('Emperors tower', 'Bottom',  1337077),
        LocationData('Emperors tower', 'After Courtyard Floor Secret',  1337078, lambda state: state._timespinner_has_upwarddash(world, player) and state._timespinner_can_break_walls(world, player)),
        LocationData('Emperors tower', 'After Courtyard Chest',  1337079, lambda state: state._timespinner_has_upwarddash(world, player)),
        LocationData('Emperors tower', 'Galactic Sage Room',  1337080),
        LocationData('Emperors tower', 'Bottom of Right Tower',  1337081),
        LocationData('Emperors tower', 'Wayyyy up there',  1337082),
        LocationData('Emperors tower', 'Left tower balcony',  1337083),
        LocationData('Emperors tower', 'Dad\'s Chambers chest',  1337084),
        LocationData('Emperors tower', 'Dad\'s Chambers pedestal',  1337085),

        # PastItemLocations
        LocationData('Refugee Camp', 'Neliste\'s Bra',  1337086),
        LocationData('Refugee Camp', 'Refugee camp storage chest 3',  1337087),
        LocationData('Refugee Camp', 'Refugee camp storage chest 2',  1337088),
        LocationData('Refugee Camp', 'Refugee camp storage chest 1',  1337089),
        LocationData('Forest', 'Refugee camp roof',  1337090),
        LocationData('Forest', 'Bat jump chest',  1337091, lambda state: state._timespinner_has_doublejump_of_npc(world, player) or state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Forest', 'Green platform secret',  1337092, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Forest', 'Rats guarded chest',  1337093),
        LocationData('Forest', 'Waterfall chest 1',  1337094, lambda state: state.has('Water Mask', player)),
        LocationData('Forest', 'Waterfall chest 2',  1337095, lambda state: state.has('Water Mask', player)),
        LocationData('Forest', 'Batcave',  1337096),
        LocationData('Forest', 'Bridge Chest',  1337097),
        LocationData('Left Side forest Caves', 'Solitary bat room',  1337098),
        LocationData('Upper Lake Sirine', 'Rat nest',  1337099),
        LocationData('Upper Lake Sirine', 'Double jump cave platform (past)',  1337100, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Upper Lake Sirine', 'Double jump cave floor (past)',  1337101),
        LocationData('Upper Lake Sirine', 'West lake serene cave secret',  1337102, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Upper Lake Sirine', 'Chest behind vines',  1337103),
        LocationData('Upper Lake Sirine', 'Pyramid keys room',  1337104),
        LocationData('Upper Lake Sirine', 'Deep dive',  1337105),
        LocationData('Upper Lake Sirine', 'Under the eels',  1337106),
        LocationData('Upper Lake Sirine', 'Water spikes room',  1337107),
        LocationData('Upper Lake Sirine', 'Underwater secret',  1337108, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Upper Lake Sirine', 'T chest',  1337109),
        LocationData('Upper Lake Sirine', 'Past the eels',  1337110),
        LocationData('Upper Lake Sirine', 'Underwater pedestal',  1337111),
        LocationData('Caves of Banishment (Maw)', 'Mushroom double jump',  1337112, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Caves of banishment secret room',  1337113),
        LocationData('Caves of Banishment (Maw)', 'Below caves of banishment secret',  1337114),
        LocationData('Caves of Banishment (Maw)', 'Single shroom room',  1337115),
        LocationData('Caves of Banishment (Maw)', 'Jackpot room chest 1',  1337116, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Jackpot room chest 2',  1337117, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Jackpot room chest 3',  1337118, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Jackpot room chest 4',  1337119, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Banishment pedestal',  1337120),
        LocationData('Caves of Banishment (Maw)', 'Last chance before Maw',  1337121, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Caves of Banishment (Maw)', 'Killed Maw',  None, lambda state: state.has('Gas Mask', player)),
        LocationData('Caves of Banishment (Maw)', 'Mineshaft',  1337122, lambda state: state.has('Gas Mask', player)),
        LocationData('Caves of Banishment (Sirens)', 'Wyvern room',  1337123),
        LocationData('Caves of Banishment (Sirens)', 'Above water sirens',  1337124),
        LocationData('Caves of Banishment (Sirens)', 'Underwater sirens left',  1337125, lambda state: state.has('Water Mask', player)),
        LocationData('Caves of Banishment (Sirens)', 'Underwater sirens right',  1337126, lambda state: state.has('Water Mask', player)),
        LocationData('Caves of Banishment (Sirens)', 'Water hook',  1337127),
        LocationData('Caste Ramparts', 'Caste Bomber chest',  1337128, lambda state: state._timespinner_has_multiple_small_jumps_of_npc(world, player)),
        LocationData('Caste Ramparts', 'Freeze the engineer',  1337129, lambda state: state.has('Talaria Attachment', player) or state._timespinner_has_timestop(world, player)),
        LocationData('Caste Ramparts', 'Giantess guarded room',  1337130),
        LocationData('Caste Ramparts', 'Knight and archer guarded room',  1337131),
        LocationData('Caste Ramparts', 'Castle pedestal',  1337132),
        LocationData('Caste Keep', 'Basement secret pedestal',  1337133, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Caste Keep', 'Break the wall',  1337134),
        LocationData('Royal towers (lower)', 'Yas queen room',  1337135, lambda state: state._timespinner_has_pink(world, player)),
        LocationData('Caste Keep', 'Basement hammer',  1337136),
        LocationData('Caste Keep', 'Omelette chest',  1337137),
        LocationData('Caste Keep', 'Just an egg',  1337138),
        LocationData('Caste Keep', 'Out of the way',  1337139),
        LocationData('Caste Keep', 'Killed Twins',  None, lambda state: state._timespinner_has_timestop(world, player)),
        LocationData('Caste Keep', 'Twins',  1337140, lambda state: state._timespinner_has_timestop(world, player)),
        LocationData('Caste Keep', 'Royal guard tiny room',  1337141, lambda state: state._timespinner_has_doublejump(world, player)),
        LocationData('Royal towers (lower)', 'Royal tower floor secret',  1337142, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_can_break_walls(world, player)),
        LocationData('Royal towers', 'Above the gap',  1337143),
        LocationData('Royal towers', 'Under the ice mage',  1337144),
        LocationData('Royal towers (upper)', 'Next to easy struggle juggle room',  1337145),
        LocationData('Royal towers (upper)', 'Easy struggle juggle',  1337146, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        LocationData('Royal towers (upper)', 'Hard struggle juggle',  1337147, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        LocationData('Royal towers (upper)', 'No sturggle required',  1337148, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        LocationData('Royal towers', 'Right tower freebie',  1337149),
        LocationData('Royal towers (upper)', 'Above the cide mage',  1337150),
        LocationData('Royal towers (upper)', 'Royal guard big room',  1337151),
        LocationData('Royal towers (upper)', 'Before Aelana',  1337152),
        LocationData('Royal towers (upper)', 'Killed Aelana',  None),
        LocationData('Royal towers (upper)', 'Statue room',  1337153, lambda state: state._timespinner_has_upwarddash(world, player)),
        LocationData('Royal towers (upper)', 'Aelana\'s pedestal',  1337154),
        LocationData('Royal towers (upper)', 'After Aelana',  1337155),

        # 1337157 - 1337170 Downloads

        # 1337171 - 1337238 Reserved

        # PyramidItemLocations
        #LocationData('Temporal Gyre', 'Transition chest 1',  1337239),
        #LocationData('Temporal Gyre', 'Transition chest 2',  1337240),
        #LocationData('Temporal Gyre', 'Transition chest 3',  1337241),
        #LocationData('Temporal Gyre', 'Ravenlord pre fight',  1337242),
        #LocationData('Temporal Gyre', 'Ravenlord post fight',  1337243),
        #LocationData('Temporal Gyre', 'Ifrid pre fight',  1337244),
        #LocationData('Temporal Gyre', 'Ifrid post fight',  1337245),
        LocationData('Ancient Pyramid (left)', 'Why not it\'s right there',  1337246),
        LocationData('Ancient Pyramid (left)', 'Conviction guarded room',  1337247),
        LocationData('Ancient Pyramid (right)', 'Pit secret room',  1337248, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Ancient Pyramid (right)', 'Regret chest',  1337249, lambda state: state._timespinner_can_break_walls(world, player)),
        LocationData('Ancient Pyramid (right)', 'Killed Nightmare',  None)
    }

    downloadable_items: Set[LocationData] = {
        # DownloadTerminals
        LocationData('Libary', 'Library terminal 1',  1337157, lambda state: state.has('Tablet', player)),
        LocationData('Libary', 'Library terminal 2',  1337156, lambda state: state.has('Tablet', player)),
        LocationData('Libary', 'Library terminal 3',  1337159, lambda state: state.has('Tablet', player)),
        LocationData('Libary', 'V terminal 1',  1337160, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        LocationData('Libary', 'V terminal 2',  1337161, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        LocationData('Libary', 'V terminal 3',  1337162, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        LocationData('Libary top', 'Backer room terminal',  1337163, lambda state: state.has('Tablet', player)),
        LocationData('Varndagroth tower right (elevator)', 'Medbay',  1337164, lambda state: state.has('Tablet', player) and state._timespinner_has_keycard_B(world, player)),
        LocationData('The lab (upper)', 'Chest and download terminal',  1337165, lambda state: state.has('Tablet', player)),
        LocationData('The lab (power off)', 'Lab terminal middle',  1337166, lambda state: state.has('Tablet', player)),
        LocationData('The lab (power off)', 'Sentry platform terminal',  1337167, lambda state: state.has('Tablet', player)),
        LocationData('The lab', 'Experiment 13 terminal',  1337168, lambda state: state.has('Tablet', player)),
        LocationData('The lab', 'Lab terminal left',  1337169, lambda state: state.has('Tablet', player)),
        LocationData('The lab (power off)', 'Lab terminal right',  1337170, lambda state: state.has('Tablet', player))
    }

    if is_option_enabled(world, player, "DownloadableItems"):
        return { *location_table, *downloadable_items }
    else:
        return location_table

starter_progression_locations: Set[str] = {
    'Starter chest 2',
    'Starter chest 3',
    'Starter chest 1',
    'Timespinner Wheel room'
}

events: Set[str] = {
    "Killed Maw",
    "Killed Twins",
    "Killed Aelana",
    'Killed Nightmare'
}