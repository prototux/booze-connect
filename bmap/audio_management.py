from enum import IntEnum

class AudioManagement(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Get
    SOURCE = 1

    # Start
    GET_ALL = 2

    # Get, Start
    CONTROL = 3

    # Get
    STATUS = 4

    # Get, Set_Get
    VOLUME = 5

    # Start
    NOW_PLAYING = 6
