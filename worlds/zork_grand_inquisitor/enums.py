import enum


class ZorkGrandInquisitorEvents(enum.Enum):
    CHARON_CALLED = "Event: Charon Called"
    CIGAR_ACCESSIBLE = "Event: Cigar Accessible"
    DALBOZ_LOCKER_OPENABLE = "Event: Dalboz Locker Openable"
    DAM_DESTROYED = "Event: Dam Destroyed"
    DOOR_DRANK_MEAD = "Event: Door Drank Mead"
    DOOR_SMOKED_CIGAR = "Event: Door Smoked Cigar"
    DUNCE_LOCKER_OPENABLE = "Event: Dunce Locker Openable"
    HAS_REPAIRABLE_OBIDIL = "Event: Has Repairable OBIDIL"
    HAS_REPAIRABLE_SNAVIG = "Event: Has Repairable SNAVIG"
    KNOWS_BEBURTT = "Event: Knows BEBURTT"
    KNOWS_OBIDIL = "Event: Knows OBIDIL"
    KNOWS_SNAVIG = "Event: Knows SNAVIG"
    KNOWS_YASTARD = "Event: Knows YASTARD"
    LANTERN_DALBOZ_ACCESSIBLE = "Event: Lantern (Dalboz) Accessible"
    ROPE_GLORFABLE = "Event: Rope GLORFable"
    VICTORY = "Victory"
    WHITE_HOUSE_LETTER_MAILABLE = "Event: White House Letter Mailable"
    ZORKMID_BILL_ACCESSIBLE = "Event: 500 Zorkmid Bill Accessible"
    ZORK_ROCKS_ACTIVATED = "Event: Zork Rocks Activated"
    ZORK_ROCKS_SUCKABLE = "Event: Zork Rocks Suckable"


class ZorkGrandInquisitorGoals(enum.Enum):
    THREE_ARTIFACTS = 0


