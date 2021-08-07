from enum import IntEnum

class HeartRate(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    GET_ALL = 1
    HEART_RATE = 2
    HEART_RATE_STATS = 3
    SPEED_AND_DISTANCE = 4
    STEP_RATE_STATS = 5
    CALORIES = 6
    VO2 = 7
    USER_INFO = 8
    WORKOUT_INFO = 9
    HR_READING_RELIABILITY = 10
    OPTICAL_SENSOR_STATUS = 11
    POST_STATUS = 12
    CALIBRATION_INFO = 13
    FIRMWARE_VERSION = 14
    HARDWARE_INFO = 15

class Gender(IntEnum):
    FEMALE = 0
    MALE = 1

class HeartRateActivityMode(IntEnum):
    NOT_SET = 0
    RUNNING = 1
    LOW_RATE = 2
    CYCLING = 3
    WEIGHTS_AND_SPORTS = 4
    AEROBICS = 5

class HeartRateMonitorStatus(IntEnum):
    UNKNOWN = 0
    OFF = 1
    INITIALIZING = 2
    ACQUIRING = 3
    SENSOR_NO_CONTACT = 4
    ACQUIRED = 5
    ERROR = 6

class HeartRateZone(IntEnum):
    NOT_SET = 0
    MODERATE = 1
    FITNESS = 2
    AEROBIC = 3
    ANAEROBIC = 4
    MAXIMUM_EFFORT = 5
