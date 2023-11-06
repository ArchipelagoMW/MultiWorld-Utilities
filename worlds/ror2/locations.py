from typing import Tuple, Dict
from BaseClasses import Location
from .options import TotalLocations, ChestsPerEnvironment, ShrinesPerEnvironment, ScavengersPerEnvironment, \
    ScannersPerEnvironment, AltarsPerEnvironment
from .ror2environments import environment_orderedstages_table, compress_dict_list_horizontal,\
    environment_vanilla_orderedstages_table, environment_sotv_orderedstages_table


class RiskOfRainLocation(Location):
    game: str = "Risk of Rain 2"


ror2_locations_start_id = 38000


def get_classic_item_pickups(n: int) -> Dict[str, int]:
    """Get n ItemPickups, capped at the max value for TotalLocations"""
    n = max(n, 0)
    n = min(n, TotalLocations.range_end)
    return {f"ItemPickup{i + 1}": ror2_locations_start_id + i for i in range(n)}


item_pickups = get_classic_item_pickups(TotalLocations.range_end)
location_table = item_pickups


# highest numbered orderedstages
# (this is so we can easily calculate the environment and location "offset" ids)
highest_ordered_stage: int = max(compress_dict_list_horizontal(environment_orderedstages_table).values())

ror2_locations_start_ordered_stage = ror2_locations_start_id + TotalLocations.range_end

# TODO is there a better, more generic way to do this?
offset_chests = 0
offset_shrines = offset_chests + ChestsPerEnvironment.range_end
offset_scavengers = offset_shrines + ShrinesPerEnvironment.range_end
offset_scanners = offset_scavengers + ScavengersPerEnvironment.range_end
offset_altars = offset_scanners + ScannersPerEnvironment.range_end

# total space allocated to the locations in a single orderedstage environment
allocation = offset_altars + AltarsPerEnvironment.range_end


def get_environment_locations(chests: int, shrines: int, scavengers: int, scanners: int, altars: int,
                              environment: Tuple[str, int]) -> Dict[str, int]:
    """Get the locations within a specific environment"""
    environment_name = environment[0]
    environment_index = environment[1]
    locations = {}

    # due to this mapping, since environment ids are not consecutive, there are lots of "wasted" id numbers
    environment_start_id = environment_index * allocation + ror2_locations_start_ordered_stage
    for n in range(chests):
        locations.update({f"{environment_name}: Chest {n + 1}":
                              n + offset_chests + environment_start_id})
    for n in range(shrines):
        locations.update({f"{environment_name}: Shrine {n + 1}":
                              n + offset_shrines + environment_start_id})
    for n in range(scavengers):
        locations.update({f"{environment_name}: Scavenger {n + 1}":
                              n + offset_scavengers + environment_start_id})
    for n in range(scanners):
        locations.update({f"{environment_name}: Radio Scanner {n + 1}":
                              n + offset_scanners + environment_start_id})
    for n in range(altars):
        locations.update({f"{environment_name}: Newt Altar {n + 1}":
                              n + offset_altars + environment_start_id})
    return locations


def get_locations(chests: int, shrines: int, scavengers: int, scanners: int, altars: int, dlc_sotv: bool) -> Dict[
    str, int]:
    """Get a dictionary of locations for the orderedstage environments with the locations from the parameters."""
    locations = {}
    orderedstages = compress_dict_list_horizontal(environment_vanilla_orderedstages_table)
    if dlc_sotv:
        orderedstages.update(compress_dict_list_horizontal(environment_sotv_orderedstages_table))
    # for every environment, generate the respective locations
    for environment_name, environment_index in orderedstages.items():
        locations.update(get_environment_locations(
            chests=chests,
            shrines=shrines,
            scavengers=scavengers,
            scanners=scanners,
            altars=altars,
            environment=(environment_name, environment_index)
        ))
    return locations


def get_all_locations(dlc_sotv: bool = True) -> Dict[str, int]:
    """
    Get all locations in ordered stages.
    Set dlc_sotv to true for the SOTV DLC to be included.
    """
    # to get all locations, attempt using as many locations as possible
    return get_locations(
        chests=ChestsPerEnvironment.range_end,
        shrines=ShrinesPerEnvironment.range_end,
        scavengers=ScavengersPerEnvironment.range_end,
        scanners=ScannersPerEnvironment.range_end,
        altars=AltarsPerEnvironment.range_end,
        dlc_sotv=dlc_sotv
    )


ror2_location_post_orderedstage = ror2_locations_start_ordered_stage + \
                                  highest_ordered_stage * allocation
location_table.update(get_all_locations())
# use the sotv dlc in the lookup table so that all ids can be looked up regardless of use
