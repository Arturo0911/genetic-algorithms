"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""

from pprint import pprint
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from pwn import *


from core.constants import *
from core.generics import *
from core.utils import *


class GenomeGenerations:

    def generate_genome(self) -> Iterable[Genome]:
        return [randint(0, 1) for _ in range(GENOME_SIZE)]


class PopulationGenerations:

    def generate_population(self) -> \
            Iterable[Population]:
        return [GenomeGenerations().generate_genome()
            for _ in range(POPULATION_SIZE)]

    # @staticmethod
    # def one_max_value(individual: Genome) -> FitnessSingle:
    #     return sum(individual),

    # @staticmethod
    # def fitness_max(population: Population) -> FitnessScore:
    #     return list(map(one_max_value, population))



class Utilities:

    # def make_fitness_values(self, individuals: Any) -> \
    #     Tuple[int]:
    #     return sum(individuals),

    def crossover_point(self, child1: Genome, child2: Genome) -> \
        Tuple[Genome, Genome]:

        size = min(len(child1), len(child2))
        check_point = randint(1, size - 1)
        child1[check_point:], child2[check_point:] = \
            child2[check_point:], child1[check_point:]

        return child1, child2



def main():

    log.progress("[*] initializing algorithm...")

    log.info("[*] setting the initial parameters...")
    max_fitness_values = list()
    mean_fitness_values = list()
    generation_counter = 0

    try:

        population = PopulationGenerations().generate_population()
        # sleep(10)
        # print(population)
        best_fitness = fintess_max_score(population)
        print(best_fitness)
        while generation_counter < MAX_NUM_GEN:
            generation_counter += 1
            continue
        # print(population[::2])
        # print(len(population[::2]))

        # print(population[1::2])
        # print(len(population[1::2]))

        log.success("[*] Process done successfully")
    except Exception as e:
        log.error(f"Error by: {str(e)}")
        exit(1)
    except KeyboardInterrupt:
        log.warn("[*] Exiting...")
        sleep(2)
        exit(1)

if __name__ == "__main__":
    main()
