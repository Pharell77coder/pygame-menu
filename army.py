import random

class Armee:
    def __init__(self, nom, effectif, owner):
        self.nom = nom
        self.effectif = effectif
        self.position = owner.territoire[random.randint(0, len(owner.territoire)-1)].get_pos()
        self.owner = owner

def lanchester_square_law(force_a, force_b, alpha, beta, delta_t, duration):
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

force_initiale_a = 500
force_initiale_b = 800
coefficient_efficacite_a = 0.02
coefficient_efficacite_b = 0.015
pas_temps = 1
duree_simulation = 100

forces_A, forces_B = lanchester_square_law(force_initiale_a, force_initiale_b,
                                            coefficient_efficacite_a, coefficient_efficacite_b,
                                            pas_temps, duree_simulation)
