import typing

from BaseClasses import Item, ItemClassification
from .Names import ItemName


class KH2Item(Item):
    game: str = "Kingdom Hearts 2"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    kh2id: int
    quantity: int = 1
    event: bool = False


Reports_Table = {
    ItemName.SecretAnsemsReport1: ItemData(0x1320027, False, 226),
    ItemName.SecretAnsemsReport2: ItemData(0x1320028, False, 227),
    ItemName.SecretAnsemsReport3: ItemData(0x1320029, False, 228),
    ItemName.SecretAnsemsReport4: ItemData(0x1320030, False, 229),
    ItemName.SecretAnsemsReport5: ItemData(0x1320031, False, 230),
    ItemName.SecretAnsemsReport6: ItemData(0x1320032, False, 231),
    ItemName.SecretAnsemsReport7: ItemData(0x1320033, False, 232),
    ItemName.SecretAnsemsReport8: ItemData(0x1320034, False, 233),
    ItemName.SecretAnsemsReport9: ItemData(0x1320035, False, 234),
    ItemName.SecretAnsemsReport10: ItemData(0x1320036, False, 235),
    ItemName.SecretAnsemsReport11: ItemData(0x1320037, False, 236),
    ItemName.SecretAnsemsReport12: ItemData(0x1320038, False, 237),
    ItemName.SecretAnsemsReport13: ItemData(0x1320039, False, 238),
}

Progression_Table = {
    ItemName.ProofofConnection: ItemData(0x1320040, False, 593),
    ItemName.ProofofNonexistence: ItemData(0x1320041, False, 594),
    ItemName.ProofofPeace: ItemData(0x1320042, False, 595),
    ItemName.PromiseCharm: ItemData(0x1320043, False, 524),
    ItemName.NamineSketches: ItemData(0x132016c, False, 368),
    ItemName.CastleKey: ItemData(0x132016d, False, 460),
    ItemName.BattlefieldsofWar: ItemData(0x1320044, False, 54),
    ItemName.SwordoftheAncestor: ItemData(0x1320045, False, 55),
    ItemName.BeastsClaw: ItemData(0x1320046, False, 59),
    ItemName.BoneFist: ItemData(0x1320047, False, 60),
    ItemName.ProudFang: ItemData(0x1320048, False, 61),
    ItemName.SkillandCrossbones: ItemData(0x1320049, False, 62),
    ItemName.Scimitar: ItemData(0x132004a, False, 72),
    ItemName.MembershipCard: ItemData(0x132004b, False, 369),
    ItemName.IceCream: ItemData(0x132004c, False, 375),
    ItemName.Picture: ItemData(0x132004d, False, 376),
    ItemName.WaytotheDawn: ItemData(0x132004e, False, 73),
    ItemName.IdentityDisk: ItemData(0x132004f, False, 74),
    ItemName.Poster: ItemData(0x1320050, False, 366),
    ItemName.TornPages: ItemData(0x1320051, False, 32),
    ItemName.TornPages: ItemData(0x1320052, False, 32),
    ItemName.TornPages: ItemData(0x1320053, False, 32),
    ItemName.TornPages: ItemData(0x1320054, False, 32),
    ItemName.TornPages: ItemData(0x1320055, False, 32),

}
Forms_Table = {
    ItemName.ValorForm: ItemData(0x1320056, False, 26),
    ItemName.WisdomForm: ItemData(0x1320057, False, 27),
    ItemName.LimitForm: ItemData(0x1320058, False, 563),
    ItemName.MasterForm: ItemData(0x1320059, False, 31),
    ItemName.FinalForm: ItemData(0x132005a, False, 29),
}
Magic_Table = {
    ItemName.FireElement: ItemData(0x132005b, False, 21),

    ItemName.BlizzardElement: ItemData(0x132005e, False, 22),

    ItemName.ThunderElement: ItemData(0x1320061, False, 23),

    ItemName.CureElement: ItemData(0x1320064, False, 24),

    ItemName.MagnetElement: ItemData(0x1320067, False, 87),

    ItemName.ReflectElement: ItemData(0x132006a, False, 88),

    ItemName.Genie: ItemData(0x132006d, False, 159),
    ItemName.PeterPan: ItemData(0x132006e, False, 160),
    ItemName.Stitch: ItemData(0x132006f, False, 25),
    ItemName.ChickenLittle: ItemData(0x1320070, False, 383),
}

Movement_Table = {
    ItemName.HighJump: ItemData(0x1320071, False, 94),
    ItemName.HighJump2: ItemData(0x1320072, False, 95),
    ItemName.HighJump3: ItemData(0x1320073, False, 96),
    ItemName.HighJump4: ItemData(0x1320074, False, 97),

    ItemName.QuickRun: ItemData(0x1320075, False, 98),
    ItemName.QuickRun2: ItemData(0x1320076, False, 99),
    ItemName.QuickRun3: ItemData(0x1320077, False, 100),
    ItemName.QuickRun4: ItemData(0x1320078, False, 101),

    ItemName.AerialDodge: ItemData(0x1320079, False, 102),
    ItemName.AerialDodge2: ItemData(0x132007a, False, 103),
    ItemName.AerialDodge3: ItemData(0x132007b, False, 104),
    ItemName.AerialDodge4: ItemData(0x132007c, False, 105),

    ItemName.Glide: ItemData(0x132007d, False, 106),
    ItemName.Glide2: ItemData(0x132007e, False, 107),
    ItemName.Glide3: ItemData(0x132007f, False, 108),
    ItemName.Glide4: ItemData(0x1320080, False, 109),

    ItemName.DodgeRoll: ItemData(0x1320081, False, 564),
    ItemName.DodgeRoll2: ItemData(0x1320082, False, 565),
    ItemName.DodgeRoll3: ItemData(0x1320083, False, 566),
    ItemName.DodgeRoll4: ItemData(0x1320084, False, 567),
}

