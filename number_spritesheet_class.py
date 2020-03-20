import pygame
from settings import *
from images_paths import *
import glob


class NumberSprites:
    def __init__(self, image, frames, surf_width, surf_height):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.sheet_width = self.sheet.get_width()
        self.img_height = self.sheet_height = self.sheet.get_height()
        self.img_width = self.sheet_width / frames
        self.num_frames = frames
        self.center_width, self.center_height = self.cellCenter = (self.img_width / 2, self.img_height / 2)
        self.images = self.splitImages()
        self.surf_width = surf_width
        self.surf_height = surf_height
        self.surface1 = pygame.Surface((self.img_width, self.img_height), pygame.SRCALPHA)

    def draw(self, screen, index, x_screen, y_screen, back_color):
        """

        :param screen:
        :param index:
        :param x_screen: top left x pos for image display
        :param y_screen: top left y pos for image display
        :param back_color:
        :return:
        """
        if index > self.num_frames - 1:
            pass
        else:
            # self.surface_1.fill(K_PURPLE)
            # self.reg_num_imgs.draw(self.surface_1, index, NUM_DISPLAY_WIDTH / 2, NUM_DISPLAY_HEIGHT / 2)
            self.surface1.fill(back_color)
            self.surface1.blit(self.sheet, (0, 0), self.images[index])
            surface2 = pygame.transform.smoothscale(self.surface1, (self.surf_width, self.surf_height))
            # surface3 = pygame.transform.scale(self.surface1)
            screen.blit(surface2, (x_screen, y_screen))
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
