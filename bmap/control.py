from enum import IntEnum

class Control(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Start
    GET_ALL = 1

    # Get, Start
    CHIRP = 2
