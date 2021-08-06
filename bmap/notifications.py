from enum import IntEnum

class Notification(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    RESET = 1
    BY_FBLOCK = 2
    BY_FUNCTION = 3
    PERIODIC = 4
