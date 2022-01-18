"""
    Generic functions to get the calls and parameters
    whenever you gonna try to make the onemaxfitness
    execution and try to search the best for each population
"""
from .generics import *



def one_max_value(individual: Genome) -> FitnessSingle:
    return sum(individual),

def fintess_max_score(population: Population) -> FitnessScore:
    return list(map(one_max_value, population))