import typing

from BaseClasses import Item
from .Names import ItemName


class KH2Item(Item):
    game: str = "Kingdom Hearts 2"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    quantity: int = 0
    kh2id: int = 0
    # Save+ mem addr
    memaddr: int = 0
    # some items have bitmasks. if bitmask>0 bitor to give item else
    bitmask: int = 0
    # if ability then
    ability: bool = False
    event: bool = False


Reports_Table = {
    ItemName.SecretAnsemsReport1: ItemData(0x130000, 1, 226,  0x36C4, 6),
    ItemName.SecretAnsemsReport2: ItemData(0x130001, 1, 227,  0x36C4, 7),
    ItemName.SecretAnsemsReport3: ItemData(0x130002, 1, 228,  0x36C5, 0),
    ItemName.SecretAnsemsReport4: ItemData(0x130003, 1, 229,  0x36C5, 1),
    ItemName.SecretAnsemsReport5: ItemData(0x130004, 1, 230,  0x36C5, 2),
    ItemName.SecretAnsemsReport6: ItemData(0x130005, 1, 231,  0x36C5, 3),
    ItemName.SecretAnsemsReport7: ItemData(0x130006, 1, 232,  0x36C5, 4),
    ItemName.SecretAnsemsReport8: ItemData(0x130007, 1, 233,  0x36C5, 5),
    ItemName.SecretAnsemsReport9: ItemData(0x130008, 1, 234,  0x36C5, 6),
    ItemName.SecretAnsemsReport10: ItemData(0x130009, 1, 235, 0x36C5, 7),
    ItemName.SecretAnsemsReport11: ItemData(0x13000A, 1, 236, 0x36C6, 0),
    ItemName.SecretAnsemsReport12: ItemData(0x13000B, 1, 237, 0x36C6, 1),
    ItemName.SecretAnsemsReport13: ItemData(0x13000C, 1, 238, 0x36C6, 2),
}

Progression_Table = {
    ItemName.ProofofConnection: ItemData(0x13000D, 1, 593,      0x36B2),
    ItemName.ProofofNonexistence: ItemData(0x13000E, 1, 594,    0x36B3),
    ItemName.ProofofPeace: ItemData(0x13000F, 1, 595,           0x36B4),
    ItemName.PromiseCharm: ItemData(0x130010, 1, 524, 0x3694),
    ItemName.NamineSketches: ItemData(0x130011, 1, 368, 0x3642),
    # dummy 13
    ItemName.CastleKey: ItemData(0x130012, 1, 460, 0x365D),
    ItemName.BattlefieldsofWar: ItemData(0x130013, 1, 54, 0x35AE),
    ItemName.SwordoftheAncestor: ItemData(0x130014, 1, 55, 0x35AF),
    ItemName.BeastsClaw: ItemData(0x130015, 1, 59, 0x35B3),
    ItemName.BoneFist: ItemData(0x130016, 1, 60, 0x35B4),
    ItemName.ProudFang: ItemData(0x130017, 1, 61, 0x35B5),
    ItemName.SkillandCrossbones: ItemData(0x130018, 1, 62, 0x35B6),
    ItemName.Scimitar: ItemData(0x130019, 1, 72, 0x35C0),
    ItemName.MembershipCard: ItemData(0x13001A, 1, 369, 0x3643),
    ItemName.IceCream: ItemData(0x13001B, 1, 375, 0x3649),
    ItemName.Picture: ItemData(0x13001C, 1, 376, 0x364A),
    ItemName.WaytotheDawn: ItemData(0x13001D, 1, 73, 0x35C1),
    ItemName.IdentityDisk: ItemData(0x13001E, 1, 74, 0x35C2),
    ItemName.Poster: ItemData(0x13001F, 1, 366, 0x3640),
    ItemName.TornPages: ItemData(0x130020, 5, 32, 0x3598),

}
Forms_Table = {
    ItemName.ValorForm: ItemData(0x130021, 1, 26,  0x36C0, 1),
    ItemName.WisdomForm: ItemData(0x130022, 1, 27, 0x36C0, 2),
    ItemName.LimitForm: ItemData(0x130023, 1, 563, 0x36CA, 3),
    ItemName.MasterForm: ItemData(0x130024, 1, 31, 0x36C0, 6),
    ItemName.FinalForm: ItemData(0x130025, 1, 29,  0x36C0, 4),
}
Magic_Table = {
    ItemName.FireElement: ItemData(0x130026, 3, 21,     0x3594),
    ItemName.BlizzardElement: ItemData(0x130027, 3, 22, 0x3595),
    ItemName.ThunderElement: ItemData(0x130028, 3, 23,  0x3596),
    ItemName.CureElement: ItemData(0x130029, 3, 24,     0x3597),
    ItemName.MagnetElement: ItemData(0x13002A, 3, 87,   0x35CF),
    ItemName.ReflectElement: ItemData(0x13002B, 3, 88,  0x35D0),
    ItemName.Genie: ItemData(0x13002C, 1, 159, 0x36C4, 4),
    ItemName.PeterPan: ItemData(0x13002D, 1, 160, 0x36C4, 5),
    ItemName.Stitch: ItemData(0x13002E, 1, 25, 0x36C0, 0),
    ItemName.ChickenLittle: ItemData(0x13002F, 1, 383, 0x36C0, 3),
}

