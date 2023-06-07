import typing

from BaseClasses import MultiWorld, Region, Entrance

from .Locations import KH2Location, RegionTable
from .Names import LocationName, ItemName, RegionName


def create_regions(world, player: int, active_locations):
    KH2REGIONS: typing.Dict[str, typing.List[str]] = {
        "Menu":                        [],
        RegionName.GoA:                [
            LocationName.Crit_1,
            LocationName.Crit_2,
            LocationName.Crit_3,
            LocationName.Crit_4,
            LocationName.Crit_5,
            LocationName.Crit_6,
            LocationName.Crit_7,
            LocationName.GardenofAssemblageMap,
            LocationName.GoALostIllusion,
            LocationName.ProofofNonexistence,
            LocationName.DonaldStarting1,
            LocationName.DonaldStarting2,
            LocationName.GoofyStarting1,
            LocationName.GoofyStarting2],
        RegionName.LoD:                [
            LocationName.BambooGroveDarkShard,
            LocationName.BambooGroveEther,
            LocationName.BambooGroveMythrilShard,
            LocationName.EncampmentAreaMap,
            LocationName.Mission3,
            LocationName.CheckpointHiPotion,
            LocationName.CheckpointMythrilShard,
            LocationName.MountainTrailLightningShard,
            LocationName.MountainTrailRecoveryRecipe,
            LocationName.MountainTrailEther,
            LocationName.MountainTrailMythrilShard,
            LocationName.VillageCaveAreaMap,
            LocationName.VillageCaveAPBoost,
            LocationName.VillageCaveDarkShard,
            LocationName.VillageCaveBonus,
            LocationName.RidgeFrostShard,
            LocationName.RidgeAPBoost,
        ],
        RegionName.ShanYu:             [
            LocationName.ShanYu,
            LocationName.ShanYuGetBonus,
            LocationName.HiddenDragon,
            LocationName.GoofyShanYu
        ],
        RegionName.LoD2:               [],
        RegionName.AnsemRiku:          [
            LocationName.ThroneRoomTornPages,
            LocationName.ThroneRoomPalaceMap,
            LocationName.ThroneRoomAPBoost,
            LocationName.ThroneRoomQueenRecipe,
            LocationName.ThroneRoomAPBoost2,
            LocationName.ThroneRoomOgreShield,
            LocationName.ThroneRoomMythrilCrystal,
            LocationName.ThroneRoomOrichalcum,
        ],
        RegionName.StormRider:         [
            LocationName.StormRider,
            LocationName.GoofyStormRider
        ],
        RegionName.DataXigbar:         [
            LocationName.XigbarDataDefenseBoost
        ],
        RegionName.Ag:                 [
            LocationName.AgrabahMap,
            LocationName.AgrabahDarkShard,
            LocationName.AgrabahMythrilShard,
            LocationName.AgrabahHiPotion,
            LocationName.AgrabahAPBoost,
            LocationName.AgrabahMythrilStone,
            LocationName.AgrabahMythrilShard2,
            LocationName.AgrabahSerenityShard,
            LocationName.BazaarMythrilGem,
            LocationName.BazaarPowerShard,
            LocationName.BazaarHiPotion,
            LocationName.BazaarAPBoost,
            LocationName.BazaarMythrilShard,
            LocationName.PalaceWallsSkillRing,
            LocationName.PalaceWallsMythrilStone,
            LocationName.CaveEntrancePowerStone,
            LocationName.CaveEntranceMythrilShard,
            LocationName.ValleyofStoneMythrilStone,
            LocationName.ValleyofStoneAPBoost,
            LocationName.ValleyofStoneMythrilShard,
            LocationName.ValleyofStoneHiPotion,
            LocationName.AbuEscort,
            LocationName.ChasmofChallengesCaveofWondersMap,
            LocationName.ChasmofChallengesAPBoost,
            LocationName.TreasureRoom,
            LocationName.TreasureRoomAPBoost,
            LocationName.TreasureRoomSerenityGem,
            LocationName.GoofyTreasureRoom,
            LocationName.DonaldAbuEscort
        ],
        RegionName.TwinLords:          [
            LocationName.ElementalLords,
            LocationName.LampCharm
        ],
        RegionName.Ag2:                [
            LocationName.RuinedChamberTornPages,
            LocationName.RuinedChamberRuinsMap,
        ],
        RegionName.GenieJafar:         [
            LocationName.GenieJafar,
            LocationName.WishingLamp
        ],
        RegionName.DataLexaeus:        [
            LocationName.LexaeusBonus,
            LocationName.LexaeusASStrengthBeyondStrength,
            LocationName.LexaeusDataLostIllusion
        ],
        RegionName.Dc:                 [
            LocationName.DCCourtyardMythrilShard,
            LocationName.DCCourtyardStarRecipe,
            LocationName.DCCourtyardAPBoost,
            LocationName.DCCourtyardMythrilStone,
            LocationName.DCCourtyardBlazingStone,
            LocationName.DCCourtyardBlazingShard,
            LocationName.DCCourtyardMythrilShard2,
            LocationName.LibraryTornPages,
            LocationName.DisneyCastleMap,
            LocationName.MinnieEscort,
            LocationName.MinnieEscortGetBonus
        ],
        RegionName.Tr:                 [
            LocationName.CornerstoneHillMap,
            LocationName.CornerstoneHillFrostShard,
            LocationName.PierMythrilShard,
            LocationName.PierHiPotion,
        ],
        RegionName.OldPete:            [
            LocationName.WaterwayMythrilStone,
            LocationName.WaterwayAPBoost,
            LocationName.WaterwayFrostStone,
            LocationName.WindowofTimeMap,
            LocationName.BoatPete,
            LocationName.DonaldBoatPete,
            LocationName.DonaldBoatPeteGetBonus,
        ],
        RegionName.FuturePete:         [
            LocationName.FuturePete,
            LocationName.FuturePeteGetBonus,
            LocationName.Monochrome,
            LocationName.WisdomForm,
            LocationName.GoofyFuturePete
        ],
        RegionName.DataMarluxia:       [
            LocationName.MarluxiaGetBonus,
            LocationName.MarluxiaASEternalBlossom,
            LocationName.MarluxiaDataLostIllusion
        ],
        RegionName.Terra:              [
            LocationName.LingeringWillBonus,
            LocationName.LingeringWillProofofConnection,
            LocationName.LingeringWillManifestIllusion
        ],
        RegionName.Ha1:                [
            LocationName.PoohsHouse100AcreWoodMap,
            LocationName.PoohsHouseAPBoost,
            LocationName.PoohsHouseMythrilStone
        ],
        RegionName.Ha2:                [
            LocationName.PigletsHouseDefenseBoost,
            LocationName.PigletsHouseAPBoost,
            LocationName.PigletsHouseMythrilGem
        ],
        RegionName.Ha3:                [
            LocationName.RabbitsHouseDrawRing,
            LocationName.RabbitsHouseMythrilCrystal,
            LocationName.RabbitsHouseAPBoost,
        ],
        RegionName.Ha4:                [
            LocationName.KangasHouseMagicBoost,
            LocationName.KangasHouseAPBoost,
            LocationName.KangasHouseOrichalcum,
        ],
        RegionName.Ha5:                [
            LocationName.SpookyCaveMythrilGem,
            LocationName.SpookyCaveAPBoost,
            LocationName.SpookyCaveOrichalcum,
            LocationName.SpookyCaveGuardRecipe,
            LocationName.SpookyCaveMythrilCrystal,
            LocationName.SpookyCaveAPBoost2,
            LocationName.SweetMemories,
            LocationName.SpookyCaveMap
        ],
        RegionName.Ha6:                [
            LocationName.StarryHillCosmicRing,
            LocationName.StarryHillStyleRecipe,
            LocationName.StarryHillCureElement,
            LocationName.StarryHillOrichalcumPlus
        ],
        RegionName.Pr:                 [
            LocationName.RampartNavalMap,
            LocationName.RampartMythrilStone,
            LocationName.RampartDarkShard,
            LocationName.TownDarkStone,
            LocationName.TownAPBoost,
            LocationName.TownMythrilShard,
            LocationName.TownMythrilGem,
            LocationName.CaveMouthBrightShard,
            LocationName.CaveMouthMythrilShard,
            LocationName.IsladeMuertaMap,
            LocationName.BoatFight,
            LocationName.InterceptorBarrels,
            LocationName.PowderStoreAPBoost1,
            LocationName.PowderStoreAPBoost2,
            LocationName.MoonlightNookMythrilShard,
            LocationName.MoonlightNookSerenityGem,
            LocationName.MoonlightNookPowerStone,
            LocationName.DonaldBoatFight,
            LocationName.GoofyInterceptorBarrels
        ],
        RegionName.Barbosa:            [
            LocationName.Barbossa,
            LocationName.BarbossaGetBonus,
            LocationName.FollowtheWind,
            LocationName.GoofyBarbossa,
            LocationName.GoofyBarbossaGetBonus,
        ],
        RegionName.Pr2:                [],
        RegionName.GrimReaper1:        [
            LocationName.GrimReaper1,
            LocationName.InterceptorsHoldFeatherCharm,
            LocationName.SeadriftKeepAPBoost,
            LocationName.SeadriftKeepOrichalcum,
            LocationName.SeadriftKeepMeteorStaff,
            LocationName.SeadriftRowSerenityGem,
            LocationName.SeadriftRowKingRecipe,
            LocationName.SeadriftRowMythrilCrystal,
            LocationName.SeadriftRowCursedMedallion,
            LocationName.SeadriftRowShipGraveyardMap,
            LocationName.GoofyGrimReaper1
        ],
        RegionName.GrimReaper2:        [
            LocationName.DonaladGrimReaper2,
            LocationName.GrimReaper2,
            LocationName.SecretAnsemReport6,
        ],
        RegionName.DataLuxord:         [
            LocationName.LuxordDataAPBoost
        ],
        RegionName.Oc:                 [
            LocationName.PassageMythrilShard,
            LocationName.PassageMythrilStone,
            LocationName.PassageEther,
            LocationName.PassageAPBoost,
            LocationName.PassageHiPotion,
            LocationName.InnerChamberUnderworldMap,
            LocationName.InnerChamberMythrilShard,
        ],
        RegionName.Cerberus:           [
            LocationName.Cerberus,
            LocationName.ColiseumMap,
            LocationName.Urns,
            LocationName.UnderworldEntrancePowerBoost,
            LocationName.CavernsEntranceLucidShard,
            LocationName.CavernsEntranceAPBoost,
            LocationName.CavernsEntranceMythrilShard,
            LocationName.TheLostRoadBrightShard,
            LocationName.TheLostRoadEther,
            LocationName.TheLostRoadMythrilShard,
            LocationName.TheLostRoadMythrilStone,
            LocationName.AtriumLucidStone,
            LocationName.AtriumAPBoost,
            LocationName.DemyxOC,
            LocationName.SecretAnsemReport5,
            LocationName.OlympusStone,
            LocationName.TheLockCavernsMap,
            LocationName.TheLockMythrilShard,
            LocationName.TheLockAPBoost
        ],
        RegionName.OlympusPete:        [
            LocationName.PeteOC,
            LocationName.DonaldDemyxOC,
            LocationName.GoofyPeteOC
        ],
        RegionName.Hydra:              [
            LocationName.Hydra,
            LocationName.HydraGetBonus,
            LocationName.HerosCrest
        ],
        RegionName.Oc2:                [
            LocationName.AuronsStatue,
        ],
        RegionName.Hades:              [
            LocationName.Hades,
            LocationName.HadesGetBonus,
            LocationName.GuardianSoul
        ],
        RegionName.Oc2_pain_and_panic: [
            LocationName.ProtectBeltPainandPanicCup,
            LocationName.SerenityGemPainandPanicCup
        ],
        RegionName.Oc2_cerberus:       [
            LocationName.RisingDragonCerberusCup,
            LocationName.SerenityCrystalCerberusCup
        ],
        RegionName.Oc2_titan:          [
            LocationName.GenjiShieldTitanCup,
            LocationName.SkillfulRingTitanCup
        ],
        RegionName.Oc2_gof:            [
            LocationName.FatalCrestGoddessofFateCup,
            LocationName.OrichalcumPlusGoddessofFateCup,
        ],
        RegionName.HadesCups:          [
            LocationName.HadesCupTrophyParadoxCups
        ],
        RegionName.DataZexion:         [
            LocationName.ZexionBonus,
            LocationName.ZexionASBookofShadows,
            LocationName.ZexionDataLostIllusion,
            LocationName.GoofyZexion
        ],
        RegionName.Bc:                 [
            LocationName.BCCourtyardAPBoost,
            LocationName.BCCourtyardHiPotion,
            LocationName.BCCourtyardMythrilShard,
            LocationName.BellesRoomCastleMap,
            LocationName.BellesRoomMegaRecipe,
            LocationName.TheEastWingMythrilShard,
            LocationName.TheEastWingTent,
            LocationName.TheWestHallHiPotion,
            LocationName.TheWestHallPowerShard,
            LocationName.TheWestHallMythrilShard2,
            LocationName.TheWestHallBrightStone,
            LocationName.TheWestHallMythrilShard,
        ],
        RegionName.Thresholder:        [
            LocationName.Thresholder,
            LocationName.DungeonBasementMap,
            LocationName.DungeonAPBoost,
            LocationName.SecretPassageMythrilShard,
            LocationName.SecretPassageHiPotion,
            LocationName.SecretPassageLucidShard,
            LocationName.TheWestHallAPBoostPostDungeon,
            LocationName.TheWestWingMythrilShard,
            LocationName.TheWestWingTent,
            LocationName.DonaldThresholder,
        ],
        RegionName.Beast:              [
            LocationName.Beast,
            LocationName.TheBeastsRoomBlazingShard,
            LocationName.GoofyBeast
        ],
        RegionName.DarkThorn:          [
            LocationName.DarkThorn,
            LocationName.DarkThornGetBonus,
            LocationName.DarkThornCureElement,
        ],
        RegionName.Bc2:                [
            LocationName.RumblingRose,
            LocationName.CastleWallsMap
        ],
        RegionName.Xaldin:             [
            LocationName.Xaldin,
            LocationName.XaldinGetBonus,
            LocationName.DonaldXaldinGetBonus,
            LocationName.SecretAnsemReport4,
        ],
        RegionName.DataXaldin:         [
            LocationName.XaldinDataDefenseBoost
        ],
        RegionName.Sp:                 [
            LocationName.PitCellAreaMap,
            LocationName.PitCellMythrilCrystal,
            LocationName.CanyonDarkCrystal,
            LocationName.CanyonMythrilStone,
            LocationName.CanyonMythrilGem,
            LocationName.CanyonFrostCrystal,
            LocationName.Screens,
            LocationName.HallwayPowerCrystal,
            LocationName.HallwayAPBoost,
            LocationName.CommunicationsRoomIOTowerMap,
            LocationName.CommunicationsRoomGaiaBelt,
            LocationName.DonaldScreens,
        ],
        RegionName.HostileProgram:     [
            LocationName.HostileProgram,
            LocationName.HostileProgramGetBonus,
            LocationName.PhotonDebugger,
            LocationName.GoofyHostileProgram
        ],
        RegionName.Sp2:                [
            LocationName.SolarSailer,
            LocationName.CentralComputerCoreAPBoost,
            LocationName.CentralComputerCoreOrichalcumPlus,
            LocationName.CentralComputerCoreCosmicArts,
            LocationName.CentralComputerCoreMap,
            LocationName.DonaldSolarSailer
        ],
        RegionName.Mcp:                [
            LocationName.MCP,
            LocationName.MCPGetBonus
        ],
        RegionName.DataLarxene:        [
            LocationName.LarxeneBonus,
            LocationName.LarxeneASCloakedThunder,
            LocationName.LarxeneDataLostIllusion
        ],
        RegionName.Ht:                 [
            LocationName.GraveyardMythrilShard,
            LocationName.GraveyardSerenityGem,
            LocationName.FinklesteinsLabHalloweenTownMap,
            LocationName.TownSquareMythrilStone,
            LocationName.TownSquareEnergyShard,
            LocationName.HinterlandsLightningShard,
            LocationName.HinterlandsMythrilStone,
            LocationName.HinterlandsAPBoost,
            LocationName.CandyCaneLaneMegaPotion,
            LocationName.CandyCaneLaneMythrilGem,
            LocationName.CandyCaneLaneLightningStone,
            LocationName.CandyCaneLaneMythrilStone,
            LocationName.SantasHouseChristmasTownMap,
            LocationName.SantasHouseAPBoost,
        ],
        RegionName.PrisonKeeper:       [
            LocationName.PrisonKeeper,
            LocationName.DonaldPrisonKeeper,
        ],
        RegionName.OogieBoogie:        [
            LocationName.OogieBoogie,
            LocationName.OogieBoogieMagnetElement,
            LocationName.GoofyOogieBoogie
        ],
        RegionName.Ht2:                [
            LocationName.Lock,
            LocationName.Present,
            LocationName.DecoyPresents,
            LocationName.GoofyLock
        ],
        RegionName.Experiment:         [
            LocationName.Experiment,
            LocationName.DecisivePumpkin,
            LocationName.DonaldExperiment,
        ],
        RegionName.DataVexen:          [
            LocationName.VexenBonus,
            LocationName.VexenASRoadtoDiscovery,
            LocationName.VexenDataLostIllusion
        ],
        RegionName.Hb:                 [
            LocationName.MarketplaceMap,
            LocationName.BoroughDriveRecovery,
            LocationName.BoroughAPBoost,
            LocationName.BoroughHiPotion,
            LocationName.BoroughMythrilShard,
            LocationName.BoroughDarkShard,
            LocationName.MerlinsHouseMembershipCard,
            LocationName.MerlinsHouseBlizzardElement,
            LocationName.Bailey,
            LocationName.BaileySecretAnsemReport7,
            LocationName.BaseballCharm
        ],
        RegionName.Hb2:                [
            LocationName.PosternCastlePerimeterMap,
            LocationName.PosternMythrilGem,
            LocationName.PosternAPBoost,
            LocationName.CorridorsMythrilStone,
            LocationName.CorridorsMythrilCrystal,
            LocationName.CorridorsDarkCrystal,
            LocationName.CorridorsAPBoost,
            LocationName.AnsemsStudyMasterForm,
            LocationName.AnsemsStudySleepingLion,
            LocationName.AnsemsStudySkillRecipe,
            LocationName.AnsemsStudyUkuleleCharm,
            LocationName.RestorationSiteMoonRecipe,
            LocationName.RestorationSiteAPBoost,
        ],
        RegionName.HBDemyx:            [
            LocationName.DonaldDemyxHBGetBonus,
            LocationName.DemyxHB,
            LocationName.DemyxHBGetBonus,
            LocationName.FFFightsCureElement,
            LocationName.CrystalFissureTornPages,
            LocationName.CrystalFissureTheGreatMawMap,
            LocationName.CrystalFissureEnergyCrystal,
            LocationName.CrystalFissureAPBoost,
        ],
        RegionName.ThousandHeartless:  [
            LocationName.ThousandHeartless,
            LocationName.ThousandHeartlessSecretAnsemReport1,
            LocationName.ThousandHeartlessIceCream,
            LocationName.ThousandHeartlessPicture,
            LocationName.PosternGullWing,
            LocationName.HeartlessManufactoryCosmicChain,
        ],
        RegionName.DataDemyx:          [
            LocationName.DemyxDataAPBoost
        ],
        RegionName.Mushroom13:         [
            LocationName.WinnersProof,
            LocationName.ProofofPeace
        ],
        RegionName.Sephi:              [
            LocationName.SephirothBonus,
            LocationName.SephirothFenrir
        ],
        RegionName.CoR:                [
            LocationName.CoRDepthsAPBoost,
            LocationName.CoRDepthsPowerCrystal,
            LocationName.CoRDepthsFrostCrystal,
            LocationName.CoRDepthsManifestIllusion,
            LocationName.CoRDepthsAPBoost2,
            LocationName.CoRMineshaftLowerLevelDepthsofRemembranceMap,
            LocationName.CoRMineshaftLowerLevelAPBoost,
        ],
        RegionName.CorFirstFight:      [
            LocationName.CoRDepthsUpperLevelRemembranceGem,
            LocationName.CoRMiningAreaSerenityGem,
            LocationName.CoRMiningAreaAPBoost,
            LocationName.CoRMiningAreaSerenityCrystal,
            LocationName.CoRMiningAreaManifestIllusion,
            LocationName.CoRMiningAreaSerenityGem2,
            LocationName.CoRMiningAreaDarkRemembranceMap,
        ],
        RegionName.CorSecondFight:     [
            LocationName.CoRMineshaftMidLevelPowerBoost,
            LocationName.CoREngineChamberSerenityCrystal,
            LocationName.CoREngineChamberRemembranceCrystal,
            LocationName.CoREngineChamberAPBoost,
            LocationName.CoREngineChamberManifestIllusion,
            LocationName.CoRMineshaftUpperLevelMagicBoost,
        ],
        RegionName.Transport:          [
            LocationName.CoRMineshaftUpperLevelAPBoost,  # last chest
            LocationName.TransporttoRemembrance
        ],
        RegionName.Pl:                 [
            LocationName.GorgeSavannahMap,
            LocationName.GorgeDarkGem,
            LocationName.GorgeMythrilStone,
            LocationName.ElephantGraveyardFrostGem,
            LocationName.ElephantGraveyardMythrilStone,
            LocationName.ElephantGraveyardBrightStone,
            LocationName.ElephantGraveyardAPBoost,
            LocationName.ElephantGraveyardMythrilShard,
            LocationName.PrideRockMap,
            LocationName.PrideRockMythrilStone,
            LocationName.PrideRockSerenityCrystal,
            LocationName.WildebeestValleyEnergyStone,
            LocationName.WildebeestValleyAPBoost,
            LocationName.WildebeestValleyMythrilGem,
            LocationName.WildebeestValleyMythrilStone,
            LocationName.WildebeestValleyLucidGem,
            LocationName.WastelandsMythrilShard,
            LocationName.WastelandsSerenityGem,
            LocationName.WastelandsMythrilStone,
            LocationName.JungleSerenityGem,
            LocationName.JungleMythrilStone,
            LocationName.JungleSerenityCrystal,
            LocationName.OasisMap,
            LocationName.OasisTornPages,
            LocationName.OasisAPBoost,
            LocationName.CircleofLife,
            LocationName.Hyenas1,

            LocationName.GoofyHyenas1
        ],
        RegionName.Scar:               [
            LocationName.Scar,
            LocationName.ScarFireElement,
            LocationName.DonaldScar,
        ],
        RegionName.Pl2:                [
            LocationName.Hyenas2,
            LocationName.GoofyHyenas2
        ],
        RegionName.GroundShaker:       [
            LocationName.Groundshaker,
            LocationName.GroundshakerGetBonus,
        ],
        RegionName.DataSaix:           [
            LocationName.SaixDataDefenseBoost,
        ],
        RegionName.Stt:                [
            LocationName.TwilightTownMap,
            LocationName.MunnyPouchOlette,
            LocationName.StationDusks,
            LocationName.StationofSerenityPotion,
            LocationName.StationofCallingPotion,
        ],
        RegionName.TwilightThorn:      [
            LocationName.TwilightThorn,
        ],
        RegionName.Axel1:              [
            LocationName.Axel1,
            LocationName.JunkChampionBelt,
            LocationName.JunkMedal,
            LocationName.TheStruggleTrophy,
            LocationName.CentralStationPotion1,
            LocationName.STTCentralStationHiPotion,
            LocationName.CentralStationPotion2,
            LocationName.SunsetTerraceAbilityRing,
            LocationName.SunsetTerraceHiPotion,
            LocationName.SunsetTerracePotion1,
            LocationName.SunsetTerracePotion2,
            LocationName.MansionFoyerHiPotion,
            LocationName.MansionFoyerPotion1,
            LocationName.MansionFoyerPotion2,
            LocationName.MansionDiningRoomElvenBandanna,
            LocationName.MansionDiningRoomPotion,
            LocationName.NaminesSketches,
            LocationName.MansionMap,
            LocationName.MansionLibraryHiPotion,
        ],
        RegionName.Axel2:              [
            LocationName.Axel2,
            LocationName.MansionBasementCorridorHiPotion,
        ],
        RegionName.DataRoxas:          [
            LocationName.RoxasDataMagicBoost
        ],
        RegionName.Tt:                 [
            LocationName.OldMansionPotion,
            LocationName.OldMansionMythrilShard,
            LocationName.TheWoodsPotion,
            LocationName.TheWoodsMythrilShard,
            LocationName.TheWoodsHiPotion,
            LocationName.TramCommonHiPotion,
            LocationName.TramCommonAPBoost,
            LocationName.TramCommonTent,
            LocationName.TramCommonMythrilShard1,
            LocationName.TramCommonPotion1,
            LocationName.TramCommonMythrilShard2,
            LocationName.TramCommonPotion2,
            LocationName.StationPlazaSecretAnsemReport2,
            LocationName.MunnyPouchMickey,
            LocationName.CrystalOrb,
            LocationName.CentralStationTent,
            LocationName.TTCentralStationHiPotion,
            LocationName.CentralStationMythrilShard,
            LocationName.TheTowerPotion,
            LocationName.TheTowerHiPotion,
            LocationName.TheTowerEther,
            LocationName.TowerEntrywayEther,
            LocationName.TowerEntrywayMythrilShard,
            LocationName.SorcerersLoftTowerMap,
            LocationName.TowerWardrobeMythrilStone,
            LocationName.StarSeeker,
            LocationName.ValorForm
        ],
        RegionName.Tt2:                [
            LocationName.SeifersTrophy,
            LocationName.Oathkeeper,
            LocationName.LimitForm
        ],
        RegionName.Tt3:                [
            LocationName.UndergroundConcourseMythrilGem,
            LocationName.UndergroundConcourseAPBoost,
            LocationName.UndergroundConcourseMythrilCrystal,
            LocationName.UndergroundConcourseOrichalcum,
            LocationName.TunnelwayOrichalcum,
            LocationName.TunnelwayMythrilCrystal,
            LocationName.SunsetTerraceOrichalcumPlus,
            LocationName.SunsetTerraceMythrilShard,
            LocationName.SunsetTerraceMythrilCrystal,
            LocationName.SunsetTerraceAPBoost,
            LocationName.MansionNobodies,
            LocationName.MansionFoyerMythrilCrystal,
            LocationName.MansionFoyerMythrilStone,
            LocationName.MansionFoyerSerenityCrystal,
            LocationName.MansionDiningRoomMythrilCrystal,
            LocationName.MansionDiningRoomMythrilStone,
            LocationName.MansionLibraryOrichalcum,
            LocationName.BeamSecretAnsemReport10,
            LocationName.MansionBasementCorridorUltimateRecipe,
            LocationName.BetwixtandBetween,
            LocationName.BetwixtandBetweenBondofFlame,
            LocationName.DonaldMansionNobodies
        ],
        RegionName.DataAxel:           [
            LocationName.AxelDataMagicBoost,
        ],
        RegionName.Twtnw:              [
            LocationName.FragmentCrossingMythrilStone,
            LocationName.FragmentCrossingMythrilCrystal,
            LocationName.FragmentCrossingAPBoost,
            LocationName.FragmentCrossingOrichalcum],
        RegionName.Roxas:              [
            LocationName.Roxas,
            LocationName.RoxasGetBonus,
            LocationName.RoxasSecretAnsemReport8,
            LocationName.TwoBecomeOne,
            LocationName.MemorysSkyscaperMythrilCrystal,
            LocationName.MemorysSkyscaperAPBoost,
            LocationName.MemorysSkyscaperMythrilStone,
            LocationName.TheBrinkofDespairDarkCityMap,
            LocationName.TheBrinkofDespairOrichalcumPlus,
            LocationName.NothingsCallMythrilGem,
            LocationName.NothingsCallOrichalcum,
            LocationName.TwilightsViewCosmicBelt
        ],
        RegionName.Xigbar:             [
            LocationName.XigbarBonus,
            LocationName.XigbarSecretAnsemReport3,
            LocationName.NaughtsSkywayMythrilGem,
            LocationName.NaughtsSkywayOrichalcum,
            LocationName.NaughtsSkywayMythrilCrystal,
            LocationName.Oblivion,
            LocationName.CastleThatNeverWasMap
        ],
        RegionName.Luxord:             [
            LocationName.Luxord,
            LocationName.LuxordGetBonus,
            LocationName.LuxordSecretAnsemReport9
        ],
        RegionName.Saix:               [
            LocationName.SaixBonus,
            LocationName.SaixSecretAnsemReport12,
        ],
        RegionName.Twtnw2:             [
            LocationName.PreXemnas1SecretAnsemReport11,
            LocationName.RuinandCreationsPassageMythrilStone,
            LocationName.RuinandCreationsPassageAPBoost,
            LocationName.RuinandCreationsPassageMythrilCrystal,
            LocationName.RuinandCreationsPassageOrichalcum
        ],
        RegionName.Xemnas:             [
            LocationName.Xemnas1,
            LocationName.Xemnas1GetBonus,
            LocationName.Xemnas1SecretAnsemReport13
        ],
        RegionName.ArmoredXemnas:      [],
        RegionName.ArmoredXemnas2:     [],
        RegionName.FinalXemnas:        [
            LocationName.FinalXemnas
        ],
        RegionName.DataXemnas:         [
            LocationName.XemnasDataPowerBoost
        ],
        RegionName.Valor:              [
            LocationName.Valorlvl2,
            LocationName.Valorlvl3,
            LocationName.Valorlvl4,
            LocationName.Valorlvl5,
            LocationName.Valorlvl6,
            LocationName.Valorlvl7
        ],
        RegionName.Wisdom:             [
            LocationName.Wisdomlvl2,
            LocationName.Wisdomlvl3,
            LocationName.Wisdomlvl4,
            LocationName.Wisdomlvl5,
            LocationName.Wisdomlvl6,
            LocationName.Wisdomlvl7
        ],
        RegionName.Limit:              [
            LocationName.Limitlvl2,
            LocationName.Limitlvl3,
            LocationName.Limitlvl4,
            LocationName.Limitlvl5,
            LocationName.Limitlvl6,
            LocationName.Limitlvl7
        ],
        RegionName.Master:             [
            LocationName.Masterlvl2,
            LocationName.Masterlvl3,
            LocationName.Masterlvl4,
            LocationName.Masterlvl5,
            LocationName.Masterlvl6,
            LocationName.Masterlvl7
        ],
        RegionName.Final:              [
            LocationName.Finallvl2,
            LocationName.Finallvl3,
            LocationName.Finallvl4,
            LocationName.Finallvl5,
            LocationName.Finallvl6,
            LocationName.Finallvl7
        ],
        RegionName.Keyblade:           [
            LocationName.FAKESlot,
            LocationName.DetectionSaberSlot,
            LocationName.EdgeofUltimaSlot,
            LocationName.KingdomKeySlot,
            LocationName.OathkeeperSlot,
            LocationName.OblivionSlot,
            LocationName.StarSeekerSlot,
            LocationName.HiddenDragonSlot,
            LocationName.HerosCrestSlot,
            LocationName.MonochromeSlot,
            LocationName.FollowtheWindSlot,
            LocationName.CircleofLifeSlot,
            LocationName.PhotonDebuggerSlot,
            LocationName.GullWingSlot,
            LocationName.RumblingRoseSlot,
            LocationName.GuardianSoulSlot,
            LocationName.WishingLampSlot,
            LocationName.DecisivePumpkinSlot,
            LocationName.SweetMemoriesSlot,
            LocationName.MysteriousAbyssSlot,
            LocationName.SleepingLionSlot,
            LocationName.BondofFlameSlot,
            LocationName.TwoBecomeOneSlot,
            LocationName.FatalCrestSlot,
            LocationName.FenrirSlot,
            LocationName.UltimaWeaponSlot,
            LocationName.WinnersProofSlot,
            LocationName.PurebloodSlot,
            LocationName.Centurion2,
            LocationName.CometStaff,
            LocationName.HammerStaff,
            LocationName.LordsBroom,
            LocationName.MagesStaff,
            LocationName.MeteorStaff,
            LocationName.NobodyLance,
            LocationName.PreciousMushroom,
            LocationName.PreciousMushroom2,
            LocationName.PremiumMushroom,
            LocationName.RisingDragon,
            LocationName.SaveTheQueen2,
            LocationName.ShamansRelic,
            LocationName.VictoryBell,
            LocationName.WisdomWand,

            LocationName.AdamantShield,
            LocationName.AkashicRecord,
            LocationName.ChainGear,
            LocationName.DreamCloud,
            LocationName.FallingStar,
            LocationName.FrozenPride2,
            LocationName.GenjiShield,
            LocationName.KnightDefender,
            LocationName.KnightsShield,
            LocationName.MajesticMushroom,
            LocationName.MajesticMushroom2,
            LocationName.NobodyGuard,
            LocationName.OgreShield,
            LocationName.SaveTheKing2,
            LocationName.UltimateMushroom
        ],
        RegionName.LevelsVS1:          [],
        RegionName.LevelsVS3:          [],
        RegionName.LevelsVS6:          [],
        RegionName.LevelsVS9:          [],
        RegionName.LevelsVS12:         [],
        RegionName.LevelsVS15:         [],
        RegionName.LevelsVS18:         [],
        RegionName.LevelsVS21:         [],
        RegionName.LevelsVS24:         [],
        RegionName.LevelsVS26:         [],

    }
    # Level region depends on level depth.
    # for every 5 levels there should be +3 visit locking

    # level 50
    if world.LevelDepth[player] == "level_50":
        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl2, LocationName.Lvl4, LocationName.Lvl7, LocationName.Lvl9,
                                            LocationName.Lvl10]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl12, LocationName.Lvl14, LocationName.Lvl15,
                                            LocationName.Lvl17,
                                            LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl23, LocationName.Lvl25, LocationName.Lvl28,
                                            LocationName.Lvl30]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl32, LocationName.Lvl34, LocationName.Lvl36,
                                            LocationName.Lvl39, LocationName.Lvl41]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl44, LocationName.Lvl46, LocationName.Lvl48]
        KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl50]
    # level 99
    elif world.LevelDepth[player] == "level_99":
        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl7, LocationName.Lvl9]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl12, LocationName.Lvl15, LocationName.Lvl17,
                                            LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl23, LocationName.Lvl25, LocationName.Lvl28]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl31, LocationName.Lvl33, LocationName.Lvl36,
                                            LocationName.Lvl39]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl41, LocationName.Lvl44, LocationName.Lvl47,
                                             LocationName.Lvl49]
        KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl53, LocationName.Lvl59]
        KH2REGIONS[RegionName.LevelsVS18] = [LocationName.Lvl65]
        KH2REGIONS[RegionName.LevelsVS21] = [LocationName.Lvl73]
        KH2REGIONS[RegionName.LevelsVS24] = [LocationName.Lvl85]
        KH2REGIONS[RegionName.LevelsVS26] = [LocationName.Lvl99]
    # level sanity
    # has to be [] instead of {} for in
    elif world.LevelDepth[player] in ["level_50_sanity", "level_99_sanity"]:

        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl2, LocationName.Lvl3, LocationName.Lvl4, LocationName.Lvl5,
                                            LocationName.Lvl6,
                                            LocationName.Lvl7, LocationName.Lvl8, LocationName.Lvl9, LocationName.Lvl10]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl11, LocationName.Lvl12, LocationName.Lvl13,
                                            LocationName.Lvl14, LocationName.Lvl15,
                                            LocationName.Lvl16, LocationName.Lvl17, LocationName.Lvl18,
                                            LocationName.Lvl19, LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl21, LocationName.Lvl22, LocationName.Lvl23,
                                            LocationName.Lvl24, LocationName.Lvl25,
                                            LocationName.Lvl26, LocationName.Lvl27, LocationName.Lvl28,
                                            LocationName.Lvl29, LocationName.Lvl30]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl31, LocationName.Lvl32, LocationName.Lvl33,
                                            LocationName.Lvl34, LocationName.Lvl35,
                                            LocationName.Lvl36, LocationName.Lvl37, LocationName.Lvl38,
                                            LocationName.Lvl39, LocationName.Lvl40]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl41, LocationName.Lvl42, LocationName.Lvl43,
                                             LocationName.Lvl44, LocationName.Lvl45,
                                             LocationName.Lvl46, LocationName.Lvl47, LocationName.Lvl48,
                                             LocationName.Lvl49, LocationName.Lvl50]
        # level 99 sanity
        if world.LevelDepth[player] == "level_99_sanity":
            KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl51, LocationName.Lvl52, LocationName.Lvl53,
                                                 LocationName.Lvl54,
                                                 LocationName.Lvl55, LocationName.Lvl56, LocationName.Lvl57,
                                                 LocationName.Lvl58,
                                                 LocationName.Lvl59, LocationName.Lvl60]
            KH2REGIONS[RegionName.LevelsVS18] = [LocationName.Lvl61, LocationName.Lvl62, LocationName.Lvl63,
                                                 LocationName.Lvl64,
                                                 LocationName.Lvl65, LocationName.Lvl66, LocationName.Lvl67,
                                                 LocationName.Lvl68,
                                                 LocationName.Lvl69, LocationName.Lvl70]
            KH2REGIONS[RegionName.LevelsVS21] = [LocationName.Lvl71, LocationName.Lvl72, LocationName.Lvl73,
                                                 LocationName.Lvl74,
                                                 LocationName.Lvl75, LocationName.Lvl76, LocationName.Lvl77,
                                                 LocationName.Lvl78,
                                                 LocationName.Lvl79, LocationName.Lvl80]
            KH2REGIONS[RegionName.LevelsVS24] = [LocationName.Lvl81, LocationName.Lvl82, LocationName.Lvl83,
                                                 LocationName.Lvl84,
                                                 LocationName.Lvl85, LocationName.Lvl86, LocationName.Lvl87,
                                                 LocationName.Lvl88,
                                                 LocationName.Lvl89, LocationName.Lvl90]
            KH2REGIONS[RegionName.LevelsVS26] = [LocationName.Lvl91, LocationName.Lvl92, LocationName.Lvl93,
                                                 LocationName.Lvl94,
                                                 LocationName.Lvl95, LocationName.Lvl96, LocationName.Lvl97,
                                                 LocationName.Lvl98,
                                                 LocationName.Lvl99]

    for region, locations in KH2REGIONS.items():
        world.regions += [create_region(world, player, active_locations, region, locations)]