class ZorkGrandInquisitorItems(enum.Enum):
    BROGS_BICKERING_TORCH = "Brog's Bickering Torch"
    BROGS_FLICKERING_TORCH = "Brog's Flickering Torch"
    BROGS_GRUE_EGG = "Brog's Grue Egg"
    BROGS_PLANK = "Brog's Plank"
    FILLER_FROBOZZ_ELECTRIC_GADGET = "Frobozz Electric Gadget"
    FILLER_INQUISITION_PROPAGANDA_FLYER = "Inquisition Propaganda Flyer"
    FILLER_MAGIC_CONTRABAND = "Magic Contraband"
    FILLER_NONSENSICAL_INQUISITION_PAPERWORK = "Nonsensical Inquisition Paperwork"
    FILLER_UNREADABLE_SPELL_SCROLL = "Unreadable Spell Scroll"
    FLATHEADIA_FUDGE = "Flatheadia Fudge"
    GRIFFS_AIR_PUMP = "Griff's Air Pump"
    GRIFFS_DRAGON_TOOTH = "Griff's Dragon Tooth"
    GRIFFS_INFLATABLE_RAFT = "Griff's Inflatable Raft"
    GRIFFS_INFLATABLE_SEA_CAPTAIN = "Griff's Inflatable Sea Captain"
    HAMMER = "Hammer"
    HOTSPOT_666_MAILBOX = "Hotspot: 666 Mailbox"
    HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS = "Hotspot: Alpine's Quandry Card Slots"
    HOTSPOT_BLANK_SCROLL_BOX = "Hotspot: Blank Scroll Box"
    HOTSPOT_BLINDS = "Hotspot: Blinds"
    HOTSPOT_CANDY_MACHINE_BUTTONS = "Hotspot: Candy Machine Buttons"
    HOTSPOT_CANDY_MACHINE_COIN_SLOT = "Hotspot: Candy Machine Coin Slot"
    HOTSPOT_CANDY_MACHINE_VACUUM_SLOT = "Hotspot: Candy Machine Vacuum Slot"
    HOTSPOT_CHANGE_MACHINE_SLOT = "Hotspot: Change Machine Slot"
    HOTSPOT_CLOSET_DOOR = "Hotspot: Closet Door"
    HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT = "Hotspot: Closing the Time Tunnels Hammer Slot"
    HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER = "Hotspot: Closing the Time Tunnels Lever"
    HOTSPOT_COOKING_POT = "Hotspot: Cooking Pot"
    HOTSPOT_DENTED_LOCKER = "Hotspot: Dented Locker"
    HOTSPOT_DIRT_MOUND = "Hotspot: Dirt Mound"
    HOTSPOT_DOCK_WINCH = "Hotspot: Dock Winch"
    HOTSPOT_DRAGON_CLAW = "Hotspot: Dragon Claw"
    HOTSPOT_DRAGON_NOSTRILS = "Hotspot: Dragon Nostrils"
    HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE = "Hotspot: Dungeon Master's Lair Entrance"
    HOTSPOT_FLOOD_CONTROL_BUTTONS = "Hotspot: Flood Control Buttons"
    HOTSPOT_FLOOD_CONTROL_DOORS = "Hotspot: Flood Control Doors"
    HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT = "Hotspot: Frozen Treat Machine Coin Slot"
    HOTSPOT_FROZEN_TREAT_MACHINE_DOORS = "Hotspot: Frozen Treat Machine Doors"
    HOTSPOT_GLASS_CASE = "Hotspot: Glass Case"
    HOTSPOT_GRAND_INQUISITOR_DOLL = "Hotspot: Grand Inquisitor Doll"
    HOTSPOT_GUE_TECH_DOOR = "Hotspot: GUE Tech Door"
    HOTSPOT_GUE_TECH_GRASS = "Hotspot: GUE Tech Grass"
    HOTSPOT_HADES_PHONE_BUTTONS = "Hotspot: Hades Phone Buttons"
    HOTSPOT_HADES_PHONE_RECEIVER = "Hotspot: Hades Phone Receiver"
    HOTSPOT_HARRY = "Hotspot: Harry"
    HOTSPOT_HARRYS_ASHTRAY = "Hotspot: Harry's Ashtray"
    HOTSPOT_HARRYS_BIRD_BATH = "Hotspot: Harry's Bird Bath"
    HOTSPOT_IN_MAGIC_WE_TRUST_DOOR = "Hotspot: In Magic We Trust Door"
    HOTSPOT_JACKS_DOOR = "Hotspot: Jack's Door"
    HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS = "Hotspot: Loudspeaker Volume Buttons"
    HOTSPOT_MAILBOX_DOOR = "Hotspot: Mailbox Door"
    HOTSPOT_MAILBOX_FLAG = "Hotspot: Mailbox Flag"
    HOTSPOT_MIRROR = "Hotspot: Mirror"
    HOTSPOT_MONASTERY_VENT = "Hotspot: Monastery Vent"
    HOTSPOT_MOSSY_GRATE = "Hotspot: Mossy Grate"
    HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR = "Hotspot: Port Foozle Past Tavern Door"
    HOTSPOT_PURPLE_WORDS = "Hotspot: Purple Words"
    HOTSPOT_QUELBEE_HIVE = "Hotspot: Quelbee Hive"
    HOTSPOT_ROPE_BRIDGE = "Hotspot: Rope Bridge"
    HOTSPOT_SKULL_CAGE = "Hotspot: Skull Cage"
    HOTSPOT_SNAPDRAGON = "Hotspot: Snapdragon"
    HOTSPOT_SODA_MACHINE_BUTTONS = "Hotspot: Soda Machine Buttons"
    HOTSPOT_SODA_MACHINE_COIN_SLOT = "Hotspot: Soda Machine Coin Slot"
    HOTSPOT_SOUVENIR_COIN_SLOT = "Hotspot: Souvenir Coin Slot"
    HOTSPOT_SPELL_CHECKER = "Hotspot: Spell Checker"
    HOTSPOT_SPELL_LAB_CHASM = "Hotspot: Spell Lab Chasm"
    HOTSPOT_SPRING_MUSHROOM = "Hotspot: Spring Mushroom"
    HOTSPOT_STUDENT_ID_MACHINE = "Hotspot: Student ID Machine"
    HOTSPOT_SUBWAY_TOKEN_SLOT = "Hotspot: Subway Token Slot"
    HOTSPOT_TAVERN_FLY = "Hotspot: Tavern Fly"
    HOTSPOT_TOTEMIZER_SWITCH = "Hotspot: Totemizer Switch"
    HOTSPOT_TOTEMIZER_WHEELS = "Hotspot: Totemizer Wheels"
    HOTSPOT_WELL = "Hotspot: Well"
    HUNGUS_LARD = "Hungus Lard"
    JAR_OF_HOTBUGS = "Jar of Hotbugs"
    LANTERN = "Lantern"
    LARGE_TELEGRAPH_HAMMER = "Large Telegraph Hammer"
    LUCYS_PLAYING_CARD_1 = "Lucy's Playing Card: 1 Pip"
    LUCYS_PLAYING_CARD_2 = "Lucy's Playing Card: 2 Pips"
    LUCYS_PLAYING_CARD_3 = "Lucy's Playing Card: 3 Pips"
    LUCYS_PLAYING_CARD_4 = "Lucy's Playing Card: 4 Pips"
    MAP = "Map"
    MEAD_LIGHT = "Mead Light"
    MOSS_OF_MAREILON = "Moss of Mareilon"
    MUG = "Mug"
    OLD_SCRATCH_CARD = "Old Scratch Card"
    PERMA_SUCK_MACHINE = "Perma-Suck Machine"
    PLASTIC_SIX_PACK_HOLDER = "Plastic Six-Pack Holder"
    POUCH_OF_ZORKMIDS = "Pouch of Zorkmids"
    PROZORK_TABLET = "Prozork Tablet"
    QUELBEE_HONEYCOMB = "Quelbee Honeycomb"
    ROPE = "Rope"
    SCROLL_FRAGMENT_ANS = "Scroll Fragment: ANS"
    SCROLL_FRAGMENT_GIV = "Scroll Fragment: GIV"
    SHOVEL = "Shovel"
    SNAPDRAGON = "Snapdragon"
    SPELL_GLORF = "Spell: GLORF"
    SPELL_GOLGATEM = "Spell: GOLGATEM"
    SPELL_IGRAM = "Spell: IGRAM"
    SPELL_KENDALL = "Spell: KENDALL"
    SPELL_NARWILE = "Spell: NARWILE"
    SPELL_REZROV = "Spell: REZROV"
    SPELL_THROCK = "Spell: THROCK"
    SPELL_VOXAM = "Spell: VOXAM"
    STUDENT_ID = "Student ID"
    SUBWAY_DESTINATION_FLOOD_CONTROL_DAM = "Subway Destination: Flood Control Dam #3"
    SUBWAY_DESTINATION_HADES = "Subway Destination: Hades"
    SUBWAY_DESTINATION_MONASTERY = "Subway Destination: Monastery"
    SUBWAY_TOKEN = "Subway Token"
    SWORD = "Sword"
    TELEPORTER_DESTINATION_DM_LAIR = "Teleporter Destination: Dungeon Master's Lair"
    TELEPORTER_DESTINATION_GUE_TECH = "Teleporter Destination: GUE Tech"
    TELEPORTER_DESTINATION_HADES = "Teleporter Destination: Hades"
    TELEPORTER_DESTINATION_MONASTERY = "Teleporter Destination: Monastery Station"
    TELEPORTER_DESTINATION_SPELL_LAB = "Teleporter Destination: Spell Lab"
    TOTEM_BROG = "Totem: Brog"
    TOTEM_GRIFF = "Totem: Griff"
    TOTEM_LUCY = "Totem: Lucy"
    TOTEMIZER_DESTINATION_HALL_OF_INQUISITION = "Totemizer Destination: Hall of Inquisition"
    TOTEMIZER_DESTINATION_INFINITY = "Totemizer Destination: Infinity"
    TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL = "Totemizer Destination: Straight to Hell"
    TOTEMIZER_DESTINATION_SURFACE_OF_MERZ = "Totemizer Destination: Surface of Merz"
    ZIMDOR_SCROLL = "ZIMDOR Scroll"
    ZORK_ROCKS = "Zork Rocks"


