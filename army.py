import random

class Army:
    def __init__(self, nom, effectif, owner):
        self.nom = "Armée de "+str(nom) # nom
        self.effectif = effectif # nombre de soldat restant
        self.position = owner.territoire[random.randint(0, len(owner.territoire)-1)].get_pos() # position de base de l'armée
        self.owner = owner # pays d'origine
        self.efficacity = random.uniform(0.01, 0.1) # niveau du commandant

    def targets(self, ennemy):
        #ennemy = random.choice(self.owner.ennemies)
        target = random.choice(ennemy.territoire)
        self.target = target.get_pos()

def bataille(army_a, army_b, delta_t, duration):
    force_a = army_a.effectif
    force_b = army_b.effectif
    alpha = army_a.efficacity
    beta = army_b.efficacity
    forces_a = [force_a]
    forces_b = [force_b]

    for _ in range(int(duration / delta_t)):
        force_a -= beta * forces_b[-1] * delta_t
        force_b -= alpha * forces_a[-1] * delta_t

        # Assure que les forces ne deviennent pas négatives
        force_a = max(force_a, 0)
        force_b = max(force_b, 0)

        forces_a.append(force_a)
        forces_b.append(force_b)

    return forces_a, forces_b