def connect_regions(world: MultiWorld, player: int):
    # connecting every first visit to the GoA
    KH2RegionConnections: typing.Dict[str, typing.Set[str]] = {
        "Menu":                       {RegionName.GoA},
        RegionName.GoA:               {RegionName.Sp, RegionName.Pr, RegionName.Tt, RegionName.Oc, RegionName.Ht,
                                       RegionName.LoD,
                                       RegionName.Twtnw, RegionName.Bc, RegionName.Ag, RegionName.Pl, RegionName.Hb,
                                       RegionName.Dc, RegionName.Stt,
                                       RegionName.Ha1, RegionName.Keyblade, RegionName.LevelsVS1,
                                       RegionName.Valor, RegionName.Wisdom, RegionName.Limit, RegionName.Master,
                                       RegionName.Final},
        RegionName.LoD:               {RegionName.ShanYu},
        RegionName.ShanYu:            {RegionName.LoD2},
        RegionName.LoD2:              {RegionName.AnsemRiku},
        RegionName.AnsemRiku:         {RegionName.StormRider},
        RegionName.StormRider:        {RegionName.DataXigbar},
        RegionName.Ag:                {RegionName.TwinLords},
        RegionName.TwinLords:         {RegionName.Ag2},
        RegionName.Ag2:               {RegionName.GenieJafar},
        RegionName.GenieJafar:        {RegionName.DataLexaeus},
        RegionName.Dc:                {RegionName.Tr},
        RegionName.Tr:                {RegionName.OldPete},
        RegionName.OldPete:           {RegionName.FuturePete},
        RegionName.FuturePete:        {RegionName.Terra, RegionName.DataMarluxia},
        RegionName.Ha1:               {RegionName.Ha2},
        RegionName.Ha2:               {RegionName.Ha3},
        RegionName.Ha3:               {RegionName.Ha4},
        RegionName.Ha4:               {RegionName.Ha5},
        RegionName.Ha5:               {RegionName.Ha6},
        RegionName.Pr:                {RegionName.Barbosa},
        RegionName.Barbosa:           {RegionName.Pr2},
        RegionName.Pr2:               {RegionName.GrimReaper1},
        RegionName.GrimReaper1:       {RegionName.GrimReaper2},
        RegionName.GrimReaper2:       {RegionName.DataLuxord},
        RegionName.Oc:                {RegionName.Cerberus},
        RegionName.Cerberus:          {RegionName.OlympusPete},
        RegionName.OlympusPete:       {RegionName.Hydra},
        RegionName.Hydra:             {RegionName.Oc2_pain_and_panic, RegionName.Cerberus, RegionName.Oc2},
        RegionName.Oc2:               {RegionName.Hades},
        RegionName.Hades:             {RegionName.Oc2_titan, RegionName.Oc2_gof, RegionName.DataZexion},
        RegionName.Oc2_gof:           {RegionName.HadesCups},
        RegionName.Bc:                {RegionName.Thresholder},
        RegionName.Thresholder:       {RegionName.Beast},
        RegionName.Beast:             {RegionName.DarkThorn},
        RegionName.DarkThorn:         {RegionName.Bc2},
        RegionName.Bc2:               {RegionName.Xaldin},
        RegionName.Xaldin:            {RegionName.DataXaldin},
        RegionName.Sp:                {RegionName.HostileProgram},
        RegionName.HostileProgram:    {RegionName.Sp2},
        RegionName.Sp2:               {RegionName.Mcp},
        RegionName.Mcp:               {RegionName.DataLarxene},
        RegionName.Ht:                {RegionName.PrisonKeeper},
        RegionName.PrisonKeeper:      {RegionName.OogieBoogie},
        RegionName.OogieBoogie:       {RegionName.Ht2},
        RegionName.Ht2:               {RegionName.Experiment},
        RegionName.Experiment:        {RegionName.DataVexen},
        RegionName.Hb:                {RegionName.Hb2},
        RegionName.Hb2:               {RegionName.CoR, RegionName.HBDemyx},
        RegionName.HBDemyx:           {RegionName.ThousandHeartless},
        RegionName.ThousandHeartless: {RegionName.Mushroom13, RegionName.DataDemyx, RegionName.Sephi},
        RegionName.CoR:               {RegionName.CorFirstFight},
        RegionName.CorFirstFight:     {RegionName.CorSecondFight},
        RegionName.CorSecondFight:    {RegionName.Transport},
        RegionName.Pl:                {RegionName.Scar},
        RegionName.Scar:              {RegionName.Pl2},
        RegionName.Pl2:               {RegionName.GroundShaker},
        RegionName.GroundShaker:      {RegionName.DataSaix},
        RegionName.Stt:               {RegionName.TwilightThorn},
        RegionName.TwilightThorn:     {RegionName.Axel1},
        RegionName.Axel1:             {RegionName.Axel2},
        RegionName.Axel2:             {RegionName.DataRoxas},
        RegionName.Tt:                {RegionName.Tt2},
        RegionName.Tt2:               {RegionName.Tt3},
        RegionName.Tt3:               {RegionName.DataAxel},
        RegionName.Twtnw:             {RegionName.Roxas},
        RegionName.Roxas:             {RegionName.Xigbar},
        RegionName.Xigbar:            {RegionName.Luxord},
        RegionName.Luxord:            {RegionName.Saix},
        RegionName.Saix:              {RegionName.Twtnw2},
        RegionName.Twtnw2:            {RegionName.Xemnas},
        RegionName.Xemnas:            {RegionName.ArmoredXemnas, RegionName.DataXemnas},
        RegionName.ArmoredXemnas:     {RegionName.ArmoredXemnas2},
        RegionName.ArmoredXemnas2:    {RegionName.FinalXemnas},
        RegionName.LevelsVS1:         {RegionName.LevelsVS3},
        RegionName.LevelsVS3:         {RegionName.LevelsVS6},
        RegionName.LevelsVS6:         {RegionName.LevelsVS9},
        RegionName.LevelsVS9:         {RegionName.LevelsVS12},
        RegionName.LevelsVS12:        {RegionName.LevelsVS15},
        RegionName.LevelsVS15:        {RegionName.LevelsVS18},
        RegionName.LevelsVS18:        {RegionName.LevelsVS21},
        RegionName.LevelsVS21:        {RegionName.LevelsVS24},
        RegionName.LevelsVS24:        {RegionName.LevelsVS26},
    }

    names: typing.Dict[str, int] = {}
    for source, target in KH2RegionConnections.items():
        for region in target:
            connect(world, player, names, source, region)
    # connect(world, player, names, "Menu", RegionName.Keyblade)
    # connect(world, player, names, "Menu", RegionName.GoA)