Keyblade_Table = {
    ItemName.Oathkeeper: ItemData(0x1320085, False, 42),
    ItemName.Oblivion: ItemData(0x1320086, False, 43),
    ItemName.StarSeeker: ItemData(0x1320087, False, 480),
    ItemName.HiddenDragon: ItemData(0x1320088, False, 481),
    ItemName.HerosCrest: ItemData(0x1320089, False, 484),
    ItemName.Monochrome: ItemData(0x132008a, False, 485),
    ItemName.FollowtheWind: ItemData(0x132008b, False, 486),
    ItemName.CircleofLife: ItemData(0x132008c, False, 487),
    ItemName.PhotonDebugger: ItemData(0x132008d, False, 488),
    ItemName.GullWing: ItemData(0x132008e, False, 489),
    ItemName.RumblingRose: ItemData(0x132008f, False, 490),
    ItemName.GuardianSoul: ItemData(0x1320090, False, 491),
    ItemName.WishingLamp: ItemData(0x1320091, False, 492),
    ItemName.DecisivePumpkin: ItemData(0x1320092, False, 493),
    ItemName.SleepingLion: ItemData(0x1320093, False, 494),
    ItemName.SweetMemories: ItemData(0x1320094, False, 495),
    ItemName.MysteriousAbyss: ItemData(0x1320095, False, 496),
    ItemName.TwoBecomeOne: ItemData(0x1320096, False, 543),
    ItemName.FatalCrest: ItemData(0x1320097, False, 497),
    ItemName.BondofFlame: ItemData(0x1320098, False, 498),
    ItemName.Fenrir: ItemData(0x1320099, False, 499),
    ItemName.UltimaWeapon: ItemData(0x132009a, False, 500),
    ItemName.WinnersProof: ItemData(0x132009b, False, 544),
    ItemName.Pureblood: ItemData(0x132009c, False, 71),
}
Staffs_Table = {
    ItemName.Centurion2: ItemData(0x132009d, False, 546),
    ItemName.MeteorStaff: ItemData(0x132009e, False, 150),
    ItemName.NobodyLance: ItemData(0x132009f, False, 155),
    ItemName.PreciousMushroom: ItemData(0x13200a0, False, 549),
    ItemName.PreciousMushroom2: ItemData(0x13200a1, False, 550),
    ItemName.PremiumMushroom: ItemData(0x13200a2, False, 551),
    ItemName.RisingDragon: ItemData(0x13200a3, False, 154),
    ItemName.SaveTheQueen2: ItemData(0x13200a4, False, 503),
    ItemName.ShamansRelic: ItemData(0x13200a5, False, 156),
}
Shields_Table = {
    ItemName.AkashicRecord: ItemData(0x13200a6, False, 146),
    ItemName.FrozenPride2: ItemData(0x13200a7, False, 553),
    ItemName.GenjiShield: ItemData(0x13200a8, False, 145),
    ItemName.MajesticMushroom: ItemData(0x13200a9, False, 556),
    ItemName.MajesticMushroom2: ItemData(0x13200aa, False, 557),
    ItemName.NobodyGuard: ItemData(0x13200ab, False, 147),
    ItemName.OgreShield: ItemData(0x13200ac, False, 141),
    ItemName.SaveTheKing2: ItemData(0x13200ad, False, 504),
    ItemName.UltimateMushroom: ItemData(0x13200ae, False, 558),
}
Accessory_Table = {
    ItemName.AbilityRing: ItemData(0x13200af, False, 8),
    ItemName.EngineersRing: ItemData(0x13200b0, False, 9),
    ItemName.TechniciansRing: ItemData(0x13200b1, False, 10),
    ItemName.SkillRing: ItemData(0x13200b2, False, 38),
    ItemName.SkillfulRing: ItemData(0x13200b3, False, 39),
    ItemName.ExpertsRing: ItemData(0x13200b4, False, 11),
    ItemName.MastersRing: ItemData(0x13200b5, False, 34),
    ItemName.CosmicRing: ItemData(0x13200b6, False, 52),
    ItemName.ExecutivesRing: ItemData(0x13200b7, False, 599),
    ItemName.SardonyxRing: ItemData(0x13200b8, False, 12),
    ItemName.TourmalineRing: ItemData(0x13200b9, False, 13),
    ItemName.AquamarineRing: ItemData(0x13200ba, False, 14),
    ItemName.GarnetRing: ItemData(0x13200bb, False, 15),
    ItemName.DiamondRing: ItemData(0x13200bc, False, 16),
    ItemName.SilverRing: ItemData(0x13200bd, False, 17),
    ItemName.GoldRing: ItemData(0x13200be, False, 18),
    ItemName.PlatinumRing: ItemData(0x13200bf, False, 19),
    ItemName.MythrilRing: ItemData(0x13200c0, False, 20),
    ItemName.OrichalcumRing: ItemData(0x13200c1, False, 28),
    ItemName.SoldierEarring: ItemData(0x13200c2, False, 40),
    ItemName.FencerEarring: ItemData(0x13200c3, False, 46),
    ItemName.MageEarring: ItemData(0x13200c4, False, 47),
    ItemName.SlayerEarring: ItemData(0x13200c5, False, 48),
    ItemName.Medal: ItemData(0x13200c6, False, 53),
    ItemName.MoonAmulet: ItemData(0x13200c7, False, 35),
    ItemName.StarCharm: ItemData(0x13200c8, False, 36),
    ItemName.CosmicArts: ItemData(0x13200c9, False, 56),
    ItemName.ShadowArchive: ItemData(0x13200ca, False, 57),
    ItemName.ShadowArchive2: ItemData(0x13200cb, False, 58),
    ItemName.FullBloom: ItemData(0x13200cc, False, 64),
    ItemName.FullBloom2: ItemData(0x13200cd, False, 66),
    ItemName.DrawRing: ItemData(0x13200ce, False, 65),
    ItemName.LuckyRing: ItemData(0x13200cf, False, 63),
}
Armor_Table = {
    ItemName.ElvenBandana: ItemData(0x13200d0, False, 67),
    ItemName.DivineBandana: ItemData(0x13200d1, False, 68),
    ItemName.ProtectBelt: ItemData(0x13200d2, False, 78),
    ItemName.GaiaBelt: ItemData(0x13200d3, False, 79),
    ItemName.PowerBand: ItemData(0x13200d4, False, 69),
    ItemName.BusterBand: ItemData(0x13200d5, False, 70),
    ItemName.CosmicBelt: ItemData(0x13200d6, False, 111),
    ItemName.FireBangle: ItemData(0x13200d7, False, 173),
    ItemName.FiraBangle: ItemData(0x13200d8, False, 174),
    ItemName.FiragaBangle: ItemData(0x13200d9, False, 197),
    ItemName.FiragunBangle: ItemData(0x13200da, False, 284),
    ItemName.BlizzardArmlet: ItemData(0x13200db, False, 286),
    ItemName.BlizzaraArmlet: ItemData(0x13200dc, False, 287),
    ItemName.BlizzagaArmlet: ItemData(0x13200dd, False, 288),
    ItemName.BlizzagunArmlet: ItemData(0x13200de, False, 289),
    ItemName.ThunderTrinket: ItemData(0x13200df, False, 291),
    ItemName.ThundaraTrinket: ItemData(0x13200e0, False, 292),
    ItemName.ThundagaTrinket: ItemData(0x13200e1, False, 293),
    ItemName.ThundagunTrinket: ItemData(0x13200e2, False, 294),
    ItemName.ShockCharm: ItemData(0x13200e3, False, 132),
    ItemName.ShockCharm2: ItemData(0x13200e4, False, 133),
    ItemName.ShadowAnklet: ItemData(0x13200e5, False, 296),
    ItemName.DarkAnklet: ItemData(0x13200e6, False, 297),
    ItemName.MidnightAnklet: ItemData(0x13200e7, False, 298),
    ItemName.ChaosAnklet: ItemData(0x13200e8, False, 299),
    ItemName.ChampionBelt: ItemData(0x13200e9, False, 305),
    ItemName.AbasChain: ItemData(0x13200ea, False, 301),
    ItemName.AegisChain: ItemData(0x13200eb, False, 302),
    ItemName.Acrisius: ItemData(0x13200ec, False, 303),
    ItemName.Acrisius2: ItemData(0x13200ed, False, 307),
    ItemName.CosmicChain: ItemData(0x13200ee, False, 308),
    ItemName.PetiteRibbon: ItemData(0x13200ef, False, 306),
    ItemName.Ribbon: ItemData(0x13200f0, False, 304),
    ItemName.GrandRibbon: ItemData(0x13200f1, False, 157),
}
Usefull_Table = {
    ItemName.MickyMunnyPouch : ItemData(0x13200f2, False, 535),
    ItemName.OletteMunnyPouch : ItemData(0x13200f3, False, 362),
    ItemName.HadesCupTrophy: ItemData(0x13200f4, False, 537),
    ItemName.UnknownDisk: ItemData(0x13200f5, False, 462),
    ItemName.OlympusStone: ItemData(0x13200f6, False, 370),
    ItemName.MaxHPUp: ItemData(0x13200f7, False, 470),
    ItemName.MaxMPUp: ItemData(0x13200f8, False, 471),
    ItemName.DriveGaugeUp: ItemData(0x13200f9, False, 472),
    ItemName.ArmorSlotUp: ItemData(0x13200fa, False, 473),
    ItemName.AccessorySlotUp: ItemData(0x13200fb, False, 474),
    ItemName.ItemSlotUp: ItemData(0x13200fc, False, 463),
}
SupportAbility_Table = {
    ItemName.Scan: ItemData(0x13200fd, False, 138),
    ItemName.Scan2: ItemData(0x13200fe, False, 138),
    ItemName.AerialRecovery: ItemData(0x13200ff, False, 158),
    ItemName.ComboMaster: ItemData(0x1320100, False, 539),
    ItemName.ComboPlus: ItemData(0x1320101, False, 162),
    ItemName.ComboPlus2: ItemData(0x1320102, False, 162),
    ItemName.ComboPlus3: ItemData(0x1320103, False, 162),
    ItemName.AirComboPlus: ItemData(0x1320104, False, 163),
    ItemName.AirComboPlus2: ItemData(0x1320105, False, 163),
    ItemName.AirComboPlus3: ItemData(0x1320106, False, 163),
    ItemName.ComboBoost: ItemData(0x1320107, False, 390),
    ItemName.AirComboBoost: ItemData(0x1320108, False, 391),
    ItemName.ReactionBoost: ItemData(0x1320109, False, 392),
    ItemName.ReactionBoost2: ItemData(0x132010a, False, 392),
    ItemName.FinishingPlus: ItemData(0x132010b, False, 393),
    ItemName.FinishingPlus2: ItemData(0x132010c, False, 393),
    ItemName.NegativeCombo: ItemData(0x132010d, False, 394),
    ItemName.BerserkCharge: ItemData(0x132010e, False, 395),
    ItemName.DamageDrive: ItemData(0x132010f, False, 396),
    ItemName.DriveBoost: ItemData(0x1320110, False, 397),
    ItemName.FormBoost: ItemData(0x1320111, False, 398),
    ItemName.FormBoost2: ItemData(0x1320112, False, 398),
    ItemName.FormBoost3: ItemData(0x1320113, False, 398),
    ItemName.SummonBoost: ItemData(0x1320114, False, 399),
    ItemName.ExperienceBoost: ItemData(0x1320115, False, 401),
    ItemName.Draw: ItemData(0x1320116, False, 405),
    ItemName.Draw2: ItemData(0x1320117, False, 405),
    ItemName.Draw3: ItemData(0x1320118, False, 405),
    ItemName.Jackpot: ItemData(0x1320119, False, 406),
    ItemName.LuckyLucky: ItemData(0x132011a, False, 407),
    ItemName.LuckyLucky2: ItemData(0x132011b, False, 407),
    ItemName.LuckyLucky3: ItemData(0x132011c, False, 407),
    ItemName.DriveConverter: ItemData(0x132011d, False, 540),
    ItemName.FireBoost: ItemData(0x132011e, False, 408),
    ItemName.BlizzardBoost: ItemData(0x132011f, False, 409),
    ItemName.ThunderBoost: ItemData(0x1320120, False, 410),
    ItemName.ItemBoost: ItemData(0x1320121, False, 411),
    ItemName.MPRage: ItemData(0x1320122, False, 412),
    ItemName.MPRage2: ItemData(0x1320123, False, 412),
    ItemName.MPHaste: ItemData(0x1320124, False, 413),
    ItemName.MPHaste2: ItemData(0x1320125, False, 413),
    ItemName.MPHastera: ItemData(0x1320126, False, 421),
    ItemName.MPHastera2: ItemData(0x1320127, False, 421),
    ItemName.MPHastega: ItemData(0x1320128, False, 422),
    ItemName.Defender: ItemData(0x1320129, False, 414),
    ItemName.DamageControl: ItemData(0x132012a, False, 542),
    ItemName.NoExperience: ItemData(0x132012b, False, 404),
    ItemName.NoExperience2: ItemData(0x132012c, False, 404),
    ItemName.LightDarkness: ItemData(0x132012d, False, 541),
}
LvlAbility_Table = {
    ItemName.ComboBoost2: ItemData(0x132012e, False, 390),
    ItemName.ExperienceBoost2: ItemData(0x132012f, False, 401),
    ItemName.MagicLock: ItemData(0x1320130, False, 403),
    ItemName.ReactionBoost3: ItemData(0x1320131, False, 392),
    ItemName.ItemBoost2: ItemData(0x1320132, False, 411),
    ItemName.LeafBracer: ItemData(0x1320133, False, 402),
    ItemName.FireBoost2: ItemData(0x1320134, False, 408),
    ItemName.DriveBoost2: ItemData(0x1320135, False, 397),
    ItemName.Draw4: ItemData(0x1320136, False, 405),
    ItemName.CombinationBoost: ItemData(0x1320137, False, 400),
    ItemName.DamageDrive: ItemData(0x1320138, False, 396),
    ItemName.AirComboBoost2: ItemData(0x1320139, False, 391),
    ItemName.BlizzardBoost2: ItemData(0x132013a, False, 409),
    ItemName.DriveConverter2: ItemData(0x132013b, False, 540),
    ItemName.NegativeCombo2: ItemData(0x132013c, False, 394),
    ItemName.OnceMore: ItemData(0x132013d, False, 416),
    ItemName.FinishingPlus3: ItemData(0x132013e, False, 393),
    ItemName.ThunderBoost2: ItemData(0x132013f, False, 410),
    ItemName.Defender2: ItemData(0x1320140, False, 414),
    ItemName.BerserkCharge2: ItemData(0x1320141, False, 395),
    ItemName.Jackpot2: ItemData(0x1320142, False, 406),
    ItemName.SecondChance: ItemData(0x1320143, False, 415),
    ItemName.DamageControl2: ItemData(0x1320144, False, 542),
}
ActionAbility_Table = {
    ItemName.Guard: ItemData(0x1320145, False, 82),
    ItemName.UpperSlash: ItemData(0x1320146, False, 137),
    ItemName.HorizontalSlash: ItemData(0x1320147, False, 271),
    ItemName.FinishingLeap: ItemData(0x1320148, False, 267),
    ItemName.RetaliatingSlash: ItemData(0x1320149, False, 273),
    ItemName.Slapshot: ItemData(0x132014a, False, 262),
    ItemName.DodgeSlash: ItemData(0x132014b, False, 263),
    ItemName.FlashStep: ItemData(0x132014c, False, 559),
    ItemName.SlideDash: ItemData(0x132014d, False, 264),
    ItemName.VicinityBreak: ItemData(0x132014e, False, 562),
    ItemName.GuardBreak: ItemData(0x132014f, False, 265),
    ItemName.Explosion: ItemData(0x1320150, False, 266),
    ItemName.AerialSweep: ItemData(0x1320151, False, 269),
    ItemName.AerialDive: ItemData(0x1320152, False, 560),
    ItemName.AerialSpiral: ItemData(0x1320153, False, 270),
    ItemName.AerialFinish: ItemData(0x1320154, False, 272),
    ItemName.MagnetBurst: ItemData(0x1320155, False, 561),
    ItemName.Counterguard: ItemData(0x1320156, False, 268),
    ItemName.AutoValor: ItemData(0x1320157, False, 385),
    ItemName.AutoWisdom: ItemData(0x1320158, False, 386),
    ItemName.AutoLimit: ItemData(0x1320159, False, 568),
    ItemName.AutoMaster: ItemData(0x132015a, False, 387),
    ItemName.AutoFinal: ItemData(0x132015b, False, 388),
    ItemName.AutoSummon: ItemData(0x132015c, False, 389),
    ItemName.TrinityLimit: ItemData(0x132015d, False, 198),
}
Items_Table = {
    ItemName.Potion: ItemData(0x132015e, False, 1),
    ItemName.HiPotion: ItemData(0x132015f, False, 2),
    ItemName.Ether: ItemData(0x1320160, False, 3),
    ItemName.Elixir: ItemData(0x1320161, False, 4),
    ItemName.MegaPotion: ItemData(0x1320162, False, 5),
    ItemName.MegaEther: ItemData(0x1320163, False, 6),
    ItemName.Megalixir: ItemData(0x1320164, False, 7),
    ItemName.Tent: ItemData(0x1320165, False, 131),
    ItemName.DriveRecovery: ItemData(0x1320166, False, 274),
    ItemName.HighDriveRecovery: ItemData(0x1320167, False, 275),
    ItemName.PowerBoost: ItemData(0x1320168, False, 276),
    ItemName.MagicBoost: ItemData(0x1320169, False, 277),
    ItemName.DefenseBoost: ItemData(0x132016a, False, 278),
    ItemName.APBoost: ItemData(0x132016b, False, 279),
}