Movement_Table = {

    ItemName.HighJump: ItemData(0x130030, 4, 94, 0x05E, 0, True),
    ItemName.QuickRun: ItemData(0x130031, 4, 98, 0x062, 0, True),
    ItemName.DodgeRoll: ItemData(0x130032, 4, 564, 0x234, 0, True),
    ItemName.AerialDodge: ItemData(0x130033, 4, 102, 0x066, 0, True),
    ItemName.Glide: ItemData(0x130034, 4, 106, 0x06A, 0, True),

}

Keyblade_Table = {
    ItemName.Oathkeeper: ItemData(0x130035, 1, 42, 0x35A2),
    ItemName.Oblivion: ItemData(0x130036, 1, 43, 0x35A3),
    ItemName.StarSeeker: ItemData(0x130037, 1, 480, 0x367B),
    ItemName.HiddenDragon: ItemData(0x130038, 1, 481, 0x367C),
    ItemName.HerosCrest: ItemData(0x130039, 1, 484, 0x367F),
    ItemName.Monochrome: ItemData(0x13003A, 1, 485, 0x3680),
    ItemName.FollowtheWind: ItemData(0x13003B, 1, 486, 0x3681),
    ItemName.CircleofLife: ItemData(0x13003C, 1, 487, 0x3682),
    ItemName.PhotonDebugger: ItemData(0x13003D, 1, 488, 0x3683),
    ItemName.GullWing: ItemData(0x13003E, 1, 489, 0x3684),
    ItemName.RumblingRose: ItemData(0x13003F, 1, 490, 0x3685),
    ItemName.GuardianSoul: ItemData(0x130040, 1, 491, 0x3686),
    ItemName.WishingLamp: ItemData(0x130041, 1, 492, 0x3687),
    ItemName.DecisivePumpkin: ItemData(0x130042, 1, 493, 0x3688),
    ItemName.SleepingLion: ItemData(0x130043, 1, 494, 0x3689),
    ItemName.SweetMemories: ItemData(0x130044, 1, 495, 0x368A),
    ItemName.MysteriousAbyss: ItemData(0x130045, 1, 496, 0x368B),
    ItemName.TwoBecomeOne: ItemData(0x130046, 1, 543, 0x3698),
    ItemName.FatalCrest: ItemData(0x130047, 1, 497, 0x368C),
    ItemName.BondofFlame: ItemData(0x130048, 1, 498, 0x368D),
    ItemName.Fenrir: ItemData(0x130049, 1, 499, 0x368E),
    ItemName.UltimaWeapon: ItemData(0x13004A, 1, 500, 0x368F),
    ItemName.WinnersProof: ItemData(0x13004B, 1, 544, 0x3699),
    ItemName.Pureblood: ItemData(0x13004C, 1, 71, 0x35BF),
}
Staffs_Table = {
    ItemName.Centurion2: ItemData(0x13004D, 1, 546, 0x369B),
    ItemName.MeteorStaff: ItemData(0x13004E, 1, 150, 0x35F1),
    ItemName.NobodyLance: ItemData(0x13004F, 1, 155, 0x35F6),
    ItemName.PreciousMushroom: ItemData(0x130050, 1, 549, 0x369E),
    ItemName.PreciousMushroom2: ItemData(0x130051, 1, 550, 0x369F),
    ItemName.PremiumMushroom: ItemData(0x130052, 1, 551, 0x36A0),
    ItemName.RisingDragon: ItemData(0x130053, 1, 154, 0x35F5),
    ItemName.SaveTheQueen2: ItemData(0x130054, 1, 503, 0x3692),
    ItemName.ShamansRelic: ItemData(0x130055, 1, 156, 0x35F7),
}
Shields_Table = {
    ItemName.AkashicRecord: ItemData(0x130056, 1, 146, 0x35ED),
    ItemName.FrozenPride2: ItemData(0x130057, 1, 553, 0x36A2),
    ItemName.GenjiShield: ItemData(0x130058, 1, 145, 0x35EC),
    ItemName.MajesticMushroom: ItemData(0x130059, 1, 556, 0x36A5),
    ItemName.MajesticMushroom2: ItemData(0x13005A, 1, 557, 0x36A6),
    ItemName.NobodyGuard: ItemData(0x13005B, 1, 147, 0x35EE),
    ItemName.OgreShield: ItemData(0x13005C, 1, 141, 0x35E8),
    ItemName.SaveTheKing2: ItemData(0x13005D, 1, 504, 0x3693),
    ItemName.UltimateMushroom: ItemData(0x13005E, 1, 558, 0x36A7),
}
Accessory_Table = {
    ItemName.AbilityRing: ItemData(0x13005F, 1, 8, 0x3587),
    ItemName.EngineersRing: ItemData(0x130060, 1, 9, 0x3588),
    ItemName.TechniciansRing: ItemData(0x130061, 1, 10, 0x3589),
    ItemName.SkillRing: ItemData(0x130062, 1, 38, 0x359F),
    ItemName.SkillfulRing: ItemData(0x130063, 1, 39, 0x35A0),
    ItemName.ExpertsRing: ItemData(0x130064, 1, 11, 0x358A),
    ItemName.MastersRing: ItemData(0x130065, 1, 34, 0x359B),
    ItemName.CosmicRing: ItemData(0x130066, 1, 52, 0x35AD),
    ItemName.ExecutivesRing: ItemData(0x130067, 1, 599, 0x36B5),
    ItemName.SardonyxRing: ItemData(0x130068, 1, 12, 0x358B),
    ItemName.TourmalineRing: ItemData(0x130069, 1, 13, 0x358C),
    ItemName.AquamarineRing: ItemData(0x13006A, 1, 14, 0x358D),
    ItemName.GarnetRing: ItemData(0x13006B, 1, 15, 0x358E),
    ItemName.DiamondRing: ItemData(0x13006C, 1, 16, 0x358F),
    ItemName.SilverRing: ItemData(0x13006D, 1, 17, 0x3590),
    ItemName.GoldRing: ItemData(0x13006E, 1, 18, 0x3591),
    ItemName.PlatinumRing: ItemData(0x13006F, 1, 19, 0x3592),
    ItemName.MythrilRing: ItemData(0x130070, 1, 20, 0x3593),
    ItemName.OrichalcumRing: ItemData(0x130071, 1, 28, 0x359A),
    ItemName.SoldierEarring: ItemData(0x130072, 1, 40, 0x35A6),
    ItemName.FencerEarring: ItemData(0x130073, 1, 46, 0x35A7),
    ItemName.MageEarring: ItemData(0x130074, 1, 47, 0x35A8),
    ItemName.SlayerEarring: ItemData(0x130075, 1, 48, 0x35AC),
    ItemName.Medal: ItemData(0x130076, 1, 53, 0x35B2),
    ItemName.MoonAmulet: ItemData(0x130077, 1, 35, 0x359C),
    ItemName.StarCharm: ItemData(0x130078, 1, 36, 0x359E),
    ItemName.CosmicArts: ItemData(0x130079, 1, 56, 0x35B1),
    ItemName.ShadowArchive: ItemData(0x13007A, 1, 57, 0x35B2),
    ItemName.ShadowArchive2: ItemData(0x13007B, 1, 58, 0x35B7),
    ItemName.FullBloom: ItemData(0x13007C, 1, 64, 0x35B9),
    ItemName.FullBloom2: ItemData(0x13007D, 1, 66, 0x35BB),
    ItemName.DrawRing: ItemData(0x13007E, 1, 65, 0x35BA),
    ItemName.LuckyRing: ItemData(0x13007F, 1, 63, 0x35B8),
}
Armor_Table = {
    ItemName.ElvenBandana: ItemData(0x130080, 1, 67, 0x35BC),
    ItemName.DivineBandana: ItemData(0x130081, 1, 68, 0x35BD),
    ItemName.ProtectBelt: ItemData(0x130082, 1, 78, 0x35C7),
    ItemName.GaiaBelt: ItemData(0x130083, 1, 79, 0x35CA),
    ItemName.PowerBand: ItemData(0x130084, 1, 69, 0x35BE),
    ItemName.BusterBand: ItemData(0x130085, 1, 70, 0x35C6),
    ItemName.CosmicBelt: ItemData(0x130086, 1, 111, 0x35D1),
    ItemName.FireBangle: ItemData(0x130087, 1, 173, 0x35D7),
    ItemName.FiraBangle: ItemData(0x130088, 1, 174, 0x35D8),
    ItemName.FiragaBangle: ItemData(0x130089, 1, 197, 0x35D9),
    ItemName.FiragunBangle: ItemData(0x13008A, 1, 284, 0x35DA),
    ItemName.BlizzardArmlet: ItemData(0x13008B, 1, 286, 0x35DC),
    ItemName.BlizzaraArmlet: ItemData(0x13008C, 1, 287, 0x35DD),
    ItemName.BlizzagaArmlet: ItemData(0x13008D, 1, 288, 0x35DE),
    ItemName.BlizzagunArmlet: ItemData(0x13008E, 1, 289, 0x35DF),
    ItemName.ThunderTrinket: ItemData(0x13008F, 1, 291, 0x35E2),
    ItemName.ThundaraTrinket: ItemData(0x130090, 1, 292, 0x35E3),
    ItemName.ThundagaTrinket: ItemData(0x130091, 1, 293, 0x35E4),
    ItemName.ThundagunTrinket: ItemData(0x130092, 1, 294, 0x35E5),
    ItemName.ShockCharm: ItemData(0x130093, 1, 132, 0x35D2),
    ItemName.ShockCharm2: ItemData(0x130094, 1, 133, 0x35D3),
    ItemName.ShadowAnklet: ItemData(0x130095, 1, 296, 0x35F9),
    ItemName.DarkAnklet: ItemData(0x130096, 1, 297, 0x35FB),
    ItemName.MidnightAnklet: ItemData(0x130097, 1, 298, 0x35FC),
    ItemName.ChaosAnklet: ItemData(0x130098, 1, 299, 0x35FD),
    ItemName.ChampionBelt: ItemData(0x130099, 1, 305, 0x3603),
    ItemName.AbasChain: ItemData(0x13009A, 1, 301, 0x35FF),
    ItemName.AegisChain: ItemData(0x13009B, 1, 302, 0x3600),
    ItemName.Acrisius: ItemData(0x13009C, 1, 303, 0x3601),
    ItemName.Acrisius2: ItemData(0x13009D, 1, 307, 0x3605),
    ItemName.CosmicChain: ItemData(0x13009E, 1, 308, 0x3606),
    ItemName.PetiteRibbon: ItemData(0x13009F, 1, 306, 0x3604),
    ItemName.Ribbon: ItemData(0x1300A0, 1, 304, 0x3602),
    ItemName.GrandRibbon: ItemData(0x1300A1, 1, 157, 0x35D4),
}
Usefull_Table = {
    ItemName.MickyMunnyPouch: ItemData(0x1300A2, 1, 535, 0x3695),
    ItemName.OletteMunnyPouch: ItemData(0x1300A3, 1, 362, 0x363C),
    ItemName.HadesCupTrophy: ItemData(0x1300A4, 1, 537, 0x3696),
    ItemName.UnknownDisk: ItemData(0x1300A5, 1, 462, 0x365F),
    ItemName.OlympusStone: ItemData(0x1300A6, 1, 370, 0x3644),
    ItemName.MaxHPUp: ItemData(0x1300A7, 20, 470, 0x3671),
    ItemName.MaxMPUp: ItemData(0x1300A8, 4, 471, 0x3672),
    ItemName.DriveGaugeUp: ItemData(0x1300A9, 6, 472, 0x3673),
    ItemName.ArmorSlotUp: ItemData(0x1300AA, 3, 473, 0x3674),
    ItemName.AccessorySlotUp: ItemData(0x1300AB, 3, 474, 0x3675),
    ItemName.ItemSlotUp: ItemData(0x1300AC, 5, 463, 0x3660),
}
SupportAbility_Table = {
    ItemName.Scan: ItemData(0x1300AD, 2, 138, 0x08A, 0, True),
    ItemName.AerialRecovery: ItemData(0x1300AE, 1, 158, 0x09E, 0, True),
    ItemName.ComboMaster: ItemData(0x1300AF, 1, 539, 0x21B, 0, True),
    ItemName.ComboPlus: ItemData(0x1300B0, 3, 162, 0x0A2, 0, True),
    ItemName.AirComboPlus: ItemData(0x1300B1, 3, 163, 0x0A3, 0, True),
    ItemName.ComboBoost: ItemData(0x1300B2, 2, 390, 0x186, 0, True),
    ItemName.AirComboBoost: ItemData(0x1300B3, 2, 391, 0x187, 0, True),
    ItemName.ReactionBoost: ItemData(0x1300B4, 3, 392, 0x188, 0, True),
    ItemName.FinishingPlus: ItemData(0x1300B5, 3, 393, 0x189, 0, True),
    ItemName.NegativeCombo: ItemData(0x1300B6, 2, 394, 0x18A, 0, True),
    ItemName.BerserkCharge: ItemData(0x1300B7, 2, 395, 0x18B, 0, True),
    ItemName.DamageDrive: ItemData(0x1300B8, 2, 396, 0x18C, 0, True),
    ItemName.DriveBoost: ItemData(0x1300B9, 2, 397, 0x18D, 0, True),
    ItemName.FormBoost: ItemData(0x1300BA, 3, 398, 0x18E, 0, True),
    ItemName.SummonBoost: ItemData(0x1300BB, 1, 399, 0x18F, 0, True),
    ItemName.ExperienceBoost: ItemData(0x1300BC, 2, 401, 0x191, 0, True),
    ItemName.Draw: ItemData(0x1300BD, 4, 405, 0x195, 0, True),
    ItemName.Jackpot: ItemData(0x1300BE, 2, 406, 0x196, 0, True),
    ItemName.LuckyLucky: ItemData(0x1300BF, 3, 407, 0x197, 0, True),
    ItemName.DriveConverter: ItemData(0x1300C0, 2, 540, 0x21C, 0, True),
    ItemName.FireBoost: ItemData(0x1300C1, 2, 408, 0x198, 0, True),
    ItemName.BlizzardBoost: ItemData(0x1300C2, 2, 409, 0x199, 0, True),
    ItemName.ThunderBoost: ItemData(0x1300C3, 2, 410, 0x19A, 0, True),
    ItemName.ItemBoost: ItemData(0x1300C4, 2, 411, 0x19B, 0, True),
    ItemName.MPRage: ItemData(0x1300C5, 2, 412, 0x19C, 0, True),
    ItemName.MPHaste: ItemData(0x1300C6, 2, 413, 0x19D, 0, True),
    ItemName.MPHastera: ItemData(0x1300C7, 2, 421, 0x1A5, 0, True),
    ItemName.MPHastega: ItemData(0x1300C8, 1, 422, 0x1A6, 0, True),
    ItemName.Defender: ItemData(0x1300C9, 2, 414, 0x19E, 0, True),
    ItemName.DamageControl: ItemData(0x1300CA, 2, 542, 0x21E, 0, True),
    # one plandoed into the starting invo
    ItemName.NoExperience: ItemData(0x1300CB, 1, 404, 0x194, 0, True),
    ItemName.LightDarkness: ItemData(0x1300CC, 1, 541, 0x21D, 0, True),
    # These are found on levels in vanilla
    ItemName.MagicLock: ItemData(0x1300CD, 1, 403, 0x193, 0, True),
    ItemName.LeafBracer: ItemData(0x1300CE, 1, 402, 0x192, 0, True),
    ItemName.CombinationBoost: ItemData(0x1300CF, 1, 400, 0x190, 0, True),
    ItemName.OnceMore: ItemData(0x1300D0, 1, 416, 0x1A0, 0, True),
    ItemName.SecondChance: ItemData(0x1300D1, 1, 415, 0x19F, 0, True),
}
ActionAbility_Table = {
    ItemName.Guard: ItemData(0x1300D2, 1, 82, 0x052, 0, True),
    ItemName.UpperSlash: ItemData(0x1300D3, 1, 137, 0x089, 0, True),
    ItemName.HorizontalSlash: ItemData(0x1300D4, 1, 271, 0x10F, 0, True),
    ItemName.FinishingLeap: ItemData(0x1300D5, 1, 267, 0x10B, 0, True),
    ItemName.RetaliatingSlash: ItemData(0x1300D6, 1, 273, 0x111, 0, True),
    ItemName.Slapshot: ItemData(0x1300D7, 1, 262, 0x106, 0, True),
    ItemName.DodgeSlash: ItemData(0x1300D8, 1, 263, 0x107, 0, True),
    ItemName.FlashStep: ItemData(0x1300D9, 1, 559, 0x22F, 0, True),
    ItemName.SlideDash: ItemData(0x1300DA, 1, 264, 0x108, 0, True),
    ItemName.VicinityBreak: ItemData(0x1300DB, 1, 562, 0x232, 0, True),
    ItemName.GuardBreak: ItemData(0x1300DC, 1, 265, 0x109, 0, True),
    ItemName.Explosion: ItemData(0x1300DD, 1, 266, 0x10A, 0, True),
    ItemName.AerialSweep: ItemData(0x1300DE, 1, 269, 0x10D, 0, True),
    ItemName.AerialDive: ItemData(0x1300DF, 1, 560, 0x230, 0, True),
    ItemName.AerialSpiral: ItemData(0x1300E0, 1, 270, 0x10E, 0, True),
    ItemName.AerialFinish: ItemData(0x1300E1, 1, 272, 0x110, 0, True),
    ItemName.MagnetBurst: ItemData(0x1300E2, 1, 561, 0x231, 0, True),
    ItemName.Counterguard: ItemData(0x1300E3, 1, 268, 0x10C, 0, True),
    ItemName.AutoValor: ItemData(0x1300E4, 1, 385, 0x181, 0, True),
    ItemName.AutoWisdom: ItemData(0x1300E5, 1, 386, 0x182, 0, True),
    ItemName.AutoLimit: ItemData(0x1300E6, 1, 568, 0x238, 0, True),
    ItemName.AutoMaster: ItemData(0x1300E7, 1, 387, 0x183, 0, True),
    ItemName.AutoFinal: ItemData(0x1300E8, 1, 388, 0x184, 0, True),
    ItemName.AutoSummon: ItemData(0x1300E9, 1, 389, 0x185, 0, True),
    ItemName.TrinityLimit: ItemData(0x1300EA, 1, 198, 0x0C6, 0, True),
}
Items_Table = {
    ItemName.Potion: ItemData(0x1300EB, 1, 1, 0x3580),
    ItemName.HiPotion: ItemData(0x1300EC, 1, 2, 0x3581),
    ItemName.Ether: ItemData(0x1300ED, 1, 3, 0x3582),
    ItemName.Elixir: ItemData(0x1300EE, 1, 4, 0x3583),
    ItemName.MegaPotion: ItemData(0x1300EF, 1, 5, 0x3584),
    ItemName.MegaEther: ItemData(0x1300F0, 1, 6, 0x3585),
    ItemName.Megalixir: ItemData(0x1300F1, 1, 7, 0x3586),
    ItemName.Tent: ItemData(0x1300F2, 1, 131, 0x35E1),
    ItemName.DriveRecovery: ItemData(0x1300F3, 1, 274, 0x3664),
    ItemName.HighDriveRecovery: ItemData(0x1300F4, 1, 275, 0x3665),
    ItemName.PowerBoost: ItemData(0x1300F5, 1, 276, 0x3666),
    ItemName.MagicBoost: ItemData(0x1300F6, 1, 277, 0x3667),
    ItemName.DefenseBoost: ItemData(0x1300F7, 1, 278, 0x3668),
    ItemName.APBoost: ItemData(0x1300F8, 1, 279, 0x3669),
}

