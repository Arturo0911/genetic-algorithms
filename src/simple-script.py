#!/usr/bin/python3

import time
from random import (
    randint,
    seed
)


seed(44)


def generate_genome():

    return [randint(0, 1) for _ in range(100)]


def generate_population():
    return [generate_genome() for _ in range(100)]


def fitness_values(genome):
    return sum(genome)




def make_implementation():

    now = time.time()

    population = generate_population()
    generation_counter = 0
    best_fitness = list(map(fitness_values, population))
    max_vals = []
    print(best_fitness)
    while generation_counter < 100 and max(best_fitness) < 100:

        generation_counter += 1
        max_vals.append(max(best_fitness))

    print(max_vals)
    print(f"The time to make this execution was: {time.time() - now}")


make_implementation()