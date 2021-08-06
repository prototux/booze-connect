from enum import IntEnum
from . import packet

class Status(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    GET_ALL_FUNCTIONS = 1
    BATTERY_LEVEL = 2
    AUX_CABLE_DETECTION = 3
    MIC_LEVEL = 4
    CHARGER_DETECT = 5

class BatteryStatus:
    def __init__(self):
        self.pkt = packet.BmapPacket(packet.FunctionBlock.STATUS, Status.BATTERY_LEVEL, packet.Operator.GET)

    def to_bytes(self):
        return self.pkt.to_bytes()

    def parse(self, data):
        return {'battery_level': data[0]} 
