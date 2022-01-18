"""
using the DEAP framework

The OneMax (or One-Max) problem is a simple optimization task that is often
used as the Hello World of genetic algorithm frameworks. We will use this
problemto demostrate how DEAP can be used to implement a genetic algorithm.

The OneMax task is to find the binary string of a given lenght that maximizes
the sum of its digits. For example, the OneMax problem of length 5 will
consider candidates such as the following:

    10010 (sum of digits=2)
    01110 (sum of digits=3)
    11111 (sum of digits=5)

Obviously (to us), the solution to this problem is always the string that
comprises all 1s. But the genetic algorithm does not have this knowledge,
and needs to blindly  look for this solutions using its genetic operators.
If the algorithm does its job, it will find the solution, or at least one
close to t, within a reasonable amount of time.
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


MAX_GENERATIONS = 50        # max number of generations for 
                            # stopping condition

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
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LENGTH)


def backup():
    try:
        genome = [1, 1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2]
        population = toolbox.populationCreator(n=100)
        print(len(population))

        print()
        fitness_val = toolbox.evaluate(population)
        print(fitness_val)

        anotherfit = list(map(toolbox.evaluate, population))
        print(anotherfit)
        # evaluing = toolbox.evaluate(genome)
    except Exception as e:
        print(str(e))
        exit(1)


def implement():

    genome = toolbox.individualCreator()
    population = toolbox.populationCreator(n=POPULATION_SIZE)


    for populus in population:
        if populus == genome:
            print(genome)
            break


def main():
    population = toolbox.populationCreator(n=POPULATION_SIZE)
    generationCounter = 0

    # to calculate the fitness for each indiviual in the initial 
    # population, we use the Python map() to apply the evaluate
    # operator to each item in the population. 

    fitnessValues = list(map(toolbox.evaluate, population))

    # since the items of firnessValues respectively match those
    # in population (which is a list of individuals), we can use
    # the zip() function to combine them and assign the matching
    # itness tuple to each individual

    # print(population[0])
    # print(sum(population[0]))
    # print(fitnessValues)
    for individual, fitnessValue in zip(population, fitnessValues):
        individual.fitness.values = fitnessValue

    fitnessValues = [individual.fitness.values[0]
            for individual in population]

    # for x in population:
    #     print(x.fitness.values[0])
    # the statistics collected will be the max fitness value and the mean
    # (average) fitness value for each generation. Two lists will be used
    # for tis purrpose, and they are created next:

    maxFitnessValues = list()
    meanFitnessValues = list()

    # we are finally ready for the main loop of the genetic flow. At the
    # top of the loop we find the stopping conditions. As we decided earlier
    # one stopping condition is set by putting a alimit on the number of
    # generations, and the other by detecting that we have reached the best
    # solution (a binary string containing all 1s):
    print(max(fitnessValues))
    while max(fitnessValues) < ONE_MAX_LENGTH and \
            generationCounter < MAX_GENERATIONS:

        generationCounter = generationCounter + 1

        # at the heart of the genetic algorithm are the generic operators,
        # which are applied next. The first is the selection operator, 
        # applied using the toolbox.select operator we earlier defined
        # as the tournament selection. Since we already set the tournament
        # size when the operator was defined, we only need to send the po-
        # pulation and its length as arguments now:

        offspring = toolbox.select(population, len(population))

        offspring = list(map(toolbox.clone, offspring))

        # for x in offspring:
        #     print(x.fitness)
        #     print(x.fitness.values)
        #     break
        # print(offspring)
        # print(len(offspring))
        # the next genetic operator is the crossover. It was earlier defined
        # as the toolbox.mate operator, and is aliasing a single-point cross-
        # over. We use Python extended slices to pair every even-ondexed item
        # of the offspring list with the one following it. We then utilize 
        # random() function to flip a coin using the crossover probability set
        # by the P_CROSSOVER constant.

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                # print(child1.fitness.values)
                # print(child1.fitness)
                # print(child1)
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < P_MUTATION:
                toolbox.mutate(mutant)
                del mutant.fitness.values


        freshIndividuals = [ind for ind in offspring if
                not ind.fitness.valid]

        freshFitnessValues = list(map(toolbox.evaluate, freshIndividuals))

        for individual, fitnessValue in zip(freshIndividuals,
                freshFitnessValues):
            individual.fitness.values = fitnessValue

        population[:] = offspring

        # before we continue to the next round, the current fitness values
        # are collected to allow for statistics gathering. Since the fitness
        # value is a (single element) tuple, we need to select the [0] index:

        fitnessValues = [ind.fitness.values[0] for ind in population]

        # the max and mean fitness values are then found , their values
        # get appended to the statistics accumulators, and summary line
        # is printed out:

        maxFitness = max(fitnessValues)
        meanFitness = sum(fitnessValues) / len(population)
        maxFitnessValues.append(maxFitness)
        meanFitnessValues.append(meanFitness)

        # print(f"""[*] Generation {generationCounter} : Max Fitness=
        #         {maxFitness}, Avg Fitness = {meanFitness}""")


        # in adition, we locte the index of the (first) best individual
        # using the max fitness value we jsut found, and print this 
        # individual out

        best_index = fitnessValues.index(max(fitnessValues))
        # print("Best Individual = ", *population[best_index], "\n")


    # once a stopping condition was activated and the gneetic algorithm
    # flow concludes, we can use the statistics accumulators to plot a 
    # couple of graphs
    """print(maxFitnessValues)
    print(meanFitnessValues)
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title("Max and Average firness over Generations")
    plt.show()"""






if __name__ == "__main__":
    main()
