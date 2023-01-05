from optparse import Option
import typing

from BaseClasses import Item, ItemClassification
from .Names import ItemName


class KH2Item(Item):
    game: str = "Kingdom Hearts 2"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
   
    kh2id: int
    #Save+ mem addr
    memaddr: int
    #some items have bitmasks. if bitmask>0 bitor to give item else 
    #if kh2id is > than everything before it and < everything after than use write short
    #OR include a boolean
    bitmask: int = 0
    quantity: int = 1
    #if ability then 
    ability: bool = False
    event: bool = False


Reports_Table = {
    ItemName.SecretAnsemsReport1: ItemData(0x1320027,  226, 0x36C4 ,0x40),
    ItemName.SecretAnsemsReport2: ItemData(0x1320028,  227, 0x36C4 ,0x80),
    ItemName.SecretAnsemsReport3: ItemData(0x1320029,  228, 0x36C5 ,0x1),
    ItemName.SecretAnsemsReport4: ItemData(0x1320030,  229, 0x36C5 ,0x2),
    ItemName.SecretAnsemsReport5: ItemData(0x1320031,  230, 0x36C5 ,0x4),
    ItemName.SecretAnsemsReport6: ItemData(0x1320032,  231, 0x36C5 ,0x8),
    ItemName.SecretAnsemsReport7: ItemData(0x1320033,  232, 0x36C5 ,0x10),
    ItemName.SecretAnsemsReport8: ItemData(0x1320034,  233, 0x36C5 ,0x20),
    ItemName.SecretAnsemsReport9: ItemData(0x1320035,  234, 0x36C5 ,0x40),
    ItemName.SecretAnsemsReport10: ItemData(0x1320036,  235,0x36C5 ,0x80),
    ItemName.SecretAnsemsReport11: ItemData(0x1320037,  236, 0x36C6 ,0x1),
    ItemName.SecretAnsemsReport12: ItemData(0x1320038,  237, 0x36C6 ,0x2),
    ItemName.SecretAnsemsReport13: ItemData(0x1320039,  238, 0x36C6 ,0x4),
}

Progression_Table = {
    ItemName.ProofofConnection: ItemData(0x1320040,  593, 0x36B0 ),
    ItemName.ProofofNonexistence: ItemData(0x1320041,  594, 0x36B3 ),
    ItemName.ProofofPeace: ItemData(0x1320042,  595, 0x36B4 ),
    ItemName.PromiseCharm: ItemData(0x1320043,  524, 0x3694 ),
    ItemName.NamineSketches: ItemData(0x132016c,  368, 0x3642 ),
    #dummy 13
    ItemName.CastleKey: ItemData(0x132016d,  460, 0x365D ),
    ItemName.BattlefieldsofWar: ItemData(0x1320044,  54, 0x35AE ),
    ItemName.SwordoftheAncestor: ItemData(0x1320045,  55, 0x35AF ),
    ItemName.BeastsClaw: ItemData(0x1320046,  59, 0x35B3 ),
    ItemName.BoneFist: ItemData(0x1320047,  60, 0x35B4 ),
    ItemName.ProudFang: ItemData(0x1320048,  61, 0x35B5 ),
    ItemName.SkillandCrossbones: ItemData(0x1320049,  62, 0x35B6 ),
    ItemName.Scimitar: ItemData(0x132004a,  72, 0x35C0 ),
    ItemName.MembershipCard: ItemData(0x132004b,  369, 0x3643 ),
    ItemName.IceCream: ItemData(0x132004c,  375, 0x3649 ),
    ItemName.Picture: ItemData(0x132004d,  376, 0x364A ),
    ItemName.WaytotheDawn: ItemData(0x132004e,  73, 0x35C1 ),
    ItemName.IdentityDisk: ItemData(0x132004f,  74, 0x35C2 ),
    ItemName.Poster: ItemData(0x1320050,  366, 0x3640 ),
    #This only needs to be one tornpage
    ItemName.TornPages: ItemData(0x1320051,  32, 0x3598),
    ItemName.TornPages: ItemData(0x1320052,  32, 0x3598),
    ItemName.TornPages: ItemData(0x1320053,  32, 0x3598),
    ItemName.TornPages: ItemData(0x1320054,  32, 0x3598),
    ItemName.TornPages: ItemData(0x1320055,  32, 0x3598),

}
Forms_Table = {
    ItemName.ValorForm: ItemData(0x1320056,  26, 0x36C0,1),
    ItemName.WisdomForm: ItemData(0x1320057,  27, 0x36C0,2),
    ItemName.LimitForm: ItemData(0x1320058,  563, 0x36CA,8),
    ItemName.MasterForm: ItemData(0x1320059,  31, 0x36C0,40),
    ItemName.FinalForm: ItemData(0x132005a,  29, 0x36C0,10),
}
Magic_Table = {
    ItemName.FireElement: ItemData(0x132005b,  21, 0x3594 ),

    ItemName.BlizzardElement: ItemData(0x132005e,  22, 0x3595 ),

    ItemName.ThunderElement: ItemData(0x1320061,  23, 0x3596 ),

    ItemName.CureElement: ItemData(0x1320064,  24, 0x3597 ),

    ItemName.MagnetElement: ItemData(0x1320067,  87, 0x35CF ),

    ItemName.ReflectElement: ItemData(0x132006a,  88, 0x35D0 ),

    ItemName.Genie: ItemData(0x132006d,  159, 0x36C4,0x10 ),
    ItemName.PeterPan: ItemData(0x132006e,  160, 0x36C4,0x20 ),
    ItemName.Stitch: ItemData(0x132006f,  25, 0x36C0,0x1 ),
    ItemName.ChickenLittle: ItemData(0x1320070,  383, 0x36C0,0x8 ),
}

