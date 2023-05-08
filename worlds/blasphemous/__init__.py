from typing import Dict, Set, Any
from collections import Counter
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Items import base_id, item_table, group_table, tears_set, reliquary_set
from .Locations import location_table
from .Rooms import room_table, door_table
from .Rules import rules
from worlds.generic.Rules import set_rule, add_rule
from .Options import blasphemous_options
from . import Vanilla


class BlasphemousWeb(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Blasphemous randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TRPG"]
    )]


class BlasphemousWorld(World):
    """
    Blasphemous is a challenging Metroidvania set in the cursed land of Cvstodia. Play as the Penitent One, trapped
    in an endless cycle of death and rebirth, and free the world from it's terrible fate in your quest to break
    your eternal damnation!
    """

    game: str = "Blasphemous"
    web = BlasphemousWeb()
    data_version = 1

    item_name_to_id = {item["name"]: (base_id + index) for index, item in enumerate(item_table)}
    location_name_to_id = {loc["name"]: (base_id + index) for index, loc in enumerate(location_table)}
    location_name_to_game_id = {loc["name"]: loc["game_id"] for loc in location_table}

    item_name_groups = group_table
    option_definitions = blasphemous_options


    #def set_rules(self):
        #rules(self)


    def create_item(self, name: str) -> "BlasphemousItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id

        return BlasphemousItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return BlasphemousItem(event, ItemClassification.progression_skip_balancing, None, self.player)


    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(tears_set)


    def create_items(self):
        placed_items = []

        placed_items.extend(Vanilla.unrandomized_dict.values())

        if not self.multiworld.reliquary_shuffle[self.player]:
            placed_items.extend(reliquary_set)
        elif self.multiworld.reliquary_shuffle[self.player]:
            placed_items.append("Tears of Atonement (250)")
            placed_items.append("Tears of Atonement (300)")
            placed_items.append("Tears of Atonement (500)")

        if not self.multiworld.cherub_shuffle[self.player]:
            for i in range(38):
                placed_items.append("Child of Moonlight")

        if not self.multiworld.life_shuffle[self.player]:
            for i in range(6):
                placed_items.append("Life Upgrade")

        if not self.multiworld.fervour_shuffle[self.player]:
            for i in range(6):
                placed_items.append("Fervour Upgrade")

        if not self.multiworld.sword_shuffle[self.player]:
            for i in range(7):
                placed_items.append("Mea Culpa Upgrade")

        if not self.multiworld.blessing_shuffle[self.player]:
            placed_items.extend(Vanilla.blessing_dict.values())

        if not self.multiworld.dungeon_shuffle[self.player]:
            placed_items.extend(Vanilla.dungeon_dict.values())

        if not self.multiworld.tirso_shuffle[self.player]:
            placed_items.extend(Vanilla.tirso_dict.values())

        if not self.multiworld.miriam_shuffle[self.player]:
            placed_items.append("Cantina of the Blue Rose")

        if not self.multiworld.redento_shuffle[self.player]:
            placed_items.extend(Vanilla.redento_dict.values())

        if not self.multiworld.jocinero_shuffle[self.player]:
            placed_items.extend(Vanilla.jocinero_dict.values())
        
        if not self.multiworld.altasgracias_shuffle[self.player]:
            placed_items.extend(Vanilla.altasgracias_dict.values())

        if not self.multiworld.tentudia_shuffle[self.player]:
            placed_items.extend(Vanilla.tentudia_dict.values())

        if not self.multiworld.gemino_shuffle[self.player]:
            placed_items.extend(Vanilla.gemino_dict.values())

        if not self.multiworld.guilt_shuffle[self.player]:
            placed_items.append("Weight of True Guilt")

        if not self.multiworld.ossuary_shuffle[self.player]:
            placed_items.extend(Vanilla.ossuary_dict.values())

        if not self.multiworld.boss_shuffle[self.player]:
            placed_items.extend(Vanilla.boss_dict.values())

        if not self.multiworld.wound_shuffle[self.player]:
            placed_items.extend(Vanilla.wound_dict.values())

        if not self.multiworld.mask_shuffle[self.player]:
            placed_items.extend(Vanilla.mask_dict.values())

        if not self.multiworld.eye_shuffle[self.player]:
            placed_items.extend(Vanilla.eye_dict.values())

        if not self.multiworld.herb_shuffle[self.player]:
            placed_items.extend(Vanilla.herb_dict.values())

        if not self.multiworld.church_shuffle[self.player]:
            placed_items.extend(Vanilla.church_dict.values())

        if not self.multiworld.shop_shuffle[self.player]:
            placed_items.extend(Vanilla.shop_dict.values())

        if self.multiworld.thorn_shuffle[self.player] == 2:
            for i in range(8):
                placed_items.append("Thorn Upgrade")

        if not self.multiworld.candle_shuffle[self.player]:
            placed_items.extend(Vanilla.candle_dict.values())

        if self.multiworld.start_wheel[self.player]:
            placed_items.append("The Young Mason's Wheel")

        if not self.multiworld.skill_randomizer[self.player]:
            placed_items.extend(Vanilla.skill_dict.values())

        counter = Counter(placed_items)

        pool = []

        for item in item_table:
            count = item["count"] - counter[item["name"]]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    pool.append(self.create_item(item["name"]))

        self.multiworld.itempool += pool


    def pre_fill(self):
        self.place_items_from_dict(Vanilla.unrandomized_dict)

        if not self.multiworld.cherub_shuffle[self.player]:
            self.place_items_from_set(Vanilla.cherub_set, "Child of Moonlight")

        if not self.multiworld.life_shuffle[self.player]:
            self.place_items_from_set(Vanilla.life_set, "Life Upgrade")

        if not self.multiworld.fervour_shuffle[self.player]:
            self.place_items_from_set(Vanilla.fervour_set, "Fervour Upgrade")

        if not self.multiworld.sword_shuffle[self.player]:
            self.place_items_from_set(Vanilla.sword_set, "Mea Culpa Upgrade")

        if not self.multiworld.blessing_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.blessing_dict)

        if not self.multiworld.dungeon_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.dungeon_dict)

        if not self.multiworld.tirso_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.tirso_dict)

        if not self.multiworld.miriam_shuffle[self.player]:
            self.multiworld.get_location("AtTotS: Miriam's gift", self.player)\
                .place_locked_item(self.create_item("Cantina of the Blue Rose"))

        if not self.multiworld.redento_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.redento_dict)

        if not self.multiworld.jocinero_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.jocinero_dict)

        if not self.multiworld.altasgracias_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.altasgracias_dict)

        if not self.multiworld.tentudia_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.tentudia_dict)

        if not self.multiworld.gemino_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.gemino_dict)

        if not self.multiworld.guilt_shuffle[self.player]:
            self.multiworld.get_location("GotP: Confessor Dungeon room", self.player)\
                .place_locked_item(self.create_item("Weight of True Guilt"))

        if not self.multiworld.ossuary_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.ossuary_dict)

        if not self.multiworld.boss_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.boss_dict)

        if not self.multiworld.wound_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.wound_dict)

        if not self.multiworld.mask_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.mask_dict)

        if not self.multiworld.eye_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.eye_dict)

        if not self.multiworld.herb_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.herb_dict)

        if not self.multiworld.church_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.church_dict)

        if not self.multiworld.shop_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.shop_dict)

        if self.multiworld.thorn_shuffle[self.player] == 2:
            self.place_items_from_set(Vanilla.thorn_set, "Thorn Upgrade")

        if not self.multiworld.candle_shuffle[self.player]:
            self.place_items_from_dict(Vanilla.candle_dict)

        if self.multiworld.start_wheel[self.player]:
            self.multiworld.get_location("BotSS: Beginning gift", self.player)\
                .place_locked_item(self.create_item("The Young Mason's Wheel"))

        if not self.multiworld.skill_randomizer[self.player]:
            self.place_items_from_dict(Vanilla.skill_dict)

        if self.multiworld.thorn_shuffle[self.player] == 1:
            self.multiworld.local_items[self.player].value.add("Thorn Upgrade")
        

    def place_items_from_set(self, location_set: Set[str], name: str):
        for loc in location_set:
            self.multiworld.get_location(loc, self.player)\
                .place_locked_item(self.create_item(name))

    
    def place_items_from_dict(self, option_dict: Dict[str, str]):
        for loc, item in option_dict.items():
            self.multiworld.get_location(loc, self.player)\
                .place_locked_item(self.create_item(item))


    def create_regions(self) -> None:
        player = self.player
        world = self.multiworld
        
        menu = Region("Menu", player, world)
        misc = Region("Misc", player, world)

        world.regions.append(menu)
        world.regions.append(misc)

        for room in room_table:
            reg = Region(room, player, world)
            world.regions.append(reg)

        ent = Entrance(player, "Misc", world.get_region("D17Z01S01", player))
        ent.connect(misc)
        world.get_region("D17Z01S01", player).exits.append(ent)

        ent2 = Entrance(player, "New Game", menu)
        ent2.connect(world.get_region("D17Z01S01", player))
        menu.exits.append(ent2)

        if not world.door_randomizer[player]:
            for door in door_table:
                if door.get("OriginalDoor") is None:
                    continue
                else:
                    parent: Region = self.get_room_from_door(door["Id"])
                    target: Region = self.get_room_from_door(door["OriginalDoor"])
                    exit = Entrance(player, door["Id"], parent)

                    exit.connect(target)
                    parent.exits.append(exit)

        for door in door_table:
            if door.get("RequiredDoors") is not None:
                for d in door["RequiredDoors"]:
                    #print(d, self.get_connected_door(d))
                    connection = self.get_connected_door(d)
                    add_rule(world.get_entrance(door["Id"], player), lambda state: state.can_reach(connection), "or")
                add_rule(world.get_entrance(door["Id"], player), lambda state: state.can_reach(self.get_connected_door(door["Id"])), "or")

        for loc in location_table:
            reg: Region

            if loc["room"] == "misc":
                reg = world.get_region("Misc", player)
            else:
                reg = world.get_region(loc["room"], player)

            id = base_id + location_table.index(loc)
            reg.locations.append(BlasphemousLocation(player, loc["name"], id, reg))
        
        victory = Location(player, "His Holiness Escribar", None, world.get_region("D07Z01S03", player))
        victory.place_locked_item(self.create_event("Victory"))
        world.get_region("D07Z01S03", player).locations.append(victory)

        if world.ending[self.player].value == 1:
            set_rule(victory, lambda state: state.has("Thorn Upgrade", player, 8))
        elif world.ending[self.player].value == 2:
            set_rule(victory, lambda state: state.has("Thorn Upgrade", player, 8) and \
                state.has("Holy Wound of Abnegation", player))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)
        

    def get_room_from_door(self, door: str) -> Region:
        return self.multiworld.get_region(door.split("[")[0], self.player)

    
    def get_connected_door(self, door: str) -> Entrance:
        player = self.player
        world = self.multiworld

        target: str

        try: 
            world.get_entrance(door, player)
        except KeyError:
            parent = self.get_room_from_door(door)
            for r in world.get_regions(player):
                for e in r.exits:
                    if e.connected_region == parent:
                        target = e.name
        else:
            parent = world.get_entrance(door, player)
            for e in parent.connected_region.exits:
                if e.connected_region == parent.parent_region:
                    target = e.name

        return world.get_entrance(target, player)

    
    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        locations = []

        world = self.multiworld
        player = self.player
        thorns: bool = True

        if world.thorn_shuffle[player].value == 2:
            thorns = False

        for loc in world.get_filled_locations(player):
            if loc.name == "His Holiness Escribar":
                continue
            else:
                data = {
                    "id": self.location_name_to_game_id[loc.name],
                    "ap_id": loc.address,
                    "name": loc.item.name,
                    "player_name": world.player_name[loc.item.player]
                }

                locations.append(data)

        config = {
            "LogicDifficulty": world.difficulty[player].value,
            "StartingLocation": "",
            "VersionCreated": "AP",
            
            "UnlockTeleportation": bool(world.prie_dieu_warp[player].value),
            "AllowHints": bool(world.corpse_hints[player].value),
            "AllowPenitence": bool(world.penitence[player].value),
            
            "ShuffleReliquaries": bool(world.reliquary_shuffle[player].value),
            "ShuffleDash": "",
            "ShuffleWallClimb": "",
            "ShuffleBootsOfPleading": "",
            "ShufflePurifiedHand": "",
            
            "ShuffleSwordSkills": bool(world.skill_randomizer[player].value),
            "ShuffleThorns": thorns,
            "JunkLongQuests": "",
            "StartWithWheel": bool(world.start_wheel[player].value),

            "EnemyShuffleType": world.enemy_randomizer[player].value,
            "MaintainClass": bool(world.enemy_groups[player].value),
            "AreaScaling": bool(world.enemy_scaling[player].value),

            "BossShuffleType": 0,
            "DoorShuffleType": 0
        }
    
        slot_data = {
            "locations": locations,
            "cfg": config,
            "ending": world.ending[self.player].value,
            "death_link": bool(world.death_link[self.player].value)
        }
    
        return slot_data


class BlasphemousItem(Item):
    game: str = "Blasphemous"


class BlasphemousLocation(Location):
    game: str = "Blasphemous"