class ZorkGrandInquisitorLocations(enum.Enum):
    ALARM_SYSTEM_IS_DOWN = "Alarm System is Down"
    ARREST_THE_VANDAL = "Arrest the Vandal!"
    ARTIFACTS_EXPLAINED = "Artifacts, Explained"
    A_BIG_FAT_SASSY_2_HEADED_MONSTER = "A Big, Fat, SASSY 2-Headed Monster"
    A_LETTER_FROM_THE_WHITE_HOUSE = "A Letter from the White House"
    A_SMALLWAY = "A Smallway"
    BEAUTIFUL_THATS_PLENTY = "Beautiful, That's Plenty!"
    BEBURTT_DEMYSTIFIED = "BEBURTT, Demystified"
    BETTER_SPELL_MANUFACTURING_IN_UNDER_10_MINUTES = "Better Spell Manufacturing in Under 10 Minutes"
    BOING_BOING_BOING = "Boing, Boing, Boing"
    BONK = "Bonk!"
    BRAVE_SOULS_WANTED = "Brave Souls Wanted"
    BROG_DO_GOOD = "Brog Do Good!"
    BROG_EAT_ROCKS = "Brog Eat Rocks"
    BROG_KNOW_DUMB_THAT_DUMB = "Brog Know Dumb. That Dumb"
    BROG_MUCH_BETTER_AT_THIS_GAME = "Brog Much Better at This Game"
    CASTLE_WATCHING_A_FIELD_GUIDE = "Castle Watching: A Field Guide"
    CAVES_NOTES = "Cave's Notes"
    CLOSING_THE_TIME_TUNNELS = "Closing the Time Tunnels"
    CRISIS_AVERTED = "Crisis Averted"
    CUT_THAT_OUT_YOU_LITTLE_CREEP = "Cut That Out You Little Creep!"
    DEATH_ARRESTED_WITH_JACK = "Death: Arrested With Jack"
    DEATH_ATTACKED_THE_QUELBEES = "Death: Attacked the Quelbees"
    DEATH_CLIMBED_OUT_OF_THE_WELL = "Death: Climbed Out of the Well"
    DEATH_EATEN_BY_A_GRUE = "Death: Eaten by a Grue"
    DEATH_JUMPED_IN_BOTTOMLESS_PIT = "Death: Jumped in Bottomless Pit"
    DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER = "Death: Lost Game of Strip Grue, Fire, Water"
    DEATH_LOST_SOUL_TO_OLD_SCRATCH = "Death: Lost Soul to Old Scratch"
    DEATH_OUTSMARTED_BY_THE_QUELBEES = "Death: Outsmarted by the Quelbees"
    DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD = "Death: Sliced up by the Invisible Guard"
    DEATH_STEPPED_INTO_THE_INFINITE = "Death: Step Into the Infinite"
    DEATH_SWALLOWED_BY_A_DRAGON = "Death: Swallowed by a Dragon"
    DEATH_THROCKED_THE_GRASS = "Death: THROCKed the Grass"
    DEATH_TOTEMIZED = "Death: Totemized?"
    DEATH_TOTEMIZED_PERMANENTLY = "Death: Totemized... Permanently"
    DEATH_YOURE_NOT_CHARON = "Death: You're Not Charon!?"
    DEATH_ZORK_ROCKS_EXPLODED = "Death: Zork Rocks Exploded"
    DENIED_BY_THE_LAKE_MONSTER = "Denied by the Lake Monster"
    DESPERATELY_SEEKING_TUTOR = "Desperately Seeking Tutor"
    DONT_EVEN_START_WITH_US_SPARKY = "Don't Even Start With Us, Sparky"
    DOOOOOOWN = "Doooooown"
    DOWN = "Down"
    DRAGON_ARCHIPELAGO_TIME_TUNNEL = "Dragon Archipelago Time Tunnel"
    DUNCE_LOCKER = "Dunce Locker"
    EGGPLANTS = "Eggplants"
    ELSEWHERE = "Elsewhere"
    EMERGENCY_MAGICATRONIC_MESSAGE = "Emergency Magicatronic Message"
    ENJOY_YOUR_TRIP = "Enjoy Your Trip!"
    FAT_LOT_OF_GOOD_THATLL_DO_YA = "Fat Lot of Good That'll Do Ya"
    FIRE_FIRE = "Fire! Fire!"
    FLOOD_CONTROL_DAM_3_THE_NOT_REMOTELY_BORING_TALE = "Flood Control Dam #3: The Not Remotely Boring Tale"
    FLYING_SNAPDRAGON = "Flying Snapdragon"
    FROBUARY_3_UNDERGROUNDHOG_DAY = "Frobruary 3 - Undergroundhog Day"
    GETTING_SOME_CHANGE = "Getting Some Change"
    GO_AWAY = "GO AWAY!"
    GUE_TECH_DEANS_LIST = "GUE Tech Dean's List"
    GUE_TECH_ENTRANCE_EXAM = "GUE Tech Entrance Exam"
    GUE_TECH_HEALTH_MEMO = "GUE Tech Health Memo"
    GUE_TECH_MAGEMEISTERS = "GUE Tech Magemeisters"
    HAVE_A_HELL_OF_A_DAY = "Have a Hell of a Day!"
    HELLO_THIS_IS_SHONA_FROM_GURTH_PUBLISHING = "Hello, This is Shona from Gurth Publishing"
    HELP_ME_CANT_BREATHE = "Help... Me. Can't... Breathe"
    HEY_FREE_DIRT = "Hey, Free Dirt!"
    HI_MY_NAME_IS_DOUG = "Hi, My Name is Doug"
    HMMM_INFORMATIVE_YET_DEEPLY_DISTURBING = "Hmmm. Informative. Yet Deeply Disturbing"
    HOLD_ON_FOR_AN_IMPORTANT_MESSAGE = "Hold on for an Important Message"
    HOW_TO_HYPNOTIZE_YOURSELF = "How to Hypnotize Yourself"
    HOW_TO_WIN_AT_DOUBLE_FANUCCI = "How to Win at Double Fanucci"
    IMBUE_BEBURTT = "Imbue BEBURTT"
    IM_COMPLETELY_NUDE = "I'm Completely Nude"
    INTO_THE_FOLIAGE = "Into the Foliage"
    INVISIBLE_FLOWERS = "Invisible Flowers"
    IN_CASE_OF_ADVENTURE = "In Case of Adventure, Break Glass!"
    IN_MAGIC_WE_TRUST = "In Magic We Trust"
    ITS_ONE_OF_THOSE_ADVENTURERS_AGAIN = "It's One of Those Adventurers Again..."
    I_DONT_THINK_YOU_WOULDVE_WANTED_THAT_TO_WORK_ANYWAY = "I Don't Think You Would've Wanted That to Work Anyway"
    I_DONT_WANT_NO_TROUBLE = "I Don't Want No Trouble!"
    I_HOPE_YOU_CAN_CLIMB_UP_THERE = "I Hope You Can Climb Up There With All This Junk"
    I_LIKE_YOUR_STYLE = "I Like Your Style!"
    I_SPIT_ON_YOUR_FILTHY_COINAGE = "I Spit on Your Filthy Coinage"
    LIT_SUNFLOWERS = "Lit Sunflowers"
    MAGIC_FOREVER = "Magic Forever!"
    MAILED_IT_TO_HELL = "Mailed it to Hell"
    MAKE_LOVE_NOT_WAR = "Make Love, Not War"
    MEAD_LIGHT = "Mead Light?"
    MIKES_PANTS = "Mike's Pants"
    MUSHROOM_HAMMERED = "Mushroom, Hammered"
    NATIONAL_TREASURE = "300 Year Old National Treasure"
    NATURAL_AND_SUPERNATURAL_CREATURES_OF_QUENDOR = "Natural and Supernatural Creatures of Quendor"
    NOOOOOOOOOOOOO = "NOOOOOOOOOOOOO!"
    NOTHIN_LIKE_A_GOOD_STOGIE = "Nothin' Like a Good Stogie"
    NOW_YOU_LOOK_LIKE_US_WHICH_IS_AN_IMPROVEMENT = "Now You Look Like Us, Which is an Improvement"
    NO_AUTOGRAPHS = "No Autographs"
    NO_BONDAGE = "No Bondage"
    OBIDIL_DRIED_UP = "OBIDIL, Dried Up"
    OH_DEAR_GOD_ITS_A_DRAGON = "Oh Dear God, It's a Dragon!"
    OH_VERY_FUNNY_GUYS = "Oh, Very Funny Guys"
    OH_WOW_TALK_ABOUT_DEJA_VU = "Oh, Wow! Talk About Deja Vu"
    OLD_SCRATCH_WINNER = "Old Scratch Winner!"
    ONLY_YOU_CAN_PREVENT_FOOZLE_FIRES = "Only You Can Prevent Foozle Fires"
    OPEN_THE_GATES_OF_HELL = "Open the Gates of Hell"
    OUTSMART_THE_QUELBEES = "Outsmart the Quelbees"
    PERMASEAL = "PermaSeal"
    PLANETFALL = "Planetfall"
    PLEASE_DONT_THROCK_THE_GRASS = "Please Don't THROCK the Grass"
    PORT_FOOZLE_TIME_TUNNEL = "Port Foozle Time Tunnel"
    PROZORKED = "Prozorked"
    REASSEMBLE_SNAVIG = "Reassemble SNAVIG"
    RESTOCKED_ON_GRUESDAY = "Restocked on Gruesday"
    RIGHT_HELLO_YES_UH_THIS_IS_SNEFFLE = "Right. Hello. Yes. Uh, This is Sneffle"
    RIGHT_UH_SORRY_ITS_ME_AGAIN_SNEFFLE = "Right. Uh, Sorry. It's Me Again. Sneffle"
    SNAVIG_REPAIRED = "SNAVIG, Repaired"
    SOUVENIR = "Souvenir"
    STRAIGHT_TO_HELL = "Straight to Hell"
    STRIP_GRUE_FIRE_WATER = "Strip Grue, Fire, Water"
    SUCKING_ROCKS = "Sucking Rocks"
    TALK_TO_ME_GRAND_INQUISITOR = "Talk to Me Grand Inquisitor"
    TAMING_YOUR_SNAPDRAGON = "Taming Your Snapdragon"
    THAR_SHE_BLOWS = "Thar She Blows!"
    THATS_A_ROPE = "That's a Rope"
    THATS_IT_JUST_KEEP_HITTING_THOSE_BUTTONS = "That's it! Just Keep Hitting Those Buttons"
    THATS_STILL_A_ROPE = "That's Still a Rope"
    THATS_THE_SPIRIT = "That's the Spirit!"
    THE_ALCHEMICAL_DEBACLE = "The Alchemical Debacle"
    THE_ENDLESS_FIRE = "The Endless Fire"
    THE_FLATHEADIAN_FUDGE_FIASCO = "The Flatheadian Fudge Fiasco"
    THE_PERILS_OF_MAGIC = "The Perils of Magic"
    THE_UNDERGROUND_UNDERGROUND = "The Underground Underground"
    THIS_DOESNT_LOOK_ANYTHING_LIKE_THE_BROCHURE = "This Doesn't Look Anything Like the Brochure"
    THROCKED_MUSHROOM_HAMMERED = "THROCKed Mushroom, Hammered"
    TIME_TRAVEL_FOR_DUMMIES = "Time Travel for Dummies"
    TOTEMIZED_DAILY_BILLBOARD = "Totemized Daily Billboard Functioning Correctly"
    UH_OH_BROG_CANT_SWIM = "Uh-Oh. Brog Can't Swim"
    UMBRELLA_FLOWERS = "Umbrella Flowers"
    UP = "Up"
    USELESS_BUT_FUN = "Useless, But Fun"
    UUUUUP = "Uuuuup"
    VOYAGE_OF_CAPTAIN_ZAHAB = "Voyage of Captain Zahab"
    WANT_SOME_RYE_COURSE_YA_DO = "Want Some Rye? Course Ya Do!"
    WE_DONT_SERVE_YOUR_KIND_HERE = "We Don't Serve Your Kind Here"
    WE_GOT_A_HIGH_ROLLER = "We Got a High Roller!"
    WHAT_ARE_YOU_STUPID = "What Are You, Stupid?"
    WHITE_HOUSE_TIME_TUNNEL = "White House Time Tunnel"
    WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE = "Wow! I've Never Gone Inside Him Before!"
    YAD_GOHDNUORGREDNU_3_YRAUBORF = "yaD gohdnuorgrednU - 3 yrauborF"
    YOUR_PUNY_WEAPONS_DONT_PHASE_ME_BABY = "Your Puny Weapons Don't Phase Me, Baby!"
    YOU_DONT_GO_MESSING_WITH_A_MANS_ZIPPER = "You Don't Go Messing With a Man's Zipper"
    YOU_GAINED_86_EXPERIENCE_POINTS = "You Gained 86 Experience Points"
    YOU_ONE_OF_THEM_AGITATORS_AINT_YA = "You One of Them Agitators, Ain't Ya?"
    YOU_WANT_A_PIECE_OF_ME_DOCK_BOY = "You Want a Piece of Me, Dock Boy? or Girl"


