# Research algorithms

Series of exercises about symbolic AI. The imposed topics are
1. Knowledge Representation and Reasoning
2. Algorithms
3. Multi-Agent Systems

The 3 exercises chosen for the assessment are SAT, Genetic Algorithm and Ant Colonies.

## Unique solution Sudoku grid generation using SAT
This exercise is divided in 2 steps.

We generate a Sudoku grid of constraints using a python script to a `.cnf` file. Those constraints define a valid grid of unique numbers per row, column and subgrid.

Then we use another python script that calls pySAT in order to find resolutions for the generated grid. Then for each solution, the solution is added to the SAT solver as a constraint to find another solution. It iterates as is until there is no more solution, now we can remove the last constraint so there is a single solution for the Sudoku.

Unfortunately, I have not been able to run the script to its end, it always finds another solution.

To launch the script :
```bash
cd pysat
chmod +x generateUniqueSudoku.sh
./generateUniqueSudoku.sh
```
That will create a grid and a temp grid for logs and once the program is done running, will append the new constraints to the original grid.

## Travelling salesman problem using Genetic Algorithm


## Travelling salesman problem using Ant Colonies
