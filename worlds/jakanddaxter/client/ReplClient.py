import time
import struct
from socket import socket, AF_INET, SOCK_STREAM
from CommonClient import logger
from worlds.jakanddaxter.locs import CellLocations as Cells, ScoutLocations as Flies, OrbLocations as Orbs
from worlds.jakanddaxter.GameID import jak1_id


class JakAndDaxterReplClient:
    ip: str
    port: int
    socket: socket
    connected: bool = False
    listening: bool = False
    compiled: bool = False

    item_inbox = {}
    inbox_index = 0

    def __init__(self, ip: str = "127.0.0.1", port: int = 8181):
        self.ip = ip
        self.port = port

    async def init(self):
        self.connected = self.connect()
        if self.connected:
            self.listening = self.listen()
        if self.connected and self.listening:
            self.compiled = self.compile()

    async def main_tick(self):

        # Receive Items from AP. Handle 1 item per tick.
        if len(self.item_inbox) > self.inbox_index:
            self.receive_item()
            self.inbox_index += 1

    # This helper function formats and sends `form` as a command to the REPL.
    # ALL commands to the REPL should be sent using this function.
    # TODO - this needs to block on receiving an acknowledgement from the REPL server.
    #  Problem is, it doesn't ack anything right now. So we need that to happen first.
    def send_form(self, form: str) -> None:
        header = struct.pack("<II", len(form), 10)
        self.socket.sendall(header + form.encode())
        logger.info("Sent Form: " + form)

    def connect(self) -> bool:
        if not self.ip or not self.port:
            return False

        try:
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            time.sleep(1)
            logger.info(self.socket.recv(1024).decode())
            return True
        except ConnectionRefusedError as e:
            logger.error(e.strerror)
            return False

    def listen(self) -> bool:
        self.send_form("(lt)")
        return True

    def compile(self) -> bool:
        # Show this visual cue when compilation is started.
        # It's the version number of the OpenGOAL Compiler.
        self.send_form("(set! *debug-segment* #t)")

        # Play this audio cue when compilation is started.
        # It's the sound you hear when you press START + CIRCLE to open the Options menu.
        self.send_form("(dotimes (i 1) "
                       "(sound-play-by-name "
                       "(static-sound-name \"start-options\") "
                       "(new-sound-id) 1024 0 0 (sound-group sfx) #t))")

        # Start compilation. This is blocking, so nothing will happen until the REPL is done.
        self.send_form("(mi)")

        # Play this audio cue when compilation is complete.
        # It's the sound you hear when you press START + START to close the Options menu.
        self.send_form("(dotimes (i 1) "
                       "(sound-play-by-name "
                       "(static-sound-name \"menu-close\") "
                       "(new-sound-id) 1024 0 0 (sound-group sfx) #t))")

        # Disable cheat-mode and debug (close the visual cue).
        self.send_form("(set! *cheat-mode* #f)")
        # self.send_form("(set! *debug-segment* #f)")
        return True

    def verify(self) -> bool:
        self.send_form("(dotimes (i 1) "
                       "(sound-play-by-name "
                       "(static-sound-name \"menu-close\") "
                       "(new-sound-id) 1024 0 0 (sound-group sfx) #t))")
        return True

    def receive_item(self):
        ap_id = getattr(self.item_inbox[self.inbox_index], "item")

        # Determine the type of item to receive.
        if ap_id in range(jak1_id, jak1_id + Flies.fly_offset):
            self.receive_power_cell(ap_id)

        elif ap_id in range(jak1_id + Flies.fly_offset, jak1_id + Orbs.orb_offset):
            self.receive_scout_fly(ap_id)

        elif ap_id > jak1_id + Orbs.orb_offset:
            pass  # TODO

    def receive_power_cell(self, ap_id: int) -> None:
        cell_id = Cells.to_game_id(ap_id)
        self.send_form("(send-event "
                       "*target* \'get-archipelago "
                       "(pickup-type fuel-cell) "
                       "(the float " + str(cell_id) + "))")

    def receive_scout_fly(self, ap_id: int) -> None:
        fly_id = Flies.to_game_id(ap_id)
        self.send_form("(send-event "
                       "*target* \'get-archipelago "
                       "(pickup-type buzzer) "
                       "(the float " + str(fly_id) + "))")