Movement_Table = {
    #        const int ADDRESS_START = 0x2544;
    #        const int ADDRESS_END = 0x25CC;
    #kh2.write_short(kh2.base_address + Save+ADDRESS_END, 0x05E)
    #For each abilit sent to sora -2 from address_end
    ItemName.HighJump: ItemData(0x1320071,  94,0x05E,True),
    ItemName.HighJump2: ItemData(0x1320072,  95,0x05E,True),
    ItemName.HighJump3: ItemData(0x1320073,  96,0x05E,True),
    ItemName.HighJump4: ItemData(0x1320074,  97,0x05E,True),

    ItemName.QuickRun: ItemData(0x1320075,   98, 0x062,True),
    ItemName.QuickRun2: ItemData(0x1320076,  99, 0x062,True),
    ItemName.QuickRun3: ItemData(0x1320077,  100,0x062,True),
    ItemName.QuickRun4: ItemData(0x1320078,  101,0x062,True),

    ItemName.AerialDodge: ItemData(0x1320079,  102,  0x066,True),
    ItemName.AerialDodge2: ItemData(0x132007a,  103, 0x066,True),
    ItemName.AerialDodge3: ItemData(0x132007b,  104, 0x066,True),
    ItemName.AerialDodge4: ItemData(0x132007c,  105, 0x066,True),

    ItemName.Glide: ItemData(0x132007d,  106,  0x06A,True),
    ItemName.Glide2: ItemData(0x132007e,  107, 0x06A,True),
    ItemName.Glide3: ItemData(0x132007f,  108, 0x06A,True),
    ItemName.Glide4: ItemData(0x1320080,  109, 0x06A,True),

    ItemName.DodgeRoll: ItemData(0x1320081,  564,  0x234,True ),
    ItemName.DodgeRoll2: ItemData(0x1320082,  565, 0x234,True ),
    ItemName.DodgeRoll3: ItemData(0x1320083,  566, 0x234,True ),
    ItemName.DodgeRoll4: ItemData(0x1320084,  567, 0x234,True ),
}

