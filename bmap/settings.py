from enum import IntEnum

from . import packet

class Settings(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    GET_ALL = 1
    PRODUCT_NAME = 2
    VOICE_PROMPTS = 3
    STANDBY_TIMER = 4
    CNC = 5 # custom noise cancelling (apparently not used/internal only)
            # only on bose 700, auto-adjust noise cancellation level
    ANR = 6 # active/audio noise reduction ("noise cancellation")
    BASS_CONTROL = 7
    ALERTS = 8
    BUTTONS = 9
    MULTIPOINT = 10
    SIDETONE = 11 # "self voice"
    IMU_VOLUME_CONTROL = 21

class ANRSettings:
    class ANRMode(IntEnum):
        OFF = 0
        HIGH = 1
        WIND = 2
        LOW = 3

    def __init__(self, read, write):
        self.read = read
        self.write = write

    def get(self):
        pkt = packet.BmapPacket(packet.FunctionBlock.SETTINGS, Settings.ANR, packet.Operator.GET)
        self.write(pkt.to_bytes())

        header = self.read(4)
        return self.parse(self.read(header[3]))

    def set(self, mode):
        mode_id = self.ANRMode[mode]
        pkt = packet.BmapPacket(packet.FunctionBlock.SETTINGS, Settings.ANR, packet.Operator.SET_GET, data=bytes({mode_id}))
        self.write(pkt.to_bytes())

    def parse(self, data):
        i = 0
        supportedModes = []
        supportedByte = int(bin(data[1])[:1:-1], 2)
        for bit in bin(supportedByte)[2:]:
            if bit == '1':
                supportedModes.append(self.ANRMode(i))
            i += 1
        return {'anr_mode': self.ANRMode(data[0]), 'supported_modes': supportedModes}
