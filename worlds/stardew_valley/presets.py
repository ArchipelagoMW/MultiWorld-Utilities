from typing import Any, Dict

from Options import Accessibility, ProgressionBalancing, DeathLink
from .options import Goal, StartingMoney, ProfitMargin, BundleRandomization, BundlePrice, EntranceRandomization, SeasonRandomization, Cropsanity, \
    BackpackProgression, ToolProgression, ElevatorProgression, SkillProgression, BuildingProgression, FestivalLocations, ArcadeMachineLocations, \
    SpecialOrderLocations, QuestLocations, Fishsanity, Museumsanity, Friendsanity, FriendsanityHeartSize, NumberOfMovementBuffs, ExcludeGingerIsland, TrapItems, \
    MultipleDaySleepEnabled, MultipleDaySleepCost, ExperienceMultiplier, FriendshipMultiplier, DebrisMultiplier, QuickStart, \
    Gifting, FarmType, Monstersanity, Shipsanity, Cooksanity, Chefsanity, Craftsanity, Booksanity, Walnutsanity, EnabledFillerBuffs

# @formatter:off
from .strings.ap_names.ap_option_names import OptionName

all_random_settings = {
    "progression_balancing":                "random",
    "accessibility":                        "random",
    Goal.internal_name:                     "random",
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "random",
    ProfitMargin.internal_name:             "random",
    BundleRandomization.internal_name:      "random",
    BundlePrice.internal_name:              "random",
    EntranceRandomization.internal_name:    "random",
    SeasonRandomization.internal_name:      "random",
    Cropsanity.internal_name:               "random",
    BackpackProgression.internal_name:      "random",
    ToolProgression.internal_name:          "random",
    ElevatorProgression.internal_name:      "random",
    SkillProgression.internal_name:         "random",
    BuildingProgression.internal_name:      "random",
    FestivalLocations.internal_name:        "random",
    ArcadeMachineLocations.internal_name:   "random",
    SpecialOrderLocations.internal_name:    "random",
    QuestLocations.internal_name:           "random",
    Fishsanity.internal_name:               "random",
    Museumsanity.internal_name:             "random",
    Monstersanity.internal_name:            "random",
    Shipsanity.internal_name:               "random",
    Cooksanity.internal_name:               "random",
    Chefsanity.internal_name:               "random",
    Craftsanity.internal_name:              "random",
    Friendsanity.internal_name:             "random",
    FriendsanityHeartSize.internal_name:    "random",
    Booksanity.internal_name:               "random",
    Walnutsanity.internal_name:             "random",
    NumberOfMovementBuffs.internal_name:    "random",
    EnabledFillerBuffs.internal_name:       "random",
    ExcludeGingerIsland.internal_name:      "random",
    TrapItems.internal_name:                "random",
    MultipleDaySleepEnabled.internal_name:  "random",
    MultipleDaySleepCost.internal_name:     "random",
    ExperienceMultiplier.internal_name:     "random",
    FriendshipMultiplier.internal_name:     "random",
    DebrisMultiplier.internal_name:         "random",
    QuickStart.internal_name:               "random",
    Gifting.internal_name:                  "random",
    "death_link":                           "random",
}

