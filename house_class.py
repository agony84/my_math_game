from settings import *
from image_paths import *
import pygame


class House:
    def __init__(self, screen):
        self.screen = screen
        self.backgroundFile = BACK_DEF
        self.backgroundImage = pygame.image.load(self.backgroundFile).convert_alpha()
        self.houseFile = HOUSE_DEF
        self.houseImage = pygame.image.load(self.houseFile).convert_alpha()
        self.windowFile = WINDOW_DEF
        self.windowImage = pygame.image.load(self.windowFile).convert_alpha()
        self.doorFile = DOOR_DEF
        self.doorImage = pygame.image.load(self.doorFile).convert_alpha()
        self.hedge = False
        self.hedgeFile = HEDGE_REG
        self.hedgeImage = pygame.image.load(self.hedgeFile).convert_alpha()
        self.path = False
        self.pathFile = PATH_CONCRETE
        self.pathImage = pygame.image.load(self.pathFile).convert_alpha()
        self.garage = False
        self.garageDoorFile = GARAGE_DOOR_DEFAULT_WHITE
        self.garageDoorImage = pygame.image.load(self.garageDoorFile).convert_alpha()
        self.grass = False
        self.grassFile = GRASS_REG
        self.grassImage = pygame.image.load(self.grassFile).convert_alpha()
        self.flora = False
        self.floraFile = DAISIES
        self.floraImage = pygame.image.load(self.floraFile).convert_alpha()
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.pos = (0, 0)

    def draw(self, image, index, x_pos, y_pos, back_color=K_ORANGE, button=None):
        self.update()
        self.screen.blit(self.backgroundImage, self.pos)
        self.screen.blit(self.houseImage, self.pos)
        self.screen.blit(self.windowImage, self.pos)
        self.screen.blit(self.doorImage, self.pos)
        if self.grass:
            self.screen.blit(self.grassImage, self.pos)
        if self.garage:
            self.screen.blit(self.garageDoorImage)
        if self.hedge:
            self.screen.blit(self.hedgeImage, self.pos)
        if self.flora:
            self.screen.blit(self.flora, self.pos)
        if self.path:
            self.screen.blit(self.pathImage, self.pos)
        if button:
            button.draw()
        image.draw(self.screen, index, x_pos, y_pos, back_color)
        pygame.display.update()

    def update(self):
        self.backgroundImage = pygame.image.load(self.backgroundFile).convert_alpha()
        self.houseImage = pygame.image.load(self.houseFile).convert_alpha()
        self.windowImage = pygame.image.load(self.windowFile).convert_alpha()
        self.doorImage = pygame.image.load(self.doorFile).convert_alpha()
        self.hedgeImage = pygame.image.load(self.hedgeFile).convert_alpha()
        self.pathImage = pygame.image.load(self.pathFile).convert_alpha()
        self.garageDoorImage = pygame.image.load(self.garageDoorFile).convert_alpha()
        self.grassImage = pygame.image.load(self.grassFile).convert_alpha()
        self.floraImage = pygame.image.load(self.floraFile).convert_alpha()
