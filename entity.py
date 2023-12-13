import random
import names

class Entity:
    def __init__(self, id):
        self.color = (random.randint(5, 155), random.randint(5, 155), random.randint(5, 155))
        self.territoire = []
        self.id = id
        self.province = random.choice(['pays des ', 'terre des ', 'îles des ', 'désert des  ', ' ']) + str(names.get_last_name()) + random.choice([' du sud', ' du nord', " de l'est", " de l'ouest", ' '])
        self.ideologie = {"communiste": 0, "liberal": 0, "fasciste": 0}

        self.garnison = 0
        self.population = 0
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}
        self.economie = 0
        self.lois = {'taxe': 1.50, 'conscription': 5}

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
            self.garnison += area.garnison
            self.population += area.population
            self.economie += area.economie - self.population - self.garnison * 10
        self.economie = round(self.economie, 2)
        self.ideologie = {"communiste": communiste//len(self.territoire), "liberal": liberal//len(self.territoire), "fasciste": fasciste//len(self.territoire)}
        self.ressource = {"electricite": 0, "port": 0, "petrole": 0}

    def get_population(self):
        return self.population

    def add_territoire(self, area):
        self.territoire.append(area)

    def del_territoire(self, area):
        self.territoire = [x for x in self.territoire if x != area]

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
