import pygame
from settings import *
import glob
from pygame.locals import *


class NumberSprites:
    def __init__(self, filename, frames, width, height):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet_width = self.sheet.get_width()
        self.img_height = self.sheet_height = self.sheet.get_height()
        self.img_width = self.sheet_width / frames
        self.num_frames = frames
        self.center_width, self.center_height = self.cellCenter = (self.img_width / 2, self.img_height / 2)
        self.images = self.splitImages()
        self.width = width
        self.height = height
        self.surface1 = pygame.Surface((NUM_DISPLAY_WIDTH, NUM_DISPLAY_HEIGHT))

    def draw(self, screen, index, x, y):
        if index > self.num_frames - 1:
            pass
        else:
            # self.surface_1.fill(K_PURPLE)
            # self.reg_num_imgs.draw(self.surface_1, index, NUM_DISPLAY_WIDTH / 2, NUM_DISPLAY_HEIGHT / 2)
            self.surface1.fill(K_PURPLE)
            self.surface1.blit(self.sheet, (NUM_DISPLAY_WIDTH / 2 - self.center_width,
                                            NUM_DISPLAY_HEIGHT / 2 - self.center_height), self.images[index])
            surface2 = pygame.transform.smoothscale(self.surface1, (self.width, self.height))
            screen.blit(surface2, (x - self.width / 2, y - self.height / 2))
            # surface.blit(self.sheet, (x - self.center_width, y - self.center_height), self.images[index])
            pygame.display.update()

    # In this function we are generating a list of the image positions.
    def splitImages(self):
        """
        The embedded for loop in the list function call returns the rectangular coordinates
        of each cell in a list.
        """
        return list([(index % self.num_frames * self.img_width,
                      index // self.num_frames * self.img_height, self.img_width, self.img_height)
                     for index in range(self.num_frames)])
