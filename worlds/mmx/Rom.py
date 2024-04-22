import typing
import bsdiff4
import Utils
import hashlib
import os
from typing import Optional, TYPE_CHECKING
from pkgutil import get_data

from worlds.AutoWorld import World
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

HASH_US = 'a10071fa78554b57538d0b459e00d224'
HASH_US_REV_1 = 'df1cc0c8c8c4b61e3b834cc03366611c'
HASH_LEGACY = 'f1dfbbcdc3d8cdeafa4b4b9aa51a56d6'

STARTING_ID = 0xBE0800

weapon_rom_data = {
    STARTING_ID + 0x000E: [0x1F88, 0xFF],
    STARTING_ID + 0x0010: [0x1F8A, 0xFF],
    STARTING_ID + 0x000D: [0x1F8C, 0xFF],
    STARTING_ID + 0x0012: [0x1F8E, 0xFF],
    STARTING_ID + 0x0011: [0x1F90, 0xFF],
    STARTING_ID + 0x000C: [0x1F92, 0xFF],
    STARTING_ID + 0x000F: [0x1F94, 0xFF],
    STARTING_ID + 0x000B: [0x1F96, 0xFF],
    #STARTING_ID + 0x001A: [0x1F7E, 0x80],
}

upgrades_rom_data = {
    STARTING_ID + 0x001C: [0x00],
    STARTING_ID + 0x001D: [0x02],
    STARTING_ID + 0x001E: [0x01],
    STARTING_ID + 0x001F: [0x03],
}

boss_access_rom_data = {
    STARTING_ID + 0x0006: [0x01],
    STARTING_ID + 0x0008: [0x02],
    STARTING_ID + 0x0002: [0x03],
    STARTING_ID + 0x0005: [0x04],
    STARTING_ID + 0x0009: [0x05],
    STARTING_ID + 0x0007: [0x06],
    STARTING_ID + 0x0003: [0x07],
    STARTING_ID + 0x0004: [0x08],
    STARTING_ID + 0x000A: [0x09],
}

refill_rom_data = {
    STARTING_ID + 0x0030: ["small hp refill"],
    STARTING_ID + 0x0031: ["large hp refill"],
    STARTING_ID + 0x0034: ["1up"],
    #0xBD0032: ["small weapon refill"],
    #0xBD0033: ["large weapon refill"]
}

class MMXProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = [HASH_US, HASH_LEGACY]
    game = "Mega Man X"
    patch_file_ending = ".apmmx"
    result_file_ending = ".sfc"
    name: bytearray
    procedure = [
        ("apply_tokens", ["token_patch.bin"]),
        ("apply_bsdiff4", ["mmx_basepatch.bsdiff4"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    def write_byte(self, offset, value):
        self.write_token(APTokenTypes.WRITE, offset, value.to_bytes(1, "little"))

    def write_bytes(self, offset, value: typing.Iterable[int]):
        self.write_token(APTokenTypes.WRITE, offset, bytes(value))

def patch_rom(world: World, patch: MMXProcedurePatch):
    from Utils import __version__

    # Prepare some ROM locations to receive the basepatch output
    patch.write_bytes(0x00098C, bytearray([0x85,0xB3,0x8A]))
    patch.write_bytes(0x0009AE, bytearray([0x85,0xB3,0x8A]))
    patch.write_bytes(0x001261, bytearray([0xA9,0x10,0x20,0xE1,0x89]))
    patch.write_bytes(0x001271, bytearray([0xA5,0xAC,0x89,0x08,0xF0,0x09,0xA5,0x3C,
                                           0x3A,0x10,0x11,0xA9,0x02,0x80,0x0D,0x89,
                                           0x24,0xF0,0x1E,0xA5,0x3C,0x1A,0xC9,0x03,
                                           0xD0,0x02,0xA9,0x00,0x85,0x3C,0xAA,0xBD,
                                           0x75,0x88,0x8D,0xB0,0x0B,0xA5,0x3C,0x18,
                                           0x69,0x10,0x20,0xE1,0x89,0xA9,0xF0,0x85,
                                           0x3B]))
    patch.write_bytes(0x00131F, bytearray([0x9C,0xA9,0x0B,0x9C,0xAA,0x0B]))
    patch.write_bytes(0x00132E, bytearray([0x90,0x8B]))
    patch.write_bytes(0x001352, bytearray([0x64,0x38,0x64,0x39]))
    patch.write_bytes(0x0025CA, bytearray([0xA9,0xF6,0xA0,0x02]))
    patch.write_bytes(0x0046F3, bytearray([0x38,0xE9,0x0A]))
    patch.write_bytes(0x006A61, bytearray([0xFB,0xEC]))
    patch.write_bytes(0x006D67, bytearray([0x85,0x00,0x0A]))
    patch.write_bytes(0x006F97, bytearray([0x9F,0xCB,0xFF,0x7E]))
    patch.write_bytes(0x00700F, bytearray([0x55,0xDB]))
    patch.write_bytes(0x007BF0, bytearray([0x90,0x8B]))
    patch.write_bytes(0x00EB4A, bytearray([0xEE,0xCF,0x0B,0xA9,0x80]))
    patch.write_bytes(0x011646, bytearray([0xA9,0x0A,0x85,0x01]))
    patch.write_bytes(0x01B392, bytearray([0xA9,0x02,0x85,0x03]))
    patch.write_bytes(0x01C67E, bytearray([0xA9,0x04,0x85,0x01]))
    patch.write_bytes(0x01D84F, bytearray([0xA9,0x3C,0x9D,0x0A,0x00]))
    patch.write_bytes(0x021D51, bytearray([0xED,0x00,0x00,0x8D,0xCF,0x0B]))
    patch.write_bytes(0x021E94, bytearray([0x64,0x27,0xA9,0xFF]))
    patch.write_bytes(0x021F5A, bytearray([0xED,0x00,0x00,0x8D,0xCF,0x0B]))
    patch.write_bytes(0x02268C, bytearray([0xE6,0x03,0xE6,0x03]))
    patch.write_bytes(0x03D0B2, bytearray([0x0C,0x99,0x1F,0x4C,0xBD,0xD0]))
    patch.write_bytes(0x03D0D9, bytearray([0xA9,0x80,0x0C,0x7E]))
    patch.write_bytes(0x044BEC, bytearray([0xA9,0x12,0x85,0x01]))
    patch.write_bytes(0x0457CC, bytearray([0xA9,0x02,0x0C,0x99,0x1F]))

    patch.write_bytes(0x0312B0, bytearray([0x20,0xC6,0x09,0x40,0x14,0x20,0x06,0x0A,
                                           0x4C,0x49,0x43,0x45,0x4E,0x53,0x45,0x44,
                                           0x20,0x42,0x59,0x20,0x4E,0x49,0x4E,0x54,
                                           0x45,0x4E,0x44,0x4F,0x00]))

    # Edit the ROM header
    patch.name = bytearray(f'MMX1{__version__.replace(".", "")[0:3]}_{world.player}_{world.multiworld.seed:11}\0', 'utf8')[:21]
    patch.name.extend([0] * (21 - len(patch.name)))
    patch.write_bytes(0x7FC0, patch.name)

    # Write options to the ROM
    patch.write_byte(0x17FFE0, world.options.sigma_open.value)
    patch.write_byte(0x17FFE1, world.options.sigma_medal_count.value)
    patch.write_byte(0x17FFE2, world.options.sigma_weapon_count.value)
    patch.write_byte(0x17FFE3, world.options.sigma_upgrade_count.value)
    patch.write_byte(0x17FFE4, world.options.sigma_heart_tank_count.value)
    patch.write_byte(0x17FFE5, world.options.sigma_sub_tank_count.value)
    patch.write_byte(0x17FFE6, world.options.starting_life_count.value)
    patch.write_byte(0x17FFE7, world.options.pickupsanity.value)
    patch.write_byte(0x17FFEB, world.options.logic_boss_weakness.value)
    #patch.write_byte(0x17FFEA, world.options.logic_hadouken.value)
    
    # EnergyLink
    patch.write_byte(0x17FFE8, world.options.energy_link.value)

    # DeathLink
    patch.write_byte(0x17FFE9, world.options.death_link.value)
    
    patch.write_file("token_patch.bin", patch.get_token_binary())

    
def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if basemd5.hexdigest() not in {HASH_US, HASH_LEGACY}:
            raise Exception('Supplied Base Rom does not match known MD5 for US or LC release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        file_name = options["mmx_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name