easy_settings = {
    "progression_balancing":                ProgressionBalancing.default,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.option_community_center,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "very rich",
    ProfitMargin.internal_name:             "double",
    BundleRandomization.internal_name:      BundleRandomization.option_thematic,
    BundlePrice.internal_name:              BundlePrice.option_cheap,
    EntranceRandomization.internal_name:    EntranceRandomization.option_disabled,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized_not_winter,
    Cropsanity.internal_name:               Cropsanity.option_enabled,
    BackpackProgression.internal_name:      BackpackProgression.option_early_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive_very_cheap,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive,
    SkillProgression.internal_name:         SkillProgression.option_progressive,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive_very_cheap,
    FestivalLocations.internal_name:        FestivalLocations.option_easy,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_disabled,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_vanilla_very_short,
    QuestLocations.internal_name:           "minimum",
    Fishsanity.internal_name:               Fishsanity.option_only_easy_fish,
    Museumsanity.internal_name:             Museumsanity.option_milestones,
    Monstersanity.internal_name:            Monstersanity.option_one_per_category,
    Shipsanity.internal_name:               Shipsanity.option_none,
    Cooksanity.internal_name:               Cooksanity.option_none,
    Chefsanity.internal_name:               Chefsanity.option_none,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_none,
    FriendsanityHeartSize.internal_name:    4,
    Booksanity.internal_name:               Booksanity.option_none,
    Walnutsanity.internal_name:             Walnutsanity.preset_none,
    NumberOfMovementBuffs.internal_name:    8,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.preset_all,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_true,
    TrapItems.internal_name:                TrapItems.option_easy,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.option_true,
    MultipleDaySleepCost.internal_name:     "free",
    ExperienceMultiplier.internal_name:     "triple",
    FriendshipMultiplier.internal_name:     "quadruple",
    DebrisMultiplier.internal_name:         DebrisMultiplier.option_quarter,
    QuickStart.internal_name:               QuickStart.option_true,
    Gifting.internal_name:                  Gifting.option_true,
    "death_link":                           "false",
}

medium_settings = {
    "progression_balancing":                25,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.option_community_center,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "rich",
    ProfitMargin.internal_name:             150,
    BundleRandomization.internal_name:      BundleRandomization.option_remixed,
    BundlePrice.internal_name:              BundlePrice.option_normal,
    EntranceRandomization.internal_name:    EntranceRandomization.option_non_progression,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized,
    Cropsanity.internal_name:               Cropsanity.option_enabled,
    BackpackProgression.internal_name:      BackpackProgression.option_early_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive_cheap,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive,
    SkillProgression.internal_name:         SkillProgression.option_progressive,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive_cheap,
    FestivalLocations.internal_name:        FestivalLocations.option_hard,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_victories_easy,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_board_short,
    QuestLocations.internal_name:           "normal",
    Fishsanity.internal_name:               Fishsanity.option_exclude_legendaries,
    Museumsanity.internal_name:             Museumsanity.option_milestones,
    Monstersanity.internal_name:            Monstersanity.option_one_per_monster,
    Shipsanity.internal_name:               Shipsanity.option_none,
    Cooksanity.internal_name:               Cooksanity.option_none,
    Chefsanity.internal_name:               Chefsanity.option_queen_of_sauce,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_starting_npcs,
    FriendsanityHeartSize.internal_name:    4,
    Booksanity.internal_name:               Booksanity.option_power_skill,
    Walnutsanity.internal_name:             [OptionName.walnutsanity_puzzles],
    NumberOfMovementBuffs.internal_name:    6,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.preset_all,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_true,
    TrapItems.internal_name:                TrapItems.option_medium,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.option_true,
    MultipleDaySleepCost.internal_name:     "free",
    ExperienceMultiplier.internal_name:     "double",
    FriendshipMultiplier.internal_name:     "triple",
    DebrisMultiplier.internal_name:         DebrisMultiplier.option_half,
    QuickStart.internal_name:               QuickStart.option_true,
    Gifting.internal_name:                  Gifting.option_true,
    "death_link":                           "false",
}

