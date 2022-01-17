"""
using the DEAP framework

The OneMax (or One-Max) problem is a simple optimization task that is often
used as the Hello World of genetic algorithm frameworks. We will use this problem
to demostrate how DEAP can be used to implement a genetic algorithm.

The OneMax task is to find the binary string of a given lenght that maximizes
the sum of its digits. For example, the OneMax problem of length 5 will consider
candidates such as the following:

    10010 (sum of digits=2)
    01110 (sum of digits=3)
    11111 (sum of digits=5)

Obviously (to us), the solution to this problem is always the string that comprises
all 1s. But the genetic algorithm does not have this knowledge, and needs to blindly 
look for this solutions using its genetic operators. If the algorithm does its job,
it will find the solution, or at least one close to t, within a reasonable amount of 
time.

"""

import random
from typing import (
    Tuple
)
from deap import (
    base,
    creator,
    tools
)
import matplotlib.pyplot as plt




# problem constants
ONE_MAX_LENGTH = 100        # length of bit string to be optimized

# Genetic Algorithm constants
POPULATION_SIZE = 200       # number of individuals in population
P_CROSSOVER = 0.9           # probability for crossover
P_MUTATION = 0.1            # probability for mutating


MAX_GENERATIONS = 50        # max number of generations for stopping condition

RANDOM_SEED = 42
random.seed(RANDOM_SEED)


toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)


creator.create("FitnessMax", base.Fitness, weights=(1.0,))


# the convention is to use a class claled Individual to represent each
# of the population's individuals.
creator.create("Individual", list, fitness=creator.FitnessMax)


# register the individualCreator operator, which creates an instance
# of the individual class, filled up with random values of either 0 or 1
toolbox.register("individualCreator", tools.initRepeat, 
        creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)


toolbox.register("populationCreator", 
        tools.initRepeat, list, toolbox.individualCreator)


def oneMaxFitness(individual) -> Tuple[int]:
    return sum(individual), # return a tuple 



toolbox.register("evaluate", oneMaxFitness)

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.MutFlipBit, indpb=1.0/ONE_MAX_LENGTH)

def main():
    population = toolbox.populationCreator(n=POPULATION_SIZE)
    generationCounter = 0

if __name__ == "__main__":
    main()
