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

class AudioControlSourceType(IntEnum):
    NONE = 0
    BLUETOOTH = 1
    AUXILIARY = 2

class AudioControleValue(IntEnum):
    STOP = 0
    PLAY = 1
    PAUSE = 2
    TRACK_FORWARD = 3
    TRACK_BACK = 4
    FAST_FORWARD_PRESS = 5
    FAST_FORWARD_RELEASE = 6
    REWIND_PRESS = 7
    REWIND_RELEASE = 8

class NowPlaying(IntEnum):
    SONG_TITLE = 0 # UTF-8
    ARTIST = 1 # UTF-8
    ALBUM = 2 # UTF-8
    TRACK_NUMBER = 3 # ASCII
    TOTAL_NUMBER_OF_TRACKS = 4 # ASCII
    GENRE = 5 # UTF-8
    PLAYING_TIME = 6 # ASCII
