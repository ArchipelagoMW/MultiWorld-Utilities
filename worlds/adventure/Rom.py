import hashlib
import json
import os
import zipfile
from typing import Optional, Any

import Utils
from .Locations import AdventureLocation
from Utils import OptionsType
from worlds.Files import APDeltaPatch, AutoPatchRegister
from itertools import chain

import bsdiff4

ADVENTUREHASH: str = "157bddb7192754a45372be196797f284"


class AdventureAutoCollectLocation:
    short_location_id: int = 0
    room_id: int = 0

    def __init__(self, short_location_id: int, room_id: int):
        self.short_location_id = short_location_id
        self.room_id = room_id

    def get_dict(self):
        return {
            "short_location_id": self.short_location_id,
            "room_id": self.room_id,
        }


class AdventureForeignItemInfo:
    short_location_id: int = 0
    room_id: int = 0
    room_x: int = 0
    room_y: int = 0

    def __init__(self, short_location_id: int, room_id: int, room_x: int, room_y: int):
        self.short_location_id = short_location_id
        self.room_id = room_id
        self.room_x = room_x
        self.room_y = room_y

    def get_dict(self):
        return {
            "short_location_id": self.short_location_id,
            "room_id": self.room_id,
            "room_x": self.room_x,
            "room_y": self.room_y,
        }


