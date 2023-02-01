import pygame, sys

FPS = 60


class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Variables pour la taille de l'écran
        self.screen_width = 640
        self.screen_height = 480

        # Initialisation de la fenêtre
        self.full_screen = False
        if self.full_screen:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        elif not self.full_screen:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Projets-001')

        # Couleurs utilisées dans le jeu
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        self.speed = 5

        # Initialisation du texte
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)

        # Variables pour le menu d'accueil
        self.menu_options = ["Commencer une Partie", "Progression", "Paramètres", "Quitter"]
        self.partie_options = ["Tutoriel", "Local", "En ligne", "Retour"]
        self.options_options = ["Pleine écran", "Volume", "Retour"]
        self._options = [""]
        self.selected_option = 0
        self.state = "menu"

        # Son du jeu
        # sound = pygame.mixer.Sound('../audio/main.ogg')
        # sound.set_volume(0.5)
        # sound.play(loops=-1)

    # Fonction pour dessiner les boutons
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
        for i, option in enumerate(options):
            x = (self.screen_width // 2) - 200
            y = (self.screen_height // 5) + (i * 75)
            inactive_color = (150, 150, 150)
            active_color = (200, 200, 200)
            color = inactive_color
            if i == self.selected_option:
                color = active_color
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
        # Boucle principale du jeu
        running = True
        while running:

            if self.full_screen:
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
            elif not self.full_screen:
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
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

                        print(self.state, self.menu_options[self.selected_option], self.partie_options[self.selected_option])

            self.screen.fill(self.white)

            if self.state == "menu":
                self.draw(self.menu_options)

            elif self.state == "partie":
                self.draw(self.partie_options)

            elif self.state == "options":
                self.draw(self.options_options)

            elif self.state == "tutorial":
                pass

            else:
                print("state no-defined")

            pygame.display.update()
            self.clock.tick(FPS)

def main():
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