Keyblade_Table = {
    ItemName.Oathkeeper: ItemData(0x1320085,  42, 0x35A2 ),
    ItemName.Oblivion: ItemData(0x1320086,  43, 0x35A3 ),
    ItemName.StarSeeker: ItemData(0x1320087,  480, 0x367B ),
    ItemName.HiddenDragon: ItemData(0x1320088,  481, 0x367C ),
    ItemName.HerosCrest: ItemData(0x1320089,  484, 0x367F ),
    ItemName.Monochrome: ItemData(0x132008a,  485, 0x3680 ),
    ItemName.FollowtheWind: ItemData(0x132008b,  486, 0x3681 ),
    ItemName.CircleofLife: ItemData(0x132008c,  487, 0x3682 ),
    ItemName.PhotonDebugger: ItemData(0x132008d,  488, 0x3683 ),
    ItemName.GullWing: ItemData(0x132008e,  489, 0x3684 ),
    ItemName.RumblingRose: ItemData(0x132008f,  490, 0x3685 ),
    ItemName.GuardianSoul: ItemData(0x1320090,  491, 0x3686 ),
    ItemName.WishingLamp: ItemData(0x1320091,  492, 0x3687 ),
    ItemName.DecisivePumpkin: ItemData(0x1320092,  493, 0x3688 ),
    ItemName.SleepingLion: ItemData(0x1320093,  494, 0x3689 ),
    ItemName.SweetMemories: ItemData(0x1320094,  495, 0x368A ),
    ItemName.MysteriousAbyss: ItemData(0x1320095,  496, 0x368B ),
    ItemName.TwoBecomeOne: ItemData(0x1320096,  543, 0x3698 ),
    ItemName.FatalCrest: ItemData(0x1320097,  497, 0x368C ),
    ItemName.BondofFlame: ItemData(0x1320098,  498, 0x368D ),
    ItemName.Fenrir: ItemData(0x1320099,  499, 0x368E ),
    ItemName.UltimaWeapon: ItemData(0x132009a,  500, 0x368F ),
    ItemName.WinnersProof: ItemData(0x132009b,  544, 0x3699 ),
    ItemName.Pureblood: ItemData(0x132009c,  71, 0x35BF ),
}
Staffs_Table = {
    ItemName.Centurion2: ItemData(0x132009d,  546, 0x369B ),
    ItemName.MeteorStaff: ItemData(0x132009e,  150, 0x35F1 ),
    ItemName.NobodyLance: ItemData(0x132009f,  155, 0x35F6 ),
    ItemName.PreciousMushroom: ItemData(0x13200a0,  549, 0x369E ),
    ItemName.PreciousMushroom2: ItemData(0x13200a1,  550, 0x369F ),
    ItemName.PremiumMushroom: ItemData(0x13200a2,  551, 0x36A0 ),
    ItemName.RisingDragon: ItemData(0x13200a3,  154, 0x35F5 ),
    ItemName.SaveTheQueen2: ItemData(0x13200a4,  503, 0x3692 ),
    ItemName.ShamansRelic: ItemData(0x13200a5,  156, 0x35F7 ),
}
Shields_Table = {
    ItemName.AkashicRecord: ItemData(0x13200a6,  146, 0x35ED ),
    ItemName.FrozenPride2: ItemData(0x13200a7,  553, 0x36A2 ),
    ItemName.GenjiShield: ItemData(0x13200a8,  145, 0x35EC ),
    ItemName.MajesticMushroom: ItemData(0x13200a9,  556, 0x36A5 ),
    ItemName.MajesticMushroom2: ItemData(0x13200aa,  557, 0x36A6 ),
    ItemName.NobodyGuard: ItemData(0x13200ab,  147, 0x35EE ),
    ItemName.OgreShield: ItemData(0x13200ac,  141, 0x35E8 ),
    ItemName.SaveTheKing2: ItemData(0x13200ad,  504, 0x3693 ),
    ItemName.UltimateMushroom: ItemData(0x13200ae,  558, 0x36A7 ),
}
Accessory_Table = {
    ItemName.AbilityRing: ItemData(0x13200af,  8, 0x3587 ),
    ItemName.EngineersRing: ItemData(0x13200b0,  9, 0x3588 ),
    ItemName.TechniciansRing: ItemData(0x13200b1,  10, 0x3589 ),
    ItemName.SkillRing: ItemData(0x13200b2,  38, 0x359F ),
    ItemName.SkillfulRing: ItemData(0x13200b3,  39, 0x35A0 ),
    ItemName.ExpertsRing: ItemData(0x13200b4,  11, 0x358A ),
    ItemName.MastersRing: ItemData(0x13200b5,  34, 0x359B ),
    ItemName.CosmicRing: ItemData(0x13200b6,  52, 0x35AD ),
    ItemName.ExecutivesRing: ItemData(0x13200b7,  599, 0x36B5 ),
    ItemName.SardonyxRing: ItemData(0x13200b8,  12, 0x358B ),
    ItemName.TourmalineRing: ItemData(0x13200b9,  13, 0x358C ),
    ItemName.AquamarineRing: ItemData(0x13200ba,  14, 0x358D ),
    ItemName.GarnetRing: ItemData(0x13200bb,  15, 0x358E ),
    ItemName.DiamondRing: ItemData(0x13200bc,  16, 0x358F ),
    ItemName.SilverRing: ItemData(0x13200bd,  17, 0x3590 ),
    ItemName.GoldRing: ItemData(0x13200be,  18, 0x3591 ),
    ItemName.PlatinumRing: ItemData(0x13200bf,  19, 0x3592 ),
    ItemName.MythrilRing: ItemData(0x13200c0,  20, 0x3593 ),
    ItemName.OrichalcumRing: ItemData(0x13200c1,  28, 0x359A ),
    ItemName.SoldierEarring: ItemData(0x13200c2,  40, 0x35A6 ),
    ItemName.FencerEarring: ItemData(0x13200c3,  46, 0x35A7 ),
    ItemName.MageEarring: ItemData(0x13200c4,  47, 0x35A8 ),
    ItemName.SlayerEarring: ItemData(0x13200c5,  48, 0x35AC ),
    ItemName.Medal: ItemData(0x13200c6,  53, 0x35B2 ),
    ItemName.MoonAmulet: ItemData(0x13200c7,  35, 0x359C ),
    ItemName.StarCharm: ItemData(0x13200c8,  36, 0x359E ),
    ItemName.CosmicArts: ItemData(0x13200c9,  56, 0x35B1 ),
    ItemName.ShadowArchive: ItemData(0x13200ca,  57, 0x35B2 ),
    ItemName.ShadowArchive2: ItemData(0x13200cb,  58, 0x35B7 ),
    ItemName.FullBloom: ItemData(0x13200cc,  64, 0x35B9 ),
    ItemName.FullBloom2: ItemData(0x13200cd,  66, 0x35BB ),
    ItemName.DrawRing: ItemData(0x13200ce,  65, 0x35BA ),
    ItemName.LuckyRing: ItemData(0x13200cf,  63, 0x35B8 ),
}
Armor_Table = {
    ItemName.ElvenBandana: ItemData(0x13200d0,  67, 0x35BC ),
    ItemName.DivineBandana: ItemData(0x13200d1,  68, 0x35BD ),
    ItemName.ProtectBelt: ItemData(0x13200d2,  78, 0x35C7 ),
    ItemName.GaiaBelt: ItemData(0x13200d3,  79, 0x35CA ),
    ItemName.PowerBand: ItemData(0x13200d4,  69, 0x35BE ),
    ItemName.BusterBand: ItemData(0x13200d5,  70, 0x35C6 ),
    ItemName.CosmicBelt: ItemData(0x13200d6,  111, 0x35D1 ),
    ItemName.FireBangle: ItemData(0x13200d7,  173, 0x35D7 ),
    ItemName.FiraBangle: ItemData(0x13200d8,  174, 0x35D8 ),
    ItemName.FiragaBangle: ItemData(0x13200d9,  197, 0x35D9 ),
    ItemName.FiragunBangle: ItemData(0x13200da,  284, 0x35DA ),
    ItemName.BlizzardArmlet: ItemData(0x13200db,  286, 0x35DC ),
    ItemName.BlizzaraArmlet: ItemData(0x13200dc,  287, 0x35DD ),
    ItemName.BlizzagaArmlet: ItemData(0x13200dd,  288, 0x35DE ),
    ItemName.BlizzagunArmlet: ItemData(0x13200de,  289, 0x35DF ),
    ItemName.ThunderTrinket: ItemData(0x13200df,  291, 0x35E2 ),
    ItemName.ThundaraTrinket: ItemData(0x13200e0,  292, 0x35E3 ),
    ItemName.ThundagaTrinket: ItemData(0x13200e1,  293, 0x35E4 ),
    ItemName.ThundagunTrinket: ItemData(0x13200e2,  294, 0x35E5 ),
    ItemName.ShockCharm: ItemData(0x13200e3,  132, 0x35D2 ),
    ItemName.ShockCharm2: ItemData(0x13200e4,  133, 0x35D3 ),
    ItemName.ShadowAnklet: ItemData(0x13200e5,  296, 0x35F9 ),
    ItemName.DarkAnklet: ItemData(0x13200e6,  297, 0x35FB ),
    ItemName.MidnightAnklet: ItemData(0x13200e7,  298, 0x35FC ),
    ItemName.ChaosAnklet: ItemData(0x13200e8,  299, 0x35FD ),
    ItemName.ChampionBelt: ItemData(0x13200e9,  305, 0x3603 ),
    ItemName.AbasChain: ItemData(0x13200ea,  301, 0x35FF ),
    ItemName.AegisChain: ItemData(0x13200eb,  302, 0x3600 ),
    ItemName.Acrisius: ItemData(0x13200ec,  303, 0x3601 ),
    ItemName.Acrisius2: ItemData(0x13200ed,  307, 0x3605 ),
    ItemName.CosmicChain: ItemData(0x13200ee,  308, 0x3606 ),
    ItemName.PetiteRibbon: ItemData(0x13200ef,  306, 0x3604 ),
    ItemName.Ribbon: ItemData(0x13200f0,  304, 0x3602 ),
    ItemName.GrandRibbon: ItemData(0x13200f1,  157, 0x35D4 ),
}
Usefull_Table = {
    ItemName.MickyMunnyPouch : ItemData(0x13200f2,  535, 0x3695 ),
    ItemName.OletteMunnyPouch : ItemData(0x13200f3,  362, 0x363C ),
    ItemName.HadesCupTrophy: ItemData(0x13200f4,  537, 0x3696 ),
    ItemName.UnknownDisk: ItemData(0x13200f5,  462, 0x365F ),
    ItemName.OlympusStone: ItemData(0x13200f6,  370, 0x3644 ),
    ItemName.MaxHPUp: ItemData(0x13200f7,  470, 0x3671 ),
    ItemName.MaxMPUp: ItemData(0x13200f8,  471, 0x3672 ),
    ItemName.DriveGaugeUp: ItemData(0x13200f9,  472, 0x3673 ),
    ItemName.ArmorSlotUp: ItemData(0x13200fa,  473, 0x3674 ),
    ItemName.AccessorySlotUp: ItemData(0x13200fb,  474, 0x3675 ),
    ItemName.ItemSlotUp: ItemData(0x13200fc,  463, 0x3660 ),
}
SupportAbility_Table = {
    ItemName.Scan: ItemData(0x13200fd,  138, 0x08A,True ),
    ItemName.Scan2: ItemData(0x13200fe,  138, 0x08A , True ),
    ItemName.AerialRecovery: ItemData(0x13200ff,  158, 0x09E , True ),
    ItemName.ComboMaster: ItemData(0x1320100,  539, 0x21B , True ),
    ItemName.ComboPlus: ItemData(0x1320101,  162, 0x0A2 , True ),
    ItemName.ComboPlus2: ItemData(0x1320102,  162, 0x0A2 , True ),
    ItemName.ComboPlus3: ItemData(0x1320103,  162, 0x0A2 , True ),
    ItemName.AirComboPlus: ItemData(0x1320104,  163, 0x0A3 , True ),
    ItemName.AirComboPlus2: ItemData(0x1320105,  163, 0x0A3 , True ),
    ItemName.AirComboPlus3: ItemData(0x1320106,  163, 0x0A3 , True ),
    ItemName.ComboBoost: ItemData(0x1320107,  390, 0x186 , True ),
    ItemName.AirComboBoost: ItemData(0x1320108,  391, 0x187 , True ),
    ItemName.ReactionBoost: ItemData(0x1320109,  392, 0x188 , True ),
    ItemName.ReactionBoost2: ItemData(0x132010a,  392, 0x188 , True ),
    ItemName.FinishingPlus: ItemData(0x132010b,  393, 0x189 , True ),
    ItemName.FinishingPlus2: ItemData(0x132010c,  393, 0x189 , True ),
    ItemName.NegativeCombo: ItemData(0x132010d,  394, 0x18A , True ),
    ItemName.BerserkCharge: ItemData(0x132010e,  395, 0x18B , True ),
    ItemName.DamageDrive: ItemData(0x132010f,  396, 0x18C , True ),
    ItemName.DriveBoost: ItemData(0x1320110,  397, 0x18D , True ),
    ItemName.FormBoost: ItemData(0x1320111,  398, 0x18E , True ),
    ItemName.FormBoost2: ItemData(0x1320112,  398, 0x18E , True ),
    ItemName.FormBoost3: ItemData(0x1320113,  398, 0x18E , True ),
    ItemName.SummonBoost: ItemData(0x1320114,  399, 0x18F , True ),
    ItemName.ExperienceBoost: ItemData(0x1320115,  401, 0x191 , True ),
    ItemName.Draw: ItemData(0x1320116,  405, 0x195 , True ),
    ItemName.Draw2: ItemData(0x1320117,  405, 0x195 , True ),
    ItemName.Draw3: ItemData(0x1320118,  405, 0x195 , True ),
    ItemName.Jackpot: ItemData(0x1320119,  406, 0x196 , True ),
    ItemName.LuckyLucky: ItemData(0x132011a,  407, 0x197 , True ),
    ItemName.LuckyLucky2: ItemData(0x132011b,  407, 0x197 , True ),
    ItemName.LuckyLucky3: ItemData(0x132011c,  407, 0x197 , True ),
    ItemName.DriveConverter: ItemData(0x132011d,  540, 0x21C , True ),
    ItemName.FireBoost: ItemData(0x132011e,  408, 0x198 , True ),
    ItemName.BlizzardBoost: ItemData(0x132011f,  409, 0x199 , True ),
    ItemName.ThunderBoost: ItemData(0x1320120,  410, 0x19A , True ),
    ItemName.ItemBoost: ItemData(0x1320121,  411, 0x19B , True ),
    ItemName.MPRage: ItemData(0x1320122,  412, 0x19C , True ),
    ItemName.MPRage2: ItemData(0x1320123,  412, 0x19C , True ),
    ItemName.MPHaste: ItemData(0x1320124,  413, 0x19D , True ),
    ItemName.MPHaste2: ItemData(0x1320125,  413, 0x19D , True ),
    ItemName.MPHastera: ItemData(0x1320126,  421, 0x1A5 , True ),
    ItemName.MPHastera2: ItemData(0x1320127,  421, 0x1A5 , True ),
    ItemName.MPHastega: ItemData(0x1320128,  422, 0x1A6 , True ),
    ItemName.Defender: ItemData(0x1320129,  414, 0x19E , True ),
    ItemName.DamageControl: ItemData(0x132012a,  542, 0x21E , True ),
    ItemName.NoExperience: ItemData(0x132012b,  404, 0x194 , True ),
    ItemName.NoExperience2: ItemData(0x132012c,  404, 0x194 , True ),
    ItemName.LightDarkness: ItemData(0x132012d,  541, 0x21D , True ),
}
LvlAbility_Table = {
    ItemName.ComboBoost2: ItemData(0x132012e,  390, 0x186 , True ),
    ItemName.ExperienceBoost2: ItemData(0x132012f,  401, 0x191 , True ),
    ItemName.MagicLock: ItemData(0x1320130,  403, 0x193 , True ),
    ItemName.ReactionBoost3: ItemData(0x1320131,  392, 0x188 , True ),
    ItemName.ItemBoost2: ItemData(0x1320132,  411, 0x19B , True ),
    ItemName.LeafBracer: ItemData(0x1320133,  402, 0x192 , True ),
    ItemName.FireBoost2: ItemData(0x1320134,  408, 0x198 , True ),
    ItemName.DriveBoost2: ItemData(0x1320135,  397, 0x18D , True ),
    ItemName.Draw4: ItemData(0x1320136,  405, 0x195 , True ),
    ItemName.CombinationBoost: ItemData(0x1320137,  400, 0x190 , True ),
    ItemName.DamageDrive: ItemData(0x1320138,  396, 0x18C , True ),
    ItemName.AirComboBoost2: ItemData(0x1320139,  391, 0x187 , True ),
    ItemName.BlizzardBoost2: ItemData(0x132013a,  409, 0x199 , True ),
    ItemName.DriveConverter2: ItemData(0x132013b,  540, 0x21C , True ),
    ItemName.NegativeCombo2: ItemData(0x132013c,  394, 0x18A , True ),
    ItemName.OnceMore: ItemData(0x132013d,  416, 0x1A0 , True ),
    ItemName.FinishingPlus3: ItemData(0x132013e,  393, 0x189 , True ),
    ItemName.ThunderBoost2: ItemData(0x132013f,  410, 0x19A , True ),
    ItemName.Defender2: ItemData(0x1320140,  414, 0x19E , True ),
    ItemName.BerserkCharge2: ItemData(0x1320141,  395, 0x18B , True ),
    ItemName.Jackpot2: ItemData(0x1320142,  406, 0x196 , True ),
    ItemName.SecondChance: ItemData(0x1320143,  415, 0x19F , True ),
    ItemName.DamageControl2: ItemData(0x1320144,  542, 0x21E , True ),
}
ActionAbility_Table = {
    ItemName.Guard: ItemData(0x1320145,  82, 0x052 , True ),                    
    ItemName.UpperSlash: ItemData(0x1320146,  137, 0x089 , True ),              
    ItemName.HorizontalSlash: ItemData(0x1320147,  271, 0x10F , True ),         
    ItemName.FinishingLeap: ItemData(0x1320148,  267, 0x10B , True ),           
    ItemName.RetaliatingSlash: ItemData(0x1320149,  273, 0x111 , True ),        
    ItemName.Slapshot: ItemData(0x132014a,  262, 0x106 , True ),                
    ItemName.DodgeSlash: ItemData(0x132014b,  263, 0x107 , True ),              
    ItemName.FlashStep: ItemData(0x132014c,  559, 0x22F , True ),               
    ItemName.SlideDash: ItemData(0x132014d,  264, 0x108 , True ),               
    ItemName.VicinityBreak: ItemData(0x132014e,  562, 0x232 , True ),           
    ItemName.GuardBreak: ItemData(0x132014f,  265, 0x109 , True ),              
    ItemName.Explosion: ItemData(0x1320150,  266, 0x10A , True ),               
    ItemName.AerialSweep: ItemData(0x1320151,  269, 0x10D , True ),             
    ItemName.AerialDive: ItemData(0x1320152,  560, 0x230 , True ),              
    ItemName.AerialSpiral: ItemData(0x1320153,  270, 0x10E , True ),            
    ItemName.AerialFinish: ItemData(0x1320154,  272, 0x110 , True ),            
    ItemName.MagnetBurst: ItemData(0x1320155,  561, 0x231 , True ),             
    ItemName.Counterguard: ItemData(0x1320156,  268, 0x10C , True ),            
    ItemName.AutoValor: ItemData(0x1320157,  385, 0x181 , True ),               
    ItemName.AutoWisdom: ItemData(0x1320158,  386, 0x182 , True ),              
    ItemName.AutoLimit: ItemData(0x1320159,  568, 0x238 , True ),               
    ItemName.AutoMaster: ItemData(0x132015a,  387, 0x183 , True ),              
    ItemName.AutoFinal: ItemData(0x132015b,  388, 0x184 , True ),               
    ItemName.AutoSummon: ItemData(0x132015c,  389, 0x185 , True ),              
    ItemName.TrinityLimit: ItemData(0x132015d,  198, 0x0C6,True ),                   
}
Items_Table = {
    ItemName.Potion: ItemData(0x132015e,  1, 0x3580 ),
    ItemName.HiPotion: ItemData(0x132015f,  2, 0x3581 ),
    ItemName.Ether: ItemData(0x1320160,  3, 0x3582 ),
    ItemName.Elixir: ItemData(0x1320161,  4, 0x3583 ),
    ItemName.MegaPotion: ItemData(0x1320162,  5, 0x3584 ),
    ItemName.MegaEther: ItemData(0x1320163,  6, 0x3585 ),
    ItemName.Megalixir: ItemData(0x1320164,  7, 0x3586 ),
    ItemName.Tent: ItemData(0x1320165,  131, 0x35E1 ),
    ItemName.DriveRecovery: ItemData(0x1320166,  274, 0x3664 ),
    ItemName.HighDriveRecovery: ItemData(0x1320167,  275, 0x3665 ),
    ItemName.PowerBoost: ItemData(0x1320168,  276, 0x3666 ),
    ItemName.MagicBoost: ItemData(0x1320169,  277, 0x3667 ),
    ItemName.DefenseBoost: ItemData(0x132016a,  278, 0x3668 ),
    ItemName.APBoost: ItemData(0x132016b,  279, 0x3669 ),
}

