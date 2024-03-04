import random
import names
from army import Army

class Entity:
    def __init__(self, id):
        self.color = (random.randint(5, 155), random.randint(5, 155), random.randint(5, 155))
        self.territoire = []
        self.id = id# 'îles des ', 'désert des  ',
        self.province = random.choice(['pays des ', 'terre des ', '']) + str(names.get_last_name()) + random.choice([' du sud', ' du nord', " de l'est", " de l'ouest", ''])
        self.ideologie = {"communiste": 0, "liberal": 0, "fasciste": 0}

        self.garnison = 0
        self.population = 0
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0
        self.lois = {'taxe': 1.50, 'conscription': 25}
        self.ennemies = []
        self.allies = []
        self.armies = []
        self.voisin = []


    def update_frontier(self, liste):
        self.voisin = []
        for territoire in self.territoire:
            for element in liste:
                if territoire.pos[0] == element.pos[0] + 1 and territoire.pos[1] == element.pos[1] and element.owner not in self.voisin and element.owner != self:
                    self.voisin.append(element.owner)

                elif territoire.pos[0] == element.pos[0] - 1 and territoire.pos[1] == element.pos[1] and element.owner not in self.voisin and element.owner != self :
                    self.voisin.append(element.owner)

                elif territoire.pos[0] == element.pos[0] and territoire.pos[1] == element.pos[1] + 1 and element.owner not in self.voisin and element.owner != self :
                    self.voisin.append(element.owner)

                elif territoire.pos[0] == element.pos[0] and territoire.pos[1] == element.pos[1] - 1 and element.owner not in self.voisin and element.owner != self :
                    self.voisin.append(element.owner)

    def update(self):
        communiste = 0
        liberal = 0
        fasciste = 0
        self.garnison = 0
        self.population = 0
        self.economie = 0
        self.effectif = 0
        for area in self.territoire:
            communiste += area.ideologie['communiste']
            liberal += area.ideologie['liberal']
            fasciste += area.ideologie['fasciste']
            self.garnison += area.garnison
            self.effectif += area.effectif
            self.population += area.population
            self.economie += area.economie - self.population - self.garnison * 10 - self.effectif * 10
        self.economie = round(self.economie, 2)
        self.ideologie = {"communiste": communiste//len(self.territoire), "liberal": liberal//len(self.territoire), "fasciste": fasciste//len(self.territoire)}
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}



    def get_population(self):
        return self.population

    def add_territoire(self, area):
        self.territoire.append(area)

    def del_territoire(self, area):
        self.territoire = [x for x in self.territoire if x != area]

    def at_war(self, agresseur = True, ennemy = None):
        if agresseur:
            ennemy = random.choice(self.voisin)
        self.ennemies.append(ennemy)
        if not agresseur:
            return
        ennemy.at_war(False, ennemy = self)

class Player(Entity):
    def __init__(self, id):
        super().__init__(id)
        self.color = (random.randint(5, 155), random.randint(5, 155), random.randint(5, 155))
        self.territoire = []
        self.province = random.choice(['pays des ', 'terre des ', 'îles des ', 'désert des  ', ' ']) + str(names.get_last_name()) + random.choice([' du sud', ' du nord', " de l'est", " de l'ouest", ' '])
        self.ideologie = {"communiste": 0, "liberal": 0, "fasciste": 0}

        self.garnison = 0
        self.population = 0
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0
        self.lois = {'taxe': 1.50, 'conscription': 5}
        self.niveau_technologique = 0
