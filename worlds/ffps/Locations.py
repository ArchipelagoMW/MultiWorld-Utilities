from BaseClasses import Location
import typing
from .Items import item_table


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    setId: str


class FFPSAdvancement(Location):
    game: str = "FFPS"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


advancement_table = {
    "Salvage ScrapTrap": AdvData(57500, 'Salvage', "m3"),
    "Salvage Scrap Baby": AdvData(57501, 'Salvage', "m4"),
    "Salvage Lefty": AdvData(57502, 'Salvage', "m5"),
    "Salvage Molten Freddy": AdvData(57503, 'Salvage', "m2"),
    "Unlocked Catalogue 2": AdvData(None, 'Pizzeria', ""),
    "Unlocked Catalogue 3": AdvData(None, 'Pizzeria', ""),
    "Unlocked Catalogue 4": AdvData(None, 'Pizzeria', ""),
}

for name, data in item_table.items():
    if data.setId != "":
        if data.code > 55503 and data.setId != "stage" and data.setId != "cups" and data.setId != "speakers":
            advancement_table.update({"Buy "+name: AdvData(len(advancement_table)+57500, 'Pizzeria', data.setId), })
for i in range(5):
    advancement_table.update({"Buy Stage Upgrade "+str(i+1): AdvData(len(advancement_table)+57500, 'Pizzeria', 'stage'), })
for i in range(4):
    advancement_table.update({"Buy Cups Upgrade "+str(i+1): AdvData(len(advancement_table)+57500, 'Pizzeria', 'cups'), })
for i in range(2):
    advancement_table.update({"Buy Speaker Upgrade "+str(i+1): AdvData(len(advancement_table)+57500, 'Pizzeria', 'speakers'), })

exclusion_table = {
}

events_table = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: item_name for item_name, data in advancement_table.items() if data.id}