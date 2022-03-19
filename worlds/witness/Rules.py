from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


class WitnessLogic(LogicMixin):
    def _witness_has_lasers(self, player: int, amount: int) -> bool:    
        lasers = 0
        
        lasers += int(self.can_reach("Symmetry Island Laser", "Location", player))
        lasers += int(self.can_reach("Desert Laser", "Location", player))
        lasers += int(self.can_reach("Town Laser", "Location", player))
        lasers += int(self.can_reach("Quarry Laser", "Location", player))
        lasers += int(self.can_reach("Shadows Laser", "Location", player))
        lasers += int(self.can_reach("Keep Laser Hedges", "Location", player) and self.can_reach("Keep Laser Pressure Plates", "Location", player))
        lasers += int(self.can_reach("Jungle Laser", "Location", player))
        lasers += int(self.can_reach("Swamp Laser", "Location", player))
        lasers += int(self.can_reach("Treehouse Laser", "Location", player))
        lasers += int(self.can_reach("Bunker Laser", "Location", player))
        lasers += int(self.can_reach("Monastery Laser", "Location", player))
        
        
        return lasers >= amount
        
    def _can_solve_panel(self, panel, player):
        from .FullLogic import checksByHex, checksByName
        panelObj = checksByHex[panel]   
    
        for option in panelObj["requirement"]:
            if len(option) == 0:
                return True
      
            solvability = [self.has(item, player) or (item == "7 Lasers" and self._witness_has_lasers(player, 7)) or (item == "11 Lasers" and self._witness_has_lasers(player, 11)) for item in option]
        
            if all(solvability):
                return True

        return False
      
    #nested can_reach can cause problems, but only if the region being checked is neither of the two original regions from the first can_reach.
    #a nested can_reach is okay here because the only panels this function is called on are panels that exist on either side of all connections they are required for.
    #the spoiler log looks so much nicer this way, it gets rid of a bunch of event items, only leaving a couple. :)
    def _safe_manual_panel_check(self, panel, player):
        from .FullLogic import checksByHex
        return self._can_solve_panel(panel, player) and self.can_reach(checksByHex[panel]["region"]["name"],"Region", player)

    def _has_event_items(self, panelHexToSolveSet, player):
        from .FullLogic import checksByHex, checksByName, originalEventPanels
        from .Locations import event_location_table
        
        for option in panelHexToSolveSet:    
            if len(option) == 0:
                return True
        
            for panel in option:
                if checksByHex[panel]["checkName"] + " Event" in event_location_table and not self.has(checksByHex[panel]["checkName"] + " Event", player):
                    break
                if panel not in originalEventPanels and not self.can_reach(checksByHex[panel]["checkName"], "Location", player):
                    break
                if panel in originalEventPanels and checksByHex[panel]["checkName"] + " Event" not in event_location_table and not self._safe_manual_panel_check(panel, player): 
                    break
                return True
        return False

def makeLambda(checkHex, player):
    return lambda state: state._can_solve_panel(checkHex, player)

def set_rules(world: MultiWorld, player: int):
    from .FullLogic import checksByName, checksByHex
    from .Locations import location_table, event_location_table
    
    for location in location_table:
        real_location = location
    
        if location in event_location_table:
            real_location = location[:-6]

        panel = checksByName[real_location]
        checkHex = panel["checkHex"]

        rule = makeLambda(checkHex, player)

        set_rule(world.get_location(location, player), rule)

    if world.logic[player] != 'nologic':
        world.completion_condition[player] = lambda state: state.has('Victory', player)
        
    