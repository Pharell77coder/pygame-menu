import pygame
import sys
from constants import *
from menu import Menu
from grid import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Un Titre")
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 24)
        self.current_time = 0
        self.button_press_time = 0
        self.press = True
        self.state = "menu"
        self.running = True
        self.full_screen = False


    def run(self):
        self.running = True
        self.menu = Menu(self.screen, self.font, self)
        self.grille = Grid(self.screen, self.font, self)
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                elif self.state == "menu" and self.press:
                    self.menu.handling(event)

                self.press = False
                self.button_press_time = pygame.time.get_ticks()

            if self.state == "menu":
                self.menu.draw()
            elif self.state == "grille":
                self.grille.draw()

            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.button_press_time > 10:
                self.press = True

            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
