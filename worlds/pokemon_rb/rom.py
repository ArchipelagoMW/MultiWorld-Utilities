import os
import hashlib
import Utils
import bsdiff4
from copy import deepcopy
from Patch import read_rom, APDeltaPatch
from .text import encode_text
from .rom_addresses import rom_addresses
from .locations import get_locations
import worlds.pokemon_rb.poke_data as poke_data


def choose_forced_type(chances, random):
    n = random.randint(1, 100)
    for chance in chances:
        if chance[0] >= n:
            return chance[1]
    return None


def filter_moves(moves, type, random):
    ret = []
    for move in moves:
        if poke_data.moves[move]["type"] == type or type is None:
            ret.append(move)
    random.shuffle(ret)
    return ret


def get_move(moves, chances, random, starting_move=False):
    type = choose_forced_type(chances, random)
    filtered_moves = filter_moves(moves, type, random)
    for move in filtered_moves:
        if poke_data.moves[move]["accuracy"] > 80 and poke_data.moves[move]["power"] > 0 or not starting_move:
            moves.remove(move)
            return move
    else:
        return get_move(moves, [], random, starting_move)


def get_encounter_slots(self):
    encounter_slots = [location for location in get_locations(self.player) if location.type == "Wild Encounter"]

    for location in encounter_slots:
        if isinstance(location.original_item, list):
            location.original_item = location.original_item[not self.world.game_version[self.player].value]
    return encounter_slots


def get_base_stat_total(mon):
    return (poke_data.pokemon_data[mon]["atk"] + poke_data.pokemon_data[mon]["def"]
            + poke_data.pokemon_data[mon]["hp"] + poke_data.pokemon_data[mon]["spd"]
            + poke_data.pokemon_data[mon]["spc"])


def randomize_pokemon(self, mon, mons_list, randomize_type):
    if randomize_type in [1, 3]:
        type_mons = [pokemon for pokemon in mons_list if any([poke_data.pokemon_data[mon][
             "type1"] in [self.local_poke_data[pokemon]["type1"], self.local_poke_data[pokemon]["type2"]],
             poke_data.pokemon_data[mon]["type2"] in [self.local_poke_data[pokemon]["type1"],
                                                      self.local_poke_data[pokemon]["type2"]]])]
        if not type_mons:
            type_mons = mons_list.copy()
        if randomize_type == 3:
            stat_base = get_base_stat_total(mon)
            type_mons.sort(key=lambda mon: abs(get_base_stat_total(mon) - stat_base))
            mon = type_mons[round(self.world.random.triangular(0, len(type_mons) - 1, 0))]
    if randomize_type == 2:
        stat_base = get_base_stat_total(mon)
        mons_list.sort(key=lambda mon: abs(get_base_stat_total(mon) - stat_base))
        mon = mons_list[round(self.world.random.triangular(0, 50, 0))]
    elif randomize_type == 4:
        mon = self.world.random.choice(mons_list)
    return mon


def process_trainer_data(self, data):
    if not self.world.randomize_trainer_parties[self.player].value:
        return
    mons_list = [pokemon for pokemon in poke_data.pokemon_data.keys() if pokemon not in poke_data.legendary_pokemon]
    address = rom_addresses["Trainer_Data"]
    while address < rom_addresses["Trainer_Data_End"]:
        if data[address] == 255:
            mode = 1
        else:
            mode = 0
        while True:
            address += 1
            if data[address] == 0:
                address += 1
                break
            address += mode
            mon = poke_data.id_to_mon[data[address]]
            mon = randomize_pokemon(self, mon, mons_list, self.world.randomize_trainer_parties[self.player].value)
            data[address] = poke_data.pokemon_data[mon]["id"]


