import itertools
from random import Random
from typing import List, Tuple, Dict, Optional, Callable

from BaseClasses import Location, LocationProgressType, Region
from .options import max_shapesanity, max_levels_and_upgrades

location_description = {  # TODO give at least some locations a description
    "Level 1": "TODO",
    "Level 1 Additional": "TODO",
    "Level 20 Additional": "TODO",
    "Level 20 Additional 2": "TODO",
    "Level 26": "TODO",
    "Level 1000": "TODO",
    "Belt Upgrade Tier II": "TODO",
    "Miner Upgrade Tier II": "TODO",
    "Processors Upgrade Tier II": "TODO",
    "Painting Upgrade Tier II": "TODO",
    "Belt Upgrade Tier VIII": "TODO",
    "Miner Upgrade Tier VIII": "TODO",
    "Processors Upgrade Tier VIII": "TODO",
    "Painting Upgrade Tier VIII": "TODO",
    "Belt Upgrade Tier M": "TODO",
    "Miner Upgrade Tier M": "TODO",
    "Processors Upgrade Tier M": "TODO",
    "Painting Upgrade Tier M": "TODO"
}

categories = ["Belt", "Miner", "Processors", "Painting"]
subshape_names = ["Circle", "Square", "Star", "Windmill"]
color_names = ["Red", "Blue", "Green", "Yellow", "Purple", "Cyan", "White", "Uncolored"]
short_subshapes = ["C", "R", "S", "W"]
short_colors = ["b", "c", "g", "p", "r", "u", "w", "y"]

translate: List[Tuple[int, str]] = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]


def roman(num: int) -> str:
    """Converts positive integers into roman numbers."""
    rom: str = ""
    for key, val in translate:
        while num >= key:
            rom += val
            num -= key
    return rom


def color_to_needed_building(color_list: List[str]) -> str:
    for next_color in color_list:
        if next_color in ["Yellow", "Purple", "Cyan", "White", "y", "p", "c", "w"]:
            return "Mixed"
    for next_color in color_list:
        if next_color not in ["Uncolored", "u"]:
            return "Painted"
    return "Uncolored"


shapesanity_simple: Dict[str, str] = {}
shapesanity_1_4: Dict[str, str] = {}
shapesanity_two_sided: Dict[str, str] = {}
shapesanity_three_parts: Dict[str, str] = {}
shapesanity_four_parts: Dict[str, str] = {}


