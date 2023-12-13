import random

def pathfinding(pos, target):
    liste = [pos,]
    i = 0
    while True:
        if liste[i] == target:
            break

        if liste[i][0] < target[0]:
            step1 = liste[i][0] + 1
        elif liste[i][0] > target[0]:
            step1 = liste[i][0] - 1
        else:
            step1 = target[0]

        if liste[i][1] < target[1]:
            step2 = liste[i][1] + 1
        elif liste[i][1] > target[1]:
            step2 = liste[i][1] - 1
        else:
            step2 = target[1]

        step = (step1, step2)
        liste.append(step)
        i += 1

    return liste

pos = (random.randint(0, 10), random.randint(0, 10))
target = (random.randint(0, 10), random.randint(0, 10))
print(f"Position de départ : {pos}, Position d'arrivée : {target}, trajet : {pathfinding(pos, target)}")