def process_static_pokemon(self):
    static_slots = [location for location in get_locations(self.player) if location.type in
                    ["Static Pokemon", "Missable Pokemon"]]

    mons_list = [pokemon for pokemon in poke_data.first_stage_pokemon if pokemon not in poke_data.legendary_pokemon]
    for slot in static_slots:
        location = self.world.get_location(slot.name, self.player)
        randomize_type = self.world.randomize_static_pokemon[self.player].value
        slot_type = slot.type.split()[0]
        if not randomize_type:
            location.item = self.create_item(slot_type + " " + slot.original_item)
        else:
            location.item = self.create_item(slot_type + " " +
                                             randomize_pokemon(self, slot.original_item, mons_list, randomize_type))
        location.event = True
        location.locked = True
        location.item.location = location


def process_wild_pokemon(self):

    encounter_slots = get_encounter_slots(self)

    placed_mons = {pokemon: 0 for pokemon in poke_data.pokemon_data.keys()}
    if self.world.randomize_wild_pokemon[self.player].value:
        mons_list = [pokemon for pokemon in poke_data.pokemon_data.keys() if pokemon not in poke_data.legendary_pokemon]
        self.world.random.shuffle(encounter_slots)
        locations = []
        for slot in encounter_slots:
            # if self.world.randomize_wild_pokemon[self.player].value in [1, 3]:
            #     type_mons = [pokemon for pokemon in mons_list if any([poke_data.pokemon_data[slot.original_item][
            #         "type1"] in [self.local_poke_data[pokemon]["type1"], self.local_poke_data[pokemon]["type2"]],
            #         poke_data.pokemon_data[slot.original_item]["type2"] in [self.local_poke_data[pokemon]["type1"],
            #                                                               self.local_poke_data[pokemon]["type2"]]])]
            #     if not type_mons:
            #         type_mons = mons_list.copy()
            #     self.world.random.shuffle(type_mons)
            #     if self.world.randomize_wild_pokemon[self.player].value == 3:
            #         stat_base = get_base_stat_total(slot.original_item)
            #         type_mons.sort(key=lambda mon: abs(get_base_stat_total(mon) - stat_base))
            #     mon = type_mons[round(self.world.random.triangular(0, len(type_mons) - 1, 0))]
            # if self.world.randomize_wild_pokemon[self.player].value == 2:
            #     stat_base = get_base_stat_total(slot.original_item)
            #     mons_list.sort(key=lambda mon: abs(get_base_stat_total(mon) - stat_base))
            #     mon = mons_list[round(self.world.random.triangular(0, 50, 0))]
            # elif self.world.randomize_wild_pokemon[self.player].value == 4:
            #     mon = self.world.random.choice(mons_list)
            mon = randomize_pokemon(self, slot.original_item, mons_list, self.world.randomize_wild_pokemon[self.player].value)
            placed_mons[mon] += 1
            location = self.world.get_location(slot.name, self.player)
            location.item = self.create_item(mon)
            location.event = True
            location.locked = True
            location.item.location = location
            locations.append(location)

        missing_mons = []
        remaining_pokemon = [pokemon for pokemon in poke_data.pokemon_data.keys() if placed_mons[pokemon] == 0 and
                            pokemon not in poke_data.legendary_pokemon]
        if self.world.catch_em_all[self.player].value == 1:
            missing_mons = [pokemon for pokemon in poke_data.first_stage_pokemon if placed_mons[pokemon] == 0 and
                            pokemon not in poke_data.legendary_pokemon]
        elif self.world.catch_em_all[self.player].value == 2:
            missing_mons = missing_mons.copy()
        logic_needed_mons = max(self.world.oaks_aide_rt_2[self.player].value,
                                self.world.oaks_aide_rt_11[self.player].value,
                                self.world.oaks_aide_rt_15[self.player].value)
        if self.world.accessibility[self.player] == "minimal":
            logic_needed_mons = 0

        self.world.random.shuffle(remaining_pokemon)
        while (len([pokemon for pokemon in placed_mons if placed_mons[pokemon] > 0])
               + len(missing_mons) < logic_needed_mons):
            missing_mons.append(remaining_pokemon.pop())
        for mon in missing_mons:
            stat_base = get_base_stat_total(mon)
            candidate_locations = get_encounter_slots(self)
            if self.world.randomize_wild_pokemon[self.player].value in [1, 3]:
                candidate_locations = [slot for slot in candidate_locations if any([poke_data.pokemon_data[slot.original_item][
                    "type1"] in [self.local_poke_data[mon]["type1"], self.local_poke_data[mon]["type2"]],
                    poke_data.pokemon_data[slot.original_item]["type2"] in [self.local_poke_data[mon]["type1"],
                                                                          self.local_poke_data[mon]["type2"]]])]
            if not candidate_locations:
                candidate_locations = get_locations(self.player)
            candidate_locations = [self.world.get_location(location.name, self.player) for location in candidate_locations]
            candidate_locations.sort(key=lambda slot: abs(get_base_stat_total(slot.item.name) - stat_base))
            for location in candidate_locations:
                if placed_mons[location.item.name] > 1 or location.item.name not in poke_data.first_stage_pokemon:
                    placed_mons[location.item.name] -= 1
                    location.item = self.create_item(mon)
                    location.item.location = location
                    placed_mons[mon] += 1
                    break

    else:
        for slot in encounter_slots:
            location = self.world.get_location(slot.name, self.player)
            location.item = self.create_item(slot.original_item)
            location.event = True
            location.locked = True
            location.item.location = location
            placed_mons[location.item.name] += 1


