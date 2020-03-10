import pygame

import glob
from pygame.locals import *


class NumberSprites:
    def __init__(self, filename, frames):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet_width = self.sheet.get_width()
        self.img_height = self.sheet_height = self.sheet.get_height()
        self.img_width = self.sheet_width / frames
        self.num_frames = frames
        self.center_width, self.center_height = self.cellCenter = (self.img_width / 2, self.img_height / 2)
        self.images = self.splitImages()

    def draw(self, surface, index, x, y):
        if index > self.num_frames - 1:
            pass
        else:
            surface.blit(self.sheet, (x - self.center_width, y - self.center_height), self.images[index])

    # In this function we are generating a list of the image positions.
    def splitImages(self):
        """
        The embedded for loop in the list function call returns the rectangular coordinates
        of each cell in a list.
        """
        return list([(index % self.num_frames * self.img_width,
                      index // self.num_frames * self.img_height, self.img_width, self.img_height)
                     for index in range(self.num_frames)])