# These items cannot be in other games so these are done locally in kh2
DonaldAbility_Table = {
    ItemName.DonaldFire: ItemData(0x1300F9, 1, 165, 0x0A5, 0, True),
    ItemName.DonaldBlizzard: ItemData(0x1300FA, 1, 166, 0x0A6, 0, True),
    ItemName.DonaldThunder: ItemData(0x1300FB, 1, 167, 0x0A7, 0, True),
    ItemName.DonaldCure: ItemData(0x1300FC, 1, 168, 0x0A8, 0, True),
    ItemName.Fantasia: ItemData(0x1300FD, 1, 199, 0x0C7, 0, True),
    ItemName.FlareForce: ItemData(0x1300FE, 1, 200, 0x0C8, 0, True),
    ItemName.DonaldMPRage: ItemData(0x1300FF, 3, 412, 0x19C, 0, True),
    ItemName.DonaldJackpot: ItemData(0x130100, 1, 406, 0x196, 0, True),
    ItemName.DonaldLuckyLucky: ItemData(0x130101, 3, 407, 0x197, 0, True),
    ItemName.DonaldFireBoost: ItemData(0x130102, 2, 408, 0x198, 0, True),
    ItemName.DonaldBlizzardBoost: ItemData(0x130103, 2, 409, 0x199, 0, True),
    ItemName.DonaldThunderBoost: ItemData(0x130104, 2, 410, 0x19A, 0, True),
    ItemName.DonaldMPHaste: ItemData(0x130105, 1, 413, 0x19D, 0, True),
    ItemName.DonaldMPHastera: ItemData(0x130106, 2, 421, 0x1A5, 0, True),
    ItemName.DonaldMPHastega: ItemData(0x130107, 2, 422, 0x1A6, 0, True),
    ItemName.DonaldAutoLimit: ItemData(0x130108, 1, 417, 0x1A1, 0, True),
    ItemName.DonaldHyperHealing: ItemData(0x130109, 2, 419, 0x1A3, 0, True),
    ItemName.DonaldAutoHealing: ItemData(0x13010A, 1, 420, 0x1A4, 0, True),
    ItemName.DonaldItemBoost: ItemData(0x13010B, 1, 411, 0x19B, 0, True),
    ItemName.DonaldDamageControl: ItemData(0x13010C, 2, 542, 0x21E, 0, True),
    ItemName.DonaldDraw: ItemData(0x13010D, 1, 405, 0x195, 0, True),
}  # 32
GoofyAbility_Table = {
    ItemName.GoofyTornado: ItemData(0x13010E, 1, 423, 0x1A7, 0, True),
    ItemName.GoofyTurbo: ItemData(0x13010F, 1, 425, 0x1A9, 0, True),
    ItemName.GoofyBash: ItemData(0x130110, 1, 429, 0x1AD, 0, True),
    ItemName.TornadoFusion: ItemData(0x130111, 1, 201, 0x0C9, 0, True),
    ItemName.Teamwork: ItemData(0x130112, 1, 202, 0x0CA, 0, True),
    ItemName.GoofyDraw: ItemData(0x130113, 1, 405, 0x195, 0, True),
    ItemName.GoofyJackpot: ItemData(0x130114, 1, 406, 0x196, 0, True),
    ItemName.GoofyLuckyLucky: ItemData(0x130115, 1, 407, 0x197, 0, True),
    ItemName.GoofyItemBoost: ItemData(0x130116, 2, 411, 0x19B, 0, True),
    ItemName.GoofyMPRage: ItemData(0x130117, 2, 412, 0x19C, 0, True),
    ItemName.GoofyDefender: ItemData(0x130118, 2, 414, 0x19E, 0, True),
    ItemName.GoofyDamageControl: ItemData(0x130119, 3, 542, 0x21E, 0, True),
    ItemName.GoofyAutoLimit: ItemData(0x13011A, 1, 417, 0x1A1, 0, True),
    ItemName.GoofySecondChance: ItemData(0x13011B, 1, 415, 0x19F, 0, True),
    ItemName.GoofyOnceMore: ItemData(0x13011C, 1, 416, 0x1A0, 0, True),
    ItemName.GoofyAutoChange: ItemData(0x13011D, 1, 418, 0x1A2, 0, True),
    ItemName.GoofyHyperHealing: ItemData(0x13011E, 2, 419, 0x1A3, 0, True),
    ItemName.GoofyAutoHealing: ItemData(0x13011F, 1, 420, 0x1A4, 0, True),
    ItemName.GoofyMPHaste: ItemData(0x130120, 1, 413, 0x19D, 0, True),
    ItemName.GoofyMPHastera: ItemData(0x130121, 1, 421, 0x1A5, 0, True),
    ItemName.GoofyMPHastega: ItemData(0x130122, 1, 422, 0x1A6, 0, True),
    ItemName.GoofyProtect: ItemData(0x130123, 2, 596, 0x254, 0, True),
    ItemName.GoofyProtera: ItemData(0x130124, 2, 597, 0x255, 0, True),
    ItemName.GoofyProtega: ItemData(0x130125, 2, 598, 0x256, 0, True),

}