class ZorkGrandInquisitorRegions(enum.Enum):
    CROSSROADS = "Crossroads"
    DM_LAIR = "Dungeon Master's Lair"
    DM_LAIR_INTERIOR = "Dungeon Master's Lair - Interior"
    DRAGON_ARCHIPELAGO = "Dragon Archipelago"
    DRAGON_ARCHIPELAGO_DRAGON = "Dragon Archipelago - Dragon"
    ENDGAME = "Endgame"
    GUE_TECH = "GUE Tech"
    GUE_TECH_HALLWAY = "GUE Tech - Hallway"
    GUE_TECH_OUTSIDE = "GUE Tech - Outside"
    HADES = "Hades"
    HADES_BEYOND_GATES = "Hades - Beyond Gates"
    HADES_SHORE = "Hades - Shore"
    MENU = "Menu"
    MONASTERY = "Monastery"
    MONASTERY_EXHIBIT = "Monastery - Exhibit"
    PORT_FOOZLE = "Port Foozle"
    PORT_FOOZLE_JACKS_SHOP = "Port Foozle - Jack's Shop"
    PORT_FOOZLE_PAST = "Port Foozle Past"
    PORT_FOOZLE_PAST_TAVERN = "Port Foozle Past - Tavern"
    SPELL_LAB = "Spell Lab"
    SPELL_LAB_BRIDGE = "Spell Lab - Bridge"
    SUBWAY_CROSSROADS = "Subway Platform - Crossroads"
    SUBWAY_FLOOD_CONTROL_DAM = "Subway Platform - Flood Control Dam #3"
    SUBWAY_MONASTERY = "Subway Platform - Monastery"
    WALKING_CASTLE = "Walking Castle"
    WHITE_HOUSE = "White House"


class ZorkGrandInquisitorTags(enum.Enum):
    CORE = "Core"
    DEATHSANITY = "Deathsanity"
    FILLER = "Filler"
    HOTSPOT = "Hotspot"
    INVENTORY_ITEM = "Inventory Item"
    MISSABLE = "Missable"
    SPELL = "Spell"
    SUBWAY_DESTINATION = "Subway Destination"
    TELEPORTER_DESTINATION = "Teleporter Destination"
    TOTEMIZER_DESTINATION = "Totemizer Destination"
    TOTEM = "Totem"
