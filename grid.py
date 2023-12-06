import pygame
import random
from constants import *


class Square:
    def __init__(self, pos, nom):
        self.x = pos[0]
        self.y = pos[1]
        self.margin = 0.5

        self.border = 'black'

        self.province = nom
        self.ideologie = {"communiste": 0, "liberal": 0, "fasciste": 0}
        self.garnison = random.randint(0, 100)
        self.population = random.randint(0, 10000)
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0

    def get_pos(self):
        return self.x, self.y

    def get_info(self):
        return [self.province, self.ideologie, self.garnison, self.population, self.ressource, self.economie]

    def draw(self, screen, color):
        pygame.draw.rect(screen, self.border,
                         (self.margin + self.x * TILESIZE, self.margin + self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(screen, color,
                         (self.margin + self.x * TILESIZE + self.margin, self.margin + self.y * TILESIZE + self.margin,
                          TILESIZE - self.margin * 2, TILESIZE - self.margin * 2))


class Grid:
    def __init__(self, screen, font, root):
        pygame.init()
        self.screen = screen
        self.font = font
        self.root = root
        self.pos = (0, 0)

        col = 7
        row = 9
        self.squares = [[(i, j) for i in range(row)] for j in range(col)]
        self.map = []
        for i in self.squares:
            for j in i:
                self.map.append(Square(j, "ville"))

    def texte(self, text, pos, color='black'):
        menu_text = self.font.render(text, True, color)
        menu_rect = menu_text.get_rect(top=pos[1])
        self.screen.blit(menu_text, menu_rect)

    def handling(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.pos = pygame.mouse.get_pos()

    def draw(self):
        global info
        self.screen.fill((0, 0, 0))
        click_pos = (self.pos[0] // TILESIZE, self.pos[1] // TILESIZE)

        for case in self.map:
            if case.get_pos() == click_pos:
                case.draw(self.screen, (135,206,235))
                info = case.get_info()
            else:
                case.draw(self.screen, (255, 255, 255))
        pygame.draw.rect(self.screen, 'white', (0, HEIGHT - TILESIZE * 2, WIDTH, TILESIZE * 2))
        self.texte(f"Nom de La province : {info[0]}", (0, 525))
        self.texte(
            f"Ideologie : Communisme : {info[1]["communiste"]}, "
            f"Libéralisme : {info[1]['liberal']}, Fascisme : {info[1]['fasciste']}",
            (0, 545))
        self.texte(f"Garnison : {info[2]}", (0, 565))
        self.texte(f"Population : {info[3]}", (0, 585))
        self.texte(f"Ressource : Petrole : {info[4]['petrole']},  "
            f"Port : {info[4]['port']},  Electricité : {info[4]['electricite']}",
            (0, 605))
        self.texte(f"Economie : {info[5]}", (0, 625))
