"""
    Generic functions to get the calls and parameters
    whenever you gonna try to make the onemaxfitness
    execution and try to search the best for each population
"""
from .generics import *
from random import (
    randint,
    choice
)
import random

def random_selection(individuals: Population, iterations: int):
    return [choice(individuals) for _ in range(iterations)]


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


def mutation(individual, indpb) -> Genome:
    """Flip the value of the attributes of the input individual and return the
    mutant. The *individual* is expected to be a :term:`sequence` and the values of the
    attributes shall stay valid after the ``not`` operator is called on them.
    The *indpb* argument is the probability of each attribute to be
    flipped. This mutation is usually applied on boolean individuals.

    :param individual: Individual to be mutated.
    :param indpb: Independent probability for each attribute to be flipped.
    :returns: A tuple of one individual.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i in range(len(individual)):
        # if random.random() < indpb:
        individual[i] = type(individual[i])(not individual[i])
    return individual,


def implement_offsprings(individuals: Population, size: int) -> Population:
    """
    :param size is the shape basically of the genome
    :returns: Population: [A list of genome type but with new elements choosen
        from the original individual, hypotetically the "best" of the "best"]
    """

    offspring = list()

    for _ in range(len(individuals)):
        aspirants = random_selection(individuals, size)
        offspring.append(max(aspirants))

    return offspring



def check_genom_object_pos(genome_object, target) -> int:

    for x in genome_object:
        if genome_object[x]["genome"] == target:
            return x