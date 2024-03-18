from BaseClasses import Location
from .data import lname, iname
from .options import CVCotMOptions

from typing import Dict, Union, List, Tuple, Optional, Set

base_id = 0xD55C0000


class CVCotMLocation(Location):
    game: str = "Castlevania Circle of the Moon"


# # #    KEY    # # #
# "code" = The unique part of the Location's AP code attribute, as well as the in-game bitflag index starting from
#          0x80389BE4 that indicates the Location has been checked. Add this + base_id to get the actual AP code.
# "offset" = The offset in the ROM to overwrite to change the Item on that Location.
# "rule" = What rule should be applied to the Location during set_rules, as defined in self.rules in the CVCotMRules
#          class definition in rules.py.
# "event" = What event Item to place on that Location, for Locations that are events specifically.
# "type" = Anything special about this Location that should be considered, whether it be a boss Location, etc.
# "countdown" = What Countdown number in the array of Countdown numbers that Location contributes to.
location_info = {
    # Sealed Room
    lname.sr3:   {"code": 0x35,   "offset": 0xD0310, "rule": "Roc"},
    # Catacombs
    lname.cc1:   {"code": 0x37,   "offset": 0xD0658, "rule": "Push"},
    lname.cc3:   {"code": 0x43,   "offset": 0xD0370, "rule": "Double"},
    lname.cc3b:  {"code": 0x36,   "offset": 0xD0364, "rule": "Double AND Freeze"},
    lname.cc4:   {"code": 0xA8,   "offset": 0xD0934},
    lname.cc5:   {"code": 0x38,   "offset": 0xD0DE4, "rule": "Tackle"},
    lname.cc8:   {"code": 0x3A,   "offset": 0xD1078},
    lname.cc8b:  {"code": 0x3B,   "offset": 0xD1084, "rule": "Kick"},
    lname.cc9:   {"code": 0x40,   "offset": 0xD0F94},
    lname.cc10:  {"code": 0x39,  "offset": 0xD12C4},
    lname.cc13:  {"code": 0x41,  "offset": 0xD0DA8},
    lname.cc14:  {"code": 0x3C,  "offset": 0xD1168},
    lname.cc14b: {"code": 0x3D,  "offset": 0xD1174, "rule": "Double OR Kick"},
    lname.cc16:  {"code": 0x3E,  "offset": 0xD0C40},
    lname.cc20:  {"code": 0x42,  "offset": 0xD103C},
    lname.cc22:  {"code": 0x3F,  "offset": 0xD07C0},
    lname.cc24:  {"code": 0xA9,  "offset": 0xD1288, "type": "boss"},
    lname.cc25:  {"code": 0x44,  "offset": 0xD12A0, "rule": "Double"},
    # Abyss Staircase
    lname.as2:   {"code": 0x47,  "offset": 0xD181C},
    lname.as3:   {"code": 0x45,  "offset": 0xD1774},
    lname.as4:   {"code": 0x46,  "offset": 0xD1678, "rule": "Roc"},
    lname.as9:   {"code": 0x48,  "offset": 0xD17EC},
    # Audience Room
    lname.ar4:   {"code": 0x53,  "offset": 0xD2344},
    lname.ar7:   {"code": 0x54,  "offset": 0xD2368},
    lname.ar8:   {"code": 0x51,  "offset": 0xD1BF4},
    lname.ar9:   {"code": 0x4B,  "offset": 0xD1E1C, "rule": "Push"},
    lname.ar10:  {"code": 0x4A,  "offset": 0xD1DE0},
    lname.ar11:  {"code": 0x49,  "offset": 0xD1E58, "rule": "Tackle"},
    lname.ar14:  {"code": 0x4D,  "offset": 0xD2158},
    lname.ar14b: {"code": 0x4C,  "offset": 0xD214C, "rule": "Roc"},
    lname.ar16:  {"code": 0x52,  "offset": 0xD20BC},
    lname.ar17:  {"code": 0x50,  "offset": 0xD2290},
    lname.ar17b: {"code": 0x4F,  "offset": 0xD2284},
    lname.ar18:  {"code": 0x4E,  "offset": 0xD1FA8},
    lname.ar19:  {"code": 0x6A,  "offset": 0xD44A4, "rule": "Kick"},
    lname.ar21:  {"code": 0x55,  "offset": 0xD238C},
    lname.ar25:  {"code": 0xAA,  "offset": 0xD1E04, "type": "boss"},
    lname.ar26:  {"code": 0x59,  "offset": 0xD3370, "rule": "Tackle AND Roc"},
    lname.ar27:  {"code": 0x58,  "offset": 0xD34E4, "rule": "Tackle AND Push"},
    lname.ar30:  {"code": 0x99,  "offset": 0xD6A24, "rule": "Roc"},
    lname.ar30b: {"code": 0x9A,  "offset": 0xD6A30, "rule": "Roc"},
    # Outer Wall
    lname.ow0:   {"code": 0x97,  "offset": 0xD6BEC, "rule": "Roc"},
    lname.ow1:   {"code": 0x98,  "offset": 0xD6CE8, "rule": "Freeze"},
    lname.ow2:   {"code": 0x9E,  "offset": 0xD6DE4},
    # Triumph Hallway
    lname.th1:   {"code": 0x57,  "offset": 0xD26D4},
    lname.th3:   {"code": 0x56,  "offset": 0xD23C8, "rule": "Kick AND Freeze"},
    # Machine Tower
    lname.mt0:   {"code": 0x61,  "offset": 0xD307C},
    lname.mt2:   {"code": 0x62,  "offset": 0xD32A4},
    lname.mt3:   {"code": 0x5B,  "offset": 0xD3244, "rule": "Kick"},
    lname.mt4:   {"code": 0x5A,  "offset": 0xD31FC},
    lname.mt6:   {"code": 0x5F,  "offset": 0xD2F38, "rule": "Kick"},
    lname.mt8:   {"code": 0x5E,  "offset": 0xD2EC0},
    lname.mt10:  {"code": 0x63,  "offset": 0xD3550},
    lname.mt11:  {"code": 0x5D,  "offset": 0xD2D88},
    lname.mt13:  {"code": 0x5C,  "offset": 0xD3580},
    lname.mt14:  {"code": 0x60,  "offset": 0xD2A64, "rule": "Tackle"},
    lname.mt17:  {"code": 0x64,  "offset": 0xD3520},
    lname.mt19:  {"code": 0xAB,  "offset": 0xD283C, "type": "boss"},
    # Eternal Corridor
    lname.ec5:   {"code": 0x66,  "offset": 0xD3B50},
    lname.ec7:   {"code": 0x65,  "offset": 0xD3A90},
    lname.ec9:   {"code": 0x67,  "offset": 0xD3B98},
    # Chapel Tower
    lname.ct1:   {"code": 0x68,  "offset": 0xD40F0, "rule": "Freeze"},
    lname.ct4:   {"code": 0x69,  "offset": 0xD4630, "rule": "Push"},
    lname.ct5:   {"code": 0x72,  "offset": 0xD481C},
    lname.ct6:   {"code": 0x6B,  "offset": 0xD4294},
    lname.ct6b:  {"code": 0x6C,  "offset": 0xD42A0},
    lname.ct8:   {"code": 0x6D,  "offset": 0xD4330},
    lname.ct10:  {"code": 0x6E,  "offset": 0xD415C, "rule": "Push"},
    lname.ct13:  {"code": 0x6F,  "offset": 0xD4060, "rule": "Freeze"},
    lname.ct15:  {"code": 0x73,  "offset": 0xD47F8},
    lname.ct16:  {"code": 0x70,  "offset": 0xD3DA8},
    lname.ct18:  {"code": 0x74,  "offset": 0xD47C8},
    lname.ct_switch: {"event": iname.ironmaidens},
    lname.ct22:  {"code": 0x71,  "offset": 0xD3CF4, "type": "boss"},
    lname.ct26:  {"code": 0x9C,  "offset": 0xD6ACC, "rule": "Roc"},
    lname.ct26b: {"code": 0x9B,  "offset": 0xD6AC0, "rule": "Roc"},
    # Underground Gallery
    lname.ug0:   {"code": 0x82,  "offset": 0xD5944},
    lname.ug1:   {"code": 0x83,  "offset": 0xD5890, "rule": "Push"},
    lname.ug2:   {"code": 0x81,  "offset": 0xD5A1C, "rule": "Push"},
    lname.ug3:   {"code": 0x85,  "offset": 0xD56A4, "rule": "Kick AND Freeze"},
    lname.ug3b:  {"code": 0x84,  "offset": 0xD5698, "rule": "Kick AND Freeze"},
    lname.ug8:   {"code": 0x86,  "offset": 0xD5E30, "rule": "Tackle"},
    lname.ug10:  {"code": 0x87,  "offset": 0xD5F68},
    lname.ug13:  {"code": 0x88,  "offset": 0xD5AB8},
    lname.ug15:  {"code": 0x89,  "offset": 0xD5BD8},
    lname.ug20:  {"code": 0xAC,  "offset": 0xD5470, "type": "boss"},
    # Underground Warehouse
    lname.uw1:   {"code": 0x75,  "offset": 0xD48DC},
    lname.uw6:   {"code": 0x76,  "offset": 0xD4D20},
    lname.uw8:   {"code": 0x77,  "offset": 0xD4BA0},
    lname.uw9:   {"code": 0x7E,  "offset": 0xD53EC},
    lname.uw10:  {"code": 0x78,  "offset": 0xD4C84, "rule": "Roc"},
    lname.uw11:  {"code": 0x79,  "offset": 0xD4EC4},
    lname.uw14:  {"code": 0x7F,  "offset": 0xD5410},
    lname.uw16:  {"code": 0x7A,  "offset": 0xD5050},
    lname.uw16b: {"code": 0x7B,  "offset": 0xD505C, "rule": "Roc"},
    lname.uw19:  {"code": 0x7C,  "offset": 0xD5344},
    lname.uw23:  {"code": 0xAE,  "offset": 0xD53B0, "type": "boss"},
    lname.uw24:  {"code": 0x80,  "offset": 0xD5434},
    lname.uw25:  {"code": 0x7D,  "offset": 0xD4FC0},
    # Underground Waterway
    lname.uy1:   {"code": 0x93,  "offset": 0xD5F98},
    lname.uy3:   {"code": 0x8B, "offset": 0xD5FEC},
    lname.uy3b:  {"code": 0x8A, "offset": 0xD5FE0},
    lname.uy4:   {"code": 0x94, "offset": 0xD697C},
    lname.uy5:   {"code": 0x8C, "offset": 0xD6214, "rule": "Freeze"},
    lname.uy7:   {"code": 0x8D, "offset": 0xD65A4},
    lname.uy8:   {"code": 0x95, "offset": 0xD69A0, "rule": "Roc"},
    lname.uy9:   {"code": 0x8E, "offset": 0xD640C},
    lname.uy9b:  {"code": 0x8F, "offset": 0xD6418},
    lname.uy12:  {"code": 0x91, "offset": 0xD673C, "rule": "Cleansing"},
    lname.uy12b: {"code": 0x90, "offset": 0xD6730},
    lname.uy13:  {"code": 0x92, "offset": 0xD685C, "rule": "Roc"},
    lname.uy17:  {"code": 0xAF, "offset": 0xD6940, "rule": "Cleansing", "type": "boss"},
    lname.uy18:  {"code": 0x96, "offset": 0xD69C4, "rule": "Roc"},
    # Observation Tower
    lname.ot1:   {"code": 0x9D, "offset": 0xD6B38},
    lname.ot2:   {"code": 0xA4, "offset": 0xD760C},
    lname.ot3:   {"code": 0x9F, "offset": 0xD72E8},
    lname.ot5:   {"code": 0xA5, "offset": 0xD75E8},
    lname.ot8:   {"code": 0xA0, "offset": 0xD71EC},
    lname.ot9:   {"code": 0xA2, "offset": 0xD6FE8},
    lname.ot12:  {"code": 0xA6, "offset": 0xD75C4},
    lname.ot13:  {"code": 0xA3, "offset": 0xD6F64},
    lname.ot16:  {"code": 0xA1, "offset": 0xD751C},
    lname.ot20:  {"code": 0xB0, "offset": 0xD6E20, "type": "boss"},
    # Ceremonial Room
    lname.cr1:   {"code": 0xA7, "offset": 0xD7690},
    lname.victory: {"event": iname.victory}
    # Battle Arena
    # lname.ba24:  {"code": 0xB2, "offset": 0xD7D20},
 }