class AdventureDeltaPatch(APDeltaPatch, metaclass=AutoPatchRegister):
    hash = ADVENTUREHASH
    game = "Adventure"
    patch_file_ending = ".apadvn"
    foreign_items: [AdventureForeignItemInfo] = None
    autocollect_items: [AdventureAutoCollectLocation] = None
    local_item_locations: {} = None
    patched_rom_sha256: str = None
    seedName: bytes = None
    dragon_speed_reducer_info: {} = None
    diff_a_mode: int = None
    diff_b_mode: int = None

    # locations: [], autocollect: [], seed_name: bytes,
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        patch_only = True
        if "autocollect" in kwargs:
            patch_only = False
            self.foreign_items = [AdventureForeignItemInfo(loc.short_location_id, loc.room_id, loc.room_x, loc.room_y)
                                  for loc in kwargs["locations"]]

            self.autocollect_items = kwargs["autocollect"]
            self.seedName = kwargs["seed_name"]
            self.local_item_locations = kwargs["local_item_locations"]
            self.dragon_speed_reducer_info = kwargs["dragon_speed_reducer_info"]
            self.diff_a_mode = kwargs["diff_a_mode"]
            self.diff_b_mode = kwargs["diff_b_mode"]
            del kwargs["locations"]
            del kwargs["autocollect"]
            del kwargs["seed_name"]
            del kwargs["local_item_locations"]
            del kwargs["dragon_speed_reducer_info"]
            del kwargs["diff_a_mode"]
            del kwargs["diff_b_mode"]
        super(AdventureDeltaPatch, self).__init__(*args, **kwargs)
        if not patch_only:
            with open(self.patched_path, "rb") as file:
                patched_rom_bytes = bytes(file.read())
                patchedsha256 = hashlib.sha256()
                patchedsha256.update(patched_rom_bytes)
                self.patched_rom_sha256 = patchedsha256.hexdigest()

    def write_contents(self, opened_zipfile: zipfile.ZipFile):
        super(AdventureDeltaPatch, self).write_contents(opened_zipfile)
        # write Delta
        if self.foreign_items is not None:
            loc_bytes = []
            for foreign_item in self.foreign_items:
                loc_bytes.append(foreign_item.short_location_id)
                loc_bytes.append(foreign_item.room_id)
                loc_bytes.append(foreign_item.room_x)
                loc_bytes.append(foreign_item.room_y)
            opened_zipfile.writestr("adventure_locations",
                                    bytes(loc_bytes),
                                    compress_type=zipfile.ZIP_LZMA)
        if self.autocollect_items is not None:
            loc_bytes = []
            for item in self.autocollect_items:
                loc_bytes.append(item.short_location_id)
                loc_bytes.append(item.room_id)
            opened_zipfile.writestr("adventure_autocollect",
                                    bytes(loc_bytes),
                                    compress_type=zipfile.ZIP_LZMA)
        if self.patched_rom_sha256 is not None:
            opened_zipfile.writestr("hash",
                                    bytes(self.patched_rom_sha256, encoding="ascii"),
                                    compress_type=zipfile.ZIP_STORED)
        if self.player_name is not None:
            opened_zipfile.writestr("player",
                                    self.player_name,  # UTF-8
                                    compress_type=zipfile.ZIP_STORED)
        if self.seedName is not None:
            opened_zipfile.writestr("seedName",
                                    self.seedName,
                                    compress_type=zipfile.ZIP_STORED)
        if self.local_item_locations is not None:
            opened_zipfile.writestr("local_item_locations",
                                    json.dumps(self.local_item_locations),
                                    compress_type=zipfile.ZIP_LZMA)
        if self.dragon_speed_reducer_info is not None:
            opened_zipfile.writestr("dragon_speed_reducer_info",
                                    json.dumps(self.dragon_speed_reducer_info),
                                    compress_type=zipfile.ZIP_LZMA)
        if self.diff_a_mode is not None:
            opened_zipfile.writestr("diff_a_mode",
                                    self.diff_a_mode.to_bytes(1, "little"),
                                    compress_type=zipfile.ZIP_STORED)
        if self.diff_b_mode is not None:
            opened_zipfile.writestr("diff_b_mode",
                                    self.diff_b_mode.to_bytes(1, "little"),
                                    compress_type=zipfile.ZIP_STORED)

    def read_contents(self, opened_zipfile: zipfile.ZipFile):
        super(AdventureDeltaPatch, self).read_contents(opened_zipfile)
        self.foreign_items = AdventureDeltaPatch.read_foreign_items(opened_zipfile)
        self.autocollect_items = AdventureDeltaPatch.read_autocollect_items(opened_zipfile)


    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    @classmethod
    def read_rom_info(cls, opened_zipfile: zipfile.ZipFile) -> (bytes, bytes, str):
        hashbytes: bytes = opened_zipfile.read("hash")
        seedbytes: bytes = opened_zipfile.read("seedName")
        namebytes: bytes = opened_zipfile.read("player")
        namestr: str = namebytes.decode("utf-8")
        return hashbytes, seedbytes, namestr

    @classmethod
    def read_difficulty_switch_info(cls, opened_zipfile: zipfile.ZipFile) -> (int, int):
        diff_a_bytes = opened_zipfile.read("diff_a_mode")
        diff_b_bytes = opened_zipfile.read("diff_b_mode")
        diff_a = 0
        diff_b = 0
        if diff_a_bytes is not None:
            diff_a = int.from_bytes(diff_a_bytes, "little")
        if diff_b_bytes is not None:
            diff_b = int.from_bytes(diff_b_bytes, "little")
        return diff_a, diff_b

    @classmethod
    def read_foreign_items(cls, opened_zipfile: zipfile.ZipFile) -> [AdventureForeignItemInfo]:
        foreign_items = []
        readbytes: bytes = opened_zipfile.read("adventure_locations")
        bytelist = list(readbytes)
        for i in range(round(len(bytelist)/4)):
            offset = i * 4
            foreign_items.append(AdventureForeignItemInfo(bytelist[offset],
                                                          bytelist[offset + 1],
                                                          bytelist[offset + 2],
                                                          bytelist[offset + 3]))
        return foreign_items

    @classmethod
    def read_autocollect_items(cls, opened_zipfile: zipfile.ZipFile) -> [AdventureForeignItemInfo]:
        autocollect_items = []
        readbytes: bytes = opened_zipfile.read("adventure_autocollect")
        bytelist = list(readbytes)
        for i in range(round(len(bytelist)/2)):
            offset = i * 2
            autocollect_items.append(AdventureAutoCollectLocation(bytelist[offset], bytelist[offset + 1]))
        return autocollect_items

    @classmethod
    def read_local_item_locations(cls, opened_zipfile: zipfile.ZipFile) -> [AdventureForeignItemInfo]:
        readbytes: bytes = opened_zipfile.read("local_item_locations")
        readstr: str = readbytes.decode()
        return json.loads(readstr)

    @classmethod
    def read_dragon_speed_info(cls, opened_zipfile: zipfile.ZipFile) -> {}:
        readbytes: bytes = opened_zipfile.read("dragon_speed_reducer_info")
        readstr: str = readbytes.decode()
        return json.loads(readstr)


def apply_basepatch(base_rom_bytes: bytes) -> bytes:
    with open(os.path.join(os.path.dirname(__file__), "adventure_basepatch.bsdiff4"), "rb") as basepatch:
        delta: bytes = basepatch.read()
    return bsdiff4.patch(base_rom_bytes, delta)


def get_base_rom_bytes(file_name: str = "") -> bytes:
    file_name = get_base_rom_path(file_name)
    with open(file_name, "rb") as file:
        base_rom_bytes = bytes(file.read())
    basemd5 = hashlib.md5()
    basemd5.update(base_rom_bytes)
    if ADVENTUREHASH != basemd5.hexdigest():
        raise Exception(f"Supplied Base Rom does not match known MD5 for Adventure. "
                        "Get the correct game and version, then dump it")
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options: OptionsType = Utils.get_options()
    if not file_name:
        file_name = options["adventure_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name
