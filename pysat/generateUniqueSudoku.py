if __name__ == '__main__':
    from src import *
else:
    from .src import *


def finish(filename, clauses, tries):
    with open(filename, "a") as file:
        for clause in clauses:
            file.write(f"{' '.join([str(c) for c in clause])} 0\n")
    print(f"Succeeded with {tries} tries and {len(clauses)} additional clauses, have a look to {sys.argv[1]}")


if __name__ == "__main__":

    unique = False
    tries = 0
    gridclauses = []
    clauses = []

    if len(sys.argv) > 1:
        for line in myopen(sys.argv[1]):
            firstChar = line[0]
            if not firstChar in ['c', 'p']:
                gridclauses.append([l for l in list(map(int, line.split())) if l is not 0])

        try:
            while not unique:

                solver = Solver()
                for clause in [*gridclauses, *clauses]:
                    solver.addClause(clause)

                solver.buildDataStructure()

                result = solver.solve()

                if result == solver._cst.lit_False:
                    print("c UNSATISFIABLE")
                elif result == solver._cst.lit_True:
                    print("c SATISFIABLE")
                else:
                    print("c UNKNOWN")
                # solver.printFinalStats()

                if result == solver._cst.lit_True and solver._config.printModel:  # SAT was claimed
                    # print("v ", end="")
                    # for v in solver.finalModel:
                    #      print(v," ", end="")
                    # print("")

                    print("v ", end="")
                    clauses.append([-v for v in solver.finalModel if v > 0])
                    # print(*[f"{-v}" for v in solver.finalModel if v > 0], 0, sep=" ")
                    # print("")

                with open("gridtmp.cnf", "w") as file:
                    file.write(" 0\n".join([str(c) for c in [*gridclauses, *clauses]]))

                # As in the SAT competition, ends with the correct error code
                unique = result != solver._cst.lit_True
                tries += 1

            finish(sys.argv[1], clauses, tries)
        except (KeyboardInterrupt, SystemExit):
            finish(sys.argv[1], clauses, tries)



    else:
        print("c - Error - Please give me a cnf(.gz) file as input")
        sys.exit(1)