def init_shapesanity_pool() -> None:
    # same shapes && same color
    for color in color_names:
        color_region = color_to_needed_building([color])
        shapesanity_simple[f"{color} Circle"] = f"Shapesanity Full {color_region}"
        shapesanity_simple[f"{color} Square"] = f"Shapesanity Full {color_region}"
        shapesanity_simple[f"{color} Star"] = f"Shapesanity Full {color_region}"
        shapesanity_simple[f"{color} Windmill"] = f"Shapesanity East Windmill {color_region}"
    for shape in subshape_names:
        for color in color_names:
            color_region = color_to_needed_building([color])
            shapesanity_simple[f"Half {color} {shape}"] = f"Shapesanity Half {color_region}"
            shapesanity_simple[f"{color} {shape} Piece"] = f"Shapesanity Piece {color_region}"
            shapesanity_simple[f"Cut Out {color} {shape}"] = f"Shapesanity Stitched {color_region}"
            shapesanity_simple[f"Cornered {color} {shape}"] = f"Shapesanity Stitched {color_region}"

    # one color && 4 shapes (including empty)
    for first_color, second_color, third_color, fourth_color in itertools.combinations(short_colors+["-"], 4):
        colors = [first_color, second_color, third_color, fourth_color]
        color_region = color_to_needed_building(colors)
        shape_regions = ["Stitched", "Stitched"] if fourth_color == "-" else ["Colorful Full", "Colorful East Windmill"]
        color_code = ''.join(colors)
        shapesanity_1_4[f"{color_code} Circle"] = f"Shapesanity {shape_regions[0]} {color_region}"
        shapesanity_1_4[f"{color_code} Square"] = f"Shapesanity {shape_regions[0]} {color_region}"
        shapesanity_1_4[f"{color_code} Star"] = f"Shapesanity {shape_regions[0]} {color_region}"
        shapesanity_1_4[f"{color_code} Windmill"] = f"Shapesanity {shape_regions[1]} {color_region}"

    # one shape && 4 colors (including empty)
    for first_shape, second_shape, third_shape, fourth_shape in itertools.combinations(short_subshapes+["-"], 4):
        for color in color_names:
            shapesanity_1_4[f"{color} {''.join([first_shape, second_shape, third_shape, fourth_shape])}"] \
                = f"Shapesanity Stitched {color_to_needed_building([color])}"

    combos = [shape + color for shape in short_subshapes for color in short_colors]
    for first_combo, second_combo in itertools.permutations(combos, 2):
        # 2-sided shapes
        color_region = color_to_needed_building([first_combo[1], second_combo[1]])
        ordered_combo = " ".join(sorted([first_combo, second_combo]))
        shape_regions = ((["East Windmill", "East Windmill", "Colorful Half"]
                          if first_combo[0] == "W" else ["Colorful Full", "Colorful Full", "Colorful Half"])
                         if first_combo[0] == second_combo[0] else ["Stitched", "Half-Half", "Stitched"])
        shapesanity_two_sided[f"3-1 {first_combo} {second_combo}"] = f"Shapesanity {shape_regions[0]} {color_region}"
        shapesanity_two_sided[f"Half-Half {ordered_combo}"] = f"Shapesanity {shape_regions[1]} {color_region}"
        shapesanity_two_sided[f"Checkered {ordered_combo}"] = f"Shapesanity {shape_regions[0]} {color_region}"
        shapesanity_two_sided[f"Adjacent Singles {ordered_combo}"] = f"Shapesanity {shape_regions[2]} {color_region}"
        shapesanity_two_sided[f"Cornered Singles {ordered_combo}"] = f"Shapesanity Stitched {color_region}"
        shapesanity_two_sided[f"Adjacent 2-1 {first_combo} {second_combo}"] = f"Shapesanity Stitched {color_region}"
        shapesanity_two_sided[f"Cornered 2-1 {first_combo} {second_combo}"] = f"Shapesanity Stitched {color_region}"
        for third_combo in combos:
            if third_combo in [first_combo, second_combo]:
                continue
            # 3-part shapes
            colors = [first_combo[1], second_combo[1], third_combo[1]]
            color_region = color_to_needed_building(colors)
            ordered_two = " ".join(sorted([second_combo, third_combo]))
            if not (first_combo[1] == second_combo[1] == third_combo[1] or
                    first_combo[0] == second_combo[0] == third_combo[0]):
                ordered_all = " ".join(sorted([first_combo, second_combo, third_combo]))
                shapesanity_three_parts[f"Singles {ordered_all}"] = f"Shapesanity Stitched {color_region}"
            shape_regions = (["Stitched", "Stitched"] if not second_combo[0] == third_combo[0]
                             else ((["East Windmill", "East Windmill"] if first_combo[0] == "W"
                                    else ["Colorful Full", "Colorful Full"])
                                   if first_combo[0] == second_combo[0] else ["Colorful Half-Half", "Stitched"]))
            shapesanity_three_parts[f"Adjacent 2-1-1 {first_combo} {ordered_two}"] \
                = f"Shapesanity {shape_regions[0]} {color_region}"
            shapesanity_three_parts[f"Cornered 2-1-1 {first_combo} {ordered_two}"] \
                = f"Shapesanity {shape_regions[1]} {color_region}"
            for fourth_combo in combos:
                if fourth_combo in [first_combo, second_combo, third_combo]:
                    continue
                if (first_combo[1] == second_combo[1] == third_combo[1] == fourth_combo[1] or
                    first_combo[0] == second_combo[0] == third_combo[0] == fourth_combo[0]):
                    continue
                colors = [first_combo[1], second_combo[1], third_combo[1], fourth_combo[1]]
                color_region = color_to_needed_building(colors)
                ordered_all = " ".join(sorted([first_combo, second_combo, third_combo, fourth_combo]))
                if ((first_combo[0] == second_combo[0] and third_combo[0] == fourth_combo[0]) or
                    (first_combo[0] == third_combo[0] and second_combo[0] == fourth_combo[0]) or
                    (first_combo[0] == fourth_combo[0] and third_combo[0] == second_combo[0])):
                    shapesanity_four_parts[f"Singles {ordered_all}"] = f"Shapesanity Colorful Half-Half {color_region}"
                else:
                    shapesanity_four_parts[f"Singles {ordered_all}"] = f"Shapesanity Stitched {color_region}"