hard_settings = {
    "progression_balancing":                0,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.option_grandpa_evaluation,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "extra",
    ProfitMargin.internal_name:             "normal",
    BundleRandomization.internal_name:      BundleRandomization.option_remixed,
    BundlePrice.internal_name:              BundlePrice.option_expensive,
    EntranceRandomization.internal_name:    EntranceRandomization.option_buildings_without_house,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized,
    Cropsanity.internal_name:               Cropsanity.option_enabled,
    BackpackProgression.internal_name:      BackpackProgression.option_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive_from_previous_floor,
    SkillProgression.internal_name:         SkillProgression.option_progressive_with_masteries,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive,
    FestivalLocations.internal_name:        FestivalLocations.option_hard,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_full_shuffling,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_board_qi_short,
    QuestLocations.internal_name:           "lots",
    Fishsanity.internal_name:               Fishsanity.option_all,
    Museumsanity.internal_name:             Museumsanity.option_all,
    Monstersanity.internal_name:            Monstersanity.option_progressive_goals,
    Shipsanity.internal_name:               Shipsanity.option_crops,
    Cooksanity.internal_name:               Cooksanity.option_queen_of_sauce,
    Chefsanity.internal_name:               Chefsanity.option_qos_and_purchases,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_all,
    FriendsanityHeartSize.internal_name:    4,
    Booksanity.internal_name:               Booksanity.option_all,
    Walnutsanity.internal_name:             Walnutsanity.preset_all,
    NumberOfMovementBuffs.internal_name:    4,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.default,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_false,
    TrapItems.internal_name:                TrapItems.option_hard,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.option_true,
    MultipleDaySleepCost.internal_name:     "cheap",
    ExperienceMultiplier.internal_name:     "vanilla",
    FriendshipMultiplier.internal_name:     "double",
    DebrisMultiplier.internal_name:         DebrisMultiplier.option_vanilla,
    QuickStart.internal_name:               QuickStart.option_true,
    Gifting.internal_name:                  Gifting.option_true,
    "death_link":                           "true",
}

nightmare_settings = {
    "progression_balancing":                0,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.option_community_center,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "vanilla",
    ProfitMargin.internal_name:             "half",
    BundleRandomization.internal_name:      BundleRandomization.option_shuffled,
    BundlePrice.internal_name:              BundlePrice.option_very_expensive,
    EntranceRandomization.internal_name:    EntranceRandomization.option_buildings,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized,
    Cropsanity.internal_name:               Cropsanity.option_enabled,
    BackpackProgression.internal_name:      BackpackProgression.option_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive_from_previous_floor,
    SkillProgression.internal_name:         SkillProgression.option_progressive_with_masteries,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive,
    FestivalLocations.internal_name:        FestivalLocations.option_hard,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_full_shuffling,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_board_qi,
    QuestLocations.internal_name:           "maximum",
    Fishsanity.internal_name:               Fishsanity.option_special,
    Museumsanity.internal_name:             Museumsanity.option_all,
    Monstersanity.internal_name:            Monstersanity.option_split_goals,
    Shipsanity.internal_name:               Shipsanity.option_full_shipment_with_fish,
    Cooksanity.internal_name:               Cooksanity.option_queen_of_sauce,
    Chefsanity.internal_name:               Chefsanity.option_qos_and_purchases,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_all_with_marriage,
    FriendsanityHeartSize.internal_name:    4,
    Booksanity.internal_name:               Booksanity.option_all,
    Walnutsanity.internal_name:             Walnutsanity.preset_all,
    NumberOfMovementBuffs.internal_name:    2,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.preset_none,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_false,
    TrapItems.internal_name:                TrapItems.option_hell,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.option_true,
    MultipleDaySleepCost.internal_name:     "expensive",
    ExperienceMultiplier.internal_name:     "half",
    FriendshipMultiplier.internal_name:     "vanilla",
    DebrisMultiplier.internal_name:         DebrisMultiplier.option_vanilla,
    QuickStart.internal_name:               QuickStart.option_false,
    Gifting.internal_name:                  Gifting.option_true,
    "death_link":                           "true",
}

