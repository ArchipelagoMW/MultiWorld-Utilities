from BaseClasses import ItemClassification
from .poke_data import pokemon_data
from .locations import location_data
from copy import deepcopy


class ItemData:
    def __init__(self, item_id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if item_id is None else item_id + 172000000


item_table = {
    "Master Ball": ItemData(1, ItemClassification.useful, ["Consumables", "Poke Balls"]),
    "Ultra Ball": ItemData(2, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Great Ball": ItemData(3, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Poke Ball": ItemData(4, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Town Map": ItemData(5, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    "Bicycle": ItemData(6, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Flippers": ItemData(7, ItemClassification.progression),
    # "Safari Ball": ItemData(8, ItemClassification.filler),
    "Pokedex": ItemData(9, ItemClassification.progression, ["Unique", "Key Items"]),
    "Moon Stone": ItemData(10, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    "Antidote": ItemData(11, ItemClassification.filler, ["Consumables"]),
    "Burn Heal": ItemData(12, ItemClassification.filler, ["Consumables"]),
    "Ice Heal": ItemData(13, ItemClassification.filler, ["Consumables"]),
    "Awakening": ItemData(14, ItemClassification.filler, ["Consumables"]),
    "Paralyze Heal": ItemData(15, ItemClassification.filler, ["Consumables"]),
    "Full Restore": ItemData(16, ItemClassification.filler, ["Consumables"]),
    "Max Potion": ItemData(17, ItemClassification.filler, ["Consumables"]),
    "Hyper Potion": ItemData(18, ItemClassification.filler, ["Consumables"]),
    "Super Potion": ItemData(19, ItemClassification.filler, ["Consumables"]),
    "Potion": ItemData(20, ItemClassification.filler, ["Consumables"]),
    "Boulder Badge": ItemData(21, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Cascade Badge": ItemData(22, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Thunder Badge": ItemData(23, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Rainbow Badge": ItemData(24, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Soul Badge": ItemData(25, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Marsh Badge": ItemData(26, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Volcano Badge": ItemData(27, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Earth Badge": ItemData(28, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    "Escape Rope": ItemData(29, ItemClassification.filler, ["Consumables"]),
    "Repel": ItemData(30, ItemClassification.filler, ["Consumables"]),
    "Old Amber": ItemData(31, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    "Fire Stone": ItemData(32, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    "Thunder Stone": ItemData(33, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones" "Key Items"]),
    "Water Stone": ItemData(34, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    "HP Up": ItemData(35, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Protein": ItemData(36, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Iron": ItemData(37, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Carbos": ItemData(38, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Calcium": ItemData(39, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Rare Candy": ItemData(40, ItemClassification.filler, ["Consumables"]),
    "Dome Fossil": ItemData(41, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    "Helix Fossil": ItemData(42, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    "Secret Key": ItemData(43, ItemClassification.progression, ["Unique", "Key Items"]),
    "Bike Voucher": ItemData(45, ItemClassification.progression, ["Unique", "Key Items"]),
    "X Accuracy": ItemData(46, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "Leaf Stone": ItemData(47, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    "Card Key": ItemData(48, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Nugget": ItemData(49, ItemClassification.filler, []),
    #"Laptop": ItemData(50, ItemClassification.useful, ["Unique"]),
    "Poke Doll": ItemData(51, ItemClassification.filler, ["Consumables"]),
    "Full Heal": ItemData(52, ItemClassification.filler, ["Consumables"]),
    "Revive": ItemData(53, ItemClassification.filler, ["Consumables"]),
    "Max Revive": ItemData(54, ItemClassification.filler, ["Consumables"]),
    "Guard Spec": ItemData(55, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "Super Repel": ItemData(56, ItemClassification.filler, ["Consumables"]),
    "Max Repel": ItemData(57, ItemClassification.filler, ["Consumables"]),
    "Dire Hit": ItemData(58, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "10 Coins": ItemData(59, ItemClassification.filler, ["Coins"]),
    "Fresh Water": ItemData(60, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    "Soda Pop": ItemData(61, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    "Lemonade": ItemData(62, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    "S.S. Ticket": ItemData(63, ItemClassification.progression, ["Unique", "Key Items"]),
    "Gold Teeth": ItemData(64, ItemClassification.progression, ["Unique", "Key Items"]),
    "X Attack": ItemData(65, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "X Defend": ItemData(66, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "X Speed": ItemData(67, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "X Special": ItemData(68, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "Coin Case": ItemData(69, ItemClassification.progression, ["Unique", "Key Items"]),
    "Oak's Parcel": ItemData(70, ItemClassification.progression, ["Unique", "Key Items"]),
    "Item Finder": ItemData(71, ItemClassification.progression, ["Unique", "Key Items"]),
    "Silph Scope": ItemData(72, ItemClassification.progression, ["Unique", "Key Items"]),
    "Poke Flute": ItemData(73, ItemClassification.progression, ["Unique", "Key Items"]),
    "Lift Key": ItemData(74, ItemClassification.progression, ["Unique", "Key Items"]),
    "Exp. All": ItemData(75, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    "Old Rod": ItemData(76, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "Good Rod": ItemData(77, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "Super Rod": ItemData(78, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "PP Up": ItemData(79, ItemClassification.filler, ["Consumables"]),
    "Ether": ItemData(80, ItemClassification.filler, ["Consumables"]),
    "Max Ether": ItemData(81, ItemClassification.filler, ["Consumables"]),
    "Elixir": ItemData(82, ItemClassification.filler, ["Consumables"]),
    "Max Elixir": ItemData(83, ItemClassification.filler, ["Consumables"]),
    "Tea": ItemData(84, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Master Sword": ItemData(85, ItemClassification.progression),
    # "Flute": ItemData(86, ItemClassification.progression),
    # "Titan's Mitt": ItemData(87, ItemClassification.progression),
    # "Lamp": ItemData(88, ItemClassification.progression),
    "Plant Key": ItemData(89, ItemClassification.progression, ["Unique", "Key Items"]),
    "Mansion Key": ItemData(90, ItemClassification.progression, ["Unique", "Key Items"]),
    "Hideout Key": ItemData(91, ItemClassification.progression, ["Unique", "Key Items"]),
    "Safari Pass": ItemData(93, ItemClassification.progression, ["Unique", "Key Items"]),
    "Poison Trap": ItemData(94, ItemClassification.trap, ["Traps"]),
    "Paralyze Trap": ItemData(95, ItemClassification.trap, ["Traps"]),
    "Ice Trap": ItemData(96, ItemClassification.trap, ["Traps"]),
    "Fire Trap": ItemData(97, ItemClassification.trap, ["Traps"]),
    "20 Coins": ItemData(98, ItemClassification.filler, ["Coins"]),
    "100 Coins": ItemData(99, ItemClassification.filler, ["Coins"]),
    "Card Key 2F": ItemData(100, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 3F": ItemData(101, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 4F": ItemData(102, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 5F": ItemData(103, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 6F": ItemData(104, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 7F": ItemData(105, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 8F": ItemData(106, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 9F": ItemData(107, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 10F": ItemData(108, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Card Key 11F": ItemData(109, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Progressive Card Key": ItemData(110, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    "Sleep Trap": ItemData(111, ItemClassification.trap, ["Traps"]),
    "HM01 Cut": ItemData(196, ItemClassification.progression, ["Unique", "HMs", "Key Items"]),
    "HM02 Fly": ItemData(197, ItemClassification.progression, ["Unique", "HMs", "Key Items"]),
    "HM03 Surf": ItemData(198, ItemClassification.progression, ["Unique", "HMs", "Key Items"]),
    "HM04 Strength": ItemData(199, ItemClassification.progression, ["Unique", "HMs", "Key Items"]),
    "HM05 Flash": ItemData(200, ItemClassification.progression, ["Unique", "HMs", "Key Items"]),
    "TM01 Mega Punch": ItemData(201, ItemClassification.useful, ["Unique", "TMs"]),
    "TM02 Razor Wind": ItemData(202, ItemClassification.filler, ["Unique", "TMs"]),
    "TM03 Swords Dance": ItemData(203, ItemClassification.useful, ["Unique", "TMs"]),
    "TM04 Whirlwind": ItemData(204, ItemClassification.filler, ["Unique", "TMs"]),
    "TM05 Mega Kick": ItemData(205, ItemClassification.useful, ["Unique", "TMs"]),
    "TM06 Toxic": ItemData(206, ItemClassification.useful, ["Unique", "TMs"]),
    "TM07 Horn Drill": ItemData(207, ItemClassification.useful, ["Unique", "TMs"]),
    "TM08 Body Slam": ItemData(208, ItemClassification.useful, ["Unique", "TMs"]),
    "TM09 Take Down": ItemData(209, ItemClassification.useful, ["Unique", "TMs"]),
    "TM10 Double Edge": ItemData(210, ItemClassification.useful, ["Unique", "TMs"]),
    "TM11 Bubble Beam": ItemData(211, ItemClassification.useful, ["Unique", "TMs"]),
    "TM12 Water Gun": ItemData(212, ItemClassification.filler, ["Unique", "TMs"]),
    "TM13 Ice Beam": ItemData(213, ItemClassification.useful, ["Unique", "TMs"]),
    "TM14 Blizzard": ItemData(214, ItemClassification.useful, ["Unique", "TMs"]),
    "TM15 Hyper Beam": ItemData(215, ItemClassification.useful, ["Unique", "TMs"]),
    "TM16 Pay Day": ItemData(216, ItemClassification.useful, ["Unique", "TMs"]),
    "TM17 Submission": ItemData(217, ItemClassification.useful, ["Unique", "TMs"]),
    "TM18 Counter": ItemData(218, ItemClassification.filler, ["Unique", "TMs"]),
    "TM19 Seismic Toss": ItemData(219, ItemClassification.useful, ["Unique", "TMs"]),
    "TM20 Rage": ItemData(220, ItemClassification.useful, ["Unique", "TMs"]),
    "TM21 Mega Drain": ItemData(221, ItemClassification.useful, ["Unique", "TMs"]),
    "TM22 Solar Beam": ItemData(222, ItemClassification.useful, ["Unique", "TMs"]),
    "TM23 Dragon Rage": ItemData(223, ItemClassification.useful, ["Unique", "TMs"]),
    "TM24 Thunderbolt": ItemData(224, ItemClassification.useful, ["Unique", "TMs"]),
    "TM25 Thunder": ItemData(225, ItemClassification.useful, ["Unique", "TMs"]),
    "TM26 Earthquake": ItemData(226, ItemClassification.useful, ["Unique", "TMs"]),
    "TM27 Fissure": ItemData(227, ItemClassification.useful, ["Unique", "TMs"]),
    "TM28 Dig": ItemData(228, ItemClassification.useful, ["Unique", "TMs"]),
    "TM29 Psychic": ItemData(229, ItemClassification.useful, ["Unique", "TMs"]),
    "TM30 Teleport": ItemData(230, ItemClassification.filler, ["Unique", "TMs"]),
    "TM31 Mimic": ItemData(231, ItemClassification.useful, ["Unique", "TMs"]),
    "TM32 Double Team": ItemData(232, ItemClassification.useful, ["Unique", "TMs"]),
    "TM33 Reflect": ItemData(233, ItemClassification.useful, ["Unique", "TMs"]),
    "TM34 Bide": ItemData(234, ItemClassification.filler, ["Unique", "TMs"]),
    "TM35 Metronome": ItemData(235, ItemClassification.useful, ["Unique", "TMs"]),
    "TM36 Self-Destruct": ItemData(236, ItemClassification.useful, ["Unique", "TMs"]),
    "TM37 Egg Bomb": ItemData(237, ItemClassification.useful, ["Unique", "TMs"]),
    "TM38 Fire Blast": ItemData(238, ItemClassification.useful, ["Unique", "TMs"]),
    "TM39 Swift": ItemData(239, ItemClassification.useful, ["Unique", "TMs"]),
    "TM40 Skull Bash": ItemData(240, ItemClassification.filler, ["Unique", "TMs"]),
    "TM41 Soft-Boiled": ItemData(241, ItemClassification.useful, ["Unique", "TMs"]),
    "TM42 Dream Eater": ItemData(242, ItemClassification.useful, ["Unique", "TMs"]),
    "TM43 Sky Attack": ItemData(243, ItemClassification.filler, ["Unique", "TMs"]),
    "TM44 Rest": ItemData(244, ItemClassification.useful, ["Unique", "TMs"]),
    "TM45 Thunder Wave": ItemData(245, ItemClassification.useful, ["Unique", "TMs"]),
    "TM46 Psywave": ItemData(246, ItemClassification.filler, ["Unique", "TMs"]),
    "TM47 Explosion": ItemData(247, ItemClassification.useful, ["Unique", "TMs"]),
    "TM48 Rock Slide": ItemData(248, ItemClassification.useful, ["Unique", "TMs"]),
    "TM49 Tri Attack": ItemData(249, ItemClassification.useful, ["Unique", "TMs"]),
    "TM50 Substitute": ItemData(250, ItemClassification.useful, ["Unique", "TMs"]),

    "Game Corner": ItemData(None, ItemClassification.progression, []),
    "Cinnabar Island": ItemData(None, ItemClassification.progression, []),
    "Buy Poke Doll": ItemData(None, ItemClassification.progression, []),
    "Vending Machine Drinks": ItemData(None, ItemClassification.progression, []),
    "Help Bill": ItemData(None, ItemClassification.progression, []),
    "Defeat Brock": ItemData(None, ItemClassification.progression, []),
    "Defeat Misty": ItemData(None, ItemClassification.progression, []),
    "Defeat Lt. Surge": ItemData(None, ItemClassification.progression, []),
    "Defeat Erika": ItemData(None, ItemClassification.progression, []),
    "Defeat Koga": ItemData(None, ItemClassification.progression, []),
    "Defeat Blaine": ItemData(None, ItemClassification.progression, []),
    "Defeat Sabrina": ItemData(None, ItemClassification.progression, []),
    "Defeat Viridian Gym Giovanni": ItemData(None, ItemClassification.progression, []),
    "Seafoam Exit Boulder": ItemData(None, ItemClassification.progression, []),
    "Seafoam Boss Boulders": ItemData(None, ItemClassification.progression, []),
    "Victory Road Boulder": ItemData(None, ItemClassification.progression, []),
    "Fuji Saved": ItemData(None, ItemClassification.progression, []),
    "Silph Co Liberated": ItemData(None, ItemClassification.progression, []),
    "Become Champion": ItemData(None, ItemClassification.progression, []),

    "Trainer Parties": ItemData(None, ItemClassification.filler, [])
}

item_table.update({f"TM{str(i).zfill(2)}": ItemData(i + 456, ItemClassification.filler, ["Unique", "TMs"])
                   for i in range(1, 51)})

item_table.update(
    {pokemon: ItemData(None, ItemClassification.progression, []) for pokemon in pokemon_data.keys()}
)
item_table.update(
    {f"Missable {pokemon}": ItemData(None, ItemClassification.useful, []) for pokemon in pokemon_data.keys()}
)
item_table.update(
    {f"Static {pokemon}": ItemData(None, ItemClassification.progression, []) for pokemon in pokemon_data.keys()}
)


item_groups = {}
for item, data in item_table.items():
    for group in data.groups:
        item_groups[group] = item_groups.get(group, []) + [item]


def generate_items(self) -> None:
    start_inventory = self.multiworld.start_inventory[self.player].value.copy()
    if self.multiworld.randomize_pokedex[self.player] == "start_with":
        start_inventory["Pokedex"] = 1
        self.multiworld.push_precollected(self.create_item("Pokedex"))
    if self.multiworld.exp_all[self.player] == "start_with":
        start_inventory["Exp. All"] = 1
        self.multiworld.push_precollected(self.create_item("Exp. All"))

    locations = [location for location in location_data if location.type in ("Item", "Trainer Parties")]
    self.item_pool = []
    combined_traps = (self.multiworld.poison_trap_weight[self.player].value
                      + self.multiworld.fire_trap_weight[self.player].value
                      + self.multiworld.paralyze_trap_weight[self.player].value
                      + self.multiworld.ice_trap_weight[self.player].value)
    stones = ["Moon Stone", "Fire Stone", "Water Stone", "Thunder Stone", "Leaf Stone"]
    for location in locations:
        event = location.event
        if not location.inclusion(self.multiworld, self.player):
            continue

        if location.original_item is None:
            item = self.create_filler()
        elif location.original_item == "Exp. All" and self.multiworld.exp_all[self.player] == "remove":
            item = self.create_filler()
        elif location.original_item == "Pokedex":
            if self.multiworld.randomize_pokedex[self.player] == "vanilla":
                self.multiworld.get_location(location.name, self.player).event = True
                event = True
            item = self.create_item("Pokedex")
        elif location.original_item == "Moon Stone" and self.multiworld.stonesanity[self.player]:
            stone = stones.pop()
            item = self.create_item(stone)
        elif location.original_item.startswith("TM"):
            if self.multiworld.randomize_tm_moves[self.player]:
                item = self.create_item(location.original_item.split(" ")[0])
            else:
                item = self.create_item(location.original_item)
        elif location.original_item == "Card Key" and self.multiworld.split_card_key[self.player] == "on":
            item = self.create_item("Card Key 3F")
        elif "Card Key" in location.original_item and self.multiworld.split_card_key[self.player] == "progressive":
            item = self.create_item("Progressive Card Key")
        else:
            item = self.create_item(location.original_item)
            if (item.classification == ItemClassification.filler and self.multiworld.random.randint(1, 100)
                    <= self.multiworld.trap_percentage[self.player].value and combined_traps != 0):
                item = self.create_item(self.select_trap())

        if self.multiworld.key_items_only[self.player] and (not location.event) and (not item.advancement):
            continue

        if item.name in start_inventory and start_inventory[item.name] > 0 and \
                location.original_item in item_groups["Unique"]:
            start_inventory[location.original_item] -= 1
            item = self.create_filler()

        if event:
            loc = self.multiworld.get_location(location.name, self.player)
            loc.place_locked_item(item)
            if location.type == "Trainer Parties":
                # loc.item.classification = ItemClassification.filler
                loc.party_data = deepcopy(location.party_data)
        else:
            self.item_pool.append(item)

    self.multiworld.random.shuffle(self.item_pool)
    advancement_items = [item.name for item in self.item_pool if item.advancement] \
                        + [item.name for item in self.multiworld.precollected_items[self.player] if
                           item.advancement]
    self.total_key_items = len(
        # The stonesanity items are not checekd for here and instead just always added as the `+ 4`
        # They will always exist, but if stonesanity is off, then only as events.
        # We don't want to just add 4 if stonesanity is off while still putting them in this list in case
        # the player puts stones in their start inventory, in which case they would be double-counted here.
        [item for item in ["Bicycle", "Silph Scope", "Item Finder", "Super Rod", "Good Rod",
                           "Old Rod", "Lift Key", "Card Key", "Town Map", "Coin Case", "S.S. Ticket",
                           "Secret Key", "Poke Flute", "Mansion Key", "Safari Pass", "Plant Key",
                           "Hideout Key", "Card Key 2F", "Card Key 3F", "Card Key 4F", "Card Key 5F",
                           "Card Key 6F", "Card Key 7F", "Card Key 8F", "Card Key 9F", "Card Key 10F",
                           "Card Key 11F", "Exp. All", "Moon Stone"] if item in advancement_items]) + 4
    if "Progressive Card Key" in advancement_items:
        self.total_key_items += 10

    self.multiworld.cerulean_cave_key_items_condition[self.player].total = int((self.total_key_items / 100)
                                                                               *
                                                                               self.multiworld.cerulean_cave_key_items_condition[
                                                                                   self.player].value)

    self.multiworld.elite_four_key_items_condition[self.player].total = int((self.total_key_items / 100)
                                                                            *
                                                                            self.multiworld.elite_four_key_items_condition[
                                                                                self.player].value)