achievement_locations: List[str] = ["My eyes no longer hurt", "Painter", "Cutter", "Rotater", "Wait, they stack?",
                                    "Wires", "Storage", "Freedom", "The logo!", "To the moon", "It's piling up",
                                    "I'll use it later", "Efficiency 1", "Preparing to launch", "SpaceY",
                                    "Stack overflow", "It's a mess", "Faster", "Even faster", "Get rid of them",
                                    "It's been a long time", "Addicted", "Can't stop", "Is this the end?",
                                    "Getting into it", "Now it's easy", "Computer Guy", "Speedrun Master",
                                    "Speedrun Novice", "Not an idle game", "Efficiency 2", "Branding specialist 1",
                                    "Branding specialist 2", "King of Inefficiency", "It's so slow",
                                    "MAM (Make Anything Machine)", "Perfectionist", "The next dimension", "Oops",
                                    "Copy-Pasta", "I've seen that before ...", "Memories from the past",
                                    "I need trains", "A bit early?", "GPS"]

all_locations: List[str] = (["Level 1 Additional", "Level 20 Additional", "Level 20 Additional 2"]
                            + [f"Level {x}" for x in range(1, max_levels_and_upgrades)]
                            + [f"{cat} Upgrade Tier {roman(x)}"
                               for cat in categories for x in range(2, max_levels_and_upgrades+1)]
                            + achievement_locations
                            + [f"Shapesanity {x}" for x in range(1, max_shapesanity+1)])


