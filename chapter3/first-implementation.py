

from deap import creator


class Developer(Employee):
    position = "Developer"

    def __init__(self):
        self.programmingLanguages = set()





creator.create('Developer', Employee, position='Developer', programmingLanguages=set)