# These items cannot be in other games so these are done locally in kh2
DonaldAbility_Table = {
    ItemName.DonaldFire: ItemData(0x132016c,  165,0x111 ),
    ItemName.DonaldBlizzard: ItemData(0x132016d,  166,0x111 ),
    ItemName.DonaldThunder: ItemData(0x132016e,  167,0x111 ),
    ItemName.DonaldCure: ItemData(0x132016f,  168,0x111 ),
    ItemName.Fantasia: ItemData(0x1320170,  199,0x111 ),
    ItemName.FlareForce: ItemData(0x1320171,  200,0x111 ),
    ItemName.DonaldMPRage: ItemData(0x1320172,  412,0x111 ),
    ItemName.DonaldJackpot: ItemData(0x1320173,  406,0x111 ),
    ItemName.DonaldLuckyLucky: ItemData(0x1320174,  407,0x111 ),
    ItemName.DonaldFireBoost: ItemData(0x1320175,  408,0x111 ),
    ItemName.DonaldBlizzardBoost: ItemData(0x1320176,  409,0x111 ),
    ItemName.DonaldThunderBoost: ItemData(0x1320177,  410,0x111 ),
    ItemName.DonaldFireBoost: ItemData(0x1320178,  408,0x111 ),
    ItemName.DonaldBlizzardBoost: ItemData(0x1320179,  409,0x111 ),
    ItemName.DonaldThunderBoost: ItemData(0x132017a,  410,0x111 ),
    ItemName.DonaldMPRage: ItemData(0x132017b,  412,0x111 ),
    ItemName.DonaldMPHastera: ItemData(0x132017c,  421,0x111 ),
    ItemName.DonaldAutoLimit: ItemData(0x132017d,  417,0x111 ),
    ItemName.DonaldHyperHealing: ItemData(0x132017e,  419,0x111 ),
    ItemName.DonaldAutoHealing: ItemData(0x132017f,  420,0x111 ),
    ItemName.DonaldMPHastega: ItemData(0x1320180,  422,0x111 ),
    ItemName.DonaldItemBoost: ItemData(0x1320181,  411,0x111 ),
    ItemName.DonaldDamageControl: ItemData(0x1320182,  542,0x111 ),
    ItemName.DonaldHyperHealing: ItemData(0x1320183,  419,0x111 ),
    ItemName.DonaldMPRage: ItemData(0x1320184,  412,0x111 ),
    ItemName.DonaldMPHaste: ItemData(0x1320185,  413,0x111 ),
    ItemName.DonaldMPHastera: ItemData(0x1320186,  421,0x111 ),
    ItemName.DonaldMPHastega: ItemData(0x1320187,  422,0x111 ),
    ItemName.DonaldMPHaste: ItemData(0x1320188,  413,0x111 ),
    ItemName.DonaldDamageControl: ItemData(0x1320189,  542,0x111 ),
    ItemName.DonaldMPHastera: ItemData(0x132018a,  421,0x111 ),
    ItemName.DonaldDraw: ItemData(0x132018b,  405,0x111 ),
}
GoofyAbility_Table = {
    ItemName.GoofyTornado: ItemData(0x132018c,  423,0x111 ),
    ItemName.GoofyTurbo: ItemData(0x132018d,  425,0x111 ),
    ItemName.GoofyBash: ItemData(0x132018e,  429,0x111 ),
    ItemName.TornadoFusion: ItemData(0x132018f,  201,0x111 ),
    ItemName.Teamwork: ItemData(0x1320190,  202,0x111 ),
    ItemName.GoofyDraw: ItemData(0x1320191,  405,0x111 ),
    ItemName.GoofyJackpot: ItemData(0x1320192,  406,0x111 ),
    ItemName.GoofyLuckyLucky: ItemData(0x1320193,  407,0x111 ),
    ItemName.GoofyItemBoost: ItemData(0x1320194,  411,0x111 ),
    ItemName.GoofyMPRage: ItemData(0x1320195,  412,0x111 ),
    ItemName.GoofyDefender: ItemData(0x1320196,  414,0x111 ),
    ItemName.GoofyDamageControl: ItemData(0x1320197,  542,0x111 ),
    ItemName.GoofyAutoLimit: ItemData(0x1320198,  417,0x111 ),
    ItemName.GoofySecondChance: ItemData(0x1320199,  415,0x111 ),
    ItemName.GoofyOnceMore: ItemData(0x132019a,  416,0x111 ),
    ItemName.GoofyAutoChange: ItemData(0x132019b,  418,0x111 ),
    ItemName.GoofyHyperHealing: ItemData(0x132019c,  419,0x111 ),
    ItemName.GoofyAutoHealing: ItemData(0x132019d,  420,0x111 ),
    ItemName.GoofyDefender: ItemData(0x132019e,  414,0x111 ),
    ItemName.GoofyHyperHealing: ItemData(0x132019f,  419,0x111 ),
    ItemName.GoofyMPHaste: ItemData(0x13201a0,  413,0x111 ),
    ItemName.GoofyMPHastera: ItemData(0x13201a1,  421,0x111 ),
    ItemName.GoofyMPRage: ItemData(0x13201a2,  412,0x111 ),
    ItemName.GoofyMPHastega: ItemData(0x13201a3,  422,0x111 ),
    ItemName.GoofyItemBoost: ItemData(0x13201a4,  411,0x111 ),
    ItemName.GoofyDamageControl: ItemData(0x13201a5,  542,0x111 ),
    ItemName.GoofyProtect: ItemData(0x13201a6,  596,0x111 ),
    ItemName.GoofyProtera: ItemData(0x13201a7,  597,0x111 ),
    ItemName.GoofyProtega: ItemData(0x13201a8,  598,0x111 ),
    ItemName.GoofyDamageControl: ItemData(0x13201a9,  542,0x111 ),
    ItemName.GoofyProtect: ItemData(0x13201aa,  596,0x111 ),
    ItemName.GoofyProtera: ItemData(0x13201ab,  597,0x111 ),
    ItemName.GoofyProtega: ItemData(0x13201ac,  598,0x111 ),
}

Misc_Table = {
    ItemName.Nothing: ItemData(0x132016c,  1,0x111 ),
    ItemName.Victory: ItemData(0x132016d,  1, True,0x111 ),
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