def process_pokemon_data(self):

    local_poke_data = deepcopy(poke_data.pokemon_data)
    learnsets = deepcopy(poke_data.learnsets)

    for mon, mon_data in local_poke_data.items():
        if self.world.randomize_pokemon_stats[self.player].value == 1:
            stats = [mon_data["hp"], mon_data["atk"], mon_data["def"], mon_data["spd"], mon_data["spc"]]
            self.world.random.shuffle(stats)
            mon_data["hp"] = stats[0]
            mon_data["atk"] = stats[1]
            mon_data["def"] = stats[2]
            mon_data["spd"] = stats[3]
            mon_data["spc"] = stats[4]
        elif self.world.randomize_pokemon_stats[self.player].value == 2:
            old_stats = mon_data["hp"] + mon_data["atk"] + mon_data["def"] + mon_data["spd"] + mon_data["spc"]
            stats = [0, 0, 0, 0, 0]
            while old_stats > 0:
                old_stats -= 1
                stats[self.world.random.randint(0, 4)] += 1
            mon_data["hp"] = stats[0]
            mon_data["atk"] = stats[1]
            mon_data["def"] = stats[2]
            mon_data["spd"] = stats[3]
            mon_data["spc"] = stats[4]
        if self.world.randomize_pokemon_types[self.player].value:
            if self.world.randomize_pokemon_types[self.player].value == 1 and mon in poke_data.evolves_from:
                type1 = local_poke_data[poke_data.evolves_from[mon]]["type1"]
                type2 = local_poke_data[poke_data.evolves_from[mon]]["type2"]
                if type1 == type2:
                    if self.world.secondary_type_chance[self.player].value == -1:
                        if mon_data["type1"] != mon_data["type2"]:
                            while type2 == type1:
                                type2 = self.world.random.choice(list(poke_data.type_names.values()))
                    elif self.world.random.randint(1, 100) <= self.world.secondary_type_chance[self.player].value:
                        type2 = self.world.random.choice(list(poke_data.type_names.values()))
            else:
                type1 = self.world.random.choice(list(poke_data.type_names.values()))
                type2 = type1
                if ((self.world.secondary_type_chance[self.player].value == -1 and mon_data["type1"]
                     != mon_data["type2"]) or self.world.random.randint(1, 100)
                        <= self.world.secondary_type_chance[self.player].value):
                    while type2 == type1:
                        type2 = self.world.random.choice(list(poke_data.type_names.values()))

            mon_data["type1"] = type1
            mon_data["type2"] = type2
        if self.world.randomize_pokemon_movesets[self.player].value:
            if self.world.randomize_pokemon_movesets[self.player].value == 1:
                if mon_data["type1"] == "Normal" and mon_data["type2"] == "Normal":
                    chances = [[75, "Normal"]]
                elif mon_data["type1"] == "Normal" or mon_data["type2"] == "Normal":
                    if mon_data["type1"] == "Normal":
                        second_type = mon_data["type2"]
                    else:
                        second_type = mon_data["type1"]
                    chances = [[30, "Normal"], [85, second_type]]
                elif mon_data["type1"] == mon_data["type2"]:
                    chances = [[60, mon_data["type1"]], [80, "Normal"]]
                else:
                    chances = [[50, mon_data["type1"]], [80, mon_data["type2"]], [85, "Normal"]]
            else:
                chances = []
            moves = set(poke_data.moves.keys())
            moves -= set(["No Move"] + poke_data.hm_moves)
            mon_data["start move 1"] = get_move(moves, chances, self.world.random, True)
            for i in range(2, 5):
                if mon_data[f"start move {i}"] != "No Move" or self.world.start_with_four_moves[
                        self.player].value == 1:
                    mon_data[f"start move {i}"] = get_move(moves, chances, self.world.random)
            if mon in learnsets:
                for move_num in range(0, len(learnsets[mon])):
                    learnsets[mon][move_num] = get_move(moves, chances, self.world.random)
        if self.world.randomize_pokemon_catch_rates[self.player].value:
            mon_data["catch rate"] = self.world.random.randint(self.world.minimum_catch_rate[self.player], 255)
        else:
            mon_data["catch rate"] = max(self.world.minimum_catch_rate[self.player], mon_data["catch rate"])

        if mon in poke_data.evolves_from.keys() and mon_data["type1"] == local_poke_data[poke_data.evolves_from[mon]]["type1"] and mon_data["type2"] == local_poke_data[poke_data.evolves_from[mon]]["type2"]:
            mon_data["tms"] = local_poke_data[poke_data.evolves_from[mon]]["tms"]
        elif mon != "Mew":
            tms_hms = poke_data.tm_moves + poke_data.hm_moves
            for flag, tm_move in enumerate(tms_hms):
                if (flag < 50 and self.world.tm_compatibility[self.player].value == 1) or (flag >= 50 and self.world.hm_compatibility[self.player].value == 1):
                    type_match = poke_data.moves[tm_move]["type"] in [mon_data["type1"], mon_data["type2"]]
                    bit = int(self.world.random.randint(1, 100) < [[90, 50, 25], [100, 75, 25]][flag >= 50][0 if type_match else 1 if poke_data.moves[tm_move]["type"] == "Normal" else 2])
                elif (flag < 50 and self.world.tm_compatibility[self.player].value == 2) or (flag >= 50 and self.world.hm_compatibility[self.player].value == 2):
                    bit = [0, 1][self.world.random.randint(0, 1)]
                elif (flag < 50 and self.world.tm_compatibility[self.player].value == 3) or (flag >= 50 and self.world.hm_compatibility[self.player].value == 3):
                    bit = 1
                else:
                    continue
                if bit:
                    mon_data["tms"][int(flag / 8)] |= 1 << (flag % 8)
                else:
                    mon_data["tms"][int(flag / 8)] &= ~(1 << (flag % 8))

    self.local_poke_data = local_poke_data
    self.learnsets = learnsets



