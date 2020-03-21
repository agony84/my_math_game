"""
Author: John Kear
Version: 1.0
Date: 2/23/2020

Description:
Main app code.
"""

import pygame
import sys
import random
from settings import *
from number_spritesheet_class import *
from sound_files import *
from buttons_class import *
from image_paths import *

pygame.init()


############## STATIC FUNCTIONS #####################
def draw_text(words, screen, pos, size, color, font_name, centered=False):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, color)
    text_size = text.get_size()
    if centered:
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
    screen.blit(text, pos)


class App:

    def __init__(self):
        # set game screen
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # set game state
        self.state = START
        # set running
        self.running = True
        # set clock
        self.clock = pygame.time.Clock()
        # images
        self.reg_num_imgs = NumberSprites(REG_NUM_IMGS, NUM_COLS, NUM_DISPLAY_WIDTH, NUM_DISPLAY_HEIGHT)
        self.higl_num_imgs = NumberSprites(HIGH_NUM_IMGS, NUM_COLS, NUM_DISPLAY_WIDTH, NUM_DISPLAY_HEIGHT)
        self.reg_upper_abc = NumberSprites(ABC_UPPER, ABC_COLS, ABC_WIDTH, ABC_HEIGHT)
        self.highl_upper_abc = NumberSprites(ABC_UPPER_HIGH, ABC_COLS, ABC_WIDTH, ABC_HEIGHT)
        self.reg_lower_abc = NumberSprites(ABC_LOWER, ABC_COLS, ABC_WIDTH, ABC_HEIGHT)
        self.highl_lower_abc = NumberSprites(ABC_LOWER_HIGH, ABC_COLS, ABC_WIDTH, ABC_HEIGHT)
        self.skip_img = NumberSprites(SKIP_ARROWS, 1, SKIP_WIDTH, SKIP_HEIGHT)
        self.sound_index = 0
        self.num_display = pygame.Surface((60, 60))
        # resources for learn_digits
        self.index = 0
        self.play = True
        self.load_state = True
        self.score = 0
        self.display_score = False
        self.incorrect_find = 0
        self.display_skip = True
        self.display_continue = False
        # buttons
        self.number_button = Button(self.screen, NUM_BUTTON_WIDTH, NUM_BUTTON_HEIGHT,
                                    SCREEN_CENTER[0] - (NUM_BUTTON_WIDTH / 2), SCREEN_CENTER[1] - NUM_BUTTON_HEIGHT,
                                    K_ORANGE, "123's", MEDIUM_TEXT_SIZE)
        self.letter_button = Button(self.screen, ABC_BUTTON_WIDTH, ABC_BUTTON_HEIGHT,
                                    SCREEN_CENTER[0] - (ABC_BUTTON_WIDTH / 2), SCREEN_CENTER[1] + ABC_BUTTON_HEIGHT,
                                    K_GREEN, "ABC's", MEDIUM_TEXT_SIZE)
        self.return_main = Button(self.screen, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, MAIN_X, MAIN_Y, MAIN_BUTTON_COLOR,
                                  'Main', SMALL_TEXT_SIZE)
        self.menu = Button(self.screen, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, MAIN_X, MAIN_Y, MAIN_BUTTON_COLOR,
                           'Menu', SMALL_TEXT_SIZE)
        self.continue_button = Button(self.screen, CONTINUE_WIDTH, CONTINUE_HEIGHT, CONTINUE_X, CONTINUE_Y,
                                      CONTINUE_COLOR, CONTINUE_TEXT, MEDIUM_TEXT_SIZE, K_YELLOW)

        # load game
        self.load()

    def run(self):
        while self.running:
            if self.state == START:
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == NUMS_LANDING:
                pass
            elif self.state == LEARN_DIGITS:
                self.learn_digits_events()
                self.learn_digits_update()
                self.learn_digits_draw()
                if self.load_state:
                    self.learn_digits_load()
            elif self.state == ALPHABET_LANDING:
                pass
            elif self.state == LEARN_ALPHABET:
                self.learn_alphabet_events()
                self.learn_alphabet_update()
                self.learn_alphabet_draw()
                if self.load_state:
                    self.learn_alphabet_load()
            elif self.state == ZERO_TO_TEN:
                self.zero_ten_events()
                self.zero_ten_update()
                self.zero_ten_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    ############## START FUNCTIONS #############
    def start_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.number_button.x <= mouse_pos[
                    0] <= self.number_button.x + self.number_button.width and self.number_button.y <= mouse_pos[
                    1] <= self.number_button.y + self.number_button.height:
                    self.state = LEARN_DIGITS
                    self.load_state = True
                if self.letter_button.x <= mouse_pos[
                    0] <= self.letter_button.x + self.letter_button.width and self.letter_button.y <= mouse_pos[
                    1] <= self.letter_button.y + self.letter_button.height:
                    self.state = LEARN_ALPHABET
                    self.load_state = True

    def start_update(self):
        pass

    def start_draw(self):
        """
        Start screen consists of two option buttons, numbers and letters
        :return: none
        """
        # set background
        self.screen.fill(K_BLUE)
        # display start message
        draw_text('Welcome', self.screen, [
            SCREEN_CENTER[0], 100], WELCOME_SIZE, K_PURPLE, ALL_FONT, centered=True)
        self.number_button.draw()
        self.letter_button.draw()
        pygame.display.update()

    ############################### LEARN DIGITS FUNCTION ################################
    def learn_digits_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.display_continue = False
                self.learn_digits_stage2()
            if event.type == pygame.MOUSEBUTTONUP and MAIN_X + MAIN_BUTTON_WIDTH >= mouse_pos[
                0] >= MAIN_X and MAIN_Y + MAIN_BUTTON_HEIGHT >= mouse_pos[1] >= MAIN_Y:
                self.state = START
                self.display_continue = False
                self.display_score = False

    def learn_digits_update(self):
        pass

    def learn_digits_draw(self):
        """
        display digits screen
        :return: none
        """
        self.screen.fill(K_PURPLE)
        if self.display_score:
            draw_text("Score = " + str(self.score), self.screen, [75, 75], 20, BLACK, ALL_FONT)
        draw_text("Let's learn digits", self.screen, [
            SCREEN_WIDTH // 2, 40], START_TEXT_SIZE + 10, K_YELLOW, ALL_FONT, centered=True)
        # draw_text("Press SPACE to continue.", self.screen, [
        #     SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_YELLOW, ALL_FONT, centered=True)
        if self.display_continue:
            self.continue_button.draw()
        self.return_main.draw()
        pygame.display.update()

    def learn_digits_load(self):
        """
        play digit intro sound clips.
        :return:
        """
        self.load_state = False
        self.play_clip(BEGIN_DIGITS)
        self.play_clip(NUMS_FROM_DIGITS)
        self.play_clip(TEN_DIGITS)
        self.play_digits()
        self.play_clip(SAY_TOGETHER)
        self.play_digits(TWO_DELAY)
        self.score = 0
        self.display_score = True
        self.display_continue = True

    def learn_digits_stage2(self):
        """
        Display numbers to be found by user.
        When user correctly clicks on target number, increment game score.
        When user chooses incorrect number more than once, display the target number and ask to find again.
        After the correct number has been found ten times, go to next number game state
        :return: none
        """
        while self.score < 10:
            self.learn_digits_draw()
            found = False
            find_digit = random.randint(0, 9)
            rand1 = random.randint(0, 9)
            rand2 = random.randint(0, 9)

            # adjust random numbers so they aren't the same as target digit
            while rand1 == find_digit:
                rand1 = random.randint(0, 9)

            while rand2 == find_digit:
                rand2 = random.randint(0, 9)

            # create number display positions
            num1_pos = ((SCREEN_CENTER[0] / 2) - (NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2))
            num2_pos = (SCREEN_CENTER[0] - (NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2))
            num3_pos = (((SCREEN_CENTER[0] / 2) + SCREEN_CENTER[0]) - (NUM_DISPLAY_WIDTH / 2),
                        SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2))
            """
            put numbers in list to display in numerical order.
            find index of target digit to use when checking for correct user selection
            """
            find_list = [find_digit, rand1, rand2]
            find_list.sort()
            find_idx = 0
            num1_idx = 0
            num2_idx = 0
            i = 0
            while i < len(find_list):
                if find_list[i] == find_digit:
                    find_idx = i
                    i += 1
                elif find_list[i] == rand1:
                    num1_idx = i
                    i += 1
                elif find_list[i] == rand2:
                    num2_idx = i
                    i += 1
            """
            put positions in list so target digit index can be used for correct user selection checking
            """
            num_pos_list = (num1_pos, num2_pos, num3_pos)

            """ Play find digit and target digit sounds and display digits"""
            self.play_clip(FIND_DIGIT)
            # FIND_DIGIT.play()
            # while pygame.mixer.get_busy():
            #     pygame.event.clear()
            self.play_number(find_digit)
            self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
            self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
            self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE)
            self.display_skip = False

            while not found:
                mouse_pos = pygame.mouse.get_pos()
                for selection in pygame.event.get():
                    if ((num1_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (
                            num1_pos[0])) and ((num1_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num1_pos[1])):
                        self.higl_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)

                    if ((num2_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (num2_pos[0])) and (
                            num2_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num2_pos[1]):
                        self.higl_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)

                    if (num3_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (num3_pos[0]) and (
                            num3_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num3_pos[1]):
                        self.higl_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE)

                    if selection.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # Check for return to main button click
                    if selection.type == pygame.MOUSEBUTTONUP and MAIN_X + MAIN_BUTTON_WIDTH >= mouse_pos[
                        0] >= MAIN_X and MAIN_Y + MAIN_BUTTON_HEIGHT >= mouse_pos[1] >= MAIN_Y:
                        self.state = START
                        self.display_score = False
                        self.display_continue = False
                        self.run()
                    if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                        if (num_pos_list[find_idx][0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (
                                num_pos_list[find_idx][0]) and (num_pos_list[find_idx][1] + NUM_DISPLAY_HEIGHT) \
                                >= mouse_pos[1] >= (num_pos_list[find_idx][1]):
                            self.play_clip(VERY_GOOD)
                            self.play_clip(FOUND_DIGIT)
                            self.play_number(find_digit)
                            found = True
                            self.incorrect_find = 0
                            self.score += 1
                            if self.score >= 10:
                                self.state = ZERO_TO_TEN
                                self.load_state = True

                        elif (num_pos_list[num1_idx][0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (
                                num_pos_list[num1_idx][0]) and (num_pos_list[num1_idx][1] + NUM_DISPLAY_HEIGHT) \
                                >= mouse_pos[1] >= (num_pos_list[num1_idx][1]):
                            self.incorrect_find += 1
                            if self.incorrect_find <= 1:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_number(rand1)
                                self.play_clip(TRY_AGAIN)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                            elif self.incorrect_find >= 2:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_number(rand1)
                                self.play_clip(THE_NUMBER)
                                self.play_number(find_digit)
                                self.play_clip(LOOKS_LIKE)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_digit, SCREEN_CENTER[0] - (
                                        NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE)

                        elif (num_pos_list[num2_idx][0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (
                                num_pos_list[num2_idx][0]) and (num_pos_list[num2_idx][1] + NUM_DISPLAY_HEIGHT) \
                                >= mouse_pos[1] >= (num_pos_list[num2_idx][1]):
                            self.incorrect_find += 1
                            if self.incorrect_find <= 1:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_number(rand2)
                                self.play_clip(TRY_AGAIN)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                            elif self.incorrect_find >= 2:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_number(rand2)
                                self.play_clip(THE_NUMBER)
                                self.play_number(find_digit)
                                self.play_clip(LOOKS_LIKE)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_digit, SCREEN_CENTER[0] - (
                                        NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE)

    ######################### END LEARN DIGITS ################################

    ############ ZERO TO TEN FUNCTIONS #########
    def zero_ten_events(self):
        pass

    def zero_ten_update(self):
        pass

    def zero_ten_draw(self):
        pass

    def zero_ten_load(self):
        pass

    ################################# END ZERO TO TEN ###########################

    ################################## LEARN ALPHABET FUNCTIONS ###########################
    def learn_alphabet_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.display_continue = False
                self.learn_alphabet_draw()
                self.play_alphabet_song()
            if event.type == pygame.MOUSEBUTTONUP and MAIN_X + MAIN_BUTTON_WIDTH >= mouse_pos[
                0] >= MAIN_X and MAIN_Y + MAIN_BUTTON_HEIGHT >= mouse_pos[1] >= MAIN_Y:
                self.state = START
                self.display_continue = False
                self.display_score = False

    def learn_alphabet_update(self):
        pass

    def learn_alphabet_draw(self):
        """
        display alphabet screen
        :return: none
        """
        self.screen.fill(K_PURPLE)
        if self.display_score:
            draw_text("Score = " + str(self.score), self.screen, [75, 75], 20, BLACK, ALL_FONT)
        draw_text("Let's learn the alphabet!", self.screen, [
            SCREEN_WIDTH // 2, 40], START_TEXT_SIZE, K_YELLOW, ALL_FONT, centered=True)
        # draw_text("Press SPACE to continue.", self.screen, [
        #     SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_YELLOW, ALL_FONT, centered=True)
        if self.display_continue:
            self.continue_button.draw()
        self.return_main.draw()
        pygame.display.update()

    def learn_alphabet_load(self):
        """
        upon load, play intro alphabet sound clips
        :return: none
        """
        self.play_clip(LEARN_ALPHABET)
        self.play_clip(SING_ALPHABET)
        self.load_state = False
        self.display_continue = True

    def play_alphabet_song(self):
        """
        play the alphabet song sound clip and display corresponding letters at appropriate time
        :return: none
        """
        index = 0
        userevent = 1
        count = 0
        ALPHABET_SONG.set_volume(0.2)
        ALPHABET_SONG.play()
        pygame.time.set_timer(pygame.USEREVENT, ABC_DELAYS[index])
        self.skip_img.draw(self.screen, 0, SKIP_X, SKIP_Y, SKIP_COLOR)
        while pygame.mixer.get_busy():
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (SKIP_X + SKIP_WIDTH >= mouse_pos[0] >= SKIP_X) and (
                            SKIP_Y + SKIP_HEIGHT >= mouse_pos[1] >= SKIP_Y):
                        ALPHABET_SONG.stop()
                if event.type == pygame.USEREVENT:
                    self.reg_upper_abc.draw(self.screen, index, SCREEN_CENTER[0] - (ABC_BUTTON_WIDTH / 2),
                                            SCREEN_CENTER[1] - (ABC_BUTTON_HEIGHT / 2), K_PURPLE)
                    if index <= len(ABC_DELAYS) - 2:
                        index += 1
                        pygame.time.set_timer(pygame.USEREVENT, ABC_DELAYS[index])
                else:
                    pygame.event.clear()

        self.display_continue = True

    ######################## END LEARN ALPHABET ######################

    ############# HELPER FUNCTIONS ##############
    def load(self):
        """
        Load the start screen
        :return: none
        """
        # set background
        self.screen.fill(K_BLUE)
        # display start message
        draw_text('Welcome', self.screen, [
            SCREEN_CENTER[0], 100], WELCOME_SIZE, K_PURPLE, ALL_FONT, centered=True)
        self.number_button.draw()
        self.letter_button.draw()
        pygame.display.update()
        self.play_clip(NUMS_OR_LETTERS)
        self.play_clip(FOR_NUMS)
        self.play_clip(CLICK)
        self.play_clip(ORANGE_SOUND)
        self.play_clip(BUTTON_SOUND)
        self.play_clip(FOR_LETTERS)
        self.play_clip(CLICK)
        self.play_clip(GREEN_SOUND)
        self.play_clip(BUTTON_SOUND)

    def play_all_num(self):
        """
        play all number sound files
        :return: None
        """
        for num in numbers_list:
            num.play()
            while pygame.mixer.get_busy():
                self.clock.tick(10)

    def play_digits(self, delay=10):
        """
        play all digits (0 - 9) sound files
        :return: None
        """
        index = 0
        while index <= 9:
            self.reg_num_imgs.draw(self.screen, index, SCREEN_CENTER[0] - (NUM_DISPLAY_WIDTH / 2),
                                   SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE)
            numbers_list[index].play()
            while pygame.mixer.get_busy():
                pygame.time.delay(delay)
                mouse_pos = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if (SKIP_X + SKIP_WIDTH >= mouse_pos[0] >= SKIP_X) and (
                                SKIP_Y + SKIP_HEIGHT >= mouse_pos[1] >= SKIP_Y):
                            index = 10
                            self.display_skip = False
                    else:
                        pygame.event.clear()
            index += 1

    def play_one_ten(self, delay=10):
        """
        play numbers 1 - 10 sound files
        :return: None
        """
        index = 1
        while index <= 10:
            self.reg_num_imgs.draw(self.screen, index, SCREEN_CENTER[0], SCREEN_CENTER[1])
            numbers_list[index].play()
            while pygame.mixer.get_busy():
                pygame.time.delay(delay)
                pygame.event.clear()
            index += 1

    def play_number(self, number, delay=10):
        """
        plays number sound file based on paramater
        :param delay:
        :param number: used to select number sound file
        :return: None
        """
        numbers_list[number].play()
        while pygame.mixer.get_busy():
            self.clock.tick(delay)
            pygame.event.clear()

    def play_clip(self, clip, delay=0):
        """
        play specified sound clip
        :param clip: Sound file to be played
        :param delay: Clock delay to allow sound clip to play
        :return: none
        """
        clip.play()
        while pygame.mixer.get_busy():
            self.skip_img.draw(self.screen, 0, SKIP_X, SKIP_Y, SKIP_COLOR)
            mouse_pos = pygame.mouse.get_pos()
            self.clock.tick(delay)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (SKIP_X + SKIP_WIDTH >= mouse_pos[0] >= SKIP_X) and (
                            SKIP_Y + SKIP_HEIGHT >= mouse_pos[1] >= SKIP_Y):
                        clip.stop()
                else:
                    pygame.event.clear()