# These items cannot be in other games so these are done locally in kh2
DonaldAbility_Table = {
    ItemName.DonaldFire: ItemData(0x132016c, False, 165),
    ItemName.DonaldBlizzard: ItemData(0x132016d, False, 166),
    ItemName.DonaldThunder: ItemData(0x132016e, False, 167),
    ItemName.DonaldCure: ItemData(0x132016f, False, 168),
    ItemName.Fantasia: ItemData(0x1320170, False, 199),
    ItemName.FlareForce: ItemData(0x1320171, False, 200),
    ItemName.DonaldMPRage: ItemData(0x1320172, False, 412),
    ItemName.DonaldJackpot: ItemData(0x1320173, False, 406),
    ItemName.DonaldLuckyLucky: ItemData(0x1320174, False, 407),
    ItemName.DonaldFireBoost: ItemData(0x1320175, False, 408),
    ItemName.DonaldBlizzardBoost: ItemData(0x1320176, False, 409),
    ItemName.DonaldThunderBoost: ItemData(0x1320177, False, 410),
    ItemName.DonaldFireBoost: ItemData(0x1320178, False, 408),
    ItemName.DonaldBlizzardBoost: ItemData(0x1320179, False, 409),
    ItemName.DonaldThunderBoost: ItemData(0x132017a, False, 410),
    ItemName.DonaldMPRage: ItemData(0x132017b, False, 412),
    ItemName.DonaldMPHastera: ItemData(0x132017c, False, 421),
    ItemName.DonaldAutoLimit: ItemData(0x132017d, False, 417),
    ItemName.DonaldHyperHealing: ItemData(0x132017e, False, 419),
    ItemName.DonaldAutoHealing: ItemData(0x132017f, False, 420),
    ItemName.DonaldMPHastega: ItemData(0x1320180, False, 422),
    ItemName.DonaldItemBoost: ItemData(0x1320181, False, 411),
    ItemName.DonaldDamageControl: ItemData(0x1320182, False, 542),
    ItemName.DonaldHyperHealing: ItemData(0x1320183, False, 419),
    ItemName.DonaldMPRage: ItemData(0x1320184, False, 412),
    ItemName.DonaldMPHaste: ItemData(0x1320185, False, 413),
    ItemName.DonaldMPHastera: ItemData(0x1320186, False, 421),
    ItemName.DonaldMPHastega: ItemData(0x1320187, False, 422),
    ItemName.DonaldMPHaste: ItemData(0x1320188, False, 413),
    ItemName.DonaldDamageControl: ItemData(0x1320189, False, 542),
    ItemName.DonaldMPHastera: ItemData(0x132018a, False, 421),
    ItemName.DonaldDraw: ItemData(0x132018b, False, 405),
}
GoofyAbility_Table = {
    ItemName.GoofyTornado: ItemData(0x132018c, False, 423),
    ItemName.GoofyTurbo: ItemData(0x132018d, False, 425),
    ItemName.GoofyBash: ItemData(0x132018e, False, 429),
    ItemName.TornadoFusion: ItemData(0x132018f, False, 201),
    ItemName.Teamwork: ItemData(0x1320190, False, 202),
    ItemName.GoofyDraw: ItemData(0x1320191, False, 405),
    ItemName.GoofyJackpot: ItemData(0x1320192, False, 406),
    ItemName.GoofyLuckyLucky: ItemData(0x1320193, False, 407),
    ItemName.GoofyItemBoost: ItemData(0x1320194, False, 411),
    ItemName.GoofyMPRage: ItemData(0x1320195, False, 412),
    ItemName.GoofyDefender: ItemData(0x1320196, False, 414),
    ItemName.GoofyDamageControl: ItemData(0x1320197, False, 542),
    ItemName.GoofyAutoLimit: ItemData(0x1320198, False, 417),
    ItemName.GoofySecondChance: ItemData(0x1320199, False, 415),
    ItemName.GoofyOnceMore: ItemData(0x132019a, False, 416),
    ItemName.GoofyAutoChange: ItemData(0x132019b, False, 418),
    ItemName.GoofyHyperHealing: ItemData(0x132019c, False, 419),
    ItemName.GoofyAutoHealing: ItemData(0x132019d, False, 420),
    ItemName.GoofyDefender: ItemData(0x132019e, False, 414),
    ItemName.GoofyHyperHealing: ItemData(0x132019f, False, 419),
    ItemName.GoofyMPHaste: ItemData(0x13201a0, False, 413),
    ItemName.GoofyMPHastera: ItemData(0x13201a1, False, 421),
    ItemName.GoofyMPRage: ItemData(0x13201a2, False, 412),
    ItemName.GoofyMPHastega: ItemData(0x13201a3, False, 422),
    ItemName.GoofyItemBoost: ItemData(0x13201a4, False, 411),
    ItemName.GoofyDamageControl: ItemData(0x13201a5, False, 542),
    ItemName.GoofyProtect: ItemData(0x13201a6, False, 596),
    ItemName.GoofyProtera: ItemData(0x13201a7, False, 597),
    ItemName.GoofyProtega: ItemData(0x13201a8, False, 598),
    ItemName.GoofyDamageControl: ItemData(0x13201a9, False, 542),
    ItemName.GoofyProtect: ItemData(0x13201aa, False, 596),
    ItemName.GoofyProtera: ItemData(0x13201ab, False, 597),
    ItemName.GoofyProtega: ItemData(0x13201ac, False, 598),
}

