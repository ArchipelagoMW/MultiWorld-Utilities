import os
import typing

import settings
from BaseClasses import ItemClassification, Tutorial

from worlds.AutoWorld import WebWorld, World

from ..LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess
from .Arrays import item_dict
from .Items import GLItem, item_frequencies, item_list, item_table
from .Locations import LocationData, all_locations, location_table
from .Options import GLOptions
from .Regions import connect_regions, create_regions
from .Rom import GLProcedurePatch, write_files
from .Rules import set_rules


def launch_client(*args):
    from GauntletLegendsClient import launch

    launch_subprocess(launch, name="GLClient")


components.append(
    Component(
        "Gauntlet Legends Client",
        "GLClient",
        func=launch_client,
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apgl"),
    ),
)


class GauntletLegendsWebWorld(WebWorld):
    settings_page = "games/gl/info/en"
    theme = "partyTime"
    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to playing Gauntlet Legends",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["jamesbrq"],
        ),
    ]


class GLSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the GL US rom"""

        copy_to = "Gauntlet Legends (U) [!].z64"
        description = "Gauntlet Legends ROM File"

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = False


class GauntletLegendsWorld(World):
    """
    Gauntlet Legends
    """

    game = "Gauntlet Legends"
    web = GauntletLegendsWebWorld()
    options_dataclass = GLOptions
    options: GLOptions
    settings: typing.ClassVar[GLSettings]
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}
    required_client_version = (0, 4, 6)
    crc32: str = None

    disabled_locations: typing.List[LocationData]

    def create_regions(self) -> None:
        self.disabled_locations = []
        if self.options.chests_barrels == 0:
            self.disabled_locations += [
                location.name
                for location in all_locations
                if "Chest" in location.name or ("Barrel" in location.name and "Barrel of Gold" not in location.name)
            ]
        elif self.options.chests_barrels == 1:
            self.disabled_locations += [
                location.name
                for location in all_locations
                if "Barrel" in location.name and "Barrel of Gold" not in location.name
            ]
        elif self.options.chests_barrels == 2:
            self.disabled_locations += [location.name for location in all_locations if "Chest" in location.name]

        create_regions(self)
        connect_regions(self)
        item = self.create_item("Key")
        self.get_location("Valley of Fire - Key 1").place_locked_item(item)
        self.get_location("Valley of Fire - Key 5").place_locked_item(item)
        if self.options.obelisks == 0:
            item = self.create_item("Valley of Fire Obelisk")
            self.get_location("Valley of Fire - Obelisk").place_locked_item(item)
            item = self.create_item("Dagger Peak Obelisk")
            self.get_location("Dagger Peak - Obelisk").place_locked_item(item)
            item = self.create_item("Cliffs of Desolation Obelisk")
            self.get_location("Cliffs of Desolation - Obelisk").place_locked_item(item)
            item = self.create_item("Castle Courtyard Obelisk")
            self.get_location("Castle Courtyard - Obelisk").place_locked_item(item)
            item = self.create_item("Dungeon of Torment Obelisk")
            self.get_location("Dungeon of Torment - Obelisk").place_locked_item(item)
            item = self.create_item("Poisoned Fields Obelisk")
            self.get_location("Poisoned Fields - Obelisk").place_locked_item(item)
            item = self.create_item("Haunted Cemetery Obelisk")
            self.get_location("Haunted Cemetery - Obelisk").place_locked_item(item)
        if self.options.mirror_shards == 0:
            item = self.create_item("Dragon Mirror Shard")
            self.get_location("Dragon's Lair - Dragon Mirror Shard").place_locked_item(item)
            item = self.create_item("Chimera Mirror Shard")
            self.get_location("Chimera's Keep - Chimera Mirror Shard").place_locked_item(item)
            item = self.create_item("Plague Fiend Mirror Shard")
            self.get_location(
                "Vat of the Plague Fiend - Plague Fiend Mirror Shard",
            ).place_locked_item(item)
            item = self.create_item("Yeti Mirror Shard")
            self.get_location("Yeti's Cavern - Yeti Mirror Shard").place_locked_item(item)

    def fill_slot_data(self) -> dict:
        dshard = self.get_location("Dragon's Lair - Dragon Mirror Shard").item
        yshard = self.get_location("Yeti's Cavern - Yeti Mirror Shard").item
        cshard = self.get_location("Chimera's Keep - Chimera Mirror Shard").item
        fshard = self.get_location("Vat of the Plague Fiend - Plague Fiend Mirror Shard").item
        shard_values = [
            item_dict[dshard.code] if dshard.player == self.player else [0x27, 0x4],
            item_dict[yshard.code] if yshard.player == self.player else [0x27, 0x4],
            item_dict[cshard.code] if cshard.player == self.player else [0x27, 0x4],
            item_dict[fshard.code] if fshard.player == self.player else [0x27, 0x4],
        ]
        return {
            "player": self.player,
            "scale": 0,
            "shards": shard_values,
            "speed": self.options.permanent_speed.value,
            "keys": self.options.infinite_keys.value,
            "character": self.options.unlock_character.value,
        }

    def create_items(self) -> None:
        # First add in all progression and useful items
        required_items = []
        precollected = [item for item in item_list if item in self.multiworld.precollected_items[self.player]]
        for item in item_list:
            if item.progression != ItemClassification.filler and item not in precollected:
                if "Obelisk" in item.item_name and self.options.obelisks == 0:
                    continue
                if "Mirror" in item.item_name and self.options.mirror_shards == 0:
                    continue
                if "Key" in item.item_name and self.options.infinite_keys:
                    continue
                freq = item_frequencies.get(item.item_name, 1) + (
                    30 if self.options.infinite_keys and item.progression is ItemClassification.filler else 0
                )
                if freq is None:
                    freq = 1
                required_items += [item.item_name for _ in range(freq)]

        for item_name in required_items:
            self.multiworld.itempool.append(self.create_item(item_name))

        # Then, get a random amount of fillers until we have as many items as we have locations
        filler_items = []
        for item in item_list:
            if item.progression == ItemClassification.filler:
                freq = item_frequencies.get(item.item_name)
                if freq is None:
                    freq = 1
                filler_items += [item.item_name for _ in range(freq)]

        remaining = len(all_locations) - len(required_items) - len(self.disabled_locations) - 2
        if self.options.obelisks == 0:
            remaining -= 7
        if self.options.mirror_shards == 0:
            remaining -= 4
        for i in range(remaining):
            filler_item_name = self.multiworld.random.choice(filler_items)
            item = self.create_item(filler_item_name)
            self.multiworld.itempool.append(item)
            filler_items.remove(filler_item_name)

    def set_rules(self) -> None:
        set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach(
            "Gates of the Underworld", "Region", self.player,
        )

    def create_item(self, name: str) -> GLItem:
        item = item_table[name]
        return GLItem(item.item_name, item.progression, item.code, self.player)

    def generate_output(self, output_directory: str) -> None:
        patch = GLProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        write_files(self, patch)
        rom_path = os.path.join(
            output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}",
        )
        patch.write(rom_path)
