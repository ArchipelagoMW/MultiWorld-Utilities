from functools import cached_property
from typing import Union, Tuple

from Utils import cache_self1
from worlds.stardew_valley.strings.craftable_names import Fishing
from .combat_logic import CombatLogic
from .crop_logic import CropLogic
from .has_logic import HasLogic
from .received_logic import ReceivedLogic
from .region_logic import RegionLogic
from .season_logic import SeasonLogic
from .time_logic import TimeLogic
from .tool_logic import ToolLogic
from .. import options
from ..data import all_crops
from ..mods.logic.magic_logic import MagicLogic
from ..mods.logic.mod_skills_levels import get_mod_skill_levels
from ..options import SkillProgression, Mods
from ..stardew_rule import StardewRule, True_, Or
from ..strings.machine_names import Machine
from ..strings.performance_names import Performance
from ..strings.region_names import Region
from ..strings.skill_names import Skill
from ..strings.tool_names import ToolMaterial, Tool

fishing_regions = (Region.beach, Region.town, Region.forest, Region.mountain, Region.island_south, Region.island_west)


class SkillLogic:
    skill_option: SkillProgression
    received: ReceivedLogic
    has: HasLogic
    region: RegionLogic
    season: SeasonLogic
    time: TimeLogic
    tool: ToolLogic
    combat: CombatLogic
    crop: CropLogic
    magic: MagicLogic
    mods: Mods

    def __init__(self, player: int, skill_option: SkillProgression, received: ReceivedLogic, has: HasLogic, region: RegionLogic, season: SeasonLogic,
                 time: TimeLogic, tool: ToolLogic, combat: CombatLogic, crop: CropLogic):
        self.player = player
        self.skill_option = skill_option
        self.received = received
        self.has = has
        self.region = region
        self.season = season
        self.time = time
        self.tool = tool
        self.combat = combat
        self.crop = crop

    def set_mod_logic(self, magic: MagicLogic, mods: Mods):
        self.magic = magic
        self.mods = mods

    # Should be cached
    def can_earn_level(self, skill: str, level: int) -> StardewRule:
        if level <= 0:
            return True_()

        tool_level = (level - 1) // 2
        tool_material = ToolMaterial.tiers[tool_level]
        months = max(1, level - 1)
        months_rule = self.time.has_lived_months(months)
        previous_level_rule = self.has_level(skill, level - 1)

        if skill == Skill.fishing:
            xp_rule = self.tool.has_tool(Tool.fishing_rod, ToolMaterial.tiers[max(tool_level, 3)])
        elif skill == Skill.farming:
            xp_rule = self.tool.has_tool(Tool.hoe, tool_material) & self.tool.can_water(tool_level)
        elif skill == Skill.foraging:
            xp_rule = self.tool.has_tool(Tool.axe,
                                         tool_material) | self.magic.can_use_clear_debris_instead_of_tool_level(
                tool_level)
        elif skill == Skill.mining:
            xp_rule = self.tool.has_tool(Tool.pickaxe,
                                         tool_material) | self.magic.can_use_clear_debris_instead_of_tool_level(
                tool_level)
        elif skill == Skill.combat:
            combat_tier = Performance.tiers[tool_level]
            xp_rule = self.combat.can_fight_at_level(combat_tier)
        else:
            raise Exception(f"Unknown skill: {skill}")

        return previous_level_rule & months_rule & xp_rule

    # Should be cached
    def has_level(self, skill: str, level: int) -> StardewRule:
        if level <= 0:
            return True_()

        if self.skill_option == options.SkillProgression.option_progressive:
            return self.received(f"{skill} Level", level)

        return self.can_earn_level(skill, level)

    @cache_self1
    def has_farming_level(self, level: int) -> StardewRule:
        return self.has_level(Skill.farming, level)

    # Should be cached
    def has_total_level(self, level: int, allow_modded_skills: bool = False) -> StardewRule:
        if level <= 0:
            return True_()

        if self.skill_option == options.SkillProgression.option_progressive:
            skills_items = ("Farming Level", "Mining Level", "Foraging Level", "Fishing Level", "Combat Level")
            if allow_modded_skills:
                skills_items += get_mod_skill_levels(self.mods)
            return self.received(skills_items, level)

        months_with_4_skills = max(1, (level // 4) - 1)
        months_with_5_skills = max(1, (level // 5) - 1)
        rule_with_fishing = self.time.has_lived_months(months_with_5_skills) & self.can_get_fishing_xp
        if level > 40:
            return rule_with_fishing
        return self.time.has_lived_months(months_with_4_skills) | rule_with_fishing

    @cached_property
    def can_get_farming_xp(self) -> StardewRule:
        crop_rules = []
        for crop in all_crops:
            crop_rules.append(self.crop.can_grow(crop))
        return Or(*crop_rules)

    @cached_property
    def can_get_foraging_xp(self) -> StardewRule:
        tool_rule = self.tool.has_tool(Tool.axe)
        tree_rule = self.region.can_reach(Region.forest) & self.season.has_any_not_winter()
        stump_rule = self.region.can_reach(Region.secret_woods) & self.tool.has_tool(Tool.axe, ToolMaterial.copper)
        return tool_rule & (tree_rule | stump_rule)

    @cached_property
    def can_get_mining_xp(self) -> StardewRule:
        tool_rule = self.tool.has_tool(Tool.pickaxe)
        stone_rule = self.region.can_reach_any((Region.mines_floor_5, Region.quarry, Region.skull_cavern_25, Region.volcano_floor_5))
        return tool_rule & stone_rule

    @cached_property
    def can_get_combat_xp(self) -> StardewRule:
        tool_rule = self.combat.has_any_weapon()
        enemy_rule = self.region.can_reach_any((Region.mines_floor_5, Region.skull_cavern_25, Region.volcano_floor_5))
        return tool_rule & enemy_rule

    @cached_property
    def can_get_fishing_xp(self) -> StardewRule:
        if self.skill_option == options.SkillProgression.option_progressive:
            return self.can_fish() | self.can_crab_pot

        return self.can_fish()

    # Should be cached
    def can_fish(self, regions: Union[str, Tuple[str, ...]] = None, difficulty: int = 0) -> StardewRule:
        if isinstance(regions, str):
            regions = regions,
        if regions is None or len(regions) == 0:
            regions = fishing_regions
        skill_required = min(10, max(0, int((difficulty / 10) - 1)))
        if difficulty <= 40:
            skill_required = 0
        skill_rule = self.has_level(Skill.fishing, skill_required)
        region_rule = self.region.can_reach_any(regions)
        number_fishing_rod_required = 1 if difficulty < 50 else (2 if difficulty < 80 else 4)
        return self.tool.has_fishing_rod(number_fishing_rod_required) & skill_rule & region_rule

    @cache_self1
    def can_crab_pot_at(self, region: str) -> StardewRule:
        return self.can_crab_pot & self.region.can_reach(region)

    @cached_property
    def can_crab_pot(self) -> StardewRule:
        crab_pot_rule = self.has(Fishing.bait)
        if self.skill_option == options.SkillProgression.option_progressive:
            crab_pot_rule = crab_pot_rule & self.has(Machine.crab_pot)
        else:
            crab_pot_rule = crab_pot_rule & self.can_get_fishing_xp

        water_region_rules = self.region.can_reach_any(fishing_regions)
        return crab_pot_rule & water_region_rules
