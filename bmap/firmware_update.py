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
