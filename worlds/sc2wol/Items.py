from BaseClasses import Item
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    type: typing.Optional[str]
    number: typing.Optional[int]
    progression: bool = False
    never_exclude: bool = True
    quantity: int = 1


class StarcraftWoLItem(Item):
    game: str = "Starcraft2WoL"

    def __init__(self, name, advancement: bool = False, code: int = None, player: int = None):
        super(StarcraftWoLItem, self).__init__(name, advancement, code, player)


def get_full_item_list():
    return item_table


SC2WOL_ITEM_ID_OFFSET = 1000

item_table = {
    "Marine": ItemData(0+SC2WOL_ITEM_ID_OFFSET, "Unit", 0, progression=True),
    "Medic": ItemData(1+SC2WOL_ITEM_ID_OFFSET, "Unit", 1, progression=True),
    "Firebat": ItemData(2+SC2WOL_ITEM_ID_OFFSET, "Unit", 2, progression=True),
    "Marauder": ItemData(3+SC2WOL_ITEM_ID_OFFSET, "Unit", 3, progression=True),
    "Reaper": ItemData(4+SC2WOL_ITEM_ID_OFFSET, "Unit", 4, progression=True),
    "Hellion": ItemData(5+SC2WOL_ITEM_ID_OFFSET, "Unit", 5, progression=True),
    "Vulture": ItemData(6+SC2WOL_ITEM_ID_OFFSET, "Unit", 6, progression=True),
    "Goliath": ItemData(7+SC2WOL_ITEM_ID_OFFSET, "Unit", 7, progression=True),
    "Diamondback": ItemData(8+SC2WOL_ITEM_ID_OFFSET, "Unit", 8, progression=True),
    "Siege Tank": ItemData(9+SC2WOL_ITEM_ID_OFFSET, "Unit", 9, progression=True),
    "Medivac": ItemData(10+SC2WOL_ITEM_ID_OFFSET, "Unit", 10, progression=True),
    "Wraith": ItemData(11+SC2WOL_ITEM_ID_OFFSET, "Unit", 11, progression=True),
    "Viking": ItemData(12+SC2WOL_ITEM_ID_OFFSET, "Unit", 12, progression=True),
    "Banshee": ItemData(13+SC2WOL_ITEM_ID_OFFSET, "Unit", 13, progression=True),
    "Battlecruiser": ItemData(14+SC2WOL_ITEM_ID_OFFSET, "Unit", 14, progression=True),
    "Ghost": ItemData(15+SC2WOL_ITEM_ID_OFFSET, "Unit", 15, progression=True),
    "Spectre": ItemData(16+SC2WOL_ITEM_ID_OFFSET, "Unit", 16, progression=True),
    "Thor": ItemData(17+SC2WOL_ITEM_ID_OFFSET, "Unit", 17, progression=True),

    "Progressive Infantry Weapon": ItemData (100+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 0, quantity=3),
    "Progressive Infantry Armor": ItemData (102+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 2, quantity=3),
    "Progressive Vehicle Weapon": ItemData (103+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 4, quantity=3),
    "Progressive Vehicle Armor": ItemData (104+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 6, quantity=3),
    "Progressive Ship Weapon": ItemData (105+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 8, quantity=3),
    "Progressive Ship Armor": ItemData (106+SC2WOL_ITEM_ID_OFFSET, "Upgrade", 10, quantity=3),

    "Projectile Accelerator": ItemData (200+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 0),
    "Neosteel Bunker": ItemData (201+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 1),
    "Titanium Housing": ItemData (202+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 2),
    "Hellstorm Batteries": ItemData (203+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 3),
    "Advanced Construction": ItemData (204+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 4),
    "Dual-Fusion Welders": ItemData (205+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 5),
    "Fire-Suppression System": ItemData (206+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 6),
    "Orbital Command": ItemData (207+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 7),
    "Stimpack": ItemData (208+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 8),
    "Combat Shield": ItemData (209+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 9),
    "Advanced Medic Facilities": ItemData (210+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 10),
    "Stabilizer Medpacks": ItemData (211+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 11),
    "Incinerator Gauntlets": ItemData (212+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 12),
    "Juggernaut Plating": ItemData (213+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 13),
    "Concussive Shells": ItemData (214+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 14),
    "Kinetic Foam": ItemData (215+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 15),
    "U-238 Rounds": ItemData (216+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 16),
    "G-4 Clusterbomb": ItemData (217+SC2WOL_ITEM_ID_OFFSET, "Armory 1", 17),

    "Twin-Linked Flamethrower": ItemData(300+SC2WOL_ITEM_ID_OFFSET, "Armory 2", 0),
    "Thermite Filaments": ItemData(301+SC2WOL_ITEM_ID_OFFSET, "Armory 2", 1),
    "Cerberus Mine": ItemData(302 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 2),
    "Replenishable Magazine": ItemData(303 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 3),
    "Multi-Lock Weapons System": ItemData(304 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 4),
    "Ares-Class Targeting System": ItemData(305 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 5),
    "Tri-Lithium Power Cell": ItemData(306 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 6),
    "Shaped Hull": ItemData(307 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 7),
    "Maelstrom Rounds": ItemData(308 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 8),
    "Shaped Blast": ItemData(309 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 9),
    "Rapid Deployment Tube": ItemData(310 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 10),
    "Advanced Healing AI": ItemData(311 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 11),
    "Tomahawk Power Cells": ItemData(312 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 12),
    "Displacement Field": ItemData(313 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 13),
    "Ripwave Missiles": ItemData(314 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 14),
    "Phobos-Class Weapons System": ItemData(315 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 15),
    "Cross-Spectrum Dampeners": ItemData(316 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 16),
    "Shockwave Missile Battery": ItemData(317 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 17),
    "Missile Pods": ItemData(318 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 18),
    "Defensive Matrix": ItemData(319 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 19),
    "Ocular Implants": ItemData(320 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 20),
    "Crius Suit": ItemData(321 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 21),
    "Psionic Lash": ItemData(322 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 22),
    "Nyx-Class Cloaking Module": ItemData(323 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 23),
    "330mm Barrage Cannon": ItemData(324 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 24),
    "Immortality Protocol": ItemData(325 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 25),

    "Bunker": ItemData (400+SC2WOL_ITEM_ID_OFFSET, "Building", 0, progression=True),
    "Missile Turret": ItemData (401+SC2WOL_ITEM_ID_OFFSET, "Building", 1, progression=True),
    "Sensor Tower": ItemData (402+SC2WOL_ITEM_ID_OFFSET, "Building", 2),

    "War Pigs": ItemData (500 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 0),
    "Devil Dogs": ItemData(501 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 1),
    "Hammer Securities": ItemData(502 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 2),
    "Spartan Company": ItemData(503 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 3),
    "Siege Breakers": ItemData(504 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 4),
    "Hell's Angel": ItemData(505 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 5),
    "Dusk Wings": ItemData(506 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 6),
    "Jackson's Revenge": ItemData(507 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 7),

    "Ultra-Capacitors": ItemData(600 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 0),
    "Vanadium Plating": ItemData(601 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 1),
    "Orbital Depots": ItemData(602 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 2),
    "Micro-Filtering": ItemData(603 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 3),
    "Automated Refinery": ItemData(604 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 4),
    "Command Center Reactor": ItemData(605 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 5),
    "Raven": ItemData(606 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 6),
    "Science Vessel": ItemData(607 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 7),
    "Tech Reactor": ItemData(608 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 8),
    "Orbital Strike": ItemData(609 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 9),
    "Shrike Turret": ItemData(610 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 10),
    "Fortified Bunker": ItemData(611 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 11),
    "Planetary Fortress": ItemData(612 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 12),
    "Perdition Turret": ItemData(613 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 13),
    "Predator": ItemData(614 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 14),
    "Hercules": ItemData(615 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 15),
    "Cellular Reactor": ItemData(616 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 16),
    "Regenerative Bio-Steel": ItemData(617 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 17),
    "Hive Mind Emulator": ItemData(618 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 18),
    "Psi Disrupter": ItemData(619 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 19),

    "Zealot": ItemData (700 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 0, progression=True),
    "Stalker": ItemData (701 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 1, progression=True),
    "High Templar": ItemData (702 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 2, progression=True),
    "Dark Templar": ItemData (703 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 3, progression=True),
    "Immortal": ItemData (704 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 4, progression=True),
    "Colossus": ItemData (705 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 5, progression=True),
    "Phoenix": ItemData (706 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 6, progression=True),
    "Void Ray": ItemData (707 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 7, progression=True),
    "Carrier": ItemData (708 + SC2WOL_ITEM_ID_OFFSET, "Protoss", 8, progression=True),

    "+5 Starting Minerals": ItemData(500+SC2WOL_ITEM_ID_OFFSET, "Minerals", 5, quantity=0),
    "+5 Starting Vespene": ItemData(501+SC2WOL_ITEM_ID_OFFSET, "Vespene", 5, quantity=0)
}

basic_unit: typing.Tuple[str, ...] = (
    'Marine',
    'Marauder',
    'Firebat',
    'Hellion',
    'Vulture'
)


item_name_groups = {"Missions":
                        {"Beat Liberation Day", "Beat The Outlaws", "Beat Zero Hour", "Beat Evacuation",
                         "None Outbreak", "Beat Safe Haven", "Beat Haven's Fall", "Beat Smash and Grab", "Beat The Dig",
                         "Beat The Moebius Factor", "Beat Supernova", "Beat Maw of the Void", "Beat Devil's Playground",
                         "Beat Welcome to the Jungle", "Beat Breakout", "Beat Ghost of a Chance",
                         "Beat The Great Train Robbery", "Beat Cutthroat", "Beat Engine of Destruction",
                         "Beat Media Blitz", "Beat Piercing the Shroud"}}

filler_items: typing.Tuple[str, ...] = (
    '+5 Starting Minerals',
    '+5 Starting Vespene'
)

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in get_full_item_list().items() if data.code}