def get_location_info(location: str, info: str) -> Union[int, str, List[str], None]:
    return location_info[location].get(info, None)


def get_all_location_names() -> List[str]:
    return [loc_name for loc_name in location_info]


def get_location_names_to_ids() -> Dict[str, int]:
    return {name: get_location_info(name, "code")+base_id for name in location_info if get_location_info(name, "code")
            is not None}


def get_locations_by_area() -> Dict[str, Set[str]]:
    areas_to_locations = {}

    for loc_name in location_info:
        # If we are looking at an event Location, don't include it.
        if get_location_info(loc_name, "event") is not None:
            continue

        # The part of the Location name's string before the colon is its area name.
        area_name = loc_name.split(":")[0]

        if area_name not in areas_to_locations:
            areas_to_locations[area_name] = {loc_name}
        else:
            areas_to_locations[area_name].add(loc_name)

    return areas_to_locations


def get_named_locations_data(locations: List[str], options: CVCotMOptions) -> \
        Tuple[Dict[str, Optional[int]], Dict[str, str]]:
    locations_with_ids = {}
    events = {}

    for loc in locations:
        # If Break Iron Maidens is on, don't place the Broke Iron Maidens Location.
        if loc == lname.ct_switch and options.break_iron_maidens:
            continue

        loc_code = get_location_info(loc, "code")

        # If we are looking at an event Location, add its associated event Item to the events' dict.
        # Otherwise, add the base_id to the Location's code.
        if loc_code is None:
            events[loc] = get_location_info(loc, "event")
        else:
            loc_code += base_id
        locations_with_ids.update({loc: loc_code})

        # If Require All Bosses is on, add a Last Key to the events dict for all Locations marked "boss" for their type.
        if options.require_all_bosses and get_location_info(loc, "type") == "boss":
            events[loc] = iname.last_key

    return locations_with_ids, events