#
# connect(world, player, names, RegionName.GoA, RegionName.LoD,
#        lambda state: state.kh_lod_unlocked(player, 1))
# connect(world, player, names, RegionName.LoD, RegionName.LoD2,
#        lambda state: state.kh_lod_unlocked(player, 2))
#
# connect(world, player, names, RegionName.GoA, RegionName.Oc,
#        lambda state: state.kh_oc_unlocked(player, 1))
# connect(world, player, names, RegionName.Oc, RegionName.Oc2,
#        lambda state: state.kh_oc_unlocked(player, 2))
# connect(world, player, names, RegionName.Oc2, RegionName.Zexion,
#        lambda state: state.kh_datazexion(player))
#
# connect(world, player, names, RegionName.Oc2, RegionName.Oc2_pain_and_panic,
#        lambda state: state.kh_painandpanic(player))
# connect(world, player, names, RegionName.Oc2, RegionName.Oc2_cerberus,
#        lambda state: state.kh_cerberuscup(player))
# connect(world, player, names, RegionName.Oc2, RegionName.Oc2_titan,
#        lambda state: state.kh_titan(player))
# connect(world, player, names, RegionName.Oc2, RegionName.Oc2_gof,
#        lambda state: state.kh_gof(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Ag,
#        lambda state: state.kh_ag_unlocked(player, 1))
# connect(world, player, names, RegionName.Ag, RegionName.Ag2,
#        lambda state: state.kh_ag_unlocked(player, 2)
#                      and (state.has(ItemName.FireElement, player)
#                           and state.has(ItemName.BlizzardElement, player)
#                           and state.has(ItemName.ThunderElement, player)))
# connect(world, player, names, RegionName.Ag2, RegionName.Lexaeus,
#        lambda state: state.kh_datalexaeus(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Dc,
#        lambda state: state.kh_dc_unlocked(player, 1))
# connect(world, player, names, RegionName.Dc, RegionName.Tr,
#       lambda state: state.kh_dc_unlocked(player, 2))
# connect(world, player, names, RegionName.Tr, RegionName.Marluxia,
#        lambda state: state.kh_datamarluxia(player))
# connect(world, player, names, RegionName.Tr, RegionName.Terra, lambda state: state.kh_terra(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Pr,
#        lambda state: state.kh_pr_unlocked(player, 1))
# connect(world, player, names, RegionName.Pr, RegionName.Pr2,
#        lambda state: state.kh_pr_unlocked(player, 2))
# connect(world, player, names, RegionName.Pr2, RegionName.Gr2,
#        lambda state: state.kh_gr2(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Bc,
#        lambda state: state.kh_bc_unlocked(player, 1))
# connect(world, player, names, RegionName.Bc, RegionName.Bc2,
#        lambda state: state.kh_bc_unlocked(player, 2))
# connect(world, player, names, RegionName.Bc2, RegionName.Xaldin,
#        lambda state: state.kh_xaldin(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Sp,
#        lambda state: state.kh_sp_unlocked(player, 1))
# connect(world, player, names, RegionName.Sp, RegionName.Sp2,
#        lambda state: state.kh_sp_unlocked(player, 2))
# connect(world, player, names, RegionName.Sp2, RegionName.Mcp,
#        lambda state: state.kh_mcp(player))
# connect(world, player, names, RegionName.Mcp, RegionName.Larxene,
#        lambda state: state.kh_datalarxene(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Ht,
#        lambda state: state.kh_ht_unlocked(player, 1))
# connect(world, player, names, RegionName.Ht, RegionName.Ht2,
#        lambda state: state.kh_ht_unlocked(player, 2))
# connect(world, player, names, RegionName.Ht2, RegionName.Vexen,
#        lambda state: state.kh_datavexen(player))
#
# connect(world, player, names, RegionName.GoA, RegionName.Hb,
#        lambda state: state.kh_hb_unlocked(player, 1))
# connect(world, player, names, RegionName.Hb, RegionName.Hb2,
#        lambda state: state.kh_hb_unlocked(player, 2))
# connect(world, player, names, RegionName.Hb2, RegionName.ThousandHeartless,
#        lambda state: state.kh_onek(player))
# connect(world, player, names, RegionName.ThousandHeartless, RegionName.Mushroom13,
#        lambda state: state.has(ItemName.ProofofPeace, player))
# connect(world, player, names, RegionName.ThousandHeartless, RegionName.Sephi,
#        lambda state: state.kh_sephi(player))
#
# connect(world, player, names, RegionName.Hb2, RegionName.CoR, lambda state: state.kh_cor(player))
# connect(world, player, names, RegionName.CoR, RegionName.Transport, lambda state:
# state.has(ItemName.HighJump, player, 3)
# and state.has(ItemName.AerialDodge, player, 3)
# and state.has(ItemName.Glide, player, 3))
#
# connect(world, player, names, RegionName.GoA, RegionName.Pl,
#        lambda state: state.kh_pl_unlocked(player, 1))
# connect(world, player, names, RegionName.Pl, RegionName.Pl2,
#        lambda state: state.kh_pl_unlocked(player, 2) and (
#                state.has(ItemName.BerserkCharge, player) or state.kh_reflect(player)))
#
# connect(world, player, names, RegionName.GoA, RegionName.STT,
#        lambda state: state.kh_stt_unlocked(player, 1))

