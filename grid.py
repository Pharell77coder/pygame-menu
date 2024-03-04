import pygame
import random
import names
from constants import *
from entity import Entity


class Square:
    def __init__(self, pos, owner):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.margin = 0.5

        self.border = 'black'
        self.owner = owner

        eng = ['bury', 'burgh', 'by', 'cester', 'ford', 'ham', 'mouth', 'stead', 'ton', 'worth']
        fra = ['court', 'ville', 'heim', 'loire', 'ac', 'a', 'o', 'mer']
        self.province = str(names.get_last_name()) + random.choice(fra)

        c = random.randint(0, 100)
        l = random.randint(0, 100 - c)
        f = 100 - (c + l)
        self.ideologie = {"communiste": c, "liberal": l, "fasciste": f}

        self.garnison = 0
        self.effectif = 0
        self.population = random.randint(1000, 10000)
        self.ressource = {"electricite": random.randint(0, 100), "port": random.randint(0, 100),
                          "petrole": random.randint(0, 100)}
        self.economie = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("arial.ttk", 14)
        self.claim = [owner.province]
        self.id_claim = [owner]

    def get_pos(self):
        return self.x, self.y

    def get_info(self):
        return [self.province, self.ideologie, self.garnison, self.population, self.ressource, self.economie,
                self.owner]

    def draw(self, screen, select):
        if select:
            color = (self.owner.color[0] + 100, self.owner.color[1] + 100, self.owner.color[2] + 100)
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

    def update(self):
        self.population = self.population * random.uniform(0.9, 1.1)
        self.population = int(self.population)
        self.garnison = self.population / 100
        self.garnison = int(self.garnison)
        self.effectif = self.population * (self.owner.lois['conscription'] / 100)
        self.effectif = int(self.effectif)
        self.civil = self.population - (self.effectif + self.garnison)
        self.economie += self.population * self.owner.lois['taxe']


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

    def draw(self, date):
        global info
        self.screen.fill((0, 0, 0))
        click_pos = (self.pos[0] // TILESIZE, self.pos[1] // TILESIZE)

        for case in self.map:
            if date[0] == 1:
                case.update()
            case.draw(self.screen, False)

        for case in self.map:
            if case.get_pos() == click_pos:
                case.draw(self.screen, True)
                info = case.get_info()

        pygame.draw.rect(self.screen, 'white', (1, HEIGHT_FIRST - TILESIZE * 2 + 1, WIDTH - 1, TILESIZE * 2 - 2))
        pygame.draw.rect(self.screen, 'white', (HEIGHT_FIRST + 1, 1, TILESIZE * 4 - 2, WIDTH - 2))
        self.texte(f"Nom de La province : {info[0]} - {info[6].province}", (0, 525))
        self.texte(
            f"Ideologie : Communisme : {info[1]["communiste"]} ({info[6].ideologie["communiste"]}), "
            f"Démocratisme : {info[1]['liberal']} ({info[6].ideologie['liberal']}), Fascisme : {info[1]['fasciste']} ({info[6].ideologie['fasciste']})",
            (0, 545))
        self.texte(f"Garnison : {info[2]} - {info[6].garnison}", (0, 565))
        self.texte(f"Population : {info[3]} - {info[6].population}", (0, 585))
        self.texte(f"Ressource : Petrole : {info[4]['petrole']},  "
                   f"Port : {info[4]['port']},  Electricité : {info[4]['electricite']}",
                   (0, 605))
        self.texte(f"Economie : {info[5]} - {info[6].economie}", (0, 625))

        mois = ['Bélier', 'Taureau', 'Gémeaux', 'Cancer', 'Lion', 'Vierge', 'Balance', 'Scorpion', 'Ophiuchus',
                'Sagittaire', 'Capricorne', 'Verseau', 'Poissons']
        texte = f"{date[0]} {mois[date[1]]} {date[2]}"
        days_text = self.font.render(texte, True, 'black')
        days_rect = days_text.get_rect(top=0, right=HEIGHT - len(texte))
        self.screen.blit(days_text, days_rect)

        texte = f"{info[6].province}"
        days1_text = self.font.render(texte, True, 'black')
        days1_rect = days1_text.get_rect(top=32, right=HEIGHT - 10)
        self.screen.blit(days1_text, days1_rect)
        texte = "En guerre : "
        if len(info[6].ennemies) == 0: texte ="En paix"
        days1_text = self.font.render(texte, True, 'black')
        days1_rect = days1_text.get_rect(top=64, right=HEIGHT - 10)
        self.screen.blit(days1_text, days1_rect)

        for i in range(len(info[6].ennemies)):
            texte = f"{info[6].ennemies[i].province}"
            days1_text = self.font.render(texte, True, 'black')
            days1_rect = days1_text.get_rect(top=96+(32*i), right=HEIGHT - 10)
            self.screen.blit(days1_text, days1_rect)
    def update(self):
        for entity in self.entities:
            entity.update()
            entity.update_frontier(self.map)
            n = random.randint(0, 10000)
            if n == 100 and len(entity.ennemies) == 0:
                entity.at_war()