import pygame
from settings import *

pygame.mixer.init()

###################### NUMBER SOUND FILES ########################
ZERO = pygame.mixer.Sound('sound_files/numbers/zero.wav')
ONE = pygame.mixer.Sound('sound_files/numbers/one.wav')
TWO = pygame.mixer.Sound('sound_files/numbers/two.wav')
THREE = pygame.mixer.Sound('sound_files/numbers/three.wav')
FOUR = pygame.mixer.Sound('sound_files/numbers/four.wav')
FIVE = pygame.mixer.Sound('sound_files/numbers/five.wav')
SIX = pygame.mixer.Sound('sound_files/numbers/six.wav')
SEVEN = pygame.mixer.Sound('sound_files/numbers/seven.wav')
EIGHT = pygame.mixer.Sound('sound_files/numbers/eight.wav')
NINE = pygame.mixer.Sound('sound_files/numbers/nine.wav')
TEN = pygame.mixer.Sound('sound_files/numbers/ten.wav')
ELEVEN = pygame.mixer.Sound('sound_files/numbers/eleven.wav')
TWELVE = pygame.mixer.Sound('sound_files/numbers/twelve.wav')
THIRTEEN = pygame.mixer.Sound('sound_files/numbers/thirteen.wav')
FOURTEEN = pygame.mixer.Sound('sound_files/numbers/fourteen.wav')
FIFTEEN = pygame.mixer.Sound('sound_files/numbers/fifteen.wav')
SIXTEEN = pygame.mixer.Sound('sound_files/numbers/sixteen.wav')
SEVENTEEN = pygame.mixer.Sound('sound_files/numbers/seventeen.wav')
EIGHTEEN = pygame.mixer.Sound('sound_files/numbers/eighteen.wav')
NINETEEN = pygame.mixer.Sound('sound_files/numbers/nineteen.wav')
TWENTY = pygame.mixer.Sound('sound_files/numbers/twenty.wav')

###################### OTHER SOUND FILES ########################
INTRO = pygame.mixer.Sound('sound_files/intro.wav')

###################### DIGITS SOUNDS ############################
BEGIN_DIGITS = pygame.mixer.Sound('sound_files/begin_digits.wav')
NUMS_FROM_DIGITS = pygame.mixer.Sound('sound_files/numbers_from_digits.wav')
TEN_DIGITS = pygame.mixer.Sound('sound_files/only_10_digits.wav')
SAY_TOGETHER = pygame.mixer.Sound('sound_files/say_together.wav')

numbers_list = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN, TWELVE, THIRTEEN, FOURTEEN,
                FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN, TWENTY)


