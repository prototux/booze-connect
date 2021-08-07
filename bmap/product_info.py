from enum import IntEnum

class ProductInfo(IntEnum):
    UNKNOWN = 0
    FUNCTION_BLOCK_INFO = 0
    BMAP_VERSION = 1
    ALL_FUNCTION_BLOCKS = 2
    PRODUCT_ID_VARIANT = 3
    GET_ALL_FUNCTIONS = 4
    FIRMWARE_VERSION = 5
    MAC_ADDRESS = 6
    SERIAL_NUMBER = 7
    HARDWARE_REVISION = 10
    COMPONENT_DEVICES = 11

class ProductType(IntEnum):
    UNKNOWN = -1
    HEADPHONES = 0
    SPEAKER = 1

class BoseProductId(IntEnum):
    ISAAC = 0 # Bose AE2 SoundLink
    WOLFCASTLE = 1 # Bose QuietComfort 35
    ICE = 2 # Bose SoundSport
    FOREMAN = 5 # Bose SoundLink Color II
    POWDER = 4 # Bose QuietControl 30
    FLURRY = 3 # Bose SoundSport Pulse
    HARVEY = 7 # Bose Revolve+ Soundlink
    FOLGERS = 6 # Bose Revolve Soundlink
    KLEOS = 8 # Bose SoundWear
    LEVI = 10 # Bose SoundSport Free
    LEVI_SLAVE = 11 # Bose SoundSport Free
    MINNOW = 12 # Bose SoundLink Micro
    BAYWOLF = 9 # Bose QuietComfort 35 Series 2
    ATLAS = 13 # Bose ProFlight
    BB2 = 14 # BOSEbuild:2  UNLISTED; DEV ONLY
    CHIBI = 21 # Bose S1 Pro
    CELINE = 22 # Bose Frames
    CELINE_II = 32 # Bose Frames
    PHELPS = 54 # Phelps
    GOODYEAR = 15 # Bose Noise Cancelling Headphones 700
    LANDO = 28 # Bose QuietComfort Earbuds
    REVEL = 25 # Bose Sport Earbuds
    OLIVIA = 44 # Bose Frames Tempo
    VEDDER = 45 # Bose Frames
    GWEN = 33 # Bose Sport Open Earbuds
    STETSON = -1 # Bose Hearphones
    BEANIE = -1 # Bose Hearphones II
    BUDLITE = -1 # Bose Budlite
    LEVI_CASE = -1 # Levi Case
    MOONRAKER = -1 # SoundLink  UNLISTED; DEV ONLY
    CHAMP = -1 # SoundLink Color  UNLISTED; DEV ONLY
    KCUP = -1 # SoundLink Mini II  UNLISTED; DEV ONLY
    BB1 = -1 # BOSEbuild:1  UNLISTED; DEV ONLY
    UNKNOWN = -1 # Unknown Device

