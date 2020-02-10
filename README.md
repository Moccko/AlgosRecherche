# Research algorithms

Series of exercises about symbolic AI. The imposed topics are
1. Knowledge Representation and Reasoning
2. Multi-Agent Systems
3. Algorithms

The 3 exercises chosen for the assessment are SAT, Ant Colonies and Genetic Algorithm.

Be sure to setup the dependencies before running the notebook.
```bash
conda install numpy
conda install -c conda-forge ipywidgets tqdm
jupyter nbextension enable --py widgetsnbextension
```

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

## Travelling salesman problem using Ant Colonies
I present this exercise as a iPython Notebook, it consists of 2 classes: `Salesman` and `Ants`. I chose to represent the map with an adjacence matrix for distances between cities identified by row and column index.

`Salesman` takes all the hyperparameters and launches a solution search with a specified number of iterations. For each iteration, the class retrieves the roads taken by the ants and updates the pheromones on the roads.

The `Ant` class manages the choices made by the ants and return the road they took during the iteration.

### Observations
While playing with the hyperparameters I noticed that they have an impact not only on the performance but also on the solution found. For instance, not enough iterations prevent the ants to be affected by the pheromones.

## Travelling salesman problem using Genetic Algorithm
This exercise is presented as a iPython Notebook, it consists of a single class `Salesman`, that contains all the logic of the Genetic Algorithm applied to the TSP.

The tweakable parameters are the number of `cities`, the `population`, the `elitism` and `mutation` rate, and the starting city. It is possible to generate a new list of cities with random distances by specifying the `generate` attribute to `True`, you can also set the `path` for the generated map or use a txt persistence of an `ndarray`.

This implementation of the GA uses the ranking approach, it orders the population by ascending heuristic and select a part of it according to the `elitism` ratio. There are other implementations such as the tournament selection that applies a ranking selection on pairs of chromosomes, or the uniform selection where every chromosome has the same probability to be selected.

The cities are stored as an adjacency matrix of distances. The chromosomes are a list of integers matching a city. The initialization consists of generating random combinations of cities, then the mutation swaps 2 random cities inside some combinations based on the `mutation rate.

### Observations
Strangely, the more elitist the solver is, the worse are the results. The GA focuses too much on a specific sample and the mutations are not deep enough to find some better solutions.

## TSP performance comparisons
The Ant Colonies method quickly shows good results, with the good parameters I usually reach the best or second best solution.

Below is a benchmark of 50 full runs of each method on the `cities_example.txt` file that contains 12 cities:

| |Ant Colonies|Genetic Algorithm|
|---|---|---|
|Iterations|100|1000|
|Execution time|2'05"||
|Parameters|60,000|3,600,000|
|Best route|23|33|

- Ant colonies (`ants=50, alpha=0.1, beta=1.1`)
- GA (`population=300, elite=0.5, mutation=0.3`)

### Tracks for improvement
That implementation of the GA is not appropriated for the TSP. This is a matter of luck, if there are some very good generated roads during the initialization but that cross one city in the wrong order, the impact on the heuristic can be so big that the elitism will throw this road away. To counter this issue, we can try to use the tournament selection approach or to insert random chromosomes during the mutation to get some fresh roads.

Both of the ant colonies and GA approaches are not the most suited for the TSP resolution, they rely a lot on luck. Even with a high number of iterations on each method, there is no guarantee to get the best solution. Ants can be too influenced by pheromones and chromosomes by the chosen heuristic.