short_settings = {
    "progression_balancing":                ProgressionBalancing.default,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.option_bottom_of_the_mines,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            "filthy rich",
    ProfitMargin.internal_name:             "quadruple",
    BundleRandomization.internal_name:      BundleRandomization.option_remixed,
    BundlePrice.internal_name:              BundlePrice.option_minimum,
    EntranceRandomization.internal_name:    EntranceRandomization.option_disabled,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized_not_winter,
    Cropsanity.internal_name:               Cropsanity.option_disabled,
    BackpackProgression.internal_name:      BackpackProgression.option_early_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive_very_cheap,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive,
    SkillProgression.internal_name:         SkillProgression.option_progressive,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive_very_cheap,
    FestivalLocations.internal_name:        FestivalLocations.option_disabled,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_disabled,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_vanilla_very_short,
    QuestLocations.internal_name:           "none",
    Fishsanity.internal_name:               Fishsanity.option_none,
    Museumsanity.internal_name:             Museumsanity.option_none,
    Monstersanity.internal_name:            Monstersanity.option_none,
    Shipsanity.internal_name:               Shipsanity.option_none,
    Cooksanity.internal_name:               Cooksanity.option_none,
    Chefsanity.internal_name:               Chefsanity.option_none,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_none,
    FriendsanityHeartSize.internal_name:    4,
    Booksanity.internal_name:               Booksanity.option_none,
    Walnutsanity.internal_name:             Walnutsanity.preset_none,
    NumberOfMovementBuffs.internal_name:    10,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.preset_all,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_true,
    TrapItems.internal_name:                TrapItems.option_easy,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.option_true,
    MultipleDaySleepCost.internal_name:     "free",
    ExperienceMultiplier.internal_name:     "quadruple",
    FriendshipMultiplier.internal_name:     800,
    DebrisMultiplier.internal_name:         DebrisMultiplier.option_none,
    QuickStart.internal_name:               QuickStart.option_true,
    Gifting.internal_name:                  Gifting.option_true,
    "death_link":                           "false",
}

minsanity_settings = {
    "progression_balancing":                ProgressionBalancing.default,
    "accessibility":                        Accessibility.option_minimal,
    Goal.internal_name:                     Goal.default,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            StartingMoney.default,
    ProfitMargin.internal_name:             ProfitMargin.default,
    BundleRandomization.internal_name:      BundleRandomization.default,
    BundlePrice.internal_name:              BundlePrice.default,
    EntranceRandomization.internal_name:    EntranceRandomization.default,
    SeasonRandomization.internal_name:      SeasonRandomization.option_disabled,
    Cropsanity.internal_name:               Cropsanity.option_disabled,
    BackpackProgression.internal_name:      BackpackProgression.option_vanilla,
    ToolProgression.internal_name:          ToolProgression.option_vanilla,
    ElevatorProgression.internal_name:      ElevatorProgression.option_vanilla,
    SkillProgression.internal_name:         SkillProgression.option_vanilla,
    BuildingProgression.internal_name:      BuildingProgression.option_vanilla,
    FestivalLocations.internal_name:        FestivalLocations.option_disabled,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_disabled,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_vanilla_very_short,
    QuestLocations.internal_name:           "none",
    Fishsanity.internal_name:               Fishsanity.option_none,
    Museumsanity.internal_name:             Museumsanity.option_none,
    Monstersanity.internal_name:            Monstersanity.option_none,
    Shipsanity.internal_name:               Shipsanity.option_none,
    Cooksanity.internal_name:               Cooksanity.option_none,
    Chefsanity.internal_name:               Chefsanity.option_none,
    Craftsanity.internal_name:              Craftsanity.option_none,
    Friendsanity.internal_name:             Friendsanity.option_none,
    FriendsanityHeartSize.internal_name:    FriendsanityHeartSize.default,
    Booksanity.internal_name:               Booksanity.option_none,
    Walnutsanity.internal_name:             Walnutsanity.preset_none,
    NumberOfMovementBuffs.internal_name:    NumberOfMovementBuffs.default,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.default,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_true,
    TrapItems.internal_name:                TrapItems.default,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.default,
    MultipleDaySleepCost.internal_name:     MultipleDaySleepCost.default,
    ExperienceMultiplier.internal_name:     ExperienceMultiplier.default,
    FriendshipMultiplier.internal_name:     FriendshipMultiplier.default,
    DebrisMultiplier.internal_name:         DebrisMultiplier.default,
    QuickStart.internal_name:               QuickStart.default,
    Gifting.internal_name:                  Gifting.default,
    "death_link":                           DeathLink.default,
}

