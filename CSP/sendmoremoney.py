from pycsp3 import *

letters = VarArray(size=8, dom=range(10))
s, e, n, d, m, o, r, y = letters

satisfy(
    AllDifferent(letters),
    s > 0,
    m > 0,
    [s, e, n, d] * [1000, 100, 10, 1] + [m, o, r, e] * [1000, 100, 10, 1] == [m, o, n, e, y] * [10000, 1000, 100, 10, 1]
)
