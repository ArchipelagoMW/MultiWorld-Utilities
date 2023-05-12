import Utils

from worlds.Files import APDeltaPatch

import hashlib
import os

from . import Patches
from .Names import RName
from .Stages import stage_info

USHASH = '1cc5cf3b4d29d8c3ade957648b529dc1'
BSUSHASH = '0bbaa6de2b9cbb822f8b4d85c1d5497b'
ROM_PLAYER_LIMIT = 65535


rom_sub_weapon_offsets = {
    0x10C6EB: 0x10,  # Forest
    0x10C6F3: 0x0F,
    0x10C6FB: 0x0E,
    0x10C703: 0x0D,

    0x10C81F: 0x0F,  # Castle Wall
    0x10C827: 0x10,
    0x10C82F: 0x0E,
    0x7F9A0F: 0x0D,

    0x83A5D9: 0x0E,  # Villa
    0x83A5E5: 0x0D,
    0x83A5F1: 0x0F,
    0xBFC903: 0x10,
    0x10C987: 0x10,
    0x10C98F: 0x0D,
    0x10C997: 0x0F,
    0x10CF73: 0x10,

    0x10CA57: 0x0D,  # Tunnel
    0x10CA5F: 0x0E,
    0x10CA67: 0x10,
    0x10CA6F: 0x0D,
    0x10CA77: 0x0F,
    0x10CA7F: 0x0E,

    0x10CBC7: 0x0E,  # Castle Center
    0x10CC0F: 0x0D,
    0x10CC5B: 0x0F,

    0x10CD3F: 0x0E,  # Character towers
    0x10CE2B: 0x0E,
    0x10CE83: 0x10,

    0x10CF8B: 0x0F,  # Room of Clocks
    0x10CF93: 0x0D,

    0x99BC5A: 0x0D,  # Clock Tower
    0x10CECB: 0x10,
    0x10CED3: 0x0F,
    0x10CEDB: 0x0E,
    0x10CEE3: 0x0D,
}

rom_sub_weapon_flags = {
    0x10C6EC: 0x0200FF04,  # Forest of Silence
    0x10C6FC: 0x0400FF04,
    0x10C6F4: 0x0800FF04,
    0x10C704: 0x4000FF04,

    0x10C831: 0x08,  # Castle Wall
    0x10C828: 0x10,
    0x10C821: 0x20,

    # Villa
    0xBFC926: 0xFF04,
    0xBFC93A: 0x80,
    0xBFC93F: 0x01,
    0xBFC943: 0x40,
    0xBFC947: 0x80,
    0x10C989: 0x10,
    0x10C991: 0x20,
    0x10C999: 0x40,
    0x10CF74: 0x01,

    0x10CA5A: 0x40FF0E,  # Tunnel
    0x10CA6B: 0x80,
    0x10CA60: 0x1000FF05,
    0x10CA70: 0x2000FF05,
    0x10CA78: 0x4000FF05,
    0x10CA80: 0x8000FF05,

    0x10CBCA: 0x02,  # Castle Center
    0x10CC10: 0x80,
    0x10CC5C: 0x40,

    0x10CE86: 0x01,  # Duel Tower
    0x10CD43: 0x02,  # Tower of Execution
    0x10CE2E: 0x20,  # Tower of Science

    0x10CF8E: 0x04,  # Room of Clocks
    0x10CF96: 0x08,

    0x10CECE: 0x08,  # Clock Tower
    0x10CED6: 0x10,
    0x10CEE6: 0x20,
    0x10CEDE: 0x80,
}

rom_empty_breakables_flags = {
    0x10C74D: 0x40FF05,  # Forest of Silence
    0x10C765: 0x80FF0D,
    0x10C774: 0x0800FF0E,
    0x10C755: 0x80FF05,
    0x10C784: 0x0100FF0E,
    0x10C73C: 0x0200FF0E,

    0x10C8D0: 0x0400FF0E,  # Villa foyer

    0x10CF9F: 0x08,  # Room of Clocks flags
    0x10CFA7: 0x01,
    0xBFCB27: 0x04,  # Room of Clocks candle property IDs
    0xBFCB2B: 0x05,
}

rom_looping_music_fade_ins = {
    0x10: None,
    0x11: None,
    0x12: None,
    0x13: None,
    0x14: None,
    0x15: None,
    0x16: 0x17,
    0x18: 0x19,
    0x1A: 0x1B,
    0x21: 0x75,
    0x27: None,
    0x2E: 0x23,
    0x39: None,
    0x45: 0x63,
    0x56: None,
    0x57: 0x58,
    0x59: None,
    0x5A: None,
    0x5B: 0x5C,
    0x5D: None,
    0x5E: None,
    0x5F: None,
    0x60: 0x61,
    0x62: None,
    0x64: None,
    0x65: None,
    0x66: None,
    0x68: None,
    0x69: None,
    0x6D: 0x78,
    0x6E: None,
    0x6F: None,
    0x73: None,
    0x74: None,
    0x77: None,
    0x79: None
}

warp_map_offsets = [0xADF67, 0xADF77, 0xADF87, 0xADF97, 0xADFA7, 0xADFBB, 0xADFCB, 0xADFDF]