Misc_Table = {
    ItemName.LuckyEmblem: ItemData(0x130126, 0, 367, 0x3641),#letter item
    ItemName.Victory: ItemData(0x130127, 1, 263, 0x111),
    ItemName.UltimaWeaponPiece1:ItemData(0x130128   ,0,250,0x36C7,2),#Halloween town Map
    ItemName.UltimaWeaponPiece2:ItemData(0x130129   ,0,251,0x36C7,3),#Naval map
    ItemName.UltimaWeaponPiece3:ItemData(0x13012A   ,0,252,0x36C7,4),#Pride Rock Map
    ItemName.UltimaWeaponPiece4:ItemData(0x13012B   ,0,253,0x36C7,5),#marketplace map
    ItemName.UltimaWeaponPiece5:ItemData(0x13012C   ,0,254,0x36C7,6),#pit cell area map
    ItemName.UltimaWeaponPiece6:ItemData(0x13012D   ,0,255,0x36C7,7),#twlight town map
    ItemName.UltimaWeaponPiece7:ItemData(0x13012E   ,0,256,0x36C8,0),#dark city map
    ItemName.UltimaWeaponPiece8:ItemData(0x13012F   ,0,506,0x36C8,1),#the black pearl map
    ItemName.UltimaWeaponPiece9:ItemData(0x130130   ,0,507,0x36C8,2),#isla de muerta map
    ItemName.UltimaWeaponPiece10:ItemData(0x130131  ,0,508,0x36C8,3),#ship graveyard map

    ItemName.UniversalKey:ItemData(0x130132,0,90,0x36C1,0)#Castle Map
    #ItemName.PaopuFruit:ItemData(0x130132,0,127,0x36C1,0)#dummy item to open the final door
}

