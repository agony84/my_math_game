"""
Author: John Kear
Version: 1.0
Date: 2/23/2020

Description:
Main app code.
"""

import pygame
import sys
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
        # set screen
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # set game state
        self.state = START
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
        self.learn_digits_stage = 0

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
                        self.clock.tick(10)
                    TEN_DIGITS.play()
                    while pygame.mixer.get_busy():
                        self.clock.tick(10)
                    self.play_digits()
                    self.learn_digits_stage += 1
                if self.index > 9:
                    self.index = 0

    def learn_digits_update(self):
        if self.play:
            BEGIN_DIGITS.play()
            while pygame.mixer.get_busy():
                self.clock.tick(10)
            self.play = False

    def learn_digits_draw(self, is_img=False, index=None):
        self.screen.fill(K_PURPLE)
        self.screen.blit(self.surface_1, (SCREEN_WIDTH / 2 - NUM_DISPLAY_WIDTH / 2,
                                          SCREEN_HEIGHT / 2 - NUM_DISPLAY_HEIGHT / 2))
        draw_text("Let's learn digits", self.screen, [
            SCREEN_WIDTH // 2, 40], START_TEXT_SIZE + 10, K_YELLOW, ALL_FONT, centered=True)
        draw_text("Press SPACE to continue.", self.screen, [
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], START_TEXT_SIZE - 10, K_YELLOW, ALL_FONT, centered=True)
        pygame.display.flip()

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
            #ignore any events while playing sound
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

    def play_digits(self):
        """
        play all digits (0 - 9) sound files
        :return: None
        """
        index = 0
        while index <= 9:
            self.reg_num_imgs.draw(self.screen, index, NUM_DISPLAY_WIDTH / 2, NUM_DISPLAY_HEIGHT / 2)
            numbers_list[index].play()
            while pygame.mixer.get_busy():
                pygame.event.clear()
            index += 1

    def play_one_ten(self):
        """
        play numbers 1 - 10 sound files
        :return: None
        """
        index = 1
        while index <= 10:
            numbers_list[index].play()
            while pygame.mixer.get_busy():
                self.clock.tick(10)
            index += 1