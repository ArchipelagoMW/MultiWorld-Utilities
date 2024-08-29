from typing import Iterable, Callable, Optional
from BaseClasses import MultiWorld, Region
from ..GameID import jak1_name
from ..Locations import JakAndDaxterLocation, location_table
from ..locs import (OrbLocations as Orbs,
                    CellLocations as Cells,
                    ScoutLocations as Scouts,
                    SpecialLocations as Specials,
                    OrbCacheLocations as Caches)


class JakAndDaxterRegion(Region):
    """
    Holds region information such as name, level name, number of orbs available, etc.
    We especially need orb counts to be tracked because we need to know when you can
    afford the Citizen and Oracle orb payments for more checks.
    """
    game: str = jak1_name
    level_name: str
    orb_count: int

    def __init__(self, name: str, player: int, multiworld: MultiWorld, level_name: str = "", orb_count: int = 0):
        formatted_name = f"{level_name} {name}".strip()
        super().__init__(formatted_name, player, multiworld)
        self.level_name = level_name
        self.orb_count = orb_count

    def add_cell_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds a Power Cell Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        """
        for loc in locations:
            ap_id = Cells.to_ap_id(loc)
            self.add_jak_locations(ap_id, location_table[ap_id], access_rule)

    def add_fly_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds a Scout Fly Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        """
        for loc in locations:
            ap_id = Scouts.to_ap_id(loc)
            self.add_jak_locations(ap_id, location_table[ap_id], access_rule)

    def add_special_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds a Special Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        Special Locations should be matched alongside their respective
        Power Cell Locations, so you get 2 unlocks for these rather than 1.
        """
        for loc in locations:
            ap_id = Specials.to_ap_id(loc)
            self.add_jak_locations(ap_id, location_table[ap_id], access_rule)

    def add_cache_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds an Orb Cache Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        """
        for loc in locations:
            ap_id = Caches.to_ap_id(loc)
            self.add_jak_locations(ap_id, location_table[ap_id], access_rule)

    def add_orb_locations(self, level_index: int, bundle_index: int, access_rule: Optional[Callable] = None):
        """
        Adds Orb Bundle Locations to this region equal to `bundle_count`. Used only when Per-Level Orbsanity is enabled.
        The orb factory class will handle AP ID enumeration.
        """
        bundle_address = Orbs.create_address(level_index, bundle_index)
        location = JakAndDaxterLocation(self.player,
                                        f"{self.level_name} Orb Bundle {bundle_index + 1}".strip(),
                                        Orbs.to_ap_id(bundle_address),
                                        self)
        if access_rule:
            location.access_rule = access_rule
        self.locations.append(location)

    def add_jak_locations(self, ap_id: int, name: str, access_rule: Optional[Callable] = None):
        """
        Helper function to add Locations. Not to be used directly.
        """
        location = JakAndDaxterLocation(self.player, name, ap_id, self)
        if access_rule:
            location.access_rule = access_rule
        self.locations.append(location)