exclusionItem_table = {
    "Ability": {
        ItemName.Scan,
        ItemName.AerialRecovery,
        ItemName.ComboMaster,
        ItemName.ComboPlus,
        ItemName.AirComboPlus,
        ItemName.ComboBoost,
        ItemName.AirComboBoost,
        ItemName.ReactionBoost,
        ItemName.FinishingPlus,
        ItemName.NegativeCombo,
        ItemName.BerserkCharge,
        ItemName.DamageDrive,
        ItemName.DriveBoost,
        ItemName.FormBoost,
        ItemName.SummonBoost,
        ItemName.ExperienceBoost,
        ItemName.Draw,
        ItemName.Jackpot,
        ItemName.LuckyLucky,
        ItemName.DriveConverter,
        ItemName.FireBoost,
        ItemName.BlizzardBoost,
        ItemName.ThunderBoost,
        ItemName.ItemBoost,
        ItemName.MPRage,
        ItemName.MPHaste,
        ItemName.MPHastera,
        ItemName.MPHastega,
        ItemName.Defender,
        ItemName.DamageControl,
        ItemName.NoExperience,
        ItemName.LightDarkness,
        ItemName.MagicLock,
        ItemName.LeafBracer,
        ItemName.CombinationBoost,
        ItemName.DamageDrive,
        ItemName.OnceMore,
        ItemName.SecondChance,
        ItemName.Guard,
        ItemName.UpperSlash,
        ItemName.HorizontalSlash,
        ItemName.FinishingLeap,
        ItemName.RetaliatingSlash,
        ItemName.Slapshot,
        ItemName.DodgeSlash,
        ItemName.FlashStep,
        ItemName.SlideDash,
        ItemName.VicinityBreak,
        ItemName.GuardBreak,
        ItemName.Explosion,
        ItemName.AerialSweep,
        ItemName.AerialDive,
        ItemName.AerialSpiral,
        ItemName.AerialFinish,
        ItemName.MagnetBurst,
        ItemName.Counterguard,
        ItemName.AutoValor,
        ItemName.AutoWisdom,
        ItemName.AutoLimit,
        ItemName.AutoMaster,
        ItemName.AutoFinal,
        ItemName.AutoSummon,
        ItemName.TrinityLimit,
        ItemName.HighJump,
        ItemName.QuickRun,
        ItemName.DodgeRoll,
        ItemName.AerialDodge,
        ItemName.Glide,

    },
    "StatUps": {
        ItemName.MaxHPUp,
        ItemName.MaxMPUp,
        ItemName.DriveGaugeUp,
        ItemName.ArmorSlotUp,
        ItemName.AccessorySlotUp,
        ItemName.ItemSlotUp,
    },
    "Forms": {
        ItemName.ValorForm,
        ItemName.WisdomForm,
        ItemName.LimitForm,
        ItemName.MasterForm,
        ItemName.FinalForm,

    },
    "Schmovement": {
        ItemName.HighJump,
        ItemName.QuickRun,
        ItemName.DodgeRoll,
        ItemName.AerialDodge,
        ItemName.Glide,
    }
}

item_dictionary_table = {**Reports_Table,
                         **Progression_Table,
                         **Forms_Table,
                         **Magic_Table,
                         **Armor_Table,
                         **Movement_Table,
                         **Staffs_Table,
                         **Shields_Table,
                         **Keyblade_Table,
                         **Accessory_Table,
                         **Usefull_Table,
                         **SupportAbility_Table,
                         **ActionAbility_Table,
                         **Items_Table,
                         **Misc_Table,
                         **Items_Table,
                         **DonaldAbility_Table,
                         **GoofyAbility_Table,
                         }

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_dictionary_table.items() if
                                            data.code}
# lookup_kh2id_to_name: typing.Dict[int, str] = {data.kh2id: item_name for item_name, data in
#                                               item_dictionary_table.items() if data.kh2id}
