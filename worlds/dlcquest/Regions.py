import math
from BaseClasses import MultiWorld, Region, Location, Entrance, ItemClassification
from .Locations import DLCquestLocation, location_table
from .Rules import create_event
from . import Options

DLCquestRegion =["Movement Pack", "Behind Tree", "Psychological Warfare", "Double Jump Left", "Double Jump Behind the Tree", "The Forest", "Final Room"]

def add_coin_freemium(region : Region, Coin: int, player: int):
    for i in range(Coin):
        location =DLCquestLocation(player, "Coin_Freemium", None, region)
        region.locations.append(location)
        location.place_locked_item(create_event(player, "Coin_Freemium"))

def add_coin_dlcquest(region : Region, Coin: int, player: int):
    for i in range(Coin):
        location =DLCquestLocation(player, "Coin", None, region)
        region.locations.append(location)
        location.place_locked_item(create_event(player, "Coin"))
def create_regions(world: MultiWorld, player: int, World_Options: Options.DLCQuestOptions):

    Regmenu = Region("Menu", player, world)
    if World_Options[Options.Campaign] == Options.Campaign.option_basic or World_Options[Options.Campaign] == Options.Campaign.option_both:
        Regmenu.exits += [Entrance(player, "DLC Quest Basic", Regmenu)]
    if World_Options[Options.Campaign] == Options.Campaign.option_live_freemium_or_die or World_Options[Options.Campaign] == Options.Campaign.option_both:
        Regmenu.exits += [Entrance(player, "Live Freemium or Die", Regmenu)]
    world.regions.append(Regmenu)


    if World_Options[Options.Campaign] == Options.Campaign.option_basic or World_Options[Options.Campaign] == Options.Campaign.option_both:

        Regmoveright =Region("Move Right", player, world, "Start of the basic game")
        Locmoveright_name = ["Movement Pack", "Animation Pack", "Audio Pack", "Pause Menu Pack"]
        Regmoveright.exits =[Entrance(player, "Moving", Regmoveright)]
        Regmoveright.locations += [DLCquestLocation(player, loc_name, location_table[loc_name],Regmoveright) for loc_name in Locmoveright_name]
        add_coin_dlcquest(Regmoveright, 4, player)
        if World_Options[Options.CoinSanity] == Options.CoinSanity.option_coin:
            coin_bundle_needed = math.floor(825 / World_Options[Options.CoinSanityRange])
            for i in range(coin_bundle_needed):
                item_coin = "Coin Bundle Basic"
                item_coin_loc = item_coin + str(i + 1)
                Regmoveright.locations +=[DLCquestLocation(player, item_coin_loc, location_table[item_coin_loc], Regmoveright)]
        world.regions.append(Regmoveright)


        Regmovpack =Region("Movement Pack", player, world)
        Locmovpack_name = ["Time is Money Pack", "Psychological Warfare Pack","Armor for your Horse Pack"]
        Regmovpack.exits =[ Entrance(player, "Tree", Regmovpack), Entrance(player, "Cloud", Regmovpack)]
        Regmovpack.locations += [DLCquestLocation(player, loc_name, location_table[loc_name],Regmovpack)for loc_name in Locmovpack_name ]
        add_coin_dlcquest(Regmovpack, 46, player)
        world.regions.append(Regmovpack)

        Regbtree = Region("Behind Tree", player, world)
        Locbtree_name = ["Double Jump Pack", "Map Pack"]
        Regbtree.exits =[ Entrance(player, "Behind Tree Double Jump", Regbtree), Entrance(player, "Forest Entrance", Regbtree)]
        Regbtree.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regbtree) for loc_name in Locbtree_name]
        add_coin_dlcquest(Regbtree, 60, player)
        world.regions.append(Regbtree)

        Regpsywarfare = Region("Psychological Warfare", player, world)
        Locpsywarfare_name = []
        Regpsywarfare.exits =[ Entrance(player, "Cloud Double Jump", Regpsywarfare)]
        Regpsywarfare.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regpsywarfare) for loc_name in Locpsywarfare_name]
        add_coin_dlcquest(Regpsywarfare, 100, player)
        world.regions.append(Regpsywarfare)

        Regdoubleleft = Region("Double Jump Total Left", player, world)
        Locdoubleleft_name = ["Pet Pack", "Top Hat Pack"]
        Regdoubleleft.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regdoubleleft) for loc_name in
                                    Locdoubleleft_name]
        add_coin_dlcquest(Regdoubleleft, 69, player)
        world.regions.append(Regdoubleleft)

        Regdoubletree = Region("Double Jump Behind Tree", player, world)
        Locdoubletree_name = ["Sexy Outfits Pack"]
        Regdoubletree.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regdoubletree) for loc_name in
                                     Locdoubletree_name]
        add_coin_dlcquest(Regdoubletree, 96, player)
        world.regions.append(Regdoubletree)

        Regforest = Region("The Forest", player, world)
        Locforest_name = ["Gun Pack", "Night Map Pack"]
        Regforest.exits = [Entrance(player, "Behind Ogre", Regforest), Entrance(player, "Forest Double Jump", Regforest)]
        Regforest.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regforest) for loc_name in
                                     Locforest_name]
        add_coin_dlcquest(Regforest, 169, player)
        world.regions.append(Regforest)

        Regforestdoublejump = Region("The Forest whit double Jump", player, world)
        Locforestdoublejump_name = [ "The Zombie Pack"]
        Regforestdoublejump.exits = [Entrance(player, "Forest True Double Jump", Regforestdoublejump)]
        Regforestdoublejump.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regforestdoublejump) for loc_name in
                                Locforestdoublejump_name]
        add_coin_dlcquest(Regforestdoublejump, 76, player)
        world.regions.append(Regforestdoublejump)

        Regforesttruedoublejump = Region("The Forest whit double Jump Part 2", player, world)
        Locforesttruedoublejump_name = []
        Regforesttruedoublejump.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regforesttruedoublejump)
                                          for loc_name in Locforesttruedoublejump_name]
        add_coin_dlcquest(Regforesttruedoublejump, 203, player)
        world.regions.append(Regforesttruedoublejump)

        Regfinalroom = Region("The Final Boss Room", player, world)
        Locfinalroom_name = [ "Finish the Fight Pack"]
        Regfinalroom.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regfinalroom) for loc_name in
                                Locfinalroom_name]
        world.regions.append(Regfinalroom)

        world.get_entrance("DLC Quest Basic", player).connect(world.get_region("Move Right", player))

        world.get_entrance("Moving", player).connect(world.get_region("Movement Pack", player))

        world.get_entrance("Tree", player).connect(world.get_region("Behind Tree", player))

        world.get_entrance("Cloud", player).connect(world.get_region("Psychological Warfare", player))

        world.get_entrance("Cloud Double Jump", player).connect(world.get_region("Double Jump Total Left", player))

        world.get_entrance("Forest Entrance", player).connect(world.get_region("The Forest", player))

        world.get_entrance("Behind Tree Double Jump", player).connect(world.get_region("Double Jump Behind Tree", player))

        world.get_entrance("Behind Ogre", player).connect(world.get_region("The Final Boss Room", player))

        world.get_entrance("Forest Double Jump", player).connect(world.get_region("The Forest whit double Jump", player))

        world.get_entrance("Forest True Double Jump", player).connect(world.get_region("The Forest whit double Jump Part 2", player))

    if World_Options[Options.Campaign] == Options.Campaign.option_live_freemium_or_die or World_Options[Options.Campaign] == Options.Campaign.option_both:

        Regfreemiumstart = Region("Freemium Start", player, world)
        Locfreemiumstart_name = ["Particles Pack","Day One Patch Pack","Checkpoint Pack","Incredibly Important Pack"]
        Regfreemiumstart.exits = [Entrance(player, "Vines", Regfreemiumstart)]
        Regfreemiumstart.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regfreemiumstart) for loc_name in
            Locfreemiumstart_name]
        add_coin_freemium(Regfreemiumstart, 50, player)
        if World_Options[Options.CoinSanity] == Options.CoinSanity.option_coin:
            coin_bundle_needed = math.floor(889 / Options.CoinSanityRange.value)
            for i in range(coin_bundle_needed):
                item_coin_freemium = "Coin Bundle Freemium"
                item_coin_freemium_loc = item_coin_freemium + str(i + 1)
                Regmoveright.locations +=[DLCquestLocation(player, item_coin_freemium_loc, location_table[item_coin_freemium_loc], Regfreemiumstart)]
        world.regions.append(Regfreemiumstart)


        Regbehindvine = Region("Behind the Vines", player, world)
        Locbehindvine_name =["Wall Jump Pack","Health Bar Pack","Parallax Pack"]
        Regbehindvine.exits = [Entrance(player, "Wall Jump Entrance", Regbehindvine)]
        Regbehindvine.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regbehindvine) for loc_name in Locbehindvine_name]
        add_coin_freemium(Regbehindvine, 95, player)
        world.regions.append(Regbehindvine)

        Regwalljump = Region("Wall Jump", player, world)
        Locwalljump_name = ["Harmless Plants Pack", "Death of Comedy Pack", "Canadian Dialog Pack", "DLC NPC Pack"]
        Regwalljump.exits = [Entrance(player, "Harmless Plants", Regwalljump), Entrance(player, "Pickaxe Hard Cave", Regwalljump)]
        Regwalljump.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regwalljump) for
                                    loc_name in Locwalljump_name]
        add_coin_freemium(Regwalljump, 150, player)
        world.regions.append(Regwalljump)

        Regfakeending = Region("Fake Ending", player, world)
        Locfakeending_name = ["Cut Content Pack", "Name Change Pack"]
        Regfakeending.exits = [Entrance(player, "Name Change Entrance", Regfakeending), Entrance(player, "Cut Content Entrance", Regfakeending)]
        Regfakeending.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regfakeending) for
                                  loc_name in Locfakeending_name]
        world.regions.append(Regfakeending)

        Reghardcave = Region("Hard Cave", player, world)
        add_coin_freemium(Reghardcave, 0, player)
        world.regions.append(Reghardcave)

        Regcutcontent = Region("Cut Content", player, world)
        add_coin_freemium(Regcutcontent, 200, player)
        world.regions.append(Regcutcontent)

        Regnamechange = Region("Name Change", player, world)
        Locnamechange_name = ["Pickaxe"]
        Regnamechange.exits = [Entrance(player, "Behind Rocks", Regnamechange)]
        Regnamechange.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regnamechange) for
                                  loc_name in Locnamechange_name]
        world.regions.append(Regnamechange)

        Regtopright = Region("Top Right", player, world)
        Loctopright_name = ["Season Pass", "High Definition Next Gen Pack", "Increased HP Pack"]
        Regtopright.exits = [Entrance(player, "Blizzard", Regtopright)]
        Regtopright.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regtopright) for
                                  loc_name in Loctopright_name]
        add_coin_freemium(Regtopright, 240, player)
        world.regions.append(Regtopright)

        Regseason = Region("Season", player, world)
        Locseason_name = ["Remove Ads Pack"]
        Regseason.exits = [Entrance(player, "Boss Door", Regseason)]
        Regseason.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regseason) for
                                  loc_name in Locseason_name]
        add_coin_freemium(Regseason, 154, player)
        world.regions.append(Regseason)

        Regfinalboss = Region("Final Boss", player, world)
        Locfinalboss_name = ["Big Sword Pack", "Really Big Sword Pack", "Unfathomable Sword Pack"]
        Regfinalboss.locations += [DLCquestLocation(player, loc_name, location_table[loc_name], Regfinalboss) for
                                loc_name in Locfinalboss_name]
        world.regions.append(Regfinalboss)

        world.get_entrance("Live Freemium or Die", player).connect(world.get_region("Freemium Start", player))

        world.get_entrance("Vines", player).connect(world.get_region("Behind the Vines", player))

        world.get_entrance("Wall Jump Entrance", player).connect(world.get_region("Wall Jump", player))

        world.get_entrance("Harmless Plants", player).connect(world.get_region("Fake Ending", player))

        world.get_entrance("Pickaxe Hard Cave", player).connect(world.get_region("Hard Cave", player))

        world.get_entrance("Name Change Entrance", player).connect(world.get_region("Name Change", player))

        world.get_entrance("Cut Content Entrance", player).connect(world.get_region("Cut Content", player))

        world.get_entrance("Behind Rocks", player).connect(world.get_region("Top Right", player))

        world.get_entrance("Blizzard", player).connect(world.get_region("Season", player))

        world.get_entrance("Boss Door", player).connect(world.get_region("Final Boss", player))