# Product varations
    UNKNOWN(BoseProductId.UNKNOWN, 0),
    MOONRAKER_BLACK(BoseProductId.MOONRAKER, 1),
    MOONRAKER_WHITE(BoseProductId.MOONRAKER, 2),
    ISAAC_BLACK(BoseProductId.ISAAC, 1),
    ISAAC_WHITE(BoseProductId.ISAAC, 2),
    WOLFCASTLE_BLACK(BoseProductId.WOLFCASTLE, 1),
    WOLFCASTLE_SILVER(BoseProductId.WOLFCASTLE, 2),
    WOLFCASTLE_ORNAMENT(BoseProductId.WOLFCASTLE, 3),
    WOLFCASTLE_GRETA(BoseProductId.WOLFCASTLE, 4),
    ICE_BLACK(BoseProductId.ICE, 1),
    ICE_BLUE(BoseProductId.ICE, 2),
    ICE_YELLOW(BoseProductId.ICE, 3),
    POWDER_BLACK(BoseProductId.POWDER, 1),
    POWDER_WHITE(BoseProductId.POWDER, 2),
    POWDER_STARK_BLACK(BoseProductId.POWDER, 3),
    POWDER_STARK_WHITE(BoseProductId.POWDER, 4),
    FLURRY_RED(BoseProductId.FLURRY, 1),
    FOREMAN_BLACK(BoseProductId.FOREMAN, 1),
    FOREMAN_WHITE(BoseProductId.FOREMAN, 2),
    FOREMAN_RED(BoseProductId.FOREMAN, 3),
    FOREMAN_BLUE(BoseProductId.FOREMAN, 4),
    FOREMAN_MIDNIGHT_BLUE(BoseProductId.FOREMAN, 5),
    FOREMAN_YELLOW_CITRON(BoseProductId.FOREMAN, 6),
    HARVEY_BLACK(BoseProductId.HARVEY, 1),
    HARVEY_WHITE(BoseProductId.HARVEY, 2),
    LANCOME_PLUS_BLACK(BoseProductId.HARVEY, 3),
    LANCOME_PLUS_SILVER(BoseProductId.HARVEY, 4),
    FOLGERS_BLACK(BoseProductId.FOLGERS, 1),
    FOLGERS_WHITE(BoseProductId.FOLGERS, 2),
    LANCOME_BLACK(BoseProductId.FOLGERS, 3),
    LANCOME_SILVER(BoseProductId.FOLGERS, 4),
    KLEOS_BLACK(BoseProductId.KLEOS, 1),
    STETSON_BLACK(BoseProductId.STETSON, 1),
    LEVI_BLACK(BoseProductId.LEVI, 1),
    LEVI_CITRON(BoseProductId.LEVI, 2),
    LEVI_ORANGE(BoseProductId.LEVI, 3),
    LEVI_PURPLE(BoseProductId.LEVI, 4),
    MINNOW_BLACK(BoseProductId.MINNOW, 1),
    MINNOW_BLUE(BoseProductId.MINNOW, 2),
    MINNOW_ORANGE(BoseProductId.MINNOW, 3),
    BAYWOLF_BLACK(BoseProductId.BAYWOLF, 1),
    BAYWOLF_SILVER(BoseProductId.BAYWOLF, 2),
    BAYWOLF_NAVY(BoseProductId.BAYWOLF, 3),
    BAYWOLF_PEACOCK(BoseProductId.BAYWOLF, 4),
    BAYWOLF_NYMERIA(BoseProductId.BAYWOLF, 5),
    TIBBERS_BLACK(BoseProductId.BAYWOLF, 6),
    ATLAS_BLACK(BoseProductId.ATLAS, 1),
    CHIBI_BLACK(BoseProductId.CHIBI, 1),
    CELINE_ALTO(BoseProductId.CELINE, 1),
    CELINE_RONDO(BoseProductId.CELINE, 2),
    GOODYEAR_BLACK(BoseProductId.GOODYEAR, 1),
    GOODYEAR_SILVER(BoseProductId.GOODYEAR, 2),
    GOODYEAR_SHENG(BoseProductId.GOODYEAR, 3),
    GOODYEAR_FUJI(BoseProductId.GOODYEAR, 4),
    GOODYEAR_FORTERA(BoseProductId.GOODYEAR, 6),
    LANDO_BLACK(BoseProductId.LANDO, 1),
    LANDO_NUE_LUX(BoseProductId.LANDO, 2),
    REVEL_BLACK(BoseProductId.REVEL, 1),
    REVEL_BALTIC_BLUE(BoseProductId.REVEL, 2),
    REVEL_GLACIER_WHITE(BoseProductId.REVEL, 3),
    OLIVIA_TEMPO(BoseProductId.OLIVIA, 1),
    VEDDER_SOPRANO(BoseProductId.VEDDER, 1),
    VEDDER_TENOR(BoseProductId.VEDDER, 2),
    PHELPS_NUE_ROSE_BLACK(BoseProductId.PHELPS, 1),
    PHELPS_SMOKE_WHITE(BoseProductId.PHELPS, 2),
    PHELPS_STONE_BLUE(BoseProductId.PHELPS, 3),
    GWEN_BLACK(BoseProductId.GWEN, 1);
