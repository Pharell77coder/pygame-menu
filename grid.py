import pygame
import random
import names
from constants import *


class Entity:
    def __init__(self, id):
        self.color = (random.randint(5, 155), random.randint(5, 155), random.randint(5, 155))
        self.territoire = []
        self.id = id
        self.province = str(names.get_last_name())
        self.ideologie = {"communiste": 0, "liberal": 0, "fasciste": 0}

        self.garnison = 0
        self.population = 0
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0

    def update(self):
        communiste = 0
        liberal = 0
        fasciste = 0
        self.garnison = 0
        self.population = 0
        self.economie = 0

        for area in self.territoire:
            communiste += area.ideologie['communiste']
            liberal += area.ideologie['liberal']
            fasciste += area.ideologie['fasciste']
            self.garnison = area.garnison
            self.population = area.population
            self.economie = area.economie
        self.ideologie = {"communiste": communiste, "liberal": liberal, "fasciste": liberal}
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}

    def draw(self):
        pass

    def add_territoire(self, area):
        self.territoire.append(area)

    def del_territoire(self, area):
        self.territoire = [x for x in self.territoire if x != area]


class Square:
    def __init__(self, pos, owner):
        self.x = pos[0]
        self.y = pos[1]
        self.margin = 0.5

        self.border = 'black'
        self.owner = owner

        eng = ['bury', 'burgh', 'by', 'cester', 'ford', 'ham', 'mouth', 'stead', 'ton', 'worth']
        fra = ['court', 'ville', 'heim', 'loire', 'ac', 'a', 'o', 'mer']
        self.province = str(names.get_last_name()) + random.choice(eng)

        c = random.randint(0, 100)
        l = random.randint(0, 100 - c)
        f = 100 - (c + l)
        self.ideologie = {"communiste": c, "liberal": l, "fasciste": f}

        self.garnison = random.randint(100, 1000)
        self.population = random.randint(1000, 10000)
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("arial.ttk", 13)

    def get_pos(self):
        return self.x, self.y

    def get_info(self):
        return [self.province, self.ideologie, self.garnison, self.population, self.ressource, self.economie]

    def draw(self, screen, select):
        if select:
            color = (self.owner.color[0]+100, self.owner.color[1]+100, self.owner.color[2]+100)
        else:
            color = self.owner.color
        pygame.draw.rect(screen, self.border,
                         (self.margin + self.x * TILESIZE, self.margin + self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(screen, color,
                         (self.margin + self.x * TILESIZE + self.margin, self.margin + self.y * TILESIZE + self.margin,
                          TILESIZE - self.margin * 2, TILESIZE - self.margin * 2))
        if select:
            menu_text = self.font.render(self.province, True, 'black')
            menu_rect = menu_text.get_rect(center=(self.x * TILESIZE + TILESIZE / 2, self.y * TILESIZE + TILESIZE / 2))
            screen.blit(menu_text, menu_rect)


class Grid:
    def __init__(self, screen, root):
        pygame.init()
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont("arial.ttk", 24)
        self.root = root
        self.pos = (0, 0)

        col = 8
        row = 10
        self.squares = [[(i, j) for i in range(row)] for j in range(col)]
        self.map = []
        self.entities = [Entity(i) for i in range(20)]

        compteur = 0
        index = 0
        carre = True

        for i in self.squares:
            for j in i:
                area = Square(j, self.entities[index])
                self.map.append(area)
                self.entities[index].add_territoire(area)
                if compteur % 2 == 1: index += 1
                if compteur % 10 == 9:
                    if carre: index -= 5
                    carre = not carre
                compteur += 1

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
                case.draw(self.screen, True)
                info = case.get_info()
            else:
                case.draw(self.screen, False)
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

    def update(self):
        for entity in self.entities:
            entity.update()
