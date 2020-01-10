# A few helper function for the Sudoku Exercices

# arrayOfVars is an array of int encoding propositional variables
# for instance, if you give this function the array [1, 2, 3, 4]
# it will print
# 1 2 3 4 0
# -1 -2 0
# -1 -3 0
# -1 -4 0
# -2 -3 0
# -2 -4 0
# -3 -4 0


def generate_constraints(callback=lambda c: print(" ".join([str(v) for v in c]) + " 0"), nq=8):
    def encode(x, y):
        return x * 10 + y

    def decode(q):
        return q // 10, q % 10

    def equals_1(l):
        callback(l)
        for i, x in enumerate(l):
            for y in l[i + 1:]:
                callback([-x, -y])

    def at_most_1(l):
        for i, x in enumerate(l):
            for y in l[i + 1:]:
                callback([-x, -y])

    # Exactly one value per cell x,y
    for x in range(0, nq):
        equals_1([encode(x + 1, y + 1) for y in range(0, nq)])

    for y in range(0, nq):
        equals_1([encode(x + 1, y + 1) for x in range(0, nq)])

    for x in range(-nq + 1, nq):
        if x < 0:
            y = -x
            x = 0
        else:
            y = 0
        diag = []
        while y < nq and x < nq:
            diag.append(encode(x + 1, y + 1))
            y += 1
            x += 1
        print("c atmost *{}*".format([decode(x) for x in diag]))
        at_most_1(diag)

    for x in range(-nq + 1, nq):
        if x < 0:
            y = nq + x
            x = 0
        else:
            y = nq - 1
        diag = []
        while y >= 0 and x < nq:
            diag.append(encode(x + 1, y + 1))
            y -= 1
            x += 1
        print("c atmost *{}*".format([decode(x) for x in diag]))
        at_most_1(diag)


if __name__ == "__main__":
    generate_constraints()
