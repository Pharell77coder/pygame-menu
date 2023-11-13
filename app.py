from pygame.locals import *
import pygame
import random
import sys

FPS = 60
HEIGHT = 640
WIDTH = 640
TILESIZE = 64
DEBUG = True


class Square:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

        self.border = 'black'

    def draw(self, screen, color):
        pygame.draw.rect(screen, self.border, (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(screen, color,
                         (self.x * TILESIZE + 0.5, self.y * TILESIZE + 0.5, TILESIZE - 0.5, TILESIZE - 0.5))


class Pawn(Square):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = 'grey'
        self.selected = False
        self.border = 'black'
        self.animation = False
        self.current_sprites = 0
        self.sprites = list()
        self.sprites.append('grey')
        self.sprites.append('blue')

    def add_selected(self):
        self.selected = True

    def del_selected(self):
        self.selected = False


    def move(self, value):
        self.x = value[0]
        self.y = value[1]

    def get_pos(self):
        return self.x, self.y

    def animate(self):
        self.animation = True

    def update(self, screen, speed) -> None:
        if self.selected :
            self.color = "red"
        elif not self.selected:
                self.color = "grey"
        if self.animation:
            self.current_sprites += speed

            if self.current_sprites >= len(self.sprites):
                self.current_sprites = 0
                self.animation = False

            self.color = self.sprites[int(self.current_sprites)]

        self.draw(screen, self.color)


class Game:
    def __init__(self):

        pygame.init()

        self.full_screen = False
        if self.full_screen:
            self.screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
        elif not self.full_screen:
            self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.clock = pygame.time.Clock()

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Game")

        self.current_time = 0
        self.button_press_time = 0
        self.selected_option = 0

        self.press = True
        self.state = "menu"

        self.menu_options = ["Commencer une Partie", "Progression", "Paramètres", "Quitter"]
        self.partie_options = ["Tutoriel", "Local", "En ligne", "Retour"]
        self.options_options = ["Pleine écran", "Volume", "Retour"]
        self._options = [""]

        self.squares = [(i, j) for i in range(WIDTH//TILESIZE) for j in range(HEIGHT//TILESIZE)]
        self.colors = ['white' for _ in self.squares]
        self.pawn = [Pawn((0, 6)), Pawn((5, 4)), Pawn((3, 7)), Pawn((2, 1))]

    def draw_button(self, text, x, y, width, height, inactive_color, active_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_color, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, inactive_color, (x, y, width, height))
            text_surface = self.font.render(text, True, self.black)
            text_rect = text_surface.get_rect()
            text_rect.center = (x + width / 2, y + height / 2)
            self.screen.blit(text_surface, text_rect)
            return False

    def draw(self, options):
        self.screen.fill((230, 250, 240))
        for i, option in enumerate(options):
            x = (WIDTH // 2) - 200
            y = (HEIGHT // 5) + (i * 75)
            inactive_color = (150, 150, 150)
            active_color = (200, 200, 200)
            color = inactive_color
            if option == "Quitter":
                color = (255, 0, 0)
            if i == self.selected_option:
                color = active_color
            if option == "Quitter" and i == self.selected_option:
                color = (255, 100, 100)
            menu_text = self.font.render(option, True, color)
            menu_rect = menu_text.get_rect(center=(x, y))
            self.screen.blit(menu_text, menu_rect)

    def state_options(self):
        if self.state == "menu":
            options = self.menu_options
        elif self.state == "partie":
            options = self.partie_options
        elif self.state == "options":
            options = self.options_options
        else:
            options = [""]
        return options

    def run(self):
        last_pawn, running = None, True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and self.press:
                    self.press = False
                    self.button_press_time = pygame.time.get_ticks()
                    options = self.state_options()
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if self.state == "menu":
                            if self.menu_options[self.selected_option] == "Commencer une Partie":
                                self.state = "partie"
                            elif self.menu_options[self.selected_option] == "Progression":
                                print('plus tard')
                            elif self.menu_options[self.selected_option] == "Paramètres":
                                self.state = "options"
                            elif self.menu_options[self.selected_option] == "Quitter":
                                running = False
                            else:
                                print('erreur menu')

                        elif self.state == "partie":
                            if self.partie_options[self.selected_option] == "Tutoriel":
                                self.state = "tutorial"
                            elif self.partie_options[self.selected_option] == "Local":
                                print('plus tard')
                            elif self.partie_options[self.selected_option] == "En ligne":
                                print('plus tard')
                            elif self.partie_options[self.selected_option] == "Retour":
                                self.state = "menu"
                            else:
                                print('erreur partie')

                        elif self.state == "options":
                            if self.options_options[self.selected_option] == "Pleine écran":
                                self.full_screen = not self.full_screen
                            elif self.options_options[self.selected_option] == "Retour":
                                self.state = "menu"
                            elif self.options_options[self.selected_option] == "Volume":
                                print('plus tard')
                            else:
                                print('erreur options')
                        if DEBUG : print(self.state, self.menu_options[self.selected_option], self.partie_options[self.selected_option])


                elif event.type == pygame.MOUSEBUTTONUP and self.press:
                    self.press = False
                    self.button_press_time = pygame.time.get_ticks()
                    if self.state == "tutorial":
                        mouse_pos = pygame.mouse.get_pos()
                        click_pos = (mouse_pos[0] // TILESIZE, mouse_pos[1] // TILESIZE)
                        if DEBUG: print(f"Clic de souris en position: {click_pos}")
                        for i, pawn in enumerate(self.pawn):
                            if pawn.get_pos() == click_pos:
                                if not self.pawn[i].selected:
                                    if last_pawn is not None:
                                        last_pawn.del_selected()
                                    self.pawn[i].add_selected()
                                    last_pawn = self.pawn[i]
                                elif self.pawn[i].selected:
                                    self.pawn[i].del_selected()
                                    last_pawn = None
                            elif last_pawn is not None:
                                if (click_pos[0], click_pos[1]) not in [p.get_pos() for p in self.pawn]:
                                    last_pawn.move(click_pos)
                                    last_pawn.del_selected()
                                    last_pawn = None

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and self.press:
                    self.press = False
                    self.button_press_time = pygame.time.get_ticks()
                    if self.state == "tutorial":
                        for elem in self.pawn:
                            if elem.selected:
                                elem.animate()
                    # if game_state == "pause": game_state == "running"
                    # elif game_state == "running": game_state = "pause"

            if self.state == "menu":
                self.draw(self.menu_options)

            elif self.state == "partie":
                self.draw(self.partie_options)

            elif self.state == "options":
                self.draw(self.options_options)

                if self.full_screen:
                    self.screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
                elif not self.full_screen:
                    self.screen = pygame.display.set_mode((HEIGHT, WIDTH))

            elif self.state == "tutorial":
                [Square(square).draw(self.screen, color) for square, color in zip(self.squares, self.colors)]

                for i in range(HEIGHT//TILESIZE):
                    for j in range(WIDTH//TILESIZE):
                        for element in self.pawn:
                            position = element.get_pos()
                            if i == position[0] and j == position[1]:
                                #element.draw(self.screen, element.color)

                                element.update(self.screen, 0.1)

            self.current_time = pygame.time.get_ticks()

            if self.current_time - self.button_press_time > 0:
                self.press = True

            self.clock.tick(FPS)
            pygame.display.update()


def rectangle(screen, surf, color, pos):
    surface = pygame.Surface(surf)
    surface.fill(color)
    rect = surface.get_rect(center=pos)
    return screen.blit(surface, rect)


def texte(screen, font, text, pos, color='black', bool=True):
    surface = font.render(text, bool, color)
    rect = surface.get_rect(center=pos)
    return screen.blit(surface, rect)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()