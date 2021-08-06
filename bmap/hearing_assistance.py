from enum import IntEnum

class HearingAssistance(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    WDRC_BRIEF_UPDATE = 1
    WDRC_INDIVIDUAL_UPDATES = 2
    DIRECTIONALITY = 3
    DIRECTIONALITY_SETTINGS = 4
    NR_CONTROL = 5
    NR_SETTINGS = 6
    MAPPED_SETTINGS_STANDARD_MODE = 7
    WDRC_BAND_DEFS = 8
    EQ_BAND_DEFS = 9
    SUB_PROCESSOR_VERSION = 10
    MUTING = 11
    BOOST_EQ = 12
    LIMITS = 13
    SUB_PROCESSOR_STATUS = 14
    MAPPED_SETTINGS_MODE = 15
    MAPPED_SETTING_OFFSET_CONTROL_MODE = 16
    GLOBAL_MUTE = 17
    ALGORITHM_CONTROL = 18
    LIVE_METRICS = 19
    DOFF_AUTO_OFF_TIME = 20