"""
First implementation from scratch of the
genetic algorithm

@author Arturo Negreiros (AKA H0n3yL0xd)
"""


class GenomeCreatorException(Exception):

    def __init__(self, message: str=
                """The size of the genome can't be Null or be
                under the limit alowed"""):
        self.message = message
        super().__init__(self.message)


class PopulationCretorException(Exception):
    def __init__(self, message: str=
                """The size of the population can't be Null or
                be under the limit alowed"""):
        self.message = message
        super().__init__(self.message)


class FitnessValueComparisonException(Exception):
    def __init__(self, message: str= 
                """The quantity of elements insied the Fitness score
                can't be different of the size of the Population"""):
        
        self.message = message
        super().__init__(self.message)