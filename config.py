VERSION = '0.1a'

DISPLAY_MODE = (1920, 1080)
USER_DISPLAY_MODES = [
    (800, 450),
    (960, 540),
    (1120, 630),
    (1280, 720),
    (1440, 810),
    (1600, 900),
    (1920, 1080)
]
USER_SOUND_MODES = [
    'Disabled',
    'Only effects enabled',
    'Only music enabled',
    'Enabled'
]
TARGET_FPS = 60

GAME_HEIGHT_TILES = 10
GAME_WIDTH_TILES = 11
TILE_HEIGHT = 108
TILE_WIDTH = 108

PLAYER_HORIZ_SPEED = 0.04
PLAYER_MAX_SPEED = 0.25
PLAYER_MIN_SPEED = 0.02
PLAYER_ACCEL_FACTOR = 0.0012
PLAYER_ACCEL_EASE = 0.003
PLAYER_DECEL_FACTOR = 0.0001
PLAYER_BRAKE_FACTOR = 0.001
PLAYER_MOVE_FACTOR = 15.0
PLAYER_WIN_SPEED = 0.025

HUD_MAX_SPEED = 250

NPC_HORIZ_SPEED = 0.02
NPC_DECISION_TILES = 6

POLICE_SPEED_DIFF_ALERT_FACTOR = 0.3
POLICE_SPEED_DIFF_ALERT_ADDIT = 0.01
POLICE_DELTA_ACCEL_FACTOR = 0.003

EPS = 1e-6
