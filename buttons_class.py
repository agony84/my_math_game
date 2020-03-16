"""
Author: John Kear
Version: 1.0
Date: 2/23/2020

Description:
Template class for all buttons.
"""
import pygame
from settings import *

vec = pygame.math.Vector2

pygame.init()


class Button:
    def __init__(self, screen, width, height, x, y, color, text='', border=True, image=None, number=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.pos = vec(x, y)
        self.border = border
        self.surface = pygame.Surface((width, height))
        self.image = image
        self.number = number
        self.screen = screen

    def update(self):
        pass

    def draw(self):
        if self.border:
            pygame.draw.rect(self.surface, self.border, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(ALL_FONT, 14)
            text = font.render(self.text, 1, BLACK)
            self.surface.fill(self.color)
            self.surface.blit(text, (self.width / 2 - (text.get_width() / 2), self.height / 2 - (text.get_height() / 2)))
            self.screen.blit(self.surface, (self.x, self.y))

        if self.number is not None:
            self.image.draw(self.screen, self.number, NUM_DISPLAY_WIDTH / 2, NUM_DISPLAY_HEIGHT / 2)