# connect(world, player, names, RegionName.GoA, RegionName.TT,
#        lambda state: state.kh_tt_unlocked(player, 1))
# connect(world, player, names, RegionName.TT, RegionName.TT2,
#        lambda state: state.kh_tt_unlocked(player, 2))
# connect(world, player, names, RegionName.TT2, RegionName.TT3,
#        lambda state: state.kh_tt_unlocked(player, 3))
#
# connect(world, player, names, RegionName.GoA, RegionName.Twtnw,
#        lambda state: state.kh_twtnw_unlocked(player, 0))
# connect(world, player, names, RegionName.Twtnw, RegionName.Twtnw_PostRoxas,
#        lambda state: state.kh_roxastools(player))
# connect(world, player, names, RegionName.Twtnw_PostRoxas, RegionName.Twtnw_PostXigbar,
#        lambda state: state.kh_basetools(player) and (state.kh_donaldlimit(player) or (
#                state.has(ItemName.FinalForm, player) and state.has(ItemName.FireElement, player))))
# connect(world, player, names, RegionName.Twtnw_PostRoxas, RegionName.Twtnw2,
#        lambda state: state.kh_twtnw_unlocked(player, 1))
#
# Havisits = {RegionName.Ha1: 0, RegionName.Ha2: 1,
#                     RegionName.Ha3: 2,
#                     RegionName.Ha4: 3, RegionName.Ha5: 4,
#                     RegionName.Ha6: 5}
# for visit, tornpage in Havisits.items():
#    connect(world, player, names, RegionName.GoA, visit,
#            lambda state: (state.has(ItemName.TornPages, player, tornpage)))

