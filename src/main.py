"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""

from pprint import pprint
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from random import (
    randint,
    seed)
from pwn import *


from core.constants import *
from core.generics import *
from core.utils import *


from core.errors.genetic_exceptions import (
    FitnessValueComparisonException,
    GenomeCreatorException,
    PopulationCretorException
)

seed(42)


class GenomeGenerations:

    def generate_genome(self, genome_size: int) -> Iterable[Genome]:

        if genome_size is None or genome_size <= 0:
            raise GenomeCreatorException
        return [randint(0, 1) for _ in range(genome_size)]


class PopulationGenerations:

    def generate_population(self) -> \
            Iterable[Population]:
        return [GenomeGenerations().generate_genome(genome_size=GENOME_SIZE)
                for _ in range(POPULATION_SIZE)]


def main():

    log.progress("[*] initializing algorithm...")

    log.info("[*] initializing statistics accumulators...")
    max_fitness_values = list()
    mean_fitness_values = list()
    generation_counter = 0

    try:

        population = PopulationGenerations().generate_population()
        best_fitness = fintess_max_score(population)
        print(max(best_fitness)[0])
        print(max(best_fitness)[0] == 61)
        while max(best_fitness)[0] < ONE_MAX_LENGTH and \
                generation_counter < MAX_NUM_GEN:
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
