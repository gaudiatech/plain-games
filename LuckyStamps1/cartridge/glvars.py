from . import pimodules


screen = ev_manager = None
forced_serial = None

GAME_PRICE = 5

# netw
GAME_CONFIG_SOURCE = "https://hiddenpath.kata.games/game_configs/lucky-stamps.json"
FORCED_GAME_HOST = "https://games.gaudia-tech.com/lucky-stamps/testluck.php"  # handy for debug

# ------------------
# taille (px) attendue pour les <stamps> img = 149x175
# ------------------
STAMPW, STAMPH = 149, 175
TEST_GAME_ID = 16
DEFAULT_USER_ID = 8

# used to debug netw.chall_* functions, but its not really needed now
DUMMY_SCORE = 9998

MyGameStates = pimodules.pyved_engine.e_struct.enum(
    'IntroState',
    'CasinoState'
)