# connect(world, player, names, RegionName.GoA, RegionName.LevelsVS1,
#        lambda state: state.kh_visit_locking_amount(player, 1))
# connect(world, player, names, RegionName.LevelsVS1, RegionName.LevelsVS3,
#        lambda state: state.kh_visit_locking_amount(player, 3))
# connect(world, player, names, RegionName.LevelsVS3, RegionName.LevelsVS6,
#        lambda state: state.kh_visit_locking_amount(player, 6))
# connect(world, player, names, RegionName.LevelsVS6, RegionName.LevelsVS9,
#        lambda state: state.kh_visit_locking_amount(player, 9))
# connect(world, player, names, RegionName.LevelsVS9, RegionName.LevelsVS12,
#        lambda state: state.kh_visit_locking_amount(player, 12))
# connect(world, player, names, RegionName.LevelsVS12, RegionName.LevelsVS15,
#        lambda state: state.kh_visit_locking_amount(player, 15))
# connect(world, player, names, RegionName.LevelsVS15, RegionName.LevelsVS18,
#        lambda state: state.kh_visit_locking_amount(player, 18))
# connect(world, player, names, RegionName.LevelsVS18, RegionName.LevelsVS21,
#         lambda state: state.kh_visit_locking_amount(player, 21))
# connect(world, player, names, RegionName.LevelsVS21, RegionName.LevelsVS24,
#         lambda state: state.kh_visit_locking_amount(player, 24))
# connect(world, player, names, RegionName.LevelsVS24, RegionName.LevelsVS26,
#         lambda state: state.kh_visit_locking_amount(player, 25))  # 25 because of goa twtnw bugs with visit locking.
#
# for region in RegionTable["ValorRegion"]:
#     connect(world, player, names, region, RegionName.Valor,
#             lambda state: state.has(ItemName.ValorForm, player))
# for region in RegionTable["WisdomRegion"]:
#     connect(world, player, names, region, RegionName.Wisdom,
#             lambda state: state.has(ItemName.WisdomForm, player))
# for region in RegionTable["LimitRegion"]:
#     connect(world, player, names, region, RegionName.Limit,
#             lambda state: state.has(ItemName.LimitForm, player))
# for region in RegionTable["MasterRegion"]:
#     connect(world, player, names, region, RegionName.Master,
#             lambda state: state.has(ItemName.MasterForm, player) and state.has(ItemName.DriveConverter, player))
# for region in RegionTable["FinalRegion"]:
#     connect(world, player, names, region, RegionName.Final,
#             lambda state: state.has(ItemName.FinalForm, player))


# shamelessly stolen from the sa2b
def connect(world: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_region(world: MultiWorld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = active_locations.get(location, 0)
            if loc_id:
                location = KH2Location(player, location, loc_id.code, ret)
                ret.locations.append(location)

    return ret