class LocalRom(object):

    def __init__(self, file, patch=True, vanilla_rom=None, name=None, hash=None):
        self.name = name
        self.hash = hash
        self.orig_buffer = None

        with open(file, 'rb') as stream:
            self.buffer = bytearray(stream.read())
        # if patch:
        #    self.patch_rom()
        #    self.orig_buffer = self.buffer.copy()
        # if vanilla_rom:
        #    with open(vanillaRom, 'rb') as vanillaStream:
        #        self.orig_buffer = read_rom(vanillaStream)
        
    def read_bit(self, address: int, bit_number: int) -> bool:
        bitflag = (1 << bit_number)
        return (self.buffer[address] & bitflag) != 0

    def read_byte(self, address: int) -> int:
        return self.buffer[address]

    def read_bytes(self, startaddress: int, length: int) -> bytes:
        return self.buffer[startaddress:startaddress + length]

    def write_byte(self, address: int, value: int):
        self.buffer[address] = value

    def write_bytes(self, startaddress: int, values: list):
        self.buffer[startaddress:startaddress + len(values)] = values

    def write_int16(self, address, value: int):
        value = value & 0xFFFF
        self.write_bytes(address, [(value >> 8) & 0xFF, value & 0xFF])

    def write_int16s(self, startaddress, values: list):
        for i, value in enumerate(values):
            self.write_int16(startaddress + (i * 2), value)

    def write_int24(self, address, value: int):
        value = value & 0xFFFFFF
        self.write_bytes(address, [(value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF])

    def write_int24s(self, startaddress, values: list):
        for i, value in enumerate(values):
            self.write_int24(startaddress + (i * 3), value)

    def write_int32(self, address, value: int):
        value = value & 0xFFFFFFFF
        self.write_bytes(address, [(value >> 24) & 0xFF, (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF])

    def write_int32s(self, startaddress, values: list):
        for i, value in enumerate(values):
            self.write_int32(startaddress + (i * 4), value)

    def write_to_file(self, file):
        with open(file, 'wb') as outfile:
            outfile.write(self.buffer)

    def read_from_file(self, file):
        with open(file, 'rb') as stream:
            self.buffer = bytearray(stream.read())


def patch_rom(multiworld, rom, player, offsets_to_ids, active_stage_list, active_stage_exits, active_warp_list,
              required_s2s, music_list):
    w1 = str(multiworld.special1s_per_warp[player]).zfill(2)
    w2 = str(multiworld.special1s_per_warp[player] * 2).zfill(2)
    w3 = str(multiworld.special1s_per_warp[player] * 3).zfill(2)
    w4 = str(multiworld.special1s_per_warp[player] * 4).zfill(2)
    w5 = str(multiworld.special1s_per_warp[player] * 5).zfill(2)
    w6 = str(multiworld.special1s_per_warp[player] * 6).zfill(2)
    w7 = str(multiworld.special1s_per_warp[player] * 7).zfill(2)

    # NOP out the CRC BNEs
    rom.write_int32(0x66C, 0x00000000)
    rom.write_int32(0x678, 0x00000000)

    # Always offer Hard Mode on file creation
    rom.write_int32(0xC8810, 0x240A0100)  # ADDIU	T2, R0, 0x0100

    # Disable Easy Mode cutoff point at Castle Center elevator
    rom.write_int32(0xD9E18, 0x240D0000)  # ADDIU	T5, R0, 0x0000

    # Disable the Forest, Castle Wall, and Villa intro cutscenes and make it possible to change the starting level
    rom.write_byte(0xB73308, 0x00)
    rom.write_byte(0xB7331A, 0x40)
    rom.write_byte(0xB7332B, 0x4C)
    rom.write_byte(0xB6302B, 0x00)
    rom.write_byte(0x109F8F, 0x00)

    # Prevent Forest end cutscene flag from setting so it can be triggered infinitely
    rom.write_byte(0xEEA51, 0x01)

    # Make the CW drawbridge always closed (since rando doesn't play the CW intro cutscene that closes it)
    rom.write_int32(0x6C00EC, 0x240A0001)  # ADDIU T2, R0, 0x0001
    rom.write_int32(0x6C0ADC, 0x240A0001)  # ADDIU T2, R0, 0x0001

    # Villa coffin time-of-day hack
    rom.write_byte(0xD9D83, 0x74)
    rom.write_int32(0xD9D84, 0x080FF14D)  # J 0x803FC534
    rom.write_int32s(0xBFC534, Patches.coffin_time_checker)

    # Fix both Castle Center elevator bridges for both characters unless enabling only one character's stages. At which
    # point one bridge will be always broken and one always repaired instead.
    if multiworld.character_stages[player].value == 2:
        rom.write_int32(0x6CEAA0, 0x240B0000)  # ADDIU T3, R0, 0x0000
    elif multiworld.character_stages[player].value == 3:
        rom.write_int32(0x6CEAA0, 0x240B0001)  # ADDIU T3, R0, 0x0001
    else:
        rom.write_int32(0x6CEAA0, 0x240B0001)  # ADDIU T3, R0, 0x0001
        rom.write_int32(0x6CEAA4, 0x240D0001)  # ADDIU T5, R0, 0x0001

    # Were-bull arena flag hack
    rom.write_int32(0x6E38F0, 0x0C0FF157)  # JAL   0x803FC55C
    rom.write_int32s(0xBFC55C, Patches.werebull_flag_unsetter)
    rom.write_int32(0xA949C,  0x0C0FF380)  # JAL   0x803FCE00
    rom.write_int32s(0xBFCE00, Patches.werebull_flag_pickup_setter)

    # Enable being able to carry multiple Special jewels, Nitros, and Mandragoras simultaneously
    rom.write_int32(0xBF1F4, 0x3C038039)  # LUI V1, 0x8039
    # Special1
    rom.write_int32(0xBF210, 0x80659C4B)  # LB A1, 0x9C4B (V1)
    rom.write_int32(0xBF214, 0x24A50001)  # ADDIU A1, A1, 0x0001
    rom.write_int32(0xBF21C, 0xA0659C4B)  # SB A1, 0x9C4B (V1)
    # Special2
    rom.write_int32(0xBF230, 0x80659C4C)  # LB A1, 0x9C4C (V1)
    rom.write_int32(0xBF234, 0x24A50001)  # ADDIU A1, A1, 0x0001
    rom.write_int32(0xbf23C, 0xA0659C4C)  # SB A1, 0x9C4C (V1)
    # Magical Nitro
    rom.write_int32(0xBF360, 0x10000004)  # B 0x8013C184
    rom.write_int32(0xBF378, 0x25E50001)  # ADDIU A1, T7, 0x0001
    rom.write_int32(0xBF37C, 0x10000003)  # B 0x8013C19C
    # Mandragora
    rom.write_int32(0xBF3A8, 0x10000004)  # B 0x8013C1CC
    rom.write_int32(0xBF3C0, 0x25050001)  # ADDIU A1, T0, 0x0001
    rom.write_int32(0xBF3C4, 0x10000003)  # B 0x8013C1E4

    # Give PowerUps their Legacy of Darkness behavior when attempting to pick up more than two
    rom.write_int32(0xA9730, 0x24090000)  # ADDIU	T1, R0, 0x0000
    rom.write_int32(0xBF2FC, 0x080FF16D)  # J	0x803FC5B4
    rom.write_int32(0xBF300, 0x00000000)  # NOP
    rom.write_int32s(0xBFC5B4, Patches.give_powerup_stopper)

    # Rename "Wooden stake" and "Rose" to "Sent major" and "Sent" respectively
    rom.write_bytes(0xEFE34, cv64_text_converter("Sent major  ", False))
    rom.write_bytes(0xEFE4E, cv64_text_converter("Sent", False))
    # Capitalize the "k" in "Archives key" to be consistent with...literally every other key name!
    rom.write_byte(0xEFF21, 0x2D)

    # Change the Stage Select menu options
    rom.write_int32s(0xADF64, Patches.warp_menu_rewrite)
    rom.write_int32s(0x10E0C8, Patches.warp_pointer_table)
    for i in range(len(active_warp_list)):
        if i == 0:
            rom.write_byte(warp_map_offsets[i], stage_info[active_warp_list[i]].start_map_id)
            rom.write_byte(warp_map_offsets[i] + 4, stage_info[active_warp_list[i]].start_spawn_id)
        else:
            rom.write_byte(warp_map_offsets[i], stage_info[active_warp_list[i]].mid_map_id)
            rom.write_byte(warp_map_offsets[i] + 4, stage_info[active_warp_list[i]].mid_spawn_id)

    # Play the "teleportation" sound effect when teleporting
    rom.write_int32s(0xAE088, [0x08004FAB,   # J 0x80013EAC
                               0x2404019E])  # ADDIU A0, R0, 0x019E

    # Change the Stage Select menu's text to reflect its new purpose
    rom.write_bytes(0xEFAD0, cv64_text_converter(f"Where to...?\t{active_warp_list[0]}\t"
                                                 f"`{w1} {active_warp_list[1]}\t"
                                                 f"`{w2} {active_warp_list[2]}\t"
                                                 f"`{w3} {active_warp_list[3]}\t"
                                                 f"`{w4} {active_warp_list[4]}\t"
                                                 f"`{w5} {active_warp_list[5]}\t"
                                                 f"`{w6} {active_warp_list[6]}\t"
                                                 f"`{w7} {active_warp_list[7]}", False))

    # Lizard-man save proofing
    rom.write_int32(0xA99AC, 0x080FF0B8)  # J 0x803FC2E0
    rom.write_int32s(0xBFC2E0, Patches.boss_save_stopper)

    # Disable or guarantee vampire Vincent's fight
    if multiworld.vincent_fight_condition[player] == "never":
        rom.write_int32(0xAACC0, 0x24010001)  # ADDIU AT, R0, 0x0001
    elif multiworld.vincent_fight_condition[player] == "always":
        rom.write_int32(0xAACE0, 0x24180010)  # ADDIU T8, R0, 0x0010
    else:
        rom.write_int32(0xAACE0, 0x24180000)  # ADDIU T8, R0, 0x0000

    # Disable or guarantee Renon's fight
    rom.write_int32(0xAACB4, 0x080FF1A4)  # J 0x803FC690
    if multiworld.renon_fight_condition[player] == "never":
        rom.write_byte(0xB804F0, 0x00)
        rom.write_byte(0xB80632, 0x00)
        rom.write_byte(0xB807E3, 0x00)
        rom.write_byte(0xB80988, 0xB8)
        rom.write_byte(0xB816BD, 0xB8)
        rom.write_byte(0xB817CF, 0x00)
        rom.write_int32s(0xBFC690, Patches.renon_cutscene_checker_jr)
    elif multiworld.renon_fight_condition[player] == "always":
        rom.write_byte(0xB804F0, 0x0C)
        rom.write_byte(0xB80632, 0x0C)
        rom.write_byte(0xB807E3, 0x0C)
        rom.write_byte(0xB80988, 0xC4)
        rom.write_byte(0xB816BD, 0xC4)
        rom.write_byte(0xB817CF, 0x0C)
        rom.write_int32s(0xBFC690, Patches.renon_cutscene_checker_jr)
    else:
        rom.write_int32s(0xBFC690, Patches.renon_cutscene_checker)

    # Disable or guarantee the Bad Ending
    if multiworld.bad_ending_condition[player] == "never":
        rom.write_int32(0xAEE5C6, 0x3C0A0000)  # LUI  T2, 0x0000
    elif multiworld.bad_ending_condition[player] == "always":
        rom.write_int32(0xAEE5C6, 0x3C0A0040)  # LUI  T2, 0x0040

    # Play Castle Keep's song if teleporting in front of Dracula's door outside the escape sequence
    rom.write_int32(0x6E937C, 0x080FF12E)  # J 0x803FC4B8
    rom.write_int32s(0xBFC4B8, Patches.ck_door_music_player)

    # Increase item capacity to 100 if "Increase Item Limit" is turned on
    if multiworld.increase_item_limit[player]:
        rom.write_byte(0xBF30B, 0x64)  # Most items
        rom.write_byte(0xBF3F7, 0x64)  # Sun/Moon cards
    rom.write_byte(0xBF353, 0x64)  # Keys (increase regardless)

    # Change the item healing values if "Nerf Healing" is turned on
    if multiworld.nerf_healing_items[player]:
        rom.write_byte(0xB56371, 0x50)  # Healing kit   (100 -> 80)
        rom.write_byte(0xB56374, 0x32)  # Roast beef    ( 80 -> 50)
        rom.write_byte(0xB56377, 0x19)  # Roast chicken ( 50 -> 25)

    # Disable loading zone healing if turned off
    if not multiworld.loading_zone_heals[player]:
        rom.write_byte(0xD99A5, 0x00)  # Skip all loading zone checks
        rom.write_byte(0xA9DFFB, 0x40)  # Disable free heal from King Skeleton by reading the unused magic meter value

    # Disable spinning on the Special1 and 2 pickup models so colorblind people can more easily identify them
    rom.write_byte(0xEE4F5, 0x00)  # Special1
    rom.write_byte(0xEE505, 0x00)  # Special2

    # Prevent the vanilla Magical Nitro transport's "can explode" flag from setting
    rom.write_int32(0xB5D7AA, 0x00000000)  # NOP

    # Ensure the vampire Nitro check will always pass, so they'll never not spawn and crash the Villa cutscenes
    rom.write_byte(0xA6253D, 0x03)

    # Enable the Game Over's "Continue" menu starting the cursor on whichever checkpoint is most recent
    rom.write_int32(0xB4DDC, 0x0C060D58)  # JAL 0x80183560
    rom.write_int32s(0x106750, Patches.continue_cursor_start_checker)
    rom.write_int32(0x1C444, 0x080FF090)  # J   0x803FC240
    rom.write_int32(0x1C2A0, 0x080FF090)  # J   0x803FC240
    rom.write_int32s(0xBFC240, Patches.savepoint_cursor_updater)
    rom.write_int32(0x1C2D0, 0x080FF094)  # J   0x803FC250
    rom.write_int32s(0xBFC250, Patches.stage_start_cursor_updater)
    rom.write_byte(0xB585C8, 0xFF)

    # Add data for White Jewel #22 (the new Duel Tower savepoint) at the end of the White Jewel ID data list
    rom.write_int16s(0x104AC8, [0x0000, 0x0006,
                                0x0013, 0x0015])

    # Spawn coordinates list extension
    rom.write_int32(0xD5BF4, 0x080FF103)  # J	0x803FC40C
    rom.write_int32s(0xBFC40C, Patches.spawn_coordinates_extension)
    rom.write_int32s(0x108A5E, Patches.waterway_end_coordinates)

    # Change the File Select stage numbers to match the new stage order. Also fix a vanilla issue wherein saving in a
    # character-exclusive stage as the other character would incorrectly display the name of that character's equivalent
    # stage on the save file instead of the one they're actually in.
    rom.write_byte(0xC9FE3, 0xD4)
    rom.write_byte(0xCA055, 0x08)
    rom.write_byte(0xCA066, 0x40)
    rom.write_int32(0xCA068, 0x860C17D0)  # LH T4, 0x17D0 (S0)
    rom.write_byte(0xCA06D, 0x08)
    rom.write_byte(0x104A31, 0x01)
    rom.write_byte(0x104A39, 0x01)
    rom.write_byte(0x104A89, 0x01)
    rom.write_byte(0x104A91, 0x01)
    rom.write_byte(0x104A99, 0x01)
    rom.write_byte(0x104AA1, 0x01)

    for stage in active_stage_list:
        for offset in stage_info[stage].stage_number_offset_list:
            rom.write_byte(offset, active_stage_exits[stage][3])

    # Top elevator switch check
    rom.write_int32(0x6CF0A0, 0x0C0FF0B0)  # JAL 0x803FC2C0
    rom.write_int32s(0xBFC2C0, Patches.elevator_flag_checker)

    # Waterway brick platforms skip
    if multiworld.skip_waterway_platforms[player]:
        rom.write_int32(0x6C7E2C, 0x00000000)  # NOP

    # Disable time restrictions
    if multiworld.disable_time_restrictions[player]:
        # Fountain
        rom.write_int32(0x6C2340, 0x00000000)  # NOP
        rom.write_int32(0x6C257C, 0x10000023)  # B [forward 0x23]
        # Rosa
        rom.write_byte(0xEEAAB, 0x00)
        rom.write_byte(0xEEAAD, 0x18)
        # Moon doors
        rom.write_int32(0xDC3E0, 0x00000000)  # NOP
        rom.write_int32(0xDC3E8, 0x00000000)  # NOP
        # Sun doors
        rom.write_int32(0xDC410, 0x00000000)  # NOP
        rom.write_int32(0xDC418, 0x00000000)  # NOP

    # Custom data-loading code
    rom.write_int32(0x6B5028, 0x08060D70)  # J 0x801835D0
    rom.write_int32s(0x1067B0, Patches.custom_code_loader)

    # Custom remote item rewarding and DeathLink receiving code
    rom.write_int32(0x19B98, 0x080FF000)  # J 0x803FC000
    rom.write_int32s(0xBFC000, Patches.remote_item_giver)

    # DeathLink counter decrementer code
    rom.write_int32(0x1C340, 0x080FF052)  # J 0x803FC148
    rom.write_int32s(0xBFC148, Patches.deathlink_counter_decrementer)

    # Death flag un-setter on "Beginning of stage" state overwrite code
    rom.write_int32(0x1C2B0, 0x080FF047)  # J 0x803FC11C
    rom.write_int32s(0xBFC11C, Patches.death_flag_unsetter)

    # Warp menu-opening code
    rom.write_int32(0xB9BA8, 0x080FF099)  # J	0x803FC264
    rom.write_int32s(0xBFC264, Patches.warp_menu_opener)

    # NPC item textbox hack
    rom.write_int32(0xBF1DC, 0x080FF067)  # J 0x803FC19C
    rom.write_int32(0xBF1E0, 0x27BDFFE0)  # ADDIU SP, SP, -0x20
    rom.write_int32s(0xBFC19C, Patches.npc_item_hack)

    # Sub-weapon check function hook
    rom.write_int32(0xBF32C, 0x00000000)  # NOP
    rom.write_int32(0xBF330, 0x080FF05D)  # J	0x803FC174
    rom.write_int32s(0xBFC174, Patches.give_subweapon_stopper)

    # Warp menu Special1 restriction
    rom.write_int32(0xADD68, 0x0C04AB12)  # JAL 0x8012AC48
    rom.write_int32s(0xADE28, Patches.stage_select_overwrite)
    rom.write_byte(0xADE47, multiworld.special1s_per_warp[player])

    # Dracula's door text pointer hijack
    rom.write_int32(0xD69F0, 0x080FF141)  # J 0x803FC504
    rom.write_int32s(0xBFC504, Patches.dracula_door_text_redirector)

    # Dracula's chamber condition
    rom.write_int32(0xE2FDC, 0x0804AB25)  # J 0x8012AC78
    rom.write_int32s(0xADE84, Patches.special_goal_checker)
    rom.write_bytes(0xBFCC3C, [0xA0, 0x00, 0xFF, 0xFF, 0xA0, 0x01, 0xFF, 0xFF, 0xA0, 0x02, 0xFF, 0xFF, 0xA0, 0x03, 0xFF,
                               0xFF, 0xA0, 0x04, 0xFF, 0xFF, 0xA0, 0x05, 0xFF, 0xFF, 0xA0, 0x06, 0xFF, 0xFF, 0xA0, 0x07,
                               0xFF, 0xFF, 0xA0, 0x08, 0xFF, 0xFF, 0xA0, 0x09])
    if multiworld.draculas_condition[player] == 1:
        rom.write_int32(0x6C8A54, 0x0C0FF089)  # JAL 0x803FC224
        rom.write_int32s(0xBFC224, Patches.crystal_special2_giver)
        rom.write_byte(0xADE8F, 0x01)
        rom.write_bytes(0xBFCC62, cv64_text_converter(f"It won't budge!\n"
                                                      f"You'll need the power\n"
                                                      f"of the basement crystal\n"
                                                      f"to undo the seal.", True))
    elif multiworld.draculas_condition[player] == 2:
        rom.write_int32(0xBBD50, 0x080FF18C)  # J	0x803FC630
        rom.write_int32s(0xBFC630, Patches.boss_special2_giver)
        rom.write_int32s(0xBFC55C, Patches.werebull_flag_unsetter_special2_electric_boogaloo)
        rom.write_byte(0xADE8F, multiworld.bosses_required[player].value)
        rom.write_bytes(0xBFCC62, cv64_text_converter(f"It won't budge!\n"
                                                      f"You'll need to defeat\n"
                                                      f"{required_s2s} powerful monsters\n"
                                                      f"to undo the seal.", True))
    elif multiworld.draculas_condition[player] == 3:
        rom.write_byte(0xADE8F, multiworld.special2s_required[player].value)
        rom.write_bytes(0xBFCC62, cv64_text_converter(f"It won't budge!\n"
                                                      f"You'll need to find\n"
                                                      f"{required_s2s} Special2 jewels\n"
                                                      f"to undo the seal.", True))
    else:
        rom.write_byte(0xADE8F, 0x00)

    # On-the-fly TLB script modifier
    rom.write_int32s(0xBFC338, Patches.double_component_checker)
    rom.write_int32s(0xBFC3D4, Patches.downstairs_seal_checker)
    rom.write_int32s(0xBFC700, Patches.overlay_modifiers)

    # On-the-fly map object data modifier hook
    rom.write_int32(0xEAB04, 0x080FF220)  # J 0x803FC880
    rom.write_int32s(0xBFC878, Patches.map_data_modifiers)

    # Fix locked doors to check the key counters instead of their vanilla key locations' bitflags
    # Pickup flag check modifications:
    rom.write_int32(0x10B2D8, 0x00000002)  # Left Tower Door
    rom.write_int32(0x10B2F0, 0x00000003)  # Storeroom Door
    rom.write_int32(0x10B2FC, 0x00000001)  # Archives Door
    rom.write_int32(0x10B314, 0x00000004)  # Maze Gate
    rom.write_int32(0x10B350, 0x00000005)  # Copper Door
    rom.write_int32(0x10B3A4, 0x00000006)  # Torture Chamber Door
    rom.write_int32(0x10B3B0, 0x00000007)  # ToE Gate
    rom.write_int32(0x10B3BC, 0x00000008)  # Science Door1
    rom.write_int32(0x10B3C8, 0x00000009)  # Science Door2
    rom.write_int32(0x10B3D4, 0x0000000A)  # Science Door3
    rom.write_int32(0x6F0094, 0x0000000B)  # CT Door 1
    rom.write_int32(0x6F00A4, 0x0000000C)  # CT Door 2
    rom.write_int32(0x6F00B4, 0x0000000D)  # CT Door 3
    # Item counter decrement check modifications:
    rom.write_int32(0xEDA84, 0x00000001)   # Archives Door
    rom.write_int32(0xEDA8C, 0x00000002)   # Left Tower Door
    rom.write_int32(0xEDA94, 0x00000003)   # Storeroom Door
    rom.write_int32(0xEDA9C, 0x00000004)   # Maze Gate
    rom.write_int32(0xEDAA4, 0x00000005)   # Copper Door
    rom.write_int32(0xEDAAC, 0x00000006)   # Torture Chamber Door
    rom.write_int32(0xEDAB4, 0x00000007)   # ToE Gate
    rom.write_int32(0xEDABC, 0x00000008)   # Science Door1
    rom.write_int32(0xEDAC4, 0x00000009)   # Science Door2
    rom.write_int32(0xEDACC, 0x0000000A)   # Science Door3
    rom.write_int32(0xEDAD4, 0x0000000B)   # CT Door 1
    rom.write_int32(0xEDADC, 0x0000000C)   # CT Door 2
    rom.write_int32(0xEDAE4, 0x0000000D)   # CT Door 3

    rom.write_int32(0x10AB2C, 0x8015FBD4)  # Maze Gates' check code pointer adjustments
    rom.write_int32(0x10AB40, 0x8015FBD4)
    rom.write_int32s(0x10AB50, [0x0D0C0000,
                                0x8015FBD4])
    rom.write_int32s(0x10AB64, [0x0D0C0000,
                                0x8015FBD4])
    rom.write_int32s(0xE2E14, Patches.normal_door_hook)
    rom.write_int32s(0xBFC5D0, Patches.normal_door_code)
    rom.write_int32s(0x6EF298, Patches.ct_door_hook)
    rom.write_int32s(0xBFC608, Patches.ct_door_code)
    # Fix key counter not decrementing if 2 or above
    rom.write_int32(0xAA0E0, 0x24020000)  # ADDIU	V0, R0, 0x0000

    # Make the Easy-only candle drops in Room of Clocks appear on any difficulty
    rom.write_byte(0x9B518F, 0x01)

    # Slightly move some once-invisible freestanding items to be more visible
    # if multiworld.reveal_invisible_items[player]:
    rom.write_byte(0x7C7F95, 0xEF)  # Forest dirge maiden statue
    rom.write_byte(0x7C7FA8, 0xAB)  # Forest werewolf statue
    rom.write_byte(0x8099C4, 0x8C)  # Villa courtyard tombstone
    rom.write_byte(0x83A626, 0xC2)  # Villa living room painting
    # rom.write_byte(0x83A62F, 0x64)  # Villa Mary's room table
    rom.write_byte(0x8985DD, 0xF5)  # CC torture instrument rack
    rom.write_byte(0x8C44D5, 0x22)  # CC red carpet hallway knight
    rom.write_byte(0x8DF57C, 0xF1)  # CC cracked wall hallway flamethrower
    rom.write_byte(0x90FCD6, 0xA5)  # CC nitro hallway flamethrower
    rom.write_byte(0x90FB9F, 0x9A)  # CC invention room round machine
    rom.write_byte(0x90FBAF, 0x03)  # CC invention room giant famicart
    rom.write_byte(0x90FE54, 0x97)  # CC staircase knight (x)
    rom.write_byte(0x90FE58, 0xFB)  # CC staircase knight (z)

    # Change bitflag on item in upper coffin in Forest final switch gate tomb to one that's not used by something else
    rom.write_int32(0x10C77C, 0x00000002)

    # Make the torch directly behind Dracula's chamber that normally doesn't set a flag set bitflag 0x08 in 0x80389BFA
    rom.write_byte(0x10CE9F, 0x01)

    # Write the randomized (or disabled) music ID list and its associated code
    if multiworld.background_music[player] != 0:
        rom.write_int32(0x14588, 0x08060D60)  # J 0x80183580
        rom.write_int32(0x14590, 0x00000000)  # NOP
        rom.write_int32s(0x106770, Patches.music_modifier)
        rom.write_bytes(0xBFCD30, music_list)
        rom.write_int32(0x15780, 0x0C0FF36E)  # JAL 0x803FCDB8
        rom.write_int32s(0xBFCDB8, Patches.music_comparer_modifier)

    # Enable storing item flags anywhere and changing the item model/visibility on any item instance.
    rom.write_int32s(0xA857C, [0x080FF38F,   # J	    0x803FCE3C
                               0x94D90038])  # LHU   T9, 0x0038 (A2)
    rom.write_int32s(0xBFCE3C, Patches.item_customizer)
    rom.write_int32s(0xA86A0, [0x0C0FF3AF,   # JAL   0x803FCEBC
                               0x95C40002])  # LHU   A0, 0x0002 (T6)
    rom.write_int32s(0xBFCEBC, Patches.item_appearance_switcher)
    rom.write_int32s(0xA8728, [0x0C0FF3B8,   # JAL   0x803FCEE4
                               0x01396021])  # ADDU  T4, T1, T9
    rom.write_int32s(0xBFCEE4, Patches.item_model_visibility_switcher)
    rom.write_int32s(0xA8A04, [0x0C0FF3C2,   # JAL   0x803FCF08
                               0x018B6021])  # ADDU  T4, T4, T3
    rom.write_int32s(0xBFCF08, Patches.item_shine_visibility_switcher)

    # If playing with universal sub-weapons or included empty breakables, write these values to have them store flags
    # and, in the case of the RoC candles, change them to two unused candle settings.
    if multiworld.empty_breakables[player]:
        offsets_to_ids.update({**rom_empty_breakables_flags})
    if multiworld.sub_weapon_shuffle[player].value > 1:
        offsets_to_ids.update({**rom_sub_weapon_flags})

    # Disable the 3HBs checking and setting flags when breaking them and enable their individual items checking and
    # setting flags instead.
    rom.write_int32(0xE87F8, 0x00000000)  # NOP
    rom.write_int16(0xE836C, 0x1000)
    rom.write_int32(0xE8B40, 0x0C0FF3CD)  # JAL 0x803FCF34
    rom.write_int32s(0xBFCF34, Patches.three_hit_item_flags_setter)
    # Villa foyer chandelier-specific functions (yeah, IDK why KCEK made different functions for this one)
    rom.write_int32(0xE7D54, 0x00000000)  # NOP
    rom.write_int16(0xE7908, 0x1000)
    rom.write_byte(0xE7A5C, 0x10)
    rom.write_int32(0xE7F08, 0x0C0FF3DF)  # JAL 0x803FCF7C
    rom.write_int32s(0xBFCF7C, Patches.chandelier_item_flags_setter)

    # New flag values to put in each 3HB vanilla flag's spot
    rom.write_int32(0x10C7C8, 0x8000FF48)  # FoS dirge maiden rock
    rom.write_int32(0x10C7B0, 0x0200FF48)  # FoS S1 bridge rock
    rom.write_int32(0x10C86C, 0x0010FF48)  # CW upper rampart save nub
    rom.write_int32(0x10C878, 0x4000FF49)  # CW Dracula switch slab
    rom.write_int32(0x10CAD8, 0x0100FF49)  # Tunnel twin arrows slab
    rom.write_int32(0x10CAE4, 0x0004FF49)  # Tunnel lonesome bucket pit rock
    rom.write_int32(0x10CB54, 0x4000FF4A)  # UW poison parkour ledge
    rom.write_int32(0x10CB60, 0x0080FF4A)  # UW skeleton crusher ledge
    rom.write_int32(0x10CBF0, 0x0008FF4A)  # CC Behemoth crate
    rom.write_int32(0x10CC2C, 0x2000FF4B)  # CC elevator pedestal
    rom.write_int32(0x10CC70, 0x0200FF4B)  # CC lizard-man generator slab
    rom.write_int32(0x10CD88, 0x0010FF4B)  # ToE pre-midsavepoint platforms ledge
    rom.write_int32(0x10CE6C, 0x4000FF4C)  # ToSci invisible bridge crate
    rom.write_int32(0x10CF20, 0x0080FF4C)  # CT inverted battery slab
    rom.write_int32(0x10CF2C, 0x0008FF4C)  # CT inverted door slab
    rom.write_int32(0x10CF38, 0x8000FF4D)  # CT final room door slab
    rom.write_int32(0x10CF44, 0x1000FF4D)  # CT Renon slab
    rom.write_int32(0x10C908, 0x0008FF4D)  # Villa foyer chandelier
    if multiworld.multi_hit_breakables[player]:
        rom.write_byte(0x10CF37, 0x04)  # pointer for CT final room door slab item data

    if multiworld.drop_previous_sub_weapon[player]:
        rom.write_int32(0xBFC18C, 0x080FF3F2)  # J 0x803FCFC8
        rom.write_int32s(0xBFCFC4, Patches.prev_subweapon_dropper)

    # Write all the new item and loading zone bytes
    for offset, item_id in offsets_to_ids.items():
        if item_id <= 0xFF:
            rom.write_byte(offset, item_id)
        elif item_id <= 0xFFFF:
            rom.write_int16(offset, item_id)
        elif item_id <= 0xFFFFFF:
            rom.write_int24(offset, item_id)
        else:
            rom.write_int32(offset, item_id)


class CV64DeltaPatch(APDeltaPatch):
    hash = USHASH
    patch_file_ending: str = ".apcv64"
    result_file_ending: str = ".z64"

    game = "Castlevania 64"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(open(file_name, "rb").read())

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if USHASH != basemd5.hexdigest() and BSUSHASH != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for US(1.0) release. '
                            'Get the correct game and version, then dump it.')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        # file_name = options["cv64_options"]["rom_file"]
        file_name = "Castlevania (USA).z64"
    if not os.path.exists(file_name):
        file_name = Utils.local_path(file_name)
    return file_name


def cv64_text_converter(cv64text: str, a_advance: bool) -> list:
    char_dict = {"\n": 0x01, " ": 0x02, "!": 0x03, '"': 0x04, "#": 0x05, "$": 0x06, "%": 0x07, "&": 0x08, "'": 0x09,
                 "(": 0x0A, ")": 0x0B, "*": 0x0C, "+": 0x0D, ",": 0x0E, "-": 0x0F, ".": 0x10, "/": 0x11, "0": 0x12,
                 "1": 0x13, "2": 0x14, "3": 0x15, "4": 0x16, "5": 0x17, "6": 0x18, "7": 0x19, "8": 0x1A, "9": 0x1B,
                 ":": 0x1C, ";": 0x1D, "<": 0x1E, "=": 0x1F, ">": 0x20, "?": 0x21, "@": 0x22, "A": 0x23, "B": 0x24,
                 "C": 0x25, "D": 0x26, "E": 0x27, "F": 0x28, "G": 0x29, "H": 0x2A, "I": 0x2B, "J": 0x2C, "K": 0x2D,
                 "L": 0x2E, "M": 0x2F, "N": 0x30, "O": 0x31, "P": 0x32, "Q": 0x33, "R": 0x34, "S": 0x35, "T": 0x36,
                 "U": 0x37, "V": 0x38, "W": 0x39, "X": 0x3A, "Y": 0x3B, "Z": 0x3C, "[": 0x3D, "\\": 0x3E, "]": 0x3F,
                 "^": 0x40, "_": 0x41, "a": 0x43, "b": 0x44, "c": 0x45, "d": 0x46, "e": 0x47, "f": 0x48, "g": 0x49,
                 "h": 0x4A, "i": 0x4B, "j": 0x4C, "k": 0x4D, "l": 0x4E, "m": 0x4F, "n": 0x50, "o": 0x51, "p": 0x52,
                 "q": 0x53, "r": 0x54, "s": 0x55, "t": 0x56, "u": 0x57, "v": 0x58, "w": 0x59, "x": 0x5A, "y": 0x5B,
                 "z": 0x5C, "{": 0x5D, "|": 0x5E, "}": 0x5F, "`": 0x61, "「": 0x62, "」": 0x63, "~": 0x65, "″": 0x72,
                 "°": 0x73, "∞": 0x74}

    text_bytes = []
    for i in cv64text:
        if i == "\t":
            text_bytes.append(0xFF)
            text_bytes.append(0xFF)
        else:
            text_bytes.append(0x00)
            if i in char_dict:
                text_bytes.append(char_dict[i])
            else:
                text_bytes.append(0x02)
    if a_advance:
        text_bytes.append(0xA3)
        text_bytes.append(0x00)
    text_bytes.append(0xFF)
    text_bytes.append(0xFF)
    return text_bytes
