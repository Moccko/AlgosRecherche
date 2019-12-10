import numpy as np


def init_cities(maxd):
    d = np.random.randint(-maxd, maxd, (cities, cities))
    d = np.abs((d + d.T) // 2) + 1
    np.fill_diagonal(d, 0)
    return d


cities = 5
k = 10 * cities
d = init_cities(16)
p = np.zeros((cities, cities))
c = np.zeros((k, cities))

print(d)

for i in range(k):
    for j in range(cities):
        break
    break
