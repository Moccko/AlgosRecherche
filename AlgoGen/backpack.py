import numpy as np
import random

objects = ("pyjama", "toothbrush", "pistol", "knife", "keys", "bow_tie", "passport")


def objects_set():
    return dict(zip(objects, np.random.randint(1, 10, len(objects))))


def populations(size):
    x = []
    for i in range(size):
        x.append(set(random.choices(objects, k=random.randint(1, len(objects)))))
    return x


def algo_gen(size, fitness, backpack, things):
    x = populations(size)
    newPop = []
    maxIt = 100
    while maxIt > 0:
        f = list(x)
        for i in range(size):
            f[i] = fitness(x[i])
        while len(newPop) < size:
            print()


nb_chromosomes = 50
backpack_size = 10
things = objects_set()
print(things)
algo_gen(nb_chromosomes, lambda x, y: (x, y), backpack_size, things)
