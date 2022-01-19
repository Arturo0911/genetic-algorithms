"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""
import seaborn as sns
from pprint import pprint
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from random import (
    randint,
    seed)
from pwn import *
import random

from core.constants import *
from core.generics import *
from core.utils import *


from core.errors.genetic_exceptions import (
    FitnessValueComparisonException,
    GenomeCreatorException,
    PopulationCretorException
)

seed(42)


def banner():

    print("""
    :'######:::'########:'##::: ##:'########:'########:'####::'######::
    '##... ##:: ##.....:: ###:: ##: ##.....::... ##..::. ##::'##... ##:
     ##:::..::: ##::::::: ####: ##: ##:::::::::: ##::::: ##:: ##:::..::
     ##::'####: ######::: ## ## ##: ######:::::: ##::::: ##:: ##:::::::
     ##::: ##:: ##...:::: ##. ####: ##...::::::: ##::::: ##:: ##:::::::
     ##::: ##:: ##::::::: ##:. ###: ##:::::::::: ##::::: ##:: ##::: ##:
    . ######::: ########: ##::. ##: ########:::: ##::::'####:. ######::
    :......::::........::..::::..::........:::::..:::::....:::......:::

    :::'###::::'##::::::::'######::::'#######::'########::'####:'########:'##::::'##:'##::::'##:
    ::'## ##::: ##:::::::'##... ##::'##.... ##: ##.... ##:. ##::... ##..:: ##:::: ##: ###::'###:
    :'##:. ##:: ##::::::: ##:::..::: ##:::: ##: ##:::: ##:: ##::::: ##:::: ##:::: ##: ####'####:
    '##:::. ##: ##::::::: ##::'####: ##:::: ##: ########::: ##::::: ##:::: #########: ## ### ##:
     #########: ##::::::: ##::: ##:: ##:::: ##: ##.. ##:::: ##::::: ##:::: ##.... ##: ##. #: ##:
     ##.... ##: ##::::::: ##::: ##:: ##:::: ##: ##::. ##::: ##::::: ##:::: ##:::: ##: ##:.:: ##:
     ##:::: ##: ########:. ######:::. #######:: ##:::. ##:'####:::: ##:::: ##:::: ##: ##:::: ##:
    ..:::::..::........:::......:::::.......:::..:::::..::....:::::..:::::..:::::..::..:::::..::

    authors:
        Arturo Negreiros
        José Hernández
        Anthony Pin
        Ricardo Solorzano
    """)


class GenomeGenerations:

    def __init__(self):
        self.fitness_score = None

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
    banner()
    log.progress("[*] initializing algorithm...")

    log.info("[*] initializing statistics accumulators...")
    max_fitness_values = list()
    mean_fitness_values = list()
    generation_counter = 0
    genetic_object = None

    try:

        population = PopulationGenerations().generate_population()
        new_population = population
        best_fitness = fintess_max_score(population)
        best_fitness = [fit[0] for fit in best_fitness]
        genetic_object = {pos+1: {"genome": ind, "fitness": sum(ind)}
                          for pos, ind in enumerate(population)}
        fitness = [genetic_object[x]["fitness"] for x in genetic_object]
        log.info("calculating new best_fitness....")
        while max(best_fitness) < ONE_MAX_LENGTH and \
                generation_counter < MAX_NUM_GEN:
            generation_counter += 1

            offspring = implement_offsprings(individuals=population, size=3)
            clone = offspring
            # print(clone)
            another = genetic_object
            for i, (child1, child2) in enumerate(zip(offspring[::2],
                                      offspring[1::2])):
                if random.random() < CROSS_PROB:
                    pos_1 = check_genom_object_pos(genetic_object, child1)
                    pos_2 = check_genom_object_pos(genetic_object, child2)
                    child_1, child_2 = make_crossover_child(child1, child2)
                    genetic_object[pos_1]["fitness"] = sum(child1)
                    genetic_object[pos_2]["fitness"] = sum(child2)

                    offspring[::2][i] = child1
                    offspring[1::2][i] = child2
            
            best_fitness_ = [genetic_object[x]["fitness"] for x in genetic_object]

            for i, mutant in enumerate(offspring):
                if random.random() < MUT_PROB:
                    new_mutant = mutation(mutant, 0.001)
                    pos = check_genom_object_pos(genetic_object, mutant)
                    genetic_object[pos]["fitness"] = sum(new_mutant[0])
                    offspring[i] = new_mutant[0]

            population = offspring

            best_fitness_ = [fit[0] for fit in fintess_max_score(population)]

            max_fitness_values.append(max(best_fitness_))
            mean_fitness_values.append((sum(best_fitness_)/len(population)))
            

        log.success("[*] initializing the plotting successfully")
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 12))
        plt.plot(max_fitness_values, color='red')
        plt.plot(mean_fitness_values, color='green')
        plt.xlabel('Generación')
        plt.ylabel('Máximo / Media puntaje')
        plt.title('Máximo y media del puntaje y generaciones')
        plt.show()
        print(max_fitness_values)
    except Exception as e:
        log.error(f"Error by: {str(e)}")
        exit(1)
    except KeyboardInterrupt:
        log.warn("[*] Exiting...")
        sleep(1)
        exit(1)


if __name__ == "__main__":
    main()
