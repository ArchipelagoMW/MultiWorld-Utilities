from typing import Dict, Set, Tuple, Union

from .data.entrance_rule_data import entrance_rule_data
from .data.item_data import item_data, ZorkGrandInquisitorItemData
from .data.location_data import location_data, ZorkGrandInquisitorLocationData

from .enums import (
    ZorkGrandInquisitorEvents,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorLocations,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorTags,
)


def item_names_to_id() -> Dict[str, int]:
    return {item.value: data.archipelago_id for item, data in item_data.items()}


def item_names_to_item() -> Dict[str, ZorkGrandInquisitorItems]:
    return {item.value: item for item, _ in item_data.items()}


def location_names_to_id() -> Dict[str, int]:
    return {
        location.value: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def location_names_to_location() -> Dict[str, ZorkGrandInquisitorLocations]:
    return {
        location.value: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_goals() -> Dict[int, ZorkGrandInquisitorGoals]:
    return {goal.value: goal for goal in ZorkGrandInquisitorGoals}


def id_to_items() -> Dict[int, ZorkGrandInquisitorItems]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, ZorkGrandInquisitorLocations]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def item_groups() -> Dict[str, Set[str]]:
    groups: Dict[str, Set[str]] = dict()

    tag: ZorkGrandInquisitorTags
    for tag in ZorkGrandInquisitorTags:
        groups[tag.value] = set()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.tags is not None:
            for tag in data.tags:
                groups[tag.value].add(item.value)

    return {k: v for k, v in groups.items() if len(v)}


def items_with_tag(tag) -> Set[ZorkGrandInquisitorItems]:
    items: Set[ZorkGrandInquisitorItems] = set()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.tags is not None and tag in data.tags:
            items.add(item)

    return items


def game_id_to_items() -> Dict[int, ZorkGrandInquisitorItems]:
    mapping: Dict[int, ZorkGrandInquisitorItems] = dict()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.game_state_keys is not None:
            for key in data.game_state_keys:
                mapping[key] = item

    return mapping


def location_groups() -> Dict[str, Set[str]]:
    groups: Dict[str, Set[str]] = dict()

    tag: ZorkGrandInquisitorTags
    for tag in ZorkGrandInquisitorTags:
        groups[tag.value] = set()

    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            for tag in data.tags:
                groups[tag.value].add(location.value)

    return {k: v for k, v in groups.items() if len(v)}


def locations_by_region(include_deathsanity: bool = False) -> Dict[
    ZorkGrandInquisitorRegions, Set[ZorkGrandInquisitorLocations]
]:
    mapping: Dict[ZorkGrandInquisitorRegions, Set[ZorkGrandInquisitorLocations]] = dict()

    region: ZorkGrandInquisitorRegions
    for region in ZorkGrandInquisitorRegions:
        mapping[region] = set()

    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData
    for location, data in location_data.items():
        if include_deathsanity is False and ZorkGrandInquisitorTags.DEATHSANITY in (
            data.tags or tuple()
        ):
            continue

        mapping[data.region].add(location)

    return mapping


def locations_with_tag(tag: ZorkGrandInquisitorTags) -> Set[ZorkGrandInquisitorLocations]:
    locations: Set[ZorkGrandInquisitorLocations] = set()

    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData
    for location, data in location_data.items():
        if data.tags is not None and tag in data.tags:
            locations.add(location)

    return locations


def location_access_rule_for(location: ZorkGrandInquisitorLocations, player: int) -> str:
    data: ZorkGrandInquisitorLocationData = location_data[location]

    if data.requirements is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement: Union[ZorkGrandInquisitorEvents, ZorkGrandInquisitorItems]
    for i, requirement in enumerate(data.requirements):
        lambda_string += f"state.has(\"{requirement.value}\", {player})"

        if i < len(data.requirements) - 1:
            lambda_string += " and "

    return lambda_string


def entrance_access_rule_for(
    region_origin: ZorkGrandInquisitorRegions,
    region_destination: ZorkGrandInquisitorRegions,
    player: int
) -> str:
    data: Union[
        Tuple[
            Tuple[
                Union[
                    ZorkGrandInquisitorEvents,
                    ZorkGrandInquisitorItems,
                    ZorkGrandInquisitorRegions,
                ],
                ...,
            ],
            ...,
        ],
        None,
    ] = entrance_rule_data[(region_origin, region_destination)]

    if data is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement_group: Tuple[
        Union[
            ZorkGrandInquisitorEvents,
            ZorkGrandInquisitorItems,
            ZorkGrandInquisitorRegions,
        ],
        ...,
    ]
    for i, requirement_group in enumerate(data):
        lambda_string += "("

        ii: int
        requirement: Union[
            ZorkGrandInquisitorEvents,
            ZorkGrandInquisitorItems,
            ZorkGrandInquisitorRegions,
        ]
        for ii, requirement in enumerate(requirement_group):
            requirement_type: Union[
                ZorkGrandInquisitorEvents,
                ZorkGrandInquisitorItems,
                ZorkGrandInquisitorRegions,
            ] = type(requirement)

            if requirement_type in (ZorkGrandInquisitorEvents, ZorkGrandInquisitorItems):
                lambda_string += f"state.has(\"{requirement.value}\", {player})"
            elif requirement_type == ZorkGrandInquisitorRegions:
                lambda_string += f"state.can_reach(\"{requirement.value}\", \"Region\", {player})"

            if ii < len(requirement_group) - 1:
                lambda_string += " and "

        lambda_string += ")"

        if i < len(data) - 1:
            lambda_string += " or "

    return lambda_string