def generate_output(self, output_directory: str):
    random = self.world.slot_seeds[self.player]
    game_version = self.world.game_version[self.player].current_key
    data = bytearray(get_base_rom_bytes(game_version))

    for location in self.world.get_locations():
        if location.player != self.player or location.rom_address is None:
            continue
        if location.item.player == self.player:
            if location.rom_address:
                rom_address = location.rom_address
                if not isinstance(rom_address, list):
                    rom_address = [rom_address]
                for address in rom_address:
                    if location.item.name in poke_data.pokemon_data.keys():
                        data[address] = poke_data.pokemon_data[location.item.name]["id"]
                    elif " ".join(location.item.name.split()[1:]) in poke_data.pokemon_data.keys():
                        data[address] = poke_data.pokemon_data[" ".join(location.item.name.split()[1:])]["id"]
                    else:
                        data[address] = self.item_name_to_id[location.item.name] - 172000000

        else:
            data[location.rom_address] = 0x2C  # AP Item
    data[rom_addresses['Fly_Location']] = self.fly_map_code

    # if self.world.goal[self.player].value:
    #     data[rom_addresses['Options']] |= 1
    if self.world.extra_key_items[self.player].value:
        data[rom_addresses['Options']] |= 4
    if self.world.blind_trainers[self.player].value > 0:
        data[rom_addresses['Option_Trainer_Encounters']] = 1
        if self.world.blind_trainers[self.player].value == 2:
            data[rom_addresses['Option_Trainer_Encounters'] + 2] = 0xC0  # ret nz
    data[rom_addresses['Option_Cerulean_Cave_Condition']] = self.world.cerulean_cave_condition[self.player].value
    data[rom_addresses['Option_Encounter_Minimum_Steps']] = self.world.minimum_steps_between_encounters[self.player].value
    data[rom_addresses['Option_Badge_Goal']] = self.world.victory_road_condition[self.player].value - 2
    data[rom_addresses['Option_Viridian_Gym_Badges']] = self.world.victory_road_condition[self.player].value - 1
    data[rom_addresses['Option_EXP_Modifier']] = self.world.exp_modifier[self.player].value
    if not self.world.require_item_finder[self.player].value:
        data[rom_addresses['Option_Itemfinder']] = 0
    if self.world.extra_strength_boulders[self.player].value:
        for i in range(0, 3):
            data[rom_addresses['Option_Boulders'] + (i * 3)] = 0x15
    if self.world.extra_key_items[self.player].value:
        for i in range(0, 4):
            data[rom_addresses['Option_Rock_Tunnel_Extra_Items'] + (i * 3)] = 0x15
    if self.world.old_man[self.player].value == 2:
        data[rom_addresses['Option_Old_Man']] = 0x11
        data[rom_addresses['Option_Old_Man_Lying']] = 0x15
    money = str(self.world.starting_money[self.player].value)
    while len(money) < 6:
        money = "0" + money
    data[rom_addresses["Starting_Money_High"]] = int(money[:2], 16)
    data[rom_addresses["Starting_Money_Middle"]] = int(money[2:4], 16)
    data[rom_addresses["Starting_Money_Low"]] = int(money[4:], 16)
    if self.world.badges_needed_for_hm_moves[self.player].value == 0:
        for hm_move in poke_data.hm_moves:
            write_bytes(data, bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
                        rom_addresses["HM_" + hm_move + "_Badge_a"])
    elif self.extra_badges:
        written_badges = set()
        for hm_move, badge in self.extra_badges.items():
            data[rom_addresses["HM_" + hm_move + "_Badge_b"]] = {"Boulder Badge": 0x47, "Cascade Badge": 0x4F,
                                                                 "Thunder Badge": 0x57, "Rainbow Badge": 0x5F,
                                                                 "Soul Badge": 0x67, "Marsh Badge": 0x6F,
                                                                 "Volcano Badge": 0x77, "Earth Badge": 0x7F}[badge]
            move_text = hm_move
            if badge not in ["Marsh Badge", "Volcano Badge", "Earth Badge"]:
                move_text = ", " + move_text
            write_bytes(data, encode_text(move_text.upper()), rom_addresses["Badge_Text_" + badge.replace(" ", "_")])
            written_badges.update(badge)
        for badge in ["Marsh Badge", "Volcano Badge", "Earth Badge"]:
            if badge not in written_badges:
                write_bytes(data, encode_text("Nothing"), rom_addresses["Badge_Text_" + badge.replace(" ", "_")])

    chart = deepcopy(poke_data.type_chart)
    if self.world.randomize_type_matchup_attacking_types[self.player].value == 1:
        attacking_types = []
        for matchup in chart:
            attacking_types.append(matchup[0])
        self.world.random.shuffle(attacking_types)
        for (matchup, attacking_type) in zip(chart, attacking_types):
            matchup[0] = attacking_type
    elif self.world.randomize_type_matchup_attacking_types[self.player].value == 2:
        for matchup in chart:
            matchup[0] = self.world.random.choice(list(poke_data.type_names.values()))
    if self.world.randomize_type_matchup_defending_types[self.player].value == 1:
        defending_types = []
        for matchup in chart:
            defending_types.append(matchup[1])
        self.world.random.shuffle(defending_types)
        for (matchup, defending_type) in zip(chart, defending_types):
            matchup[1] = defending_type
    elif self.world.randomize_type_matchup_defending_types[self.player].value == 2:
        for matchup in chart:
            matchup[1] = self.world.random.choice(list(poke_data.type_names.values()))
    if self.world.randomize_type_matchup_type_effectiveness[self.player].value == 1:
        effectiveness_list = []
        for matchup in chart:
            effectiveness_list.append(matchup[2])
        self.world.random.shuffle(effectiveness_list)
        for (matchup, effectiveness) in zip(chart, effectiveness_list):
            matchup[2] = effectiveness
    elif self.world.randomize_type_matchup_type_effectiveness[self.player].value == 2:
        for matchup in chart:
            matchup[2] = self.world.random.choice([0] + ([5, 20] * 5))
    elif self.world.randomize_type_matchup_type_effectiveness[self.player].value == 3:
        #data[rom_addresses["Option_Chaos_Types"]] = 1
        for matchup in chart:
            matchup[2] = self.world.random.choice([i for i in range(0, 21) if i != 10])
    type_loc = rom_addresses["Type_Chart"]
    for matchup in chart:
        data[type_loc] = poke_data.type_ids[matchup[0]]
        data[type_loc + 1] = poke_data.type_ids[matchup[1]]
        data[type_loc + 2] = matchup[2]
        type_loc += 3
    self.type_chart = chart

    if self.world.normalize_encounter_chances[self.player].value:
        chances = [25, 51, 77, 103, 129, 155, 180, 205, 230, 255]
        for i, chance in enumerate(chances):
            data[rom_addresses['Encounter_Chances'] + (i * 2)] = chance

    for mon, mon_data in self.local_poke_data.items():
        if mon == "Mew":
            address = rom_addresses["Base_Stats_Mew"]
        else:
            address = rom_addresses["Base_Stats"] + (28 * (mon_data["dex"] - 1))
        data[address + 1] = self.local_poke_data[mon]["hp"]
        data[address + 2] = self.local_poke_data[mon]["atk"]
        data[address + 3] = self.local_poke_data[mon]["def"]
        data[address + 4] = self.local_poke_data[mon]["spd"]
        data[address + 5] = self.local_poke_data[mon]["spc"]
        data[address + 6] = poke_data.type_ids[self.local_poke_data[mon]["type1"]]
        data[address + 7] = poke_data.type_ids[self.local_poke_data[mon]["type2"]]
        data[address + 8] = self.local_poke_data[mon]["catch rate"]
        data[address + 15] = poke_data.moves[self.local_poke_data[mon]["start move 1"]]["id"]
        data[address + 16] = poke_data.moves[self.local_poke_data[mon]["start move 2"]]["id"]
        data[address + 17] = poke_data.moves[self.local_poke_data[mon]["start move 3"]]["id"]
        data[address + 18] = poke_data.moves[self.local_poke_data[mon]["start move 4"]]["id"]
        write_bytes(data, self.local_poke_data[mon]["tms"], address + 20)
        if mon in self.learnsets:
            address = rom_addresses["Learnset_" + mon.replace(" ", "")]
            for i, move in enumerate(self.learnsets[mon]):
                data[(address + 1) + i * 2] = poke_data.moves[move]["id"]

    data[rom_addresses["Option_Aide_Rt2"]] = self.world.oaks_aide_rt_2[self.player]
    data[rom_addresses["Option_Aide_Rt11"]] = self.world.oaks_aide_rt_11[self.player]
    data[rom_addresses["Option_Aide_Rt15"]] = self.world.oaks_aide_rt_15[self.player]

    if self.world.safari_zone_normal_battles[self.player].value == 1:
        data[rom_addresses["Option_Safari_Zone_Battle_Type"]] = 255

    process_trainer_data(self, data)

    mons = [mon["id"] for mon in poke_data.pokemon_data.values()]
    random.shuffle(mons)
    data[rom_addresses['Title_Mon_First']] = mons.pop()
    for mon in range(0, 16):
        data[rom_addresses['Title_Mons'] + mon] = mons.pop()
    write_bytes(data, self.world.seed_name.encode(), 0xFFDC)
    write_bytes(data, encode_text(self.world.seed_name, 20, True), rom_addresses['Title_Seed'])
    write_bytes(data, self.world.player_name[self.player].encode(), 0xFFF0)
    slot_name = self.world.player_name[self.player]
    slot_name.replace("@", " ")
    slot_name.replace("<", " ")
    slot_name.replace(">", " ")
    write_bytes(data, encode_text(slot_name, 16, True, True), rom_addresses['Title_Slot_Name'])
    outfilepname = f'_P{self.player}'
    outfilepname += f"_{self.world.get_file_safe_player_name(self.player).replace(' ', '_')}" \
        if self.world.player_name[self.player] != 'Player%d' % self.player else ''
    rompath = os.path.join(output_directory, f'AP_{self.world.seed_name}{outfilepname}.gb')
    with open(rompath, 'wb') as outfile:
        outfile.write(data)
    if self.world.game_version[self.player].current_key == "red":
        patch = RedDeltaPatch(os.path.splitext(rompath)[0] + RedDeltaPatch.patch_file_ending, player=self.player,
                              player_name=self.world.player_name[self.player], patched_path=rompath)
    else:
        patch = BlueDeltaPatch(os.path.splitext(rompath)[0] + BlueDeltaPatch.patch_file_ending, player=self.player,
                               player_name=self.world.player_name[self.player], patched_path=rompath)

    patch.write()
    os.unlink(rompath)


