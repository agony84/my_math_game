"""
Author: John Kear
Version: 0.0.1
Date: 2/23/2020

Description:
Main app code.
"""

import random
import sys
import shelve
from buttons_class import *
from house_class import *
from number_spritesheet_class import *
from sound_files import *

"""
using shelve and dbm.dumb for game state saves. Shelve is used for the save, dbm.dumb is necessary
for saving game state of distributable version.
"""
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
        self.stage = 0
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
        self.house_button = NumberSprites(HOUSE_BTN, 1, HOUSE_BUT_WIDTH_HEIGHT, HOUSE_BUT_WIDTH_HEIGHT)
        self.back_arrow = NumberSprites(BACK_ARROW, 1, BACK_ARROW_WIDTH_HEIGHT, BACK_ARROW_WIDTH_HEIGHT)
        self.star_img = NumberSprites(STAR, 1, STAR_WIDTH, STAR_HEIGHT)
        self.sound_index = 0
        self.num_display = pygame.Surface((60, 60))
        # resources for learn_digits
        self.stars = 1000
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
        self.save_button = Button(self.screen, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, MAIN_X, MAIN_Y,
                                  MAIN_BUTTON_COLOR, "Save", SMALL_TEXT_SIZE)
        self.load_button = Button(self.screen, MAIN_BUTTON_WIDTH, MAIN_BUTTON_HEIGHT, MAIN_X, MAIN_Y - 100,
                                  MAIN_BUTTON_COLOR, "Load", SMALL_TEXT_SIZE)
        self.upgrades_button = Button(self.screen, UPGRADE_WIDTH, UPGRADE_HEIGHT, UPGRADE_X, UPGRADE_Y, K_ORANGE,
                                      'Upgrades', SMALL_TEXT_SIZE)

        self.player_house = House(self.screen)
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
                if self.load_state:
                    self.learn_digits_load()
                self.learn_digits_events()
                self.learn_digits_update()
                self.learn_digits_draw()
            elif self.state == ALPHABET_LANDING:
                pass
            elif self.state == LEARN_ALPHABET:
                if self.load_state:
                    self.learn_alphabet_load()
                self.learn_alphabet_events()
                self.learn_alphabet_update()
                self.learn_alphabet_draw()
            elif self.state == ZERO_TO_TEN:
                self.zero_ten_events()
                self.zero_ten_update()
                self.zero_ten_draw()
            elif self.state == HOUSE_LANDING:
                if self.load_state:
                    self.house_load()
                self.house_events()
                self.house_update()
                self.house_draw()
            elif self.state == UPGRADES:
                if self.load_state:
                    self.upgrades_load()
                self.upgrades_events()
                self.upgrades_update()
                self.upgrades_draw()
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
                    0] <= self.number_button.x + self.number_button.width and self.number_button.y <= \
                        mouse_pos[1] <= self.number_button.y + self.number_button.height:
                    self.state = LEARN_DIGITS
                    self.load_state = True
                if self.letter_button.x <= mouse_pos[
                    0] <= self.letter_button.x + self.letter_button.width and self.letter_button.y <= mouse_pos[
                    1] <= self.letter_button.y + self.letter_button.height:
                    self.state = LEARN_ALPHABET
                    self.load_state = True
                if self.save_button.x <= mouse_pos[
                    0] <= self.save_button.x + self.save_button.width and self.save_button.y <= mouse_pos[
                    1] <= self.save_button.y + self.save_button.height:
                    selected = False
                    menu_screen = pygame.Surface(SAVE_SIZE)
                    to_save = Button(menu_screen, SAVE_SCREEN_WIDTH, 50, 0, 0, WHITE,
                                     'Are you sure you want to save?')
                    ok_button = Button(menu_screen, OK_WIDTH, OK_HEIGHT, OK_X, OK_Y, L_GREEN, 'OK')
                    cancel_button = Button(menu_screen, CANCEL_WIDTH, CANCEL_HEIGHT, CANCEL_X, CANCEL_Y, RED, 'CANCEL')

                    while not selected:
                        select_pos = pygame.mouse.get_pos()
                        menu_screen.fill(WHITE)
                        to_save.draw()
                        ok_button.draw()
                        cancel_button.draw()
                        to_save.draw()
                        self.screen.blit(menu_screen, (0, 0))
                        pygame.display.update()
                        for choice in pygame.event.get():
                            if choice.type == pygame.MOUSEBUTTONUP and choice.button == 1:
                                if ok_button.x <= select_pos[0] <= ok_button.x + ok_button.width and ok_button.y <= \
                                        select_pos[1] <= ok_button.y + ok_button.height:
                                    saveData = (
                                        self.player_house.backgroundFile,
                                        self.player_house.houseFile,
                                        self.player_house.windowFile,
                                        self.player_house.doorFile,
                                        self.player_house.hedge,
                                        self.player_house.hedgeFile,
                                        self.player_house.path,
                                        self.player_house.pathFile,
                                        self.player_house.garage,
                                        self.player_house.garageDoorFile,
                                        self.player_house.grass,
                                        self.player_house.grassFile,
                                        self.player_house.flora,
                                        self.player_house.floraFile,
                                        self.stars
                                    )
                                    shelfFile = shelve.open(SAVE_FILE, writeback=True)
                                    shelfFile['saved_data'] = saveData
                                    shelfFile.close()
                                    selected = True
                                if cancel_button.x <= select_pos[0] <= cancel_button.x + cancel_button.width and \
                                        cancel_button.y <= select_pos[1] <= cancel_button.y + cancel_button.height:
                                    selected = True
                if self.load_button.x <= mouse_pos[
                    0] <= self.load_button.x + self.load_button.width and self.load_button.y <= mouse_pos[
                    1] <= self.load_button.y + self.load_button.height:
                    selected = False
                    menu_screen = pygame.Surface(SAVE_SIZE)
                    to_save = Button(menu_screen, SAVE_SCREEN_WIDTH, 50, 0, 0, WHITE,
                                     'Are you sure you want to load?')
                    ok_button = Button(menu_screen, OK_WIDTH, OK_HEIGHT, OK_X, OK_Y, L_GREEN, 'OK')
                    cancel_button = Button(menu_screen, CANCEL_WIDTH, CANCEL_HEIGHT, CANCEL_X, CANCEL_Y, RED, 'CANCEL')

                    while not selected:
                        select_pos = pygame.mouse.get_pos()
                        menu_screen.fill(WHITE)
                        to_save.draw()
                        ok_button.draw()
                        cancel_button.draw()
                        to_save.draw()
                        self.screen.blit(menu_screen, (0, 0))
                        pygame.display.update()
                        for choice in pygame.event.get():
                            if choice.type == pygame.MOUSEBUTTONUP and choice.button == 1:
                                if ok_button.x <= select_pos[0] <= ok_button.x + ok_button.width and ok_button.y <= \
                                        select_pos[1] <= ok_button.y + ok_button.height:
                                    shelfFile = shelve.open(SAVE_FILE)
                                    loadInfo = shelfFile['saved_data']
                                    shelfFile.close()
                                    self.player_house.backgroundFile = loadInfo[0]
                                    self.player_house.houseFile = loadInfo[1]
                                    self.player_house.windowFile = loadInfo[2]
                                    self.player_house.doorFile = loadInfo[3]
                                    self.player_house.hedge = loadInfo[4]
                                    self.player_house.hedgeFile = loadInfo[5]
                                    self.player_house.path = loadInfo[6]
                                    self.player_house.pathFile = loadInfo[7]
                                    self.player_house.garage = loadInfo[8]
                                    self.player_house.garageDoorFile = loadInfo[9]
                                    self.player_house.grass = loadInfo[10]
                                    self.player_house.grassFile = loadInfo[11]
                                    self.player_house.flora = loadInfo[12]
                                    self.player_house.floraFile = loadInfo[13]
                                    self.stars = loadInfo[14]
                                    selected = True
                                if cancel_button.x <= select_pos[0] <= cancel_button.x + cancel_button.width and \
                                        cancel_button.y <= select_pos[1] <= cancel_button.y + cancel_button.height:
                                    selected = True
                if HOUSE_BUT_X <= mouse_pos[0] <= HOUSE_BUT_X + HOUSE_BUT_WIDTH_HEIGHT and HOUSE_BUT_Y <= \
                        mouse_pos[1] <= HOUSE_BUT_Y + HOUSE_BUT_WIDTH_HEIGHT:
                    self.state = HOUSE_LANDING

    def start_update(self):
        pass

    def start_load(self):
        self.start_draw()
        self.load_state = False

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
        self.save_button.draw()
        self.load_button.draw()
        self.house_button.draw(self.screen, 0, HOUSE_BUT_X, HOUSE_BUT_Y, K_ORANGE)
        self.star_img.draw(self.screen, 0, STAR_X, STAR_Y + 70, K_BLUE)
        draw_text("= " + str(self.stars), self.screen, [STAR_X + 50, STAR_Y + 80], 20, BLACK, ALL_FONT)
        pygame.display.update()

    ############################### HOUSE LANDING FUNCTIONS ################################

    def house_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if MAIN_X + BACK_ARROW_WIDTH_HEIGHT >= mouse_pos[0] >= MAIN_X and MAIN_Y + BACK_ARROW_WIDTH_HEIGHT >= \
                        mouse_pos[1] >= MAIN_Y:
                    self.state = START
                if UPGRADE_X + UPGRADE_WIDTH >= mouse_pos[0] >= UPGRADE_X and UPGRADE_Y + UPGRADE_HEIGHT >= mouse_pos[
                    1] >= UPGRADE_Y:
                    self.state = UPGRADES
                print(mouse_pos)

    def house_update(self):
        pass

    def house_draw(self):
        # self.player_house.draw(0, MAIN_X, MAIN_Y, K_ORANGE, self.upgrades_button)
        self.player_house.draw(0)
        self.back_arrow.draw(self.screen, 0, MAIN_X, MAIN_Y, pygame.SRCALPHA)
        self.upgrades_button.draw()
        pygame.display.update()

    def house_load(self):
        self.house_draw()

    ########################## UPGRADES FUNCTIONS ############################
    def upgrades_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if MAIN_X + BACK_ARROW_WIDTH_HEIGHT >= mouse_pos[0] >= MAIN_X and MAIN_Y + BACK_ARROW_WIDTH_HEIGHT >= \
                        mouse_pos[1] >= MAIN_Y:
                    self.state = HOUSE_LANDING
                # Column one
                if UP_COL_1 + UP_WIDTH >= mouse_pos[0] > UP_COL_1 and UP_ROW_1 + UP_HEIGHT >= mouse_pos[1] >= UP_ROW_1:
                    self.upgrades_house_selection()
                if UP_COL_1 + UP_WIDTH >= mouse_pos[0] > UP_COL_1 and UP_ROW_2 + UP_HEIGHT >= mouse_pos[1] >= UP_ROW_2:
                    self.upgrades_door_selection()
                if UP_COL_1 + UP_WIDTH >= mouse_pos[0] > UP_COL_1 and UP_ROW_3 + UP_HEIGHT >= mouse_pos[1] >= UP_ROW_3:
                    self.upgrades_grass_selection()
                # Column two
                if UP_COL_2 + UP_WIDTH >= mouse_pos[0] > UP_COL_2 and UP_ROW_1 + UP_HEIGHT >= mouse_pos[1] >= UP_ROW_1:
                    self.upgrades_path_selection()

                print(mouse_pos)

    def upgrades_update(self):
        pass

    def upgrades_draw(self):
        self.screen.fill(K_BLUE)

        self.star_img.draw(self.screen, 0, STAR_X + 30, STAR_Y - 40, pygame.SRCALPHA)
        draw_text("= " + str(self.stars), self.screen, [STAR_X + 75, STAR_Y - 30], MEDIUM_TEXT_SIZE, BLACK, ALL_FONT)
        draw_text("Upgrades", self.screen, [SCREEN_CENTER[0], BORDER_BUFFER], WELCOME_SIZE, K_PURPLE, ALL_FONT, True)
        self.back_arrow.draw(self.screen, 0, MAIN_X, MAIN_Y, K_BLUE)
        house = pygame.image.load(HOUSE_DEF).convert_alpha()
        self.upgrades_display_element(house, UP_WIDTH, UP_HEIGHT, UP_COL_1, UP_ROW_1)
        doorImage = pygame.image.load(DOOR_DEF).convert_alpha()
        self.upgrades_display_element(doorImage, UP_WIDTH, UP_HEIGHT, UP_COL_1, UP_ROW_2)
        grass = pygame.image.load(GRASS_REG).convert_alpha()
        self.upgrades_display_element(grass, UP_WIDTH, UP_HEIGHT, UP_COL_1, UP_ROW_3)
        path = pygame.image.load(PATH_CONCRETE)
        self.upgrades_display_element(path, UP_WIDTH, UP_HEIGHT, UP_COL_2, UP_ROW_1)
        hedge = pygame.image.load(UP_HEDGE)
        self.upgrades_display_element(hedge, UP_WIDTH, UP_HEIGHT, UP_COL_2, UP_ROW_2)
        flora = pygame.image.load(UP_FLORA)
        self.upgrades_display_element(flora, UP_WIDTH, UP_HEIGHT, UP_COL_2, UP_ROW_3)
        garage_door = pygame.image.load(GARAGE_DOOR_DEFAULT_WHITE)
        self.upgrades_display_element(garage_door, UP_WIDTH, UP_HEIGHT, UP_COL_3, UP_ROW_1)
        driveway = pygame.image.load(DRIVEWAY_DEFAULT)
        self.upgrades_display_element(driveway, UP_WIDTH, UP_HEIGHT, UP_COL_3, UP_ROW_2)
        window = pygame.image.load(WINDOW_DEF)
        self.upgrades_display_element(window, UP_WIDTH, UP_HEIGHT, UP_COL_3, UP_ROW_3)
        pygame.display.update()

    def upgrades_load(self):
        pass

    def upgrades_house_menu(self):
        # display all house menu items with corresponding cost
        star = pygame.image.load(STAR).convert_alpha()
        up_surf = pygame.Surface((UP_MENU_WIDTH, UP_MENU_HEIGHT))
        up_surf_border = pygame.Surface((UP_MENU_WIDTH + 10, UP_MENU_HEIGHT + 10))
        up_surf_border.fill(K_PURPLE)
        up_surf.fill(K_GREEN)
        default = pygame.image.load(HOUSE_DEF)
        self.upgrades_display_element(default, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(DEFAULTS_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        pink = pygame.image.load(HOUSE_PINK)
        self.upgrades_display_element(pink, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y2, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_COLORS_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        blue = pygame.image.load(HOUSE_BLUE)
        self.upgrades_display_element(blue, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y3, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_COLORS_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        lblue = pygame.image.load(HOUSE_LBLUE)
        self.upgrades_display_element(lblue, UP_WIDTH, UP_HEIGHT, UP_MENU_X2, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X2 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_COLORS_COST), up_surf,
                  [UP_MENU_X2 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        gar_white = pygame.image.load(HOUSE_GARAGE_WHITE)
        self.upgrades_display_element(gar_white, UP_WIDTH, UP_HEIGHT, UP_MENU_X2, UP_MENU_Y2, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X2 - STAR_BUFFER,
                                      UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_GAR_DEF_COST), up_surf,
                  [UP_MENU_X2 + UP_STAR_W_H + 2, UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        gar_pink = pygame.image.load(HOUSE_GARAGE_PINK)
        self.upgrades_display_element(gar_pink, UP_WIDTH, UP_HEIGHT, UP_MENU_X2, UP_MENU_Y3, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X2 - STAR_BUFFER,
                                      UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_GAR_COLOR_COST), up_surf,
                  [UP_MENU_X2 + UP_STAR_W_H + 2, UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        gar_blue = pygame.image.load(HOUSE_GARAGE_BLUE)
        self.upgrades_display_element(gar_blue, UP_WIDTH, UP_HEIGHT, UP_MENU_X3, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X3 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(HOUSE_GAR_COLOR_COST), up_surf,
                  [UP_MENU_X3 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        # escape = pygame.image.load(EXIT)
        # self.upgrades_display_element(escape, EXIT_WIDTH, EXIT_HEIGHT, UP_MENU_WIDTH - EXIT_WIDTH, 0, up_surf)
        self.screen.blit(up_surf_border, (UP_MENU_X - 5, UP_MENU_Y - 5))
        self.screen.blit(up_surf, (UP_MENU_X, UP_MENU_Y))
        pygame.display.update()

    def upgrades_house_selection(self):
        selected = False
        self.upgrades_house_menu()
        # Get user selection
        while not selected:
            mouse_pos = pygame.mouse.get_pos()
            for selection in pygame.event.get():
                if selection.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                    if UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("house", DEFAULTS_COST, HOUSE_DEF, "White house activated.")
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_2 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_2:
                        self.upgrades_selected("house", HOUSE_COLORS_COST, HOUSE_PINK, "Pink house activated.")
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_3 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_3:
                        self.upgrades_selected("house", HOUSE_COLORS_COST, HOUSE_BLUE, "Blue house activated.")
                        selected = True
                    elif UP_MENU_COL_2 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_2 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("house", HOUSE_COLORS_COST, HOUSE_LBLUE, "Light blue house activated.")
                        selected = True
                    elif UP_MENU_COL_2 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_2 and UP_MENU_ROW_2 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_2:
                        self.upgrades_selected("house", HOUSE_GAR_DEF_COST, HOUSE_GARAGE_WHITE,
                                               "White garage activated.", True)
                        selected = True
                    elif UP_MENU_COL_2 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_2 and UP_MENU_ROW_3 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_3:
                        self.upgrades_selected("house", HOUSE_GAR_COLOR_COST, HOUSE_GARAGE_PINK,
                                               "Pink garage activated.", True)
                        selected = True
                    elif UP_MENU_COL_3 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_3 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("house", HOUSE_GAR_COLOR_COST, HOUSE_GARAGE_BLUE,
                                               "Blue garage activated.", True)
                        selected = True
                    elif (UP_MENU_X > mouse_pos[0] or UP_MENU_X + UP_MENU_WIDTH < mouse_pos[0]) or \
                            (UP_MENU_Y > mouse_pos[1] or UP_MENU_Y + UP_MENU_HEIGHT < mouse_pos[1]):
                        selected = True
        self.upgrades_draw()

    def upgrades_door_menu(self):
        # display all door menu items with corresponding cost
        star = pygame.image.load(STAR).convert_alpha()
        up_surf = pygame.Surface((UP_MENU_WIDTH, UP_MENU_HEIGHT))
        up_surf_border = pygame.Surface((UP_MENU_WIDTH + 10, UP_MENU_HEIGHT + 10))
        up_surf_border.fill(K_PURPLE)
        up_surf.fill(K_GREEN)
        default = pygame.image.load(DOOR_DEF)
        self.upgrades_display_element(default, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(DEFAULTS_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        red = pygame.image.load(DOOR_RED)
        self.upgrades_display_element(red, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y2, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(DOOR_COLOR_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        blue = pygame.image.load(DOOR_BLUE)
        self.upgrades_display_element(blue, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y3, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(DOOR_COLOR_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        # escape = pygame.image.load(EXIT)
        # self.upgrades_display_element(escape, EXIT_WIDTH, EXIT_HEIGHT, UP_MENU_WIDTH - EXIT_WIDTH, 0, up_surf)
        self.screen.blit(up_surf_border, (UP_MENU_X - 5, UP_MENU_Y - 5))
        self.screen.blit(up_surf, (UP_MENU_X, UP_MENU_Y))
        pygame.display.update()

    def upgrades_door_selection(self):
        selected = False
        self.upgrades_door_menu()
        # Get user selection
        while not selected:
            mouse_pos = pygame.mouse.get_pos()
            for selection in pygame.event.get():
                if selection.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                    if UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("door", DEFAULTS_COST, DOOR_DEF, "Brown door activated.")
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_2 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_2:
                        self.upgrades_selected("door", DOOR_COLOR_COST, DOOR_RED, "Red door activated.")
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_3 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_3:
                        self.upgrades_selected("door", DOOR_COLOR_COST, DOOR_BLUE, "Blue door activated.")
                        selected = True
                    elif (UP_MENU_X > mouse_pos[0] or UP_MENU_X + UP_MENU_WIDTH < mouse_pos[0]) or \
                            (UP_MENU_Y > mouse_pos[1] or UP_MENU_Y + UP_MENU_HEIGHT < mouse_pos[1]):
                        selected = True
        self.upgrades_draw()

    def upgrades_grass_menu(self):
        # display all grass menu items with corresponding cost
        star = pygame.image.load(STAR).convert_alpha()
        up_surf = pygame.Surface((UP_MENU_WIDTH, UP_MENU_HEIGHT))
        up_surf_border = pygame.Surface((UP_MENU_WIDTH + 10, UP_MENU_HEIGHT + 10))
        up_surf_border.fill(K_PURPLE)
        up_surf.fill(K_GREEN)
        default = pygame.image.load(GRASS_REG)
        self.upgrades_display_element(default, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(GRASS_REG_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        # escape = pygame.image.load(EXIT)
        # self.upgrades_display_element(escape, EXIT_WIDTH, EXIT_HEIGHT, UP_MENU_WIDTH - EXIT_WIDTH, 0, up_surf)
        self.screen.blit(up_surf_border, (UP_MENU_X - 5, UP_MENU_Y - 5))
        self.screen.blit(up_surf, (UP_MENU_X, UP_MENU_Y))
        pygame.display.update()

    def upgrades_grass_selection(self):
        selected = False
        self.upgrades_grass_menu()
        # Get user selection
        while not selected:
            mouse_pos = pygame.mouse.get_pos()
            for selection in pygame.event.get():
                if selection.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                    if UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("grass", GRASS_REG_COST, GRASS_REG, "Grass activated.", True)
                        selected = True
                    elif (UP_MENU_X > mouse_pos[0] or UP_MENU_X + UP_MENU_WIDTH < mouse_pos[0]) or \
                            (UP_MENU_Y > mouse_pos[1] or UP_MENU_Y + UP_MENU_HEIGHT < mouse_pos[1]):
                        selected = True
        self.upgrades_draw()

    def upgrades_path_menu(self):
        # display all grass menu items with corresponding cost
        star = pygame.image.load(STAR).convert_alpha()
        up_surf = pygame.Surface((UP_MENU_WIDTH, UP_MENU_HEIGHT))
        up_surf_border = pygame.Surface((UP_MENU_WIDTH + 10, UP_MENU_HEIGHT + 10))
        up_surf_border.fill(K_PURPLE)
        up_surf.fill(K_GREEN)
        concrete = pygame.image.load(PATH_CONCRETE)
        self.upgrades_display_element(concrete, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y1, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(PATH_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y1 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        stone = pygame.image.load(PATH_STONES)
        self.upgrades_display_element(stone, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y2, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(PATH_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y2 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        gravel = pygame.image.load(PATH_GRAVEL)
        self.upgrades_display_element(gravel, UP_WIDTH, UP_HEIGHT, UP_MENU_X1, UP_MENU_Y3, up_surf)
        self.upgrades_display_element(star, UP_STAR_W_H, UP_STAR_W_H, UP_MENU_X1 - STAR_BUFFER,
                                      UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER, up_surf)
        draw_text("= " + str(PATH_COST), up_surf,
                  [UP_MENU_X1 + UP_STAR_W_H + 2, UP_MENU_Y3 + UP_HEIGHT + STAR_BUFFER + 4],
                  12, BLACK, ALL_FONT)
        # escape = pygame.image.load(EXIT)
        # self.upgrades_display_element(escape, EXIT_WIDTH, EXIT_HEIGHT, UP_MENU_WIDTH - EXIT_WIDTH, 0, up_surf)
        self.screen.blit(up_surf_border, (UP_MENU_X - 5, UP_MENU_Y - 5))
        self.screen.blit(up_surf, (UP_MENU_X, UP_MENU_Y))
        pygame.display.update()

    def upgrades_path_selection(self):
        selected = False
        self.upgrades_path_menu()
        # Get user selection
        while not selected:
            mouse_pos = pygame.mouse.get_pos()
            for selection in pygame.event.get():
                if selection.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if selection.type == pygame.MOUSEBUTTONUP and selection.button == 1:
                    if UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_1 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_1:
                        self.upgrades_selected("path", PATH_COST, PATH_CONCRETE, "Concrete path activated.", True)
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_2 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_2:
                        self.upgrades_selected("path", PATH_COST, PATH_STONES, 'Stone path activated', True)
                        selected = True
                    elif UP_MENU_COL_1 + UP_WIDTH >= mouse_pos[0] >= UP_MENU_COL_1 and UP_MENU_ROW_3 + UP_HEIGHT >= \
                            mouse_pos[1] >= UP_MENU_ROW_3:
                        self.upgrades_selected("path", PATH_COST, PATH_GRAVEL, 'Gravel path activated', True)
                        selected = True
                    elif (UP_MENU_X > mouse_pos[0] or UP_MENU_X + UP_MENU_WIDTH < mouse_pos[0]) or \
                            (UP_MENU_Y > mouse_pos[1] or UP_MENU_Y + UP_MENU_HEIGHT < mouse_pos[1]):
                        selected = True
        self.upgrades_draw()

    def upgrades_selected(self, select_type, cost, file, str1, activate=False):
        if cost <= self.stars:
            self.stars -= cost
            if select_type == "path":
                self.player_house.pathFile = file
                self.player_house.path = activate
            elif select_type == "house":
                self.player_house.houseFile = file
                self.player_house.garage = activate
            elif select_type == "door":
                self.player_house.doorFile = file
            elif select_type == "grass":
                self.player_house.grassFile = file
                self.player_house.grass = activate
            elif select_type == "hedge":
                self.player_house.hedgeFile = file
                self.player_house.hedge = activate
            elif select_type == "flora":
                self.player_house.floraFile = file
                self.player_house.flora = activate
            elif select_type == "garage door":
                self.player_house.garageDoorFile = file
            elif select_type == "driveway":
                self.player_house.drivewayFile = file
            elif select_type == "window":
                self.player_house.windowFile = file
            surf = pygame.Surface((300, 100))
            surf.fill(WHITE)
            draw_text('Congratulations!', surf, [20, 20], SMALL_TEXT_SIZE, BLACK, ALL_FONT)
            draw_text(str1, surf, [16, 60], SMALL_TEXT_SIZE, BLACK, ALL_FONT)
            self.screen.blit(surf, (UP_MENU_X + (UP_MENU_WIDTH / 2) - (surf.get_width() / 2),
                                    UP_MENU_Y + (UP_MENU_HEIGHT / 2) - (surf.get_height() / 2)))
            pygame.display.update()
            pygame.event.wait()
            pygame.time.delay(TWO_DELAY)
        else:
            surf_width = UP_MENU_WIDTH - 50
            surf_height = 150
            surf = pygame.Surface((surf_width, surf_height))
            surf.fill(WHITE)
            draw_text('Sorry! You need', surf, [20, 20], SMALL_TEXT_SIZE, BLACK, ALL_FONT)
            self.star_img.draw(surf, 0, 20, 60, pygame.SRCALPHA)
            draw_text('= ' + str(cost), surf,
                      [20 + STAR_WIDTH + STAR_BUFFER, 75], SMALL_TEXT_SIZE, BLACK, ALL_FONT)
            self.screen.blit(surf, ((UP_MENU_X + UP_MENU_WIDTH / 2) - (surf_width / 2),
                                    (UP_MENU_Y + UP_MENU_HEIGHT / 2) - (surf_height / 2)))
            pygame.display.update()
            pygame.event.wait()
            pygame.time.delay(TWO_DELAY)
            if select_type == "path":
                self.upgrades_path_menu()
            elif select_type == "house":
                self.upgrades_house_menu()
            elif select_type == "door":
                self.upgrades_door_menu()
            elif select_type == "grass":
                self.upgrades_grass_menu()
            elif select_type == "hedge":
                pass
                # self.upgrades_hedge_menu()
            elif select_type == "flora":
                pass
                # self.upgrades_flora_menu()
            elif select_type == "garage door":
                pass
                # self.upgrades_garage_menu()
            elif select_type == "driveway":
                pass
                # self.upgrades_driveway_menu()
            elif select_type == "window":
                pass
                # self.upgrades_window_menu()

    def upgrades_display_element(self, img, img_width, img_height, img_x, img_y, surface=None, update=False):
        surf = pygame.transform.smoothscale(img, (img_width, img_height))
        if surface is None:
            self.screen.blit(surf, (img_x, img_y))
        else:
            surface.blit(surf, (img_x, img_y))
        if update:
            pygame.display.update()

    ########################### END UPGRADES FUNCTIONS ######################

    ############################### LEARN DIGITS FUNCTIONS ################################
    def learn_digits_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.display_continue = False
                self.learn_digits_stage2()
                self.display_continue = True
            if event.type == pygame.MOUSEBUTTONUP and MAIN_X + MAIN_BUTTON_WIDTH >= mouse_pos[0] >= MAIN_X and MAIN_Y + \
                    MAIN_BUTTON_HEIGHT >= mouse_pos[1] >= MAIN_Y:
                self.display_continue = False
                self.display_score = False
                self.score = 0
                self.load_state = True
                self.state = START

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
        self.star_img.draw(self.screen, 0, STAR_X, STAR_Y, K_PURPLE)
        draw_text("= " + str(self.stars), self.screen, [STAR_X + 50, STAR_Y + 10], 20, BLACK, ALL_FONT)
        pygame.display.update()

    def learn_digits_load(self):
        """
        play digit intro sound clips.
        :return:
        """
        self.learn_digits_draw()
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
            self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE, True)
            self.display_skip = False

            while not found:
                mouse_pos = pygame.mouse.get_pos()
                for selection in pygame.event.get():
                    if ((num1_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (
                            num1_pos[0])) and ((num1_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num1_pos[1])):
                        self.higl_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE, True)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE, True)

                    if ((num2_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (num2_pos[0])) and (
                            num2_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num2_pos[1]):
                        self.higl_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE, True)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE, True)

                    if (num3_pos[0] + NUM_DISPLAY_WIDTH) >= mouse_pos[0] >= (num3_pos[0]) and (
                            num3_pos[1] + NUM_DISPLAY_HEIGHT) >= mouse_pos[1] >= (num3_pos[1]):
                        self.higl_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE, True)
                    else:
                        self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE, True)

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
                            self.stars += 1

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
                                        NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE,
                                                       True)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE,
                                                       True)

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
                                        NUM_DISPLAY_WIDTH / 2), SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE,
                                                       True)
                                self.play_clip(FIND_DIGIT)
                                self.play_number(find_digit)
                                self.learn_digits_draw()
                                self.reg_num_imgs.draw(self.screen, find_list[0], num1_pos[0], num1_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[1], num2_pos[0], num2_pos[1], K_PURPLE)
                                self.reg_num_imgs.draw(self.screen, find_list[2], num3_pos[0], num3_pos[1], K_PURPLE,
                                                       True)
        self.score = 0

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
                if self.stage == 0:
                    self.display_continue = False
                    self.learn_alphabet_draw()
                    self.play_alphabet_song(self.reg_upper_abc)
                    self.stage += 1
                    self.display_score = True
                elif self.stage == 1:
                    self.display_continue = False
                    self.learn_alphabet_draw()
                    self.learn_alphabet_find(self.reg_upper_abc, self.highl_upper_abc)
                    self.stage += 1
                    self.display_continue = True
                elif self.stage == 2:
                    self.display_continue = False
                    self.learn_alphabet_draw()
                    self.play_clip(LEARN_LOWER_CASE)
                    self.play_clip(SING_ALPHABET)
                    self.play_clip(BEGIN_SING)
                    self.play_alphabet_song(self.reg_lower_abc)
                    self.stage += 1
                    self.display_score = True
                elif self.stage == 3:
                    self.display_continue = False
                    self.learn_alphabet_draw()
                    self.learn_alphabet_find(self.reg_lower_abc, self.highl_lower_abc)
                    self.display_continue = True
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
        self.star_img.draw(self.screen, 0, STAR_X, STAR_Y, K_PURPLE)
        draw_text("= " + str(self.stars), self.screen, [STAR_X + 50, STAR_Y + 10], 20, BLACK, ALL_FONT)
        pygame.display.update()

    def learn_alphabet_load(self):
        """
        upon load, play intro alphabet sound clips
        :return: none
        """
        self.learn_alphabet_draw()
        self.play_clip(LEARN_ALPHABET)
        self.play_clip(SING_ALPHABET)
        self.load_state = False
        self.display_continue = True

    def play_alphabet_song(self, image):
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
        self.skip_img.draw(self.screen, 0, SKIP_X, SKIP_Y, SKIP_COLOR, True)
        while pygame.mixer.get_busy():
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (SKIP_X + SKIP_WIDTH >= mouse_pos[0] >= SKIP_X) and (
                            SKIP_Y + SKIP_HEIGHT >= mouse_pos[1] >= SKIP_Y):
                        ALPHABET_SONG.stop()
                if event.type == pygame.USEREVENT:
                    image.draw(self.screen, index, SCREEN_CENTER[0] - (ABC_BUTTON_WIDTH / 2),
                               SCREEN_CENTER[1] - (ABC_BUTTON_HEIGHT / 2), K_PURPLE, True)
                    if index <= len(ABC_DELAYS) - 2:
                        index += 1
                        pygame.time.set_timer(pygame.USEREVENT, ABC_DELAYS[index])
                else:
                    pygame.event.clear()

        self.display_continue = True

    def learn_alphabet_find(self, reg_image, hi_image):
        while self.score < 10:
            self.learn_alphabet_draw()
            found = False
            find_letter = random.randint(0, 25)
            rand1 = random.randint(0, 25)
            rand2 = random.randint(0, 25)

            # adjust random numbers so they aren't the same as target digit
            while rand1 == find_letter:
                rand1 = random.randint(0, 25)

            while rand2 == find_letter:
                rand2 = random.randint(0, 25)

            # create number display positions
            letter1_pos = ((SCREEN_CENTER[0] / 2) - (ABC_WIDTH / 2), SCREEN_CENTER[1] - (ABC_HEIGHT / 2))
            letter2_pos = (SCREEN_CENTER[0] - (ABC_WIDTH / 2), SCREEN_CENTER[1] - (ABC_HEIGHT / 2))
            letter3_pos = (((SCREEN_CENTER[0] / 2) + SCREEN_CENTER[0]) - (ABC_WIDTH / 2),
                           SCREEN_CENTER[1] - (ABC_HEIGHT / 2))
            """
            put numbers in list to display in numerical order.
            find index of target digit to use when checking for correct user selection
            """
            find_list = [find_letter, rand1, rand2]
            find_list.sort()
            find_idx = 0
            letter1_idx = 0
            letter2_idx = 0
            i = 0
            while i < len(find_list):
                if find_list[i] == find_letter:
                    find_idx = i
                    i += 1
                elif find_list[i] == rand1:
                    letter1_idx = i
                    i += 1
                elif find_list[i] == rand2:
                    letter2_idx = i
                    i += 1
            """
            put positions in list so target digit index can be used for correct user selection checking
            """
            letter_pos_list = (letter1_pos, letter2_pos, letter3_pos)

            """ Play find digit and target digit sounds and display digits"""
            self.play_clip(FIND_LETTER)
            # FIND_DIGIT.play()
            # while pygame.mixer.get_busy():
            #     pygame.event.clear()
            self.play_letter(find_letter)
            reg_image.draw(self.screen, find_list[0], letter1_pos[0], letter1_pos[1], K_PURPLE)
            reg_image.draw(self.screen, find_list[1], letter2_pos[0], letter2_pos[1], K_PURPLE)
            reg_image.draw(self.screen, find_list[2], letter3_pos[0], letter3_pos[1], K_PURPLE, True)
            self.display_skip = False

            while not found:
                mouse_pos = pygame.mouse.get_pos()
                for selection in pygame.event.get():
                    if ((letter1_pos[0] + ABC_WIDTH) >= mouse_pos[0] >= (
                            letter1_pos[0])) and (
                            (letter1_pos[1] + ABC_HEIGHT) >= mouse_pos[1] >= (letter1_pos[1])):
                        hi_image.draw(self.screen, find_list[0], letter1_pos[0], letter1_pos[1], K_PURPLE, True)
                    else:
                        reg_image.draw(self.screen, find_list[0], letter1_pos[0], letter1_pos[1], K_PURPLE, True)

                    if ((letter2_pos[0] + ABC_WIDTH) >= mouse_pos[0] >= (letter2_pos[0])) and (
                            letter2_pos[1] + ABC_HEIGHT) >= mouse_pos[1] >= (letter2_pos[1]):
                        hi_image.draw(self.screen, find_list[1], letter2_pos[0], letter2_pos[1], K_PURPLE, True)
                    else:
                        reg_image.draw(self.screen, find_list[1], letter2_pos[0], letter2_pos[1], K_PURPLE, True)

                    if (letter3_pos[0] + ABC_WIDTH) >= mouse_pos[0] >= (letter3_pos[0]) and (
                            letter3_pos[1] + ABC_HEIGHT) >= mouse_pos[1] >= (letter3_pos[1]):
                        hi_image.draw(self.screen, find_list[2], letter3_pos[0], letter3_pos[1], K_PURPLE, True)
                    else:
                        reg_image.draw(self.screen, find_list[2], letter3_pos[0], letter3_pos[1], K_PURPLE, True)

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
                        if (letter_pos_list[find_idx][0] + ABC_WIDTH) >= mouse_pos[0] >= (
                                letter_pos_list[find_idx][0]) and (letter_pos_list[find_idx][1] + ABC_HEIGHT) \
                                >= mouse_pos[1] >= (letter_pos_list[find_idx][1]):
                            self.play_clip(VERY_GOOD)
                            self.play_clip(FOUND_LETTER)
                            self.play_letter(find_letter)
                            found = True
                            self.incorrect_find = 0
                            self.score += 1
                            self.stars += 1

                        elif (letter_pos_list[letter1_idx][0] + ABC_WIDTH) >= mouse_pos[0] >= (
                                letter_pos_list[letter1_idx][0]) and (letter_pos_list[letter1_idx][1] + ABC_HEIGHT) \
                                >= mouse_pos[1] >= (letter_pos_list[letter1_idx][1]):
                            self.incorrect_find += 1
                            if self.incorrect_find <= 1:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_letter(rand1)
                                self.play_clip(TRY_AGAIN)
                                self.play_clip(FIND_LETTER)
                                self.play_letter(find_letter)
                            elif self.incorrect_find >= 2:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_letter(rand1)
                                self.play_clip(THE_LETTER)
                                self.play_letter(find_letter)
                                self.play_clip(LOOKS_LIKE)
                                self.learn_alphabet_draw()
                                reg_image.draw(self.screen, find_letter, SCREEN_CENTER[0] - (
                                        ABC_WIDTH / 2), SCREEN_CENTER[1] - (ABC_HEIGHT / 2), K_PURPLE, True)
                                self.play_clip(FIND_LETTER)
                                self.play_letter(find_letter)
                                self.learn_alphabet_draw()
                                reg_image.draw(self.screen, find_list[0], letter1_pos[0], letter1_pos[1], K_PURPLE)
                                reg_image.draw(self.screen, find_list[1], letter2_pos[0], letter2_pos[1], K_PURPLE)
                                reg_image.draw(self.screen, find_list[2], letter3_pos[0], letter3_pos[1], K_PURPLE,
                                               True)

                        elif (letter_pos_list[letter2_idx][0] + ABC_WIDTH) >= mouse_pos[0] >= (
                                letter_pos_list[letter2_idx][0]) and (letter_pos_list[letter2_idx][1] + ABC_HEIGHT) \
                                >= mouse_pos[1] >= (letter_pos_list[letter2_idx][1]):
                            self.incorrect_find += 1
                            if self.incorrect_find <= 1:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_letter(rand2)
                                self.play_clip(TRY_AGAIN)
                                self.play_clip(FIND_LETTER)
                                self.play_letter(find_letter)
                            elif self.incorrect_find >= 2:
                                self.play_clip(NOT_RIGHT)
                                self.play_clip(YOU_CHOSE)
                                self.play_letter(rand2)
                                self.play_clip(THE_LETTER)
                                self.play_letter(find_letter)
                                self.play_clip(LOOKS_LIKE)
                                self.learn_alphabet_draw()
                                reg_image.draw(self.screen, find_letter, SCREEN_CENTER[0] - (
                                        ABC_WIDTH / 2), SCREEN_CENTER[1] - (ABC_HEIGHT / 2), K_PURPLE, True)
                                self.play_clip(FIND_LETTER)
                                self.play_letter(find_letter)
                                self.learn_alphabet_draw()
                                reg_image.draw(self.screen, find_list[0], letter1_pos[0], letter1_pos[1], K_PURPLE)
                                reg_image.draw(self.screen, find_list[1], letter2_pos[0], letter2_pos[1], K_PURPLE)
                                reg_image.draw(self.screen, find_list[2], letter3_pos[0], letter3_pos[1], K_PURPLE,
                                               True)
        self.score = 0

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
        self.star_img.draw(self.screen, 0, STAR_X, STAR_Y + 70, K_BLUE)
        draw_text("= " + str(self.stars), self.screen, [STAR_X + 50, STAR_Y + 80], 20, BLACK, ALL_FONT)
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
                                   SCREEN_CENTER[1] - (NUM_DISPLAY_HEIGHT / 2), K_PURPLE, True)
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
            self.reg_num_imgs.draw(self.screen, index, SCREEN_CENTER[0], SCREEN_CENTER[1], K_BLUE, True)
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
            self.skip_img.draw(self.screen, 0, SKIP_X, SKIP_Y, SKIP_COLOR, True)
            mouse_pos = pygame.mouse.get_pos()
            self.clock.tick(delay)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (SKIP_X + SKIP_WIDTH >= mouse_pos[0] >= SKIP_X) and (
                            SKIP_Y + SKIP_HEIGHT >= mouse_pos[1] >= SKIP_Y):
                        clip.stop()
                else:
                    pygame.event.clear()

    def play_letter(self, index, delay=0):
        letter_list[index].play()
        while pygame.mixer.get_busy():
            self.clock.tick(delay)
            pygame.event.clear()
