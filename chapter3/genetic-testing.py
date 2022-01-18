"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""

import numpy as np
from random import randint
from typing import (
    Any,
    List,
    Iterable
)
from pwn import *


Genome = List[int]


class GenomeGenerations:

    GENOME_SIZE = 100
    def __init__(self):
        pass

    def generate_genome(self) -> Iterable[Genome]:
        return [randint(0, 1) for _ in range(GENOME_SIZE)]



class PopulationGenerations:

    POPULATION_SIZE = 200

    def __init__(self):
        pass

    def generate_population(self) -> \
            Iterable[List[GenomeGenerations.generate_genome]]:
        return


def generate_genome(size_genome: int) -> Iterable[Genome]:
    return [randint(0, 1) for _ in range(size_genome)]



def main():
    # print(type(generate_genome(10)))

    new_genome = GenomeGenerations()
    print(new_genome.GENOME_SIZE)



if __name__ == "__main__":
    main()
