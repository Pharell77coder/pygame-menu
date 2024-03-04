import matplotlib.pyplot as plt
import random
def lanchester_square_law(force_a, force_b, alpha, beta, delta_t, duration):
    """
    Simule la loi de Lanchester (version carrée) pour deux forces en fonction du temps.

    :param force_a: Force initiale de l'unité A
    :param force_b: Force initiale de l'unité B
    :param alpha: Coefficient d'efficacité de l'unité A
    :param beta: Coefficient d'efficacité de l'unité B
    :param delta_t: Pas de temps pour la simulation
    :param duration: Durée totale de la simulation
    :return: Deux listes, une pour la force de l'unité A à chaque étape et une pour la force de l'unité B
    """
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

def plot_forces(forces_a, forces_b):
    """
    Affiche un graphique représentant l'évolution des forces au fil du temps.

    :param forces_a: Liste des forces de l'unité A à chaque étape
    :param forces_b: Liste des forces de l'unité B à chaque étape
    """
    plt.plot(forces_a, label='Force de l\'unité A')
    plt.plot(forces_b, label='Force de l\'unité B')
    plt.xlabel('Temps')
    plt.ylabel('Force')
    plt.legend()
    plt.title('Simulation de la loi de Lanchester (version carrée)')
    plt.show()

# Paramètres de la simulation
force_initiale_a = 500
force_initiale_b = 800
coefficient_efficacite_a = 0.02
coefficient_efficacite_b = 0.015
pas_temps = 1
duree_simulation = 100

# Simulation
forces_A, forces_B = lanchester_square_law(force_initiale_a, force_initiale_b,
                                            coefficient_efficacite_a, coefficient_efficacite_b,
                                            pas_temps, duree_simulation)

# Affichage du graphique
plot_forces(forces_A, forces_B)
