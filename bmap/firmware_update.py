from enum import IntEnum

class FirmwareUpdate(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Get
    STATE = 1

    # Start
    INIT = 2

    # Start
    DATA_TRANSFER = 3

    # Get
    SYNCHRONIZE = 4

    # Start
    VALIDATE = 5

    # Start
    RUN = 6

    # Start
    RESET = 7

class FirmwareUpdateState(IntEnum):
    ERROR = 0
    IDLE = 1
    READY_FOR_DATA_TRANSFER = 2
    READY_FOR_VALIDATE = 3
    READY_FOR_RUN_UPDATE = 4
    UPDATE_COMPLETE = 5

class LocationUpdateType(IntEnum):
    MASTER_ONLY = 0
    PUPPET_ONLY = 1
    BOTH = 2
