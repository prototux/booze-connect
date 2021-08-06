from enum import IntEnum

class VoicePersonalAssistant(IntEnum):
    UNKNOWN = 0

    # Get
    FUNCTION_BLOCK_INFO = 0

    # Start
    GET_ALL = 1

    # Get, Set_Get
    SUPPORTED_VPAS = 2

class VoicePersonalAssistantTypes(IntEnum):
    GOOGLE_ASSISTANT = 0
    ALEXA = 1

class VoicePersonalAssistantTrigger(IntEnum):
    VPA_NOT_TRIGGERED = 0
    BUTTON_PRESS = 1
    WAKE_UP_WORD = 2
    VPA_NOTIFICATION = 3

class WakeUpWord(IntEnum):
    OK_GOOGLE = 0
    ALEXA = 1
