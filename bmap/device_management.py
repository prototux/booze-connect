from enum import IntEnum

class DeviceManagement(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Start
    CONNECT = 1

    # Start
    DISCONNECT = 2

    # Start
    REMOVE_DEVICE = 3

    # Get
    LIST_DEVICES = 4

    # Get
    INFO = 5

    ## Unused?!?
    EXTENDED_INFO = 6

    # Start
    CLEAR_DEVICE_LIST = 7

    # Get, Start
    PAIRING_MODE = 8

    ## Unused
    LOCAL_MAC_ADDRESS = 9

    ## Unused
    PREPARE_P2P = 10

    # Get, Get_Set
    P2P_MODE = 11

    # Get, Start
    ROUTING = 12

class SomethingEnum(IntEnum):
    UNKNOWN = -1
    UNSUPPORTED_CONNECTION_TYPE_MASTER = 0
    UNSUPPORTED_CONNECTION_TYPE_PUPPET = 1
    INCOMPATIBLE_PUPPET_NEEDS_UPDATE = 2
    INCOMPATIBLE_MASTER_NEEDS_UPDATE = 3

class ConnectionStatusEnum(IntEnum):
    DOWN = 0
    UP = 1