def addlevels(maxlevel: int, logictype: str,
              random_logic_phase_length: List[int]) -> Dict[str, Tuple[str, LocationProgressType]]:
    """Returns a dictionary with all level locations based on player options (maxlevel INCLUDED).
    If shape requirements are not randomized, give logic type 0."""

    # Level 1 is always directly accessible
    locations: Dict[str, Tuple[str, LocationProgressType]] = {"Level 1": ("Main", LocationProgressType.PRIORITY),
                                                              "Level 1 Additional": (
                                                              "Main", LocationProgressType.PRIORITY)}

    if logictype.startswith("vanilla"):
        locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 20 Additional 2"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 2"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 3"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 4"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 5"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Level 6"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Level 7"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Level 8"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Level 9"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        locations["Level 10"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(11, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    elif logictype.startswith("stretched"):
        phaselength = maxlevel//6
        l20phase = 20//phaselength
        if l20phase == 0:
            locations["Level 20 Additional"] = ("Main", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Main", LocationProgressType.DEFAULT)
        elif l20phase == 1:
            locations["Level 20 Additional"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        else:
            locations["Level 20 Additional"] = (f"Levels with {min(l20phase, 5)} Buildings",
                                                LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = (f"Levels with {min(l20phase, 5)} Buildings",
                                                  LocationProgressType.DEFAULT)
        for x in range(2, phaselength):
            locations[f"Level {x}"] = ("Main", LocationProgressType.DEFAULT)
        for x in range(phaselength, phaselength*2):
            locations[f"Level {x}"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        for x in range(phaselength*2, phaselength*3):
            locations[f"Level {x}"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*3, phaselength*4):
            locations[f"Level {x}"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*4, phaselength*5):
            locations[f"Level {x}"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*5, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    elif logictype.startswith("quick"):
        locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 20 Additional 2"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 2"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 3"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Level 4"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Level 5"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(6, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    elif logictype.startswith("random_steps"):
        nextlevel = 2
        l20set = False
        for _ in range(0, random_logic_phase_length[0]):
            locations[f"Level {nextlevel}"] = ("Main", LocationProgressType.DEFAULT)
            nextlevel += 1
        if nextlevel > 20 and not l20set:
            locations["Level 20 Additional"] = ("Main", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Main", LocationProgressType.DEFAULT)
            l20set = True
        for _ in range(0, random_logic_phase_length[1]):
            locations[f"Level {nextlevel}"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            nextlevel += 1
        if nextlevel > 20 and not l20set:
            locations["Level 20 Additional"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            l20set = True
        for _ in range(0, random_logic_phase_length[2]):
            locations[f"Level {nextlevel}"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
            nextlevel += 1
        if nextlevel > 20 and not l20set:
            locations["Level 20 Additional"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
            l20set = True
        for _ in range(0, random_logic_phase_length[3]):
            locations[f"Level {nextlevel}"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
            nextlevel += 1
        if nextlevel > 20 and not l20set:
            locations["Level 20 Additional"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
            l20set = True
        for _ in range(0, random_logic_phase_length[4]):
            locations[f"Level {nextlevel}"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
            nextlevel += 1
        if nextlevel > 20 and not l20set:
            locations["Level 20 Additional"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
            l20set = True
        for x in range(nextlevel, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        if not l20set:
            locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
            locations["Level 20 Additional 2"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    else:  # logictype == hardcore
        locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 20 Additional 2"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        for x in range(2, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    return locations


def addupgrades(finaltier: int, logictype: str,
                category_random_logic_amounts: Dict[str, int]) -> Dict[str, Tuple[str, LocationProgressType]]:
    """Returns a dictionary with all upgrade locations based on player options (finaltier INCLUDED).
    If shape requirements are not randomized, give logic type 0."""

    locations: Dict[str, Tuple[str, LocationProgressType]] = {}

    if logictype == "vanilla_like":
        locations["Belt Upgrade Tier II"] = ("Main", LocationProgressType.DEFAULT)
        locations["Miner Upgrade Tier II"] = ("Main", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier II"] = ("Main", LocationProgressType.DEFAULT)
        locations["Painting Upgrade Tier II"] = ("Upgrades with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Belt Upgrade Tier III"] = ("Upgrades with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Miner Upgrade Tier III"] = ("Upgrades with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier III"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        locations["Painting Upgrade Tier III"] = ("Upgrades with 3 Buildings", LocationProgressType.DEFAULT)
        for x in range(4, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                               LocationProgressType.DEFAULT)
    elif logictype == "linear":
        for cat in categories:
            locations[f"{cat} Upgrade Tier II"] = ("Main", LocationProgressType.DEFAULT)
        for cat in categories:
            locations[f"{cat} Upgrade Tier III"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        for x in range(4, 7):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = (f"Upgrades with {x-2} Buildings",
                                                               LocationProgressType.DEFAULT)
        for x in range(7, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                               LocationProgressType.DEFAULT)

    elif logictype == "category":
        for x in range(2, 5):
            locations[f"Belt Upgrade Tier {roman(x)}"] = ("Main", LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Belt Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
        for x in range(2, 5):
            locations[f"Miner Upgrade Tier {roman(x)}"] = ("Main", LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Miner Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier II"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier III"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier IV"] = ("Upgrades with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier V"] = ("Upgrades with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Processors Upgrade Tier VI"] = ("Upgrades with 3 Buildings", LocationProgressType.DEFAULT)
        for x in range(7, finaltier+1):
            locations[f"Processors Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                                LocationProgressType.DEFAULT)
        locations["Painting Upgrade Tier II"] = ("Upgrades with 4 Buildings", LocationProgressType.DEFAULT)
        locations["Painting Upgrade Tier III"] = ("Upgrades with 4 Buildings", LocationProgressType.DEFAULT)
        locations["Painting Upgrade Tier IV"] = ("Upgrades with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Painting Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)

    elif logictype == "category_random":
        regions = ["Main", "Upgrades with 1 Building", "Upgrades with 2 Buildings", "Upgrades with 3 Buildings",
                   "Upgrades with 4 Buildings", "Upgrades with 5 Buildings"]
        for x in range(2, 5):
            locations[f"Belt Upgrade Tier {roman(x)}"] = (regions[category_random_logic_amounts["belt"]],
                                                          LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Belt Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                          LocationProgressType.DEFAULT)
        for x in range(2, 5):
            locations[f"Miner Upgrade Tier {roman(x)}"] = (regions[category_random_logic_amounts["miner"]],
                                                           LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Miner Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                           LocationProgressType.DEFAULT)
        for x in range(2, 5):
            locations[f"Processors Upgrade Tier {roman(x)}"] = (regions[category_random_logic_amounts["processors"]],
                                                                LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Processors Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                                LocationProgressType.DEFAULT)
        for x in range(2, 5):
            locations[f"Painting Upgrade Tier {roman(x)}"] = (regions[category_random_logic_amounts["painting"]],
                                                              LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            locations[f"Painting Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                              LocationProgressType.DEFAULT)

    else:  # logictype == hardcore
        for cat in categories:
            locations[f"{cat} Upgrade Tier II"] = ("Main", LocationProgressType.DEFAULT)
        for x in range(3, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings",
                                                               LocationProgressType.DEFAULT)

    return locations


def addachievements(excludesoftlock: bool, excludelong: bool, excludeprogressive: bool,
                    maxlevel: int, upgradelogictype: str, category_random_logic_amounts: Dict[str, int],
                    goal: str, presentlocations: Dict[str, Tuple[str, LocationProgressType]],
                    add_alias: Callable[[str,str],None]) -> Dict[str, Tuple[str, LocationProgressType]]:
    """Returns a dictionary with all achievement locations based on player options."""

    locations: Dict[str, Tuple[str, LocationProgressType]] = dict()

    def f(name: str, region: str, alias: str, progress: LocationProgressType = LocationProgressType.DEFAULT):
        locations[name] = (region, progress)
        add_alias(name, alias)

    f("My eyes no longer hurt", "Menu", "Activate dark mode")
    f("Painter", "Painted Shape Achievements", "Paint a shape")
    f("Cutter", "Cut Shape Achievements", "Cut a shape")
    f("Rotater", "Rotated Shape Achievements", "Rotate a shape")
    f("Wait, they stack?", "Stacked Shape Achievements", "Stack a shape")
    f("Storage", "Stored Shape Achievements", "Store a shape in the storage")
    f("The logo!", "All Buildings Shapes", "Produce the shapez.io logo")
    f("To the moon", "All Buildings Shapes", "Produce the rocket shape")
    f("It's piling up", "All Buildings Shapes", "100k blueprint shapes")
    f("I'll use it later", "All Buildings Shapes", "1 million blueprint shapes")
    f("Efficiency 1", "All Buildings Shapes", "25 blueprints shapes / second")
    f("Preparing to launch", "All Buildings Shapes", "10 rocket shapes / second")
    f("SpaceY", "All Buildings Shapes", "20 rocket shapes / second")

    f("Stack overflow", "Stacked Shape Achievements", "4 layers shape")
    f("It's a mess", "Main", "100 different shapes")
    f("Even faster", "Upgrades with 5 Buildings", "All upgrades on tier 8")
    f("Get rid of them", "Trashed Shape Achievements", "1000 shapes trashed")
    f("Getting into it", "Menu", "1 hour")
    f("Now it's easy", "Blueprint Achievements", "Place a blueprint")
    f("Computer Guy", "Wiring Achievements", "Place 5,000 wires")
    f("Efficiency 2", "All Buildings Shapes", "50 blueprints shapes / second")
    f("Branding specialist 1", "All Buildings Shapes", "25 logo shapes / second")
    f("Branding specialist 2", "All Buildings Shapes", "50 logo shapes / second")
    f("Perfectionist", "Main", "Destroy more than 1000 objects at once")
    f("The next dimension", "Wiring Achievements", "Open the wires layer")
    f("Oops", "Main", "Deliver an irrelevant shape")
    f("Copy-Pasta", "Blueprint Achievements", "Place a 1000 buildings blueprint")
    f("I've seen that before ...", "All Buildings Shapes", "Produce RgRyRbRr")
    f("Memories from the past", "All Buildings Shapes", "Produce WrRgWrRg:CwCrCwCr:SgSgSgSg")
    f("I need trains", "Main", "Have a 500 tiles belt")
    f("GPS", "Menu", "15 map markers")
    # Achievements that depend on upgrades
    if upgradelogictype == "linear":
        f("Faster", "Upgrades with 3 Buildings", "All upgrades on tier 5")
    else:
        f("Faster", "Upgrades with 5 Buildings", "All upgrades on tier 5")
    # Achievements that depend on the level
    f("Wires", presentlocations["Level 20"][0], "Complete level 20")
    if not goal == "vanilla":
        f("Freedom", presentlocations["Level 26"][0], "Complete level 26")
        f("MAM (Make Anything Machine)", "MAM needed", "Complete any level > 26 without modifications")
    if maxlevel >= 50:
        f("Can't stop", presentlocations["Level 50"][0], "Reach level 50")
    elif not goal == "vanilla":
        f("Can't stop", "Levels with 5 Buildings", "Reach level 50")
    if maxlevel >= 100:
        f("Is this the end?", presentlocations["Level 100"][0], "Reach level 100")
    elif not goal == "vanilla":
        f("Is this the end?", "Levels with 5 Buildings", "Reach level 100")

    if excludeprogressive:
        unreasonable_type = LocationProgressType.EXCLUDED
    else:
        unreasonable_type = LocationProgressType.DEFAULT

    if not excludesoftlock:
        f("Speedrun Master", presentlocations["Level 12"][0], "Complete level 12 in under 30 min", unreasonable_type)
        f("Speedrun Novice", presentlocations["Level 12"][0], "Complete level 12 in under 60 min", unreasonable_type)
        f("Not an idle game", presentlocations["Level 12"][0], "Complete level 12 in under 120 min", unreasonable_type)
        f("It's so slow", presentlocations["Level 12"][0],
          "Complete level 12 without upgrading belts", unreasonable_type)
        f("King of Inefficiency", presentlocations["Level 14"][0], "No ccw rotator until level 14", unreasonable_type)
        f("A bit early?", "All Buildings Shapes", "Produce logo shape before level 18", unreasonable_type)

    if not excludelong:
        f("It's been a long time", "Menu", "10 hours")
        f("Addicted", "Menu", "20 hours")

    return locations


def addshapesanity(amount: int, random: Random, append_shapesanity: Callable[[str],None],
                   add_alias: Callable[[str,str],None]) -> Dict[str, Tuple[str, LocationProgressType]]:
    """Returns a dictionary with a given number of random shapesanity locations."""

    included_shapes: Dict[str, Tuple[str, LocationProgressType]] = {}
    shapes_list = list(shapesanity_simple.items())
    # Always have at least 4 shapesanity checks because of sphere 1 usefulls + both hardcore logic
    included_shapes[f"Shapesanity 1"] = ("Shapesanity Full Uncolored", LocationProgressType.DEFAULT)
    included_shapes[f"Shapesanity 2"] = ("Shapesanity Full Uncolored", LocationProgressType.DEFAULT)
    included_shapes[f"Shapesanity 3"] = ("Shapesanity Full Uncolored", LocationProgressType.DEFAULT)
    included_shapes[f"Shapesanity 4"] = ("Shapesanity East Windmill Uncolored", LocationProgressType.DEFAULT)
    append_shapesanity(f"Uncolored Circle")
    append_shapesanity(f"Uncolored Star")
    append_shapesanity(f"Uncolored Square")
    append_shapesanity(f"Uncolored Windmill")
    shapes_list.remove((f"Uncolored Circle", "Shapesanity Full Uncolored"))
    shapes_list.remove((f"Uncolored Star", "Shapesanity Full Uncolored"))
    shapes_list.remove((f"Uncolored Square", "Shapesanity Full Uncolored"))
    shapes_list.remove((f"Uncolored Windmill", "Shapesanity East Windmill Uncolored"))
    add_alias("Shapesanity 1", "Uncolored Circle")
    add_alias("Shapesanity 2", "Uncolored Star")
    add_alias("Shapesanity 3", "Uncolored Square")
    add_alias("Shapesanity 4", "Uncolored Windmill")
    switched = 0
    for counting in range(4, amount):
        if switched == 0 and (len(shapes_list) == 0 or counting == amount//2):
            shapes_list = list(shapesanity_1_4.items())
            switched = 1
        if switched == 1 and (len(shapes_list) == 0 or counting == amount*7//12):
            shapes_list = list(shapesanity_two_sided.items())
            switched = 2
        if switched == 2 and (len(shapes_list) == 0 or counting == amount*5//6):
            shapes_list = list(shapesanity_three_parts.items())
            switched = 3
        if switched == 3 and (len(shapes_list) == 0 or counting == amount*11//12):
            shapes_list = list(shapesanity_four_parts.items())
            switched = 4
        x = random.randint(0, len(shapes_list)-1)
        next_shape = shapes_list.pop(x)
        included_shapes[f"Shapesanity {counting+1}"] = (next_shape[1], LocationProgressType.DEFAULT)
        append_shapesanity(next_shape[0])
        add_alias(f"Shapesanity {counting+1}", next_shape[0])

    return included_shapes


def addshapesanity_ut(shapesanity_names: List[str], add_alias: Callable[[str,str],None]
                      ) -> Dict[str, Tuple[str, LocationProgressType]]:
    """Returns the same information as addshapesanity but will add specific values based on a UT rebuild."""

    included_shapes: Dict[str, Tuple[str, LocationProgressType]] = {}

    for name in shapesanity_names:
        for options in [shapesanity_simple, shapesanity_1_4, shapesanity_two_sided,
                        shapesanity_three_parts, shapesanity_four_parts]:
            if name in options:
                next_shape = options[name]
                break
        else:
            raise ValueError(f"Could not find shapesanity name {name}")
        included_shapes[f"Shapesanity {len(included_shapes)+1}"] = (next_shape, LocationProgressType.DEFAULT)
        add_alias(f"Shapesanity {len(included_shapes)}", name)
    return included_shapes


class ShapezLocation(Location):
    game = "shapez"

    def __init__(self, player: int, name: str, address: Optional[int], region: Region,
                 progress_type: LocationProgressType):
        super(ShapezLocation, self).__init__(player, name, address, region)
        self.progress_type = progress_type
