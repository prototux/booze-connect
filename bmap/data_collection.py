from enum import IntEnum

class DataCollection(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Start
    GET_ALL = 1

    # Start
    RECORDS = 2

    # Get, Set, Set_Get
    PAUSE = 3

    # Start
    CLEAR = 4

    # Get
    UID  = 5

    # Get, Set, Get_Set
    ENABLE = 6
