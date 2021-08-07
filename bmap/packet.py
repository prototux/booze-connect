from enum import IntEnum

class FunctionBlock(IntEnum):
    UNKNOWN = 0
    PRODUCT_INFO = 0
    SETTINGS = 1
    STATUS = 2
    FIRMWARE_UPDATE = 3
    DEVICE_MANAGEMENT = 4
    AUDIO_MANAGEMENT = 5
    CALL_MANAGEMENT = 6
    CONTROL = 7
    DEBUG = 8
    NOTIFICATION = 9
    RESERVED_BOSEBUILD_1 = 10
    RESERVED_BOSEBUILD_2 = 11
    HEARING_ASSISTANCE = 12
    DATA_COLLECTION = 13
    HEART_RATE = 14
    VPA = 16 # voice personal assistant
    AUGMENTED_REALITY = 21


class Operator(IntEnum):
    UNKNOWN = 0
    SET = 0
    GET = 1
    SET_GET = 2
    STATUS = 3
    ERROR = 4
    START = 5
    RESULT = 6
    PROCESSING = 7

class DisconnectReasonCode(IntEnum):
    UNKNOWN = 0
    USER_TRIGGERED_POWER_OFF = 1
    AUTO_OFF = 2
    BATTERY = 3
    RESTART = 4
    SAFETY = 5
    OVER_THE_AIR_UPDATE = 6
    CHARGING = 7
    OUT_OF_RANGE = 16
    INSUFFICIENT_CONNECTION_SLOTS = 32
    APP_TRIGGERED_DISCONNECT = 33

class SupportedBluetoothProfiles(IntEnum):
    A2DP = 1
    DEFAULT = 1
    HEARTRATE = 4
    MAX_PROFILES = 3
    SPP = 0

class BmapPacket:
    def __init__(self, functionBlock, function, operator, data=b'', device_id=0, port=0):
        self.functionBlock = functionBlock
        self.function = function
        self.operator = operator
        self.data = data
        self.device_id = device_id
        self.port = port

    def to_bytes(self):
        return bytes([
            self.functionBlock,
            self.function,
            (self.device_id<<6) | (self.port<<4) | (self.operator),
            len(self.data)
        ]) + self.data

