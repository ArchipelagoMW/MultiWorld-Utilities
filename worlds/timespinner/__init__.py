from typing import Dict, List, Set, Tuple, TextIO
from BaseClasses import Item, Tutorial, ItemClassification
from .Items import get_item_names_per_category
from .Items import item_table, starter_melee_weapons, starter_spells, filler_items, starter_progression_items
from .Locations import get_location_datas, EventId
from .Options import TimespinnerOptions
from .PreCalculatedWeights import PreCalculatedWeights
from .Regions import create_regions_and_locations
from worlds.AutoWorld import World, WebWorld

class TimespinnerWebWorld(WebWorld):
    theme = "ice"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Timespinner randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Jarno"]
    )

    setup_de = Tutorial(
        setup.tutorial_name,
        setup.description,
        "Deutsch",
        "setup_de.md",
        "setup/de",
        ["Grrmo", "Fynxes", "Blaze0168"]
    )

    tutorials = [setup, setup_de]

class TimespinnerWorld(World):
    """
    Timespinner is a beautiful metroidvania inspired by classic 90s action-platformers.
    Travel back in time to change fate itself. Join timekeeper Lunais on her quest for revenge against the empire that killed her family.
    """
    options_dataclass = TimespinnerOptions
    options: TimespinnerOptions
    game = "Timespinner"
    topology_present = True
    data_version = 11
    web = TimespinnerWebWorld()
    required_client_version = (0, 3, 7)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {location.name: location.code for location in get_location_datas(-1, None, None)}
    item_name_groups = get_item_names_per_category()

    precalculated_weights: PreCalculatedWeights

    def generate_early(self) -> None:
        self.precalculated_weights = PreCalculatedWeights(self.options, self.random)

        # in generate_early the start_inventory isnt copied over to precollected_items yet, so we can still modify the options directly
        if self.options.start_inventory.value.pop('Meyef', 0) > 0:
            self.options.start_with_meyef.value = self.options.start_with_meyef.option_true
        if self.options.start_inventory.value.pop('Talaria Attachment', 0) > 0:
            self.options.quick_seed.value = self.options.quick_seed.option_true
        if self.options.start_inventory.value.pop('Jewelry Box', 0) > 0:
            self.options.start_with_jewelry_box.value = self.options.start_with_jewelry_box.option_true

    def create_regions(self) -> None: 
        create_regions_and_locations(self.multiworld, self.player, self.options, self.precalculated_weights)

    def create_items(self) -> None: 
        self.create_and_assign_event_items()

        excluded_items: Set[str] = self.get_excluded_items()

        self.assign_starter_items(excluded_items)
        self.place_first_progression_item(excluded_items)

        self.multiworld.itempool += self.get_item_pool(excluded_items)

    def set_rules(self) -> None:
        final_boss: str
        if self.options.dad_percent:
            final_boss = "Killed Emperor"
        else:
            final_boss = "Killed Nightmare"

        self.multiworld.completion_condition[self.player] = lambda state: state.has(final_boss, self.player) 

    def fill_slot_data(self) -> Dict[str, object]:
        return {
            # options
            "StartWithJewelryBox": self.options.start_with_jewelry_box,
            "DownloadableItems": self.options.downloadable_items,
            "EyeSpy": self.options.eye_spy,
            "StartWithMeyef": self.options.start_with_meyef,
            "QuickSeed": self.options.quick_seed,
            "SpecificKeycards": self.options.Specific_keycards,
            "Inverted": self.options.inverted,
            "GyreArchives": self.options.gyre_archives,
            "Cantoran": self.options.cantoran,
            "LoreChecks": self.options.lore_checks,
            "BossRando": self.options.boss_rando,
            "BossScaling": self.options.boss_scaling,
            "DamageRando": self.options.damage_rando,
            "DamageRandoOverrides": self.options.damage_rando_overrides,
            "HpCap": self.options.hp_cap,
            "LevelCap": self.options.level_cap,
            "ExtraEarringsXP": self.options.extra_earrings_xp,
            "BossHealing": self.options.boss_healing,
            "ShopFill": self.options.shop_fill,
            "ShopWarpShards": self.options.shop_warp_shards,
            "ShopMultiplier": self.options.shop_multiplier,
            "LootPool": self.options.loot_pool,
            "DropRateCategory": self.options.drop_rate_category,
            "FixedDropRate": self.options.fixed_drop_rate,
            "LootTierDistro": self.options.loot_tier_distro,
            "ShowBestiary": self.options.show_bestiary,
            "ShowDrops": self.options.show_drops,
            "EnterSandman": self.options.enter_sandman,
            "DadPercent": self.options.dad_percent,
            "RisingTides": self.options.rising_tides,
            "UnchainedKeys": self.options.unchained_keys,
            "Traps": self.options.traps,
            "DeathLink": self.options.death_link,
            "StinkyMaw": True,
            # data
            "PersonalItems": self.get_personal_items(),
            "PyramidKeysGate": self.precalculated_weights.pyramid_keys_unlock,
            "PresentGate": self.precalculated_weights.present_key_unlock,
            "PastGate": self.precalculated_weights.past_key_unlock,
            "TimeGate": self.precalculated_weights.time_key_unlock,
            # rising tides
            "Basement": int(self.precalculated_weights.flood_basement) + \
                                    int(self.precalculated_weights.flood_basement_high),
            "Xarion": self.precalculated_weights.flood_xarion,
            "Maw": self.precalculated_weights.flood_maw,
            "PyramidShaft": self.precalculated_weights.flood_pyramid_shaft,
            "BackPyramid": self.precalculated_weights.flood_pyramid_back,
            "CastleMoat": self.precalculated_weights.flood_moat,
            "CastleCourtyard": self.precalculated_weights.flood_courtyard,
            "LakeDesolation": self.precalculated_weights.flood_lake_desolation,
            "DryLakeSerene": self.precalculated_weights.dry_lake_serene,
        }

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.unchained_keys:
            spoiler_handle.write(f'Modern Warp Beacon unlock:       {self.precalculated_weights.present_key_unlock}\n')
            spoiler_handle.write(f'Timeworn Warp Beacon unlock:     {self.precalculated_weights.past_key_unlock}\n')

            if self.options.enter_sandman:
                spoiler_handle.write(f'Mysterious Warp Beacon unlock:   {self.precalculated_weights.time_key_unlock}\n')
        else:
            spoiler_handle.write(f'Twin Pyramid Keys unlock:        {self.precalculated_weights.pyramid_keys_unlock}\n')
       
        if self.options.rising_tides:
            flooded_areas: List[str] = []

            if self.precalculated_weights.flood_basement:
                if self.precalculated_weights.flood_basement_high:
                    flooded_areas.append("Castle Basement")
                else:
                    flooded_areas.append("Castle Basement (Savepoint available)")
            if self.precalculated_weights.flood_xarion:
                flooded_areas.append("Xarion (boss)")
            if self.precalculated_weights.flood_maw:
                flooded_areas.append("Maw (caves + boss)")
            if self.precalculated_weights.flood_pyramid_shaft:
                flooded_areas.append("Ancient Pyramid Shaft")
            if self.precalculated_weights.flood_pyramid_back:
                flooded_areas.append("Sandman\\Nightmare (boss)")
            if self.precalculated_weights.flood_moat:
                flooded_areas.append("Castle Ramparts Moat")
            if self.precalculated_weights.flood_courtyard:
                flooded_areas.append("Castle Courtyard")
            if self.precalculated_weights.flood_lake_desolation:
                flooded_areas.append("Lake Desolation")
            if not self.precalculated_weights.dry_lake_serene:
                flooded_areas.append("Lake Serene")

            if len(flooded_areas) == 0:
                flooded_areas_string: str = "None"
            else:
                flooded_areas_string: str = ", ".join(flooded_areas)

            spoiler_handle.write(f'Flooded Areas:                   {flooded_areas_string}\n')

    def create_item(self, name: str) -> Item:
        data = item_table[name]

        if data.useful:
            classification = ItemClassification.useful
        elif data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
            
        item = Item(name, classification, data.code, self.player)

        if not item.advancement:
            return item

        if (name == 'Tablet' or name == 'Library Keycard V') and not self.options.downloadable_items:
            item.classification = ItemClassification.filler
        elif name == 'Oculus Ring' and not self.options.eye_spy:
            item.classification = ItemClassification.filler
        elif (name == 'Kobo' or name == 'Merchant Crow') and not self.options.gyre_archives:
            item.classification = ItemClassification.filler
        elif name in {"Timeworn Warp Beacon", "Modern Warp Beacon", "Mysterious Warp Beacon"} \
                and not self.options.unchained_keys:
            item.classification = ItemClassification.filler

        return item

    def get_filler_item_name(self) -> str:
        trap_chance: int = self.options.trap_chance.value
        enabled_traps: List[str] = self.options.traps.value

        if self.random.random() < (trap_chance / 100) and enabled_traps:
            return self.random.choice(enabled_traps)
        else:
            return self.random.choice(filler_items) 

    def get_excluded_items(self) -> Set[str]:
        excluded_items: Set[str] = set()

        if self.options.start_with_jewelry_box:
            excluded_items.add('Jewelry Box')
        if self.options.start_with_meyef:
            excluded_items.add('Meyef')
        if self.options.quick_seed:
            excluded_items.add('Talaria Attachment')

        if self.options.unchained_keys:
            excluded_items.add('Twin Pyramid Key')

            if not self.options.enter_sandman:
                excluded_items.add('Mysterious Warp Beacon')
        else:
            excluded_items.add('Timeworn Warp Beacon')
            excluded_items.add('Modern Warp Beacon')
            excluded_items.add('Mysterious Warp Beacon')

        for item in self.multiworld.precollected_items[self.player]:
            if item.name not in self.item_name_groups['UseItem']:
                excluded_items.add(item.name)

        return excluded_items

    def assign_starter_items(self, excluded_items: Set[str]) -> None:
        non_local_items: Set[str] = self.multiworld.non_local_items[self.player].value

        local_starter_melee_weapons = tuple(item for item in starter_melee_weapons if item not in non_local_items)
        if not local_starter_melee_weapons:
            if 'Plasma Orb' in non_local_items:
                raise Exception("Atleast one melee orb must be local")
            else:
                local_starter_melee_weapons = ('Plasma Orb',)

        local_starter_spells = tuple(item for item in starter_spells if item not in non_local_items)
        if not local_starter_spells:
            if 'Lightwall' in non_local_items:
                raise Exception("Atleast one spell must be local")
            else:
                local_starter_spells = ('Lightwall',)

        self.assign_starter_item(excluded_items, 'Tutorial: Yo Momma 1', local_starter_melee_weapons)
        self.assign_starter_item(excluded_items, 'Tutorial: Yo Momma 2', local_starter_spells)

    def assign_starter_item(self, excluded_items: Set[str], location: str, item_list: Tuple[str, ...]) -> None:
        item_name = self.multiworld.random.choice(item_list)

        self.place_locked_item(excluded_items, location, item_name)

    def place_first_progression_item(self, excluded_items: Set[str]) -> None:
        if self.options.quick_seed or self.options.inverted or self.precalculated_weights.flood_lake_desolation:
            return

        for item in self.multiworld.precollected_items[self.player]:
            if item.name in starter_progression_items and not item.name in excluded_items:
                return

        local_starter_progression_items = tuple(
            item for item in starter_progression_items 
                if item not in excluded_items and item not in self.multiworld.non_local_items[self.player].value)

        if not local_starter_progression_items:
            return

        progression_item = self.random.choice(local_starter_progression_items)

        self.multiworld.local_early_items[self.player][progression_item] = 1

    def place_locked_item(self, excluded_items: Set[str], location: str, item: str) -> None:
        excluded_items.add(item)

        item = self.create_item(item)

        self.multiworld.get_location(location, self.player).place_locked_item(item)

    def get_item_pool(self, excluded_items: Set[str]) -> List[Item]:
        pool: List[Item] = []

        for name, data in item_table.items():
            if name not in excluded_items:
                for _ in range(data.count):
                    item = self.create_item(name)
                    pool.append(item)

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)):
            item = self.create_item(self.get_filler_item_name())
            pool.append(item)

        return pool

    def create_and_assign_event_items(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            if location.address == EventId:
                item = Item(location.name, ItemClassification.progression, EventId, self.player)
                location.place_locked_item(item)

    def get_personal_items(self) -> Dict[int, int]:
        personal_items: Dict[int, int] = {}

        for location in self.multiworld.get_locations(self.player):
            if location.address and location.item and location.item.code and location.item.player == self.player:
                personal_items[location.address] = location.item.code

        return personal_items