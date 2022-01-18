"""
    Generic functions to get the calls and parameters
    whenever you gonna try to make the onemaxfitness
    execution and try to search the best for each population
"""
from .generics import *
from random import randint


def one_max_value(individual: Genome) -> FitnessSingle:
    return sum(individual),


def fintess_max_score(population: Population) -> FitnessScore:
    return list(map(one_max_value, population))


def make_crossover_child(child1: Genome, child2: Genome) -> CrossChild:

    size = min(len(child1), len(child2))
    check_point = randint(1, size-1)
    child1[check_point:], child2[check_point:] = \
        child2[check_point:], child1[check_point:]
    return child1, child2
