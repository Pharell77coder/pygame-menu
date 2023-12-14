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
        self.current_time = 0
        self.button_press_time = 0
        self.press = True
        self.state = "grille"#"menu"
        self.running = True
        self.full_screen = False
        self.menu = Menu(self.screen, self)
        self.grille = Grid(self.screen, self)

    def run(self):
        date = [1, 0, 1] # jour mois années
        self.running = True
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                elif self.state == "menu" and self.press:
                    self.menu.handling(event)
                elif self.state == "grille" and self.press:
                    self.grille.handling(event)

                self.press = False
                self.button_press_time = pygame.time.get_ticks()

            if self.state == "menu":
                self.menu.draw()
            elif self.state == "grille":
                self.grille.update()
                self.grille.draw(date)
                date[0] += 1
                if date[0] == 29:
                    date[0] = 1
                    date[1] += 1
                if date[1] == 13:
                    date[1] = 0
                    date[2] += 1


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
