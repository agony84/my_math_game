"""
NOTE: The abc song used in this program is copyright of freeabcsongs.com
"""
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

###################### INTRO SOUND FILES ########################
COUNT_INTRO = pygame.mixer.Sound('sound_files/intro.wav')
NUMS_OR_LETTERS = pygame.mixer.Sound('sound_files/numbers_or_letters.wav')

######################## OTHER SOUND FILES #######################
FOR_LETTERS = pygame.mixer.Sound('sound_files/for_letters.wav')
FOR_NUMS = pygame.mixer.Sound('sound_files/for_numbers.wav')
CLICK = pygame.mixer.Sound('sound_files/click_the.wav')
BUTTON_SOUND = pygame.mixer.Sound('sound_files/button.wav')
YOU_CHOSE = pygame.mixer.Sound('sound_files/you_chose.wav')

###################### DIGITS SOUNDS ############################
BEGIN_DIGITS = pygame.mixer.Sound('sound_files/begin_digits.wav')
NUMS_FROM_DIGITS = pygame.mixer.Sound('sound_files/numbers_from_digits.wav')
TEN_DIGITS = pygame.mixer.Sound('sound_files/only_10_digits.wav')
SAY_TOGETHER = pygame.mixer.Sound('sound_files/say_together.wav')
FIND_DIGIT = pygame.mixer.Sound('sound_files/find_the_digit.wav')
FOUND_DIGIT = pygame.mixer.Sound('sound_files/found_digit.wav')
VERY_GOOD = pygame.mixer.Sound('sound_files/very_good.wav')
NOT_RIGHT = pygame.mixer.Sound('sound_files/not_right.wav')
TRY_AGAIN = pygame.mixer.Sound('sound_files/try_again.wav')
LOOKS_LIKE = pygame.mixer.Sound('sound_files/looks_like.wav')
THE_NUMBER = pygame.mixer.Sound('sound_files/the_number.wav')

############### COLOR SOUND FILES #########################
BLUE_SOUND = pygame.mixer.Sound('sound_files/colors/blue.wav')
GREEN_SOUND = pygame.mixer.Sound('sound_files/colors/green.wav')
PURPLE_SOUND = pygame.mixer.Sound('sound_files/colors/purple.wav')
RED_SOUND = pygame.mixer.Sound('sound_files/colors/red.wav')
YELLOW_SOUND = pygame.mixer.Sound('sound_files/colors/yellow.wav')
ORANGE_SOUND = pygame.mixer.Sound('sound_files/colors/orange.wav')

numbers_list = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN, TWELVE, THIRTEEN, FOURTEEN,
                FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN, TWENTY)

############# ALPHABET SOUND FILES ##################
ALPHABET_SONG = pygame.mixer.Sound('sound_files/alphabet/alphabet_song.wav')
BEGIN_SING = pygame.mixer.Sound('sound_files/alphabet/begin_sing.wav')
FIND_LETTER = pygame.mixer.Sound('sound_files/alphabet/find_letter.wav')
LEARN_ALPHABET = pygame.mixer.Sound('sound_files/alphabet/learn_alphabet.wav')
SING_ALPHABET = pygame.mixer.Sound('sound_files/alphabet/sing_alphabet.wav')

######################## ALPHABET SOUND FILES ########################
A_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/a.wav')
B_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/b.wav')
C_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/c.wav')
D_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/d.wav')
E_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/e.wav')
F_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/f.wav')
G_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/g.wav')
H_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/h.wav')
I_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/i.wav')
J_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/j.wav')
K_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/k.wav')
L_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/l.wav')
M_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/m.wav')
N_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/n.wav')
O_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/o.wav')
P_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/p.wav')
Q_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/q.wav')
R_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/r.wav')
S_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/s.wav')
T_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/t.wav')
U_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/u.wav')
V_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/v.wav')
W_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/w.wav')
X_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/x.wav')
Y_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/y.wav')
Z_SOUND = pygame.mixer.Sound('sound_files/alphabet/letters/z.wav')

letter_list = (A_SOUND, B_SOUND, C_SOUND, D_SOUND, E_SOUND, F_SOUND, G_SOUND, H_SOUND, I_SOUND, J_SOUND, K_SOUND,
               L_SOUND, M_SOUND, N_SOUND, O_SOUND, P_SOUND, Q_SOUND, R_SOUND, S_SOUND, T_SOUND, U_SOUND, V_SOUND,
               W_SOUND, X_SOUND, Y_SOUND, Z_SOUND)