allsanity_settings = {
    "progression_balancing":                ProgressionBalancing.default,
    "accessibility":                        Accessibility.option_full,
    Goal.internal_name:                     Goal.default,
    FarmType.internal_name:                 "random",
    StartingMoney.internal_name:            StartingMoney.default,
    ProfitMargin.internal_name:             ProfitMargin.default,
    BundleRandomization.internal_name:      BundleRandomization.default,
    BundlePrice.internal_name:              BundlePrice.default,
    EntranceRandomization.internal_name:    EntranceRandomization.option_buildings,
    SeasonRandomization.internal_name:      SeasonRandomization.option_randomized,
    Cropsanity.internal_name:               Cropsanity.option_enabled,
    BackpackProgression.internal_name:      BackpackProgression.option_early_progressive,
    ToolProgression.internal_name:          ToolProgression.option_progressive,
    ElevatorProgression.internal_name:      ElevatorProgression.option_progressive,
    SkillProgression.internal_name:         SkillProgression.option_progressive_with_masteries,
    BuildingProgression.internal_name:      BuildingProgression.option_progressive,
    FestivalLocations.internal_name:        FestivalLocations.option_hard,
    ArcadeMachineLocations.internal_name:   ArcadeMachineLocations.option_full_shuffling,
    SpecialOrderLocations.internal_name:    SpecialOrderLocations.option_board_qi,
    QuestLocations.internal_name:           "maximum",
    Fishsanity.internal_name:               Fishsanity.option_all,
    Museumsanity.internal_name:             Museumsanity.option_all,
    Monstersanity.internal_name:            Monstersanity.option_progressive_goals,
    Shipsanity.internal_name:               Shipsanity.option_everything,
    Cooksanity.internal_name:               Cooksanity.option_all,
    Chefsanity.internal_name:               Chefsanity.option_all,
    Craftsanity.internal_name:              Craftsanity.option_all,
    Friendsanity.internal_name:             Friendsanity.option_all,
    FriendsanityHeartSize.internal_name:    1,
    Booksanity.internal_name:               Booksanity.option_all,
    Walnutsanity.internal_name:             Walnutsanity.preset_all,
    NumberOfMovementBuffs.internal_name:    12,
    EnabledFillerBuffs.internal_name:       EnabledFillerBuffs.preset_all,
    ExcludeGingerIsland.internal_name:      ExcludeGingerIsland.option_false,
    TrapItems.internal_name:                TrapItems.default,
    MultipleDaySleepEnabled.internal_name:  MultipleDaySleepEnabled.default,
    MultipleDaySleepCost.internal_name:     MultipleDaySleepCost.default,
    ExperienceMultiplier.internal_name:     ExperienceMultiplier.default,
    FriendshipMultiplier.internal_name:     FriendshipMultiplier.default,
    DebrisMultiplier.internal_name:         DebrisMultiplier.default,
    QuickStart.internal_name:               QuickStart.default,
    Gifting.internal_name:                  Gifting.default,
    "death_link":                           DeathLink.default,
}
# @formatter:on


sv_options_presets: Dict[str, Dict[str, Any]] = {
    "All random": all_random_settings,
    "Easy": easy_settings,
    "Medium": medium_settings,
    "Hard": hard_settings,
    "Nightmare": nightmare_settings,
    "Short": short_settings,
    "Minsanity": minsanity_settings,
    "Allsanity": allsanity_settings,
}
