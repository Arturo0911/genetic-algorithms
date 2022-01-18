"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""

from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from typing import (
    Any,
    List,
    Iterable,
    Tuple
)
from pwn import *

GENOME_SIZE = 100
POPULATION_SIZE = 200
CROSS_PROB = 0.9
MUT_PROB = 0.1
MAX_NUM_GEN = 50


Genome = List[int]


class GenomeGenerations:
    def __init__(self):
        pass
    def generate_genome(self) -> Iterable[Genome]:
        return [randint(0, 1) for _ in range(GENOME_SIZE)]



class PopulationGenerations:
    def __init__(self):
        pass

    def generate_population(self) -> \
            Iterable[List[GenomeGenerations.generate_genome]]:
        return [GenomeGenerations().generate_genome() 
            for _ in range(POPULATION_SIZE)]



class Utilities:

    def make_fitness_values(self, individuals: Any) -> \
        Tuple[int]:
        return sum(individuals), 

    def crossover_point(self, child1: Genome, child2: Genome) -> \
        Tuple[Genome, Genome]:

        size = min(len(child1), len(child2))
        check_point = randint(1, size - 1)
        child1[check_point:], child2[check_point:] = \
            child2[check_point:], child1[check_point:]
        
        return child1, child2

def get_one_max(individuals) -> Tuple[int]:
    return sum(individuals), 


def fitness_values():
    pass


def main():
    
    log.progress("[*] initializing algorithm...")

    log.info("[*] setting the initial settings...")
    max_fitness_values = list()
    mean_fitness_values = list()
    generation_counter = 0

    try:

        population = PopulationGenerations().generate_population()
        sleep(10)

        while generation_counter < MAX_NUM_GEN:
            generation_counter += 1
            continue
        # print(population[::2])
        # print(len(population[::2]))

        # print(population[1::2])
        # print(len(population[1::2]))
    
    except Exception as e:
        log.error(f"Error by: {str(e)}")
        exit(1)
    
    except KeyboardInterrupt:
        log.warn("[*] Exiting...")
        exit(1)

if __name__ == "__main__":
    main()
