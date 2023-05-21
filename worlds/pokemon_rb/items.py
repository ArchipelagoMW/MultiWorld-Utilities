from BaseClasses import ItemClassification
from .poke_data import pokemon_data

class ItemData:
    def __init__(self, id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if id is None else id + 172000000

item_table = {
    "Master Ball": ItemData(1, ItemClassification.useful, ["Consumables", "Poke Balls"]),
    "Ultra Ball": ItemData(2, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Great Ball": ItemData(3, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Poke Ball": ItemData(4, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    "Town Map": ItemData(5, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    "Bicycle": ItemData(6, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Flippers": ItemData(7, ItemClassification.progression),
    #"Safari Ball": ItemData(8, ItemClassification.filler),
    "Pokedex": ItemData(9, ItemClassification.progression, []), # ["Unique", "Key Items"]),
    "Moon Stone": ItemData(10, ItemClassification.useful, ["Unique", "Evolution Stones"]),
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
    "Old Amber": ItemData(31, ItemClassification.progression_skip_balancing, ["Unique", "Fossils"]),
    "Fire Stone": ItemData(32, ItemClassification.useful, ["Unique", "Evolution Stones"]),
    "Thunder Stone": ItemData(33, ItemClassification.useful, ["Unique", "Evolution Stones"]),
    "Water Stone": ItemData(34, ItemClassification.useful, ["Unique", "Evolution Stones"]),
    "HP Up": ItemData(35, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Protein": ItemData(36, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Iron": ItemData(37, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Carbos": ItemData(38, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Calcium": ItemData(39, ItemClassification.filler, ["Consumables", "Vitamins"]),
    "Rare Candy": ItemData(40, ItemClassification.useful, ["Consumables"]),
    "Dome Fossil": ItemData(41, ItemClassification.progression_skip_balancing, ["Unique", "Fossils"]),
    "Helix Fossil": ItemData(42, ItemClassification.progression_skip_balancing, ["Unique", "Fossils"]),
    "Secret Key": ItemData(43, ItemClassification.progression, ["Unique", "Key Items"]),
    "Bike Voucher": ItemData(45, ItemClassification.progression, ["Unique", "Key Items"]),
    "X Accuracy": ItemData(46, ItemClassification.filler, ["Consumables", "Battle Items"]),
    "Leaf Stone": ItemData(47, ItemClassification.useful, ["Unique", "Evolution Stones"]),
    "Card Key": ItemData(48, ItemClassification.progression, []), #, ["Unique", "Key Items"]),
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
    "Coin Case": ItemData(69, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    "Oak's Parcel": ItemData(70, ItemClassification.progression, ["Unique", "Key Items"]),
    "Item Finder": ItemData(71, ItemClassification.progression, ["Unique", "Key Items"]),
    "Silph Scope": ItemData(72, ItemClassification.progression, ["Unique", "Key Items"]),
    "Poke Flute": ItemData(73, ItemClassification.progression, ["Unique", "Key Items"]),
    "Lift Key": ItemData(74, ItemClassification.progression, ["Unique", "Key Items"]),
    "Exp. All": ItemData(75, ItemClassification.useful, ["Unique"]),
    "Old Rod": ItemData(76, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "Good Rod": ItemData(77, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "Super Rod": ItemData(78, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    "PP Up": ItemData(79, ItemClassification.filler, ["Consumables"]),
    "Ether": ItemData(80, ItemClassification.filler, ["Consumables"]),
    "Max Ether": ItemData(81, ItemClassification.filler, ["Consumables"]),
    "Elixir": ItemData(82, ItemClassification.filler, ["Consumables"]),
    "Max Elixir": ItemData(83, ItemClassification.filler, ["Consumables"]),
    "Tea": ItemData(84, ItemClassification.progression, []), #["Unique", "Key Items"]),
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
    "Card Key 2F": ItemData(100, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 3F": ItemData(101, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 4F": ItemData(102, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 5F": ItemData(103, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 6F": ItemData(104, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 7F": ItemData(105, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 8F": ItemData(106, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 9F": ItemData(107, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 10F": ItemData(108, ItemClassification.progression, ["Unique", "Key Items"]),
    "Card Key 11F": ItemData(109, ItemClassification.progression, ["Unique", "Key Items"]),
    "HM01 Cut": ItemData(196, ItemClassification.progression, ["Unique", "HMs"]),
    "HM02 Fly": ItemData(197, ItemClassification.progression, ["Unique", "HMs"]),
    "HM03 Surf": ItemData(198, ItemClassification.progression, ["Unique", "HMs"]),
    "HM04 Strength": ItemData(199, ItemClassification.progression, ["Unique", "HMs"]),
    "HM05 Flash": ItemData(200, ItemClassification.progression, ["Unique", "HMs"]),
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

    "Vending Machine Drinks": ItemData(None, ItemClassification.progression, []),
    "Visit Bill": ItemData(None, ItemClassification.progression, []),
    "Defeat Brock": ItemData(None, ItemClassification.progression, []),
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