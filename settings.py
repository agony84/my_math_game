"""
Author: John Kear
Version: 1.0
Date: 2/23/2020

Description:
settings for math game.
"""

#################### SCREEN SETTINGS ###################

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
TOP_LEFT = (0, 0)
TOP_RIGHT = (SCREEN_WIDTH, 0)
BOTTOM_LEFT = (0, SCREEN_HEIGHT)
BOTTOM_RIGHT = (SCREEN_WIDTH, SCREEN_HEIGHT)
LEFT_CENTER = (0, SCREEN_HEIGHT // 2)
TOP_CENTER = (SCREEN_WIDTH // 2, 0)
RIGHT_CENTER = (SCREEN_WIDTH, SCREEN_HEIGHT // 2)
BOTTOM_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

BORDER_BUFFER = 50

FPS = 60

##################### IMAGE SETTINGS ####################

NUM_COLS = 10
NUM_DISPLAY_WIDTH = 50
NUM_DISPLAY_HEIGHT = 50

#################### BUTTON SETTINGS ###################

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 20

########## COLOR SETTINGS ########################

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PEACH = (255, 178, 102)
L_BLUE = (33, 137, 156)
GREY = (107, 107, 107)
PLAYER_COLOUR = (255, 255, 0)
GOLD = (207, 181, 59)
PURPLE = (210, 118, 255)
ORANGE = (255, 165, 0)
L_GREEN = (138, 255, 134)
K_GREEN = (53, 212, 97)
K_YELLOW = (249, 225, 4)
K_ORANGE = (249, 157, 7)
K_PURPLE = (136, 47, 246)
K_BLUE = (55, 182, 246)


################### FONT SETTINGS ########################

START_TEXT_SIZE = 30
ALL_FONT = "goudystout"

##################### GAME STATES ########################
START = 'start'
LEARN_DIGITS = 'learn digits'
ZERO_TO_TEN = 'zero to ten'
TEN_TO_TWENTY = 'ten to twenty'

###################### PRINT MESSAGES ##########################
START_MESSAGE = 'Welcom to '

####################### DELAY TIMES ############################
TWO_DELAY = 2000
THREE_DELAY = 3000
FIVE_DELAY = 5000
TEN_DELAY = 10000