def write_bytes(data, byte_array, address):
    for byte in byte_array:
        data[address] = byte
        address += 1


def get_base_rom_bytes(game_version: str, hash: str="") -> bytes:
    file_name = get_base_rom_path(game_version)
    base_rom_bytes = bytes(read_rom(open(file_name, "rb")))
    if hash:
        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if hash != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for US(1.0) release. '
                            'Get the correct game and version, then dump it')
    with open(os.path.join(os.path.dirname(__file__), f'basepatch_{game_version}.bsdiff4'), 'rb') as stream:
        base_patch = bytes(stream.read())
    base_rom_bytes = bsdiff4.patch(base_rom_bytes, base_patch)
    return base_rom_bytes


def get_base_rom_path(game_version: str) -> str:
    options = Utils.get_options()
    file_name = options["pkrb_options"][f"{game_version}_rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.local_path(file_name)
    return file_name


class BlueDeltaPatch(APDeltaPatch):
    patch_file_ending = ".apblue"
    hash = "50927e843568814f7ed45ec4f944bd8b"
    game_version = "blue"
    game = "Pokemon Red - Blue"
    result_file_ending = ".gb"
    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes(cls.game_version, cls.hash)


class RedDeltaPatch(APDeltaPatch):
    patch_file_ending = ".apred"
    hash = "3d45c1ee9abd5738df46d2bdda8b57dc"
    game_version = "red"
    game = "Pokemon Red - Blue"
    result_file_ending = ".gb"
    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes(cls.game_version, cls.hash)