Misc_Table = {
    ItemName.Nothing: ItemData(0x132016c, False, 1),
    ItemName.Victory: ItemData(0x132016d, False, 1, True),
}
# Required items for the Rules
# This is basiccly checking how many of the items you have
# Thanks for reading this you a homie :)
required_items = {
    ItemName.FireElement: 3,
    ItemName.BlizzardElement: 3,
    ItemName.ThunderElement: 3,
    ItemName.CureElement: 3,
    ItemName.MagnetElement: 3,
    ItemName.ReflectElement: 3,
    ItemName.HighJump: 4,
    ItemName.QuickRun: 4,
    ItemName.AerialDodge: 4,
    ItemName.DodgeRoll: 4,
    ItemName.Glide: 4,
    ItemName.TornPages: 5,
    ItemName.BattlefieldsofWar: 1,
    ItemName.SwordoftheAncestor: 1,
    ItemName.BeastsClaw: 1,
    ItemName.BoneFist: 1,
    ItemName.ProudFang: 1,
    ItemName.SkillandCrossbones: 1,
    ItemName.Scimitar: 1,
    ItemName.MembershipCard: 1,
    ItemName.IceCream: 1,
    ItemName.Picture: 1,
    ItemName.WaytotheDawn: 1,
    ItemName.IdentityDisk: 1,
}
# there are 541 locations and 379 items
# This means we need to add some filler
# some numbers are taken from vanilla kh2 some are just out of my ass
exclusionItem_table = {
    "Ability": {
        ItemName.Scan,
        ItemName.Scan2,
        ItemName.AerialRecovery,
        ItemName.ComboMaster,
        ItemName.ComboPlus,
        ItemName.ComboPlus2,
        ItemName.ComboPlus3,
        ItemName.AirComboPlus,
        ItemName.AirComboPlus2,
        ItemName.AirComboPlus3,
        ItemName.ComboBoost,
        ItemName.AirComboBoost,
        ItemName.ReactionBoost,
        ItemName.ReactionBoost2,
        ItemName.FinishingPlus,
        ItemName.FinishingPlus2,
        ItemName.NegativeCombo,
        ItemName.BerserkCharge,
        ItemName.DamageDrive,
        ItemName.DriveBoost,
        ItemName.FormBoost,
        ItemName.FormBoost2,
        ItemName.FormBoost3,
        ItemName.SummonBoost,
        ItemName.ExperienceBoost,
        ItemName.Draw,
        ItemName.Draw2,
        ItemName.Draw3,
        ItemName.Jackpot,
        ItemName.LuckyLucky,
        ItemName.LuckyLucky2,
        ItemName.LuckyLucky3,
        ItemName.DriveConverter,
        ItemName.FireBoost,
        ItemName.BlizzardBoost,
        ItemName.ThunderBoost,
        ItemName.ItemBoost,
        ItemName.MPRage,
        ItemName.MPRage2,
        ItemName.MPHaste,
        ItemName.MPHaste2,
        ItemName.MPHastera,
        ItemName.MPHastera2,
        ItemName.MPHastega,
        ItemName.Defender,
        ItemName.DamageControl,
        ItemName.NoExperience,
        ItemName.NoExperience2,
        ItemName.LightDarkness,
        ItemName.ComboBoost2,
        ItemName.ExperienceBoost2,
        ItemName.MagicLock,
        ItemName.ReactionBoost3,
        ItemName.ItemBoost2,
        ItemName.LeafBracer,
        ItemName.FireBoost2,
        ItemName.DriveBoost2,
        ItemName.Draw4,
        ItemName.CombinationBoost,
        ItemName.DamageDrive,
        ItemName.AirComboBoost2,
        ItemName.BlizzardBoost2,
        ItemName.DriveConverter2,
        ItemName.NegativeCombo2,
        ItemName.OnceMore,
        ItemName.FinishingPlus3,
        ItemName.ThunderBoost2,
        ItemName.Defender2,
        ItemName.BerserkCharge2,
        ItemName.Jackpot2,
        ItemName.SecondChance,
        ItemName.DamageControl2,
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
        ItemName.HighJump2,
        ItemName.HighJump3,
        ItemName.HighJump4,
        ItemName.QuickRun,
        ItemName.QuickRun2,
        ItemName.QuickRun3,
        ItemName.QuickRun4,
        ItemName.AerialDodge,
        ItemName.AerialDodge2,
        ItemName.AerialDodge3,
        ItemName.AerialDodge4,
        ItemName.Glide,
        ItemName.Glide2,
        ItemName.Glide3,
        ItemName.Glide4,
        ItemName.DodgeRoll,
        ItemName.DodgeRoll2,
        ItemName.DodgeRoll3,
        ItemName.DodgeRoll4,
        # these are not abilitys need to add a lua increase category for forbidding items
        ItemName.MaxHPUp,
        ItemName.MaxMPUp,
        ItemName.DriveGaugeUp,
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
# Abilites that could be on keyblades
keybladeAbilities = [
    ItemName.Scan,
    ItemName.Scan2,
    ItemName.AerialRecovery,
    ItemName.ComboMaster,
    ItemName.ComboPlus,
    ItemName.ComboPlus2,
    ItemName.ComboPlus3,
    ItemName.AirComboPlus,
    ItemName.AirComboPlus2,
    ItemName.AirComboPlus3,
    ItemName.ComboBoost,
    ItemName.AirComboBoost,
    ItemName.ReactionBoost,
    ItemName.ReactionBoost2,
    ItemName.FinishingPlus,
    ItemName.FinishingPlus2,
    ItemName.NegativeCombo,
    ItemName.BerserkCharge,
    ItemName.DamageDrive,
    ItemName.DriveBoost,
    ItemName.FormBoost,
    ItemName.FormBoost2,
    ItemName.FormBoost3,
    ItemName.SummonBoost,
    ItemName.ExperienceBoost,
    ItemName.Draw,
    ItemName.Draw2,
    ItemName.Draw3,
    ItemName.Jackpot,
    ItemName.LuckyLucky,
    ItemName.LuckyLucky2,
    ItemName.LuckyLucky3,
    ItemName.DriveConverter,
    ItemName.FireBoost,
    ItemName.BlizzardBoost,
    ItemName.ThunderBoost,
    ItemName.ItemBoost,
    ItemName.MPRage,
    ItemName.MPRage2,
    ItemName.MPHaste,
    ItemName.MPHaste2,
    ItemName.MPHastera,
    ItemName.MPHastera2,
    ItemName.MPHastega,
    ItemName.Defender,
    ItemName.DamageControl,
    ItemName.NoExperience,
    ItemName.NoExperience2,
    ItemName.LightDarkness,
    ItemName.ComboBoost2,
    ItemName.ExperienceBoost2,
    ItemName.MagicLock,
    ItemName.ReactionBoost3,
    ItemName.ItemBoost2,
    ItemName.LeafBracer,
    ItemName.FireBoost2,
    ItemName.DriveBoost2,
    ItemName.Draw4,
    ItemName.CombinationBoost,
    ItemName.DamageDrive,
    ItemName.AirComboBoost2,
    ItemName.BlizzardBoost2,
    ItemName.DriveConverter2,
    ItemName.NegativeCombo2,
    ItemName.OnceMore,
    ItemName.FinishingPlus3,
    ItemName.ThunderBoost2,
    ItemName.Defender2,
    ItemName.BerserkCharge2,
    ItemName.Jackpot2,
    ItemName.SecondChance,
    ItemName.DamageControl2,
    ItemName.AutoValor,
    ItemName.AutoWisdom,
    ItemName.AutoLimit,
    ItemName.AutoMaster,
    ItemName.AutoFinal,
    ItemName.AutoSummon,
]
# donald abiltys that are only donalds
donaldAbility = [
    ItemName.DonaldFire,
    ItemName.DonaldBlizzard,
    ItemName.DonaldThunder,
    ItemName.DonaldCure,
    ItemName.Fantasia,
    ItemName.FlareForce,
    ItemName.DonaldMPRage,
    ItemName.DonaldJackpot,
    ItemName.DonaldLuckyLucky,
    ItemName.DonaldFireBoost,
    ItemName.DonaldBlizzardBoost,
    ItemName.DonaldThunderBoost,
    ItemName.DonaldFireBoost,
    ItemName.DonaldBlizzardBoost,
    ItemName.DonaldThunderBoost,
    ItemName.DonaldMPRage,
    ItemName.DonaldMPHastera,
    ItemName.DonaldAutoLimit,
    ItemName.DonaldHyperHealing,
    ItemName.DonaldAutoHealing,
    ItemName.DonaldMPHastega,
    ItemName.DonaldItemBoost,
    ItemName.DonaldDamageControl,
    ItemName.DonaldHyperHealing,
    ItemName.DonaldMPRage,
    ItemName.DonaldMPHaste,
    ItemName.DonaldMPHastera,
    ItemName.DonaldMPHastega,
    ItemName.DonaldMPHaste,
    ItemName.DonaldDamageControl,
    ItemName.DonaldMPHastera,
    ItemName.DonaldDraw,
]
goofyAbility = [
    ItemName.GoofyTornado,
    ItemName.GoofyTurbo,
    ItemName.GoofyBash,
    ItemName.TornadoFusion,
    ItemName.Teamwork,
    ItemName.GoofyDraw,
    ItemName.GoofyJackpot,
    ItemName.GoofyLuckyLucky,
    ItemName.GoofyItemBoost,
    ItemName.GoofyMPRage,
    ItemName.GoofyDefender,
    ItemName.GoofyDamageControl,
    ItemName.GoofyAutoLimit,
    ItemName.GoofySecondChance,
    ItemName.GoofyOnceMore,
    ItemName.GoofyAutoChange,
    ItemName.GoofyHyperHealing,
    ItemName.GoofyAutoHealing,
    ItemName.GoofyDefender,
    ItemName.GoofyHyperHealing,
    ItemName.GoofyMPHaste,
    ItemName.GoofyMPHastera,
    ItemName.GoofyMPRage,
    ItemName.GoofyMPHastega,
    ItemName.GoofyItemBoost,
    ItemName.GoofyDamageControl,
    ItemName.GoofyProtect,
    ItemName.GoofyProtera,
    ItemName.GoofyProtega,
    ItemName.GoofyDamageControl,
    ItemName.GoofyProtect,
    ItemName.GoofyProtera,
    ItemName.GoofyProtega,
]
junk_weights = {
    ItemName.Potion: 34,
    ItemName.Ether: 26,
    ItemName.PowerBoost: 10,
    ItemName.MagicBoost: 10,
    ItemName.DefenseBoost: 10,
    ItemName.APBoost: 66,
    ItemName.DriveRecovery: 10,
    ItemName.HighDriveRecovery: 5,
    ItemName.Megalixir: 5,
    ItemName.Elixir: 5,
    ItemName.Tent: 5,
    ItemName.MaxHPUp: 20,
    ItemName.MaxMPUp: 4,
    ItemName.DriveGaugeUp: 6,
    ItemName.ArmorSlotUp: 3,
    ItemName.AccessorySlotUp: 3,
    ItemName.ItemSlotUp: 5,
}

item_dictionary_table = {**Reports_Table,
                         **Progression_Table,
                         **Forms_Table,
                         **Magic_Table,
                         **Armor_Table,
                         **Movement_Table,
                         **Shields_Table,
                         **Keyblade_Table,
                         **Accessory_Table,
                         **Usefull_Table,
                         **SupportAbility_Table,
                         **LvlAbility_Table,
                         **ActionAbility_Table,
                         **Items_Table,
                         **Misc_Table,
                         **Items_Table,
                         **DonaldAbility_Table,
                         **GoofyAbility_Table,
                         }

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_dictionary_table.items() if
                                            data.code}
lookup_kh2id_to_name: typing.Dict[int, str] = {data.kh2id: item_name for item_name, data in
                                               item_dictionary_table.items() if data.kh2id}
