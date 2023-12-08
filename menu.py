import pygame
from constants import *


class Menu:
    def __init__(self, screen, root):
        pygame.init()
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont("arial.ttk", 24)

        self.index = 0
        self.selected_option = 0
        self.menu_options = (("Commencer une Partie", "Paramètres", "Quitter"),
                             ("Grille", "Retour"),
                             ("Pleine écran", "Retour"))
        self.root = root

    def handling(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.menu_options[self.index])
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.menu_options[self.index])

            elif event.key == pygame.K_RETURN:
                if self.index == 0:
                    if self.menu_options[self.index][self.selected_option] == "Commencer une Partie":
                        self.index = 1
                    elif self.menu_options[self.index][self.selected_option] == "Paramètres":
                        self.index = 2
                    elif self.menu_options[self.index][self.selected_option] == "Quitter":
                        self.root.running = False

                elif self.index == 1:
                    if self.menu_options[self.index][self.selected_option] == "Grille":
                        self.root.state = "grille"
                    elif self.menu_options[self.index][self.selected_option] == "Retour":
                        self.index = 0

                elif self.index == 2:
                    if self.menu_options[self.index][self.selected_option] == "Pleine écran":
                        if self.root.full_screen:
                            self.root.screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
                        elif not self.root.full_screen:
                            self.root.screen = pygame.display.set_mode((HEIGHT, WIDTH))
                    elif self.menu_options[self.index][self.selected_option] == "Retour":
                        self.index = 0

    def draw(self):
        self.screen.fill((230, 250, 240))
        for i, option in enumerate(self.menu_options[self.index]):
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


# Tests
