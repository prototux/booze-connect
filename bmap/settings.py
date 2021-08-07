from enum import IntEnum

from . import packet

class Settings(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    GET_ALL = 1
    PRODUCT_NAME = 2
    VOICE_PROMPTS = 3
    STANDBY_TIMER = 4
    CNC = 5 # custom noise cancelling (apparently not used/internal only)
            # only on bose 700, auto-adjust noise cancellation level
    ANR = 6 # active/audio noise reduction ("noise cancellation")
    BASS_CONTROL = 7
    ALERTS = 8
    BUTTONS = 9
    MULTIPOINT = 10
    SIDETONE = 11 # "self voice"
    IMU_VOLUME_CONTROL = 21

class VoicePromptLanguage(IntEnum):
    UK_ENGLISH = 0 # English (U.K.)
    US_ENGLISH = 1 # English (U.S.)
    FRENCH = 2 # Français
    ITALIAN = 3 # Italiano
    GERMAN = 4 # Deutsch
    EUROPEAN_SPANISH = 5 # Español (E.U.)
    MEXICAN_SPANISH = 6 # Español (M.X.)
    BRAZILIAN_PORTUGUESE = 7 # Português
    MANDARIN_CHINESE = 8 # 普通话 (Mandarin)
    KOREAN = 9 # 한국어 (Korean)
    RUSSIAN = 10 # Русский (Russian)
    POLISH = 11 # Polski
    HEBREW = 12 # עִברִית (Hebrew)
    TURKISH = 13 # Türk
    DUTCH = 14 # Nederlands
    JAPANESE = 15 # 日本語 (Japanese)
    CANTONESE = 16 # 廣東話 (Cantonese)
    ARABIC = 17 # العربية (Arabic)
    SWEDISH = 18 # Svensk
    DANISH = 19 # Dansk
    NORWEGIAN = 20 # Norsk
    FINNISH = 21 # Suomen kieli (Finnish)

class SidetoneMode(IntEnum):
    OFF = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class ANRSettings:
    class ANRMode(IntEnum):
        OFF = 0
        HIGH = 1
        WIND = 2
        LOW = 3

    def __init__(self, read, write):
        self.read = read
        self.write = write

    def get(self):
        pkt = packet.BmapPacket(packet.FunctionBlock.SETTINGS, Settings.ANR, packet.Operator.GET)
        self.write(pkt.to_bytes())

        header = self.read(4)
        return self.parse(self.read(header[3]))

    def set(self, mode):
        mode_id = self.ANRMode[mode]
        pkt = packet.BmapPacket(packet.FunctionBlock.SETTINGS, Settings.ANR, packet.Operator.SET_GET, data=bytes({mode_id}))
        self.write(pkt.to_bytes())

    def parse(self, data):
        i = 0
        supportedModes = []
        supportedByte = int(bin(data[1])[:1:-1], 2)
        for bit in bin(supportedByte)[2:]:
            if bit == '1':
                supportedModes.append(self.ANRMode(i))
            i += 1
        return {'anr_mode': self.ANRMode(data[0]), 'supported_modes': supportedModes}
