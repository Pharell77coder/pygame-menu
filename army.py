import random

class Army:
    def __init__(self, nom, effectif, owner):
        self.nom = nom
        self.effectif = effectif
        self.position = owner.territoire[random.randint(0, len(owner.territoire)-1)].get_pos()
        self.owner = owner

    def targets(self):
        ennemy = random.choice(self.owner.ennemies)
        target = random.choice(ennemy.territoire)
        self.target = target.get_pos()

def fight(force_a, force_b, alpha, beta, delta_t):
    forces_a = [force_a]
    forces_b = [force_b]

    force_a -= beta * forces_b[-1] * delta_t
    force_b -= alpha * forces_a[-1] * delta_t

    force_a = max(force_a, 0)
    force_b = max(force_b, 0)

    forces_a.append(force_a)
    forces_b.append(force_b)

    return forces_a[-1], forces_b[-1]

