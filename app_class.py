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

pygame.init()


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
        self.state = LEARN_DIGITS
        # set running
        self.running = True
        # set clock
        self.clock = pygame.time.Clock()
        self.load()
        self.reg_num_imgs = NumberSprites('images/spritesheet_numbers_plain.png', NUM_COLS)
        self.higl_num_imgs = NumberSprites('images/numbers_highlight.png', NUM_COLS)
        self.sound_index = 0
        self.num_display = pygame.Surface((60, 60))
        # resources for learn_digits
        self.index = 0
        self.play = True
        self.learn_digits_stage = 2
        self.load_state = True
        self.score = 0

    def run(self):
        while self.running:
            if self.state == START:
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == LEARN_DIGITS:
                self.learn_digits_events()
                self.learn_digits_update()
                self.learn_digits_draw()
            elif self.state == ZERO_TO_TEN:
                if self.load_state:
                    self.zero_ten_load()
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                self.state = LEARN_DIGITS
                # self.reg_num_imgs.draw(0, LEFT_CENTER[0], LEFT_CENTER[1])
                # self.higl_num_imgs.draw(self.screen, self.sound_index, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                # if self.sound_index == 0:
                #     ZERO.play()
                # elif self.sound_index == 1:
                #     ONE.play()
                # elif self.sound_index == 2:
                #     TWO.play()
                # self.sound_index += 1

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(K_BLUE)
        draw_text('Welcome', self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50], START_TEXT_SIZE, K_PURPLE, ALL_FONT, centered=True)
        draw_text("Let's learn to count!", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50], START_TEXT_SIZE, K_PURPLE, ALL_FONT, centered=True)
        draw_text("Press SPACE to get started.", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_PURPLE, ALL_FONT, centered=True)
        pygame.display.update()

    ############################### LEARN DIGITS FUNCTION ################################
    def learn_digits_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                if self.learn_digits_stage == 0:
                    NUMS_FROM_DIGITS.play()
                    while pygame.mixer.get_busy():
                        pygame.event.clear()
                    TEN_DIGITS.play()
                    while pygame.mixer.get_busy():
                        pygame.event.clear()
                    self.play_digits()
                    self.learn_digits_stage += 1
                elif self.learn_digits_stage == 1:
                    SAY_TOGETHER.play()
                    while pygame.mixer.get_busy():
                        pygame.event.clear()
                    self.play_digits(TWO_DELAY)
                    self.learn_digits_stage += 1
                elif self.learn_digits_stage == 2:
                    found = False
                    find_digit = random.randint(0, 9)
                    rand1 = random.randint(0, 9)
                    while rand1 == find_digit:
                        rand1 = random.randint(0, 9)
                    rand2 = random.randint(0, 9)
                    while rand2 == find_digit:
                        rand2 = random.randint(0, 9)
                    FIND_DIGIT.play()
                    while pygame.mixer.get_busy():
                        pygame.event.clear()
                    num1_pos = (SCREEN_CENTER[0] / 2, SCREEN_CENTER[1])
                    num2_pos = (SCREEN_CENTER[0], SCREEN_CENTER[1])
                    num3_pos = (((SCREEN_CENTER[0] / 2) + SCREEN_CENTER[0]), SCREEN_CENTER[1])
                    find_list = [find_digit, rand1, rand2]
                    find_list.sort()
                    find_idx = 0
                    num_pos_list = (num1_pos, num2_pos, num3_pos)
                    while find_idx < len(find_list):
                        if find_list[find_idx] == find_digit:
                            break
                        else:
                            find_idx += 1

                    self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1])
                    self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1])
                    self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1])
                    self.play_number(find_digit)
                    while not found:
                        mouse_pos = pygame.mouse.get_pos()
                        for selection in pygame.event.get():
                            if (num1_pos[0] + NUM_DISPLAY_WIDTH / 2) >= mouse_pos[0] >= (
                                    num1_pos[0] - NUM_DISPLAY_WIDTH / 2) and (
                                    num1_pos[1] + NUM_DISPLAY_HEIGHT / 2) >= mouse_pos[1] >= (
                                    num1_pos[1] - NUM_DISPLAY_HEIGHT / 2):
                                self.higl_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1])
                            else:
                                self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1])

                            if (num2_pos[0] + NUM_DISPLAY_WIDTH / 2) >= mouse_pos[0] >= (
                                    num2_pos[0] - NUM_DISPLAY_WIDTH / 2) and (
                                    num2_pos[1] + NUM_DISPLAY_HEIGHT / 2) >= mouse_pos[1] >= (
                                    num2_pos[1] - NUM_DISPLAY_HEIGHT / 2):
                                self.higl_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1])
                            else:
                                self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1])

                            if (num3_pos[0] + NUM_DISPLAY_WIDTH / 2) >= mouse_pos[0] >= (
                                    num3_pos[0] - NUM_DISPLAY_WIDTH / 2) and (
                                    num3_pos[1] + NUM_DISPLAY_HEIGHT / 2) >= mouse_pos[1] >= (
                                    num3_pos[1] - NUM_DISPLAY_HEIGHT / 2):
                                self.higl_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1])
                            else:
                                self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1])

                            if selection.type == pygame.QUIT or (selection.type == pygame.KEYDOWN and selection.key == QUIT):
                                pygame.quit()
                                sys.exit()
                            if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                                if (num_pos_list[find_idx][0] + NUM_DISPLAY_WIDTH / 2) >= mouse_pos[0] >= (
                                        num_pos_list[find_idx][0] - NUM_DISPLAY_WIDTH / 2) and (
                                        num_pos_list[find_idx][1] + NUM_DISPLAY_HEIGHT / 2) >= mouse_pos[1] >= (
                                        num_pos_list[find_idx][1] - NUM_DISPLAY_HEIGHT / 2):
                                    VERY_GOOD.play()
                                    while pygame.mixer.get_busy():
                                        self.clock.tick(1000)
                                        pygame.event.clear()
                                    FOUND_DIGIT.play()
                                    while pygame.mixer.get_busy():
                                        self.clock.tick(1000)
                                        pygame.event.clear()
                                    self.play_number(find_digit)
                                    found = True
                                else:
                                    NOT_RIGHT.play()
                                    while pygame.mixer.get_busy():
                                        self.clock.tick(1000)
                                        pygame.event.clear()
                                    TRY_AGAIN.play()
                                    while pygame.mixer.get_busy():
                                        self.clock.tick(1000)
                                        pygame.event.clear()
                                    FIND_DIGIT.play()
                                    while pygame.mixer.get_busy():
                                        self.clock.tick(1000)
                                        pygame.event.clear()
                                    self.play_number(find_digit)




    def learn_digits_update(self):
        if self.play:
            BEGIN_DIGITS.play()
            while pygame.mixer.get_busy():
                self.clock.tick(10)
            self.play = False

    def learn_digits_draw(self, is_img=False, index=None):
        self.screen.fill(K_PURPLE)
        # self.screen.blit(self.surface_1, (SCREEN_WIDTH / 2 - NUM_DISPLAY_WIDTH / 2,
        #                                   SCREEN_HEIGHT / 2 - NUM_DISPLAY_HEIGHT / 2))
        draw_text("Let's learn digits", self.screen, [
            SCREEN_WIDTH // 2, 40], START_TEXT_SIZE + 10, K_YELLOW, ALL_FONT, centered=True)
        draw_text("Press SPACE to continue.", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_YELLOW, ALL_FONT, centered=True)
        pygame.display.flip()

    ############ ZERO TO TEN FUNCTIONS #########
    def zero_ten_events(self):
        pass

    def zero_ten_update(self):
        pass

    def zero_ten_draw(self):
        pass

    def zero_ten_load(self):
        pass


    ############# HELPER FUNCTIONS ##############
    def load(self):
        # set background
        self.screen.fill(K_BLUE)
        # display start message
        draw_text('Welcome', self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50], START_TEXT_SIZE, K_PURPLE, ALL_FONT, centered=True)
        draw_text("Let's learn to count!", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50], START_TEXT_SIZE, K_PURPLE, ALL_FONT, centered=True)
        draw_text("Press SPACE to get started.", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_PURPLE, ALL_FONT, centered=True)
        pygame.display.update()
        INTRO.play()
        while pygame.mixer.get_busy():
            self.clock.tick(10)
            # ignore any events while playing sound
            pygame.event.clear()

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
            self.reg_num_imgs.draw(self.screen, index, SCREEN_CENTER[0], SCREEN_CENTER[1])
            numbers_list[index].play()
            while pygame.mixer.get_busy():
                pygame.time.delay(delay)
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

    def play_number(self, number):
        """
        plays number sound file based on paramater
        :param number: used to select number sound file
        :return: None
        """
        numbers_list[number].play()
        while pygame.mixer.get_busy():
            pygame.event.clear()