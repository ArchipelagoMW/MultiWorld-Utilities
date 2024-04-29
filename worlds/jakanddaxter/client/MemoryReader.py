import typing
import subprocess
import pymem
from pymem import pattern
from pymem.exception import ProcessNotFound
from worlds.jakanddaxter.locs import CellLocations as Cells, ScoutLocations as Flies

# Some helpful constants.
next_cell_index_offset = 0    # Each of these is an uint64, so 8 bytes.
next_buzzer_index_offset = 8  # Each of these is an uint64, so 8 bytes.
cells_offset = 16
buzzers_offset = 420          # cells_offset + (sizeof uint32 * 101 cells) = 16 + (4 * 101)
end_marker_offset = 868       # buzzers_offset + (sizeof uint32 * 112 flies) = 420 + (4 * 112)


class JakAndDaxterMemoryReader:
    marker: typing.ByteString
    connected: bool = False
    marked: bool = False

    process = None
    marker_address = None
    goal_address = None

    location_outbox = []
    outbox_index = 0

    def __init__(self, marker: typing.ByteString = b'UnLiStEdStRaTs_JaK1\x00'):
        self.marker = marker
        self.connected = self.connect()
        if self.connected and self.marker:
            self.marked = self.find_marker()

    async def main_tick(self, location_callback: typing.Callable):
        self.read_memory()

        # Checked Locations in game. Handle 1 location per tick.
        if len(self.location_outbox) > self.outbox_index:
            await location_callback(self.location_outbox[self.outbox_index])
            self.outbox_index += 1

    def connect(self) -> bool:
        try:
            self.process = pymem.Pymem("gk.exe")  # The GOAL Kernel
            return True
        except ProcessNotFound:
            return False

    def find_marker(self) -> bool:

        # If we don't find the marker in the first module's worth of memory, we've failed.
        modules = list(self.process.list_modules())
        self.marker_address = pattern.pattern_scan_module(self.process.process_handle, modules[0], self.marker)
        if self.marker_address:
            # At this address is another address that contains the struct we're looking for: the game's state.
            # From here we need to add the length in bytes for the marker and 4 bytes of padding,
            # and the struct address is 8 bytes long (it's u64).
            goal_pointer = self.marker_address + len(self.marker) + 4
            self.goal_address = int.from_bytes(self.process.read_bytes(goal_pointer, 8),
                                               byteorder="little",
                                               signed=False)
            return True
        return False

    def read_memory(self) -> typing.List[int]:
        next_cell_index = int.from_bytes(self.process.read_bytes(self.goal_address, 8))
        next_buzzer_index = int.from_bytes(self.process.read_bytes(self.goal_address + next_buzzer_index_offset, 8))
        next_cell = int.from_bytes(self.process.read_bytes(self.goal_address + cells_offset + (next_cell_index * 4), 4))
        next_buzzer = int.from_bytes(self.process.read_bytes(self.goal_address + cells_offset + (next_buzzer_index * 4), 4))

        if next_cell not in self.location_outbox:
            self.location_outbox.append(Cells.to_ap_id(next_cell))
        if next_buzzer not in self.location_outbox:
            self.location_outbox.append(Flies.to_ap_id(next_buzzer))

        return self.location_outbox


