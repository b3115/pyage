# coding=utf-8

from pyage.SAT_CNF.SAT_genotype import SATGenotype
from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.core.operator import Operator




class EmasInitializer(object):
    def __init__(self, filename, energy, size):
        self.clauses, self.variables= EmasInitializer.get_clauses_from_file(filename)
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(SATGenotype(self.clauses, self.variables), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents

    @staticmethod
    def get_clauses_from_file(filename):
        clauses = []
        with open(filename, "r") as input:
            variables_count = int(input.readline())
            variables = [i for i in range(variables_count)]
            for line in input:
                clause_variables_raw = line.strip().split(",")
                clause_variables = {}
                for variable in clause_variables_raw:
                    if variable[0] == '!':
                        variable_value=False
                        variable_id=int(variable[1:])
                    else:
                        variable_value = True
                        variable_id=int(variable)
                    if variable_id not in variables:
                        variables.append(variable_id)
                    clause_variables[variable_id] = variable_value
                clauses.append(clause_variables)
        return clauses, variables


class SATInitializer(Operator):
    def __init__(self, population_size=1000, filename=None):
        super(SATInitializer, self).__init__(SATGenotype)
        self.size = population_size
        if filename:
            self.clauses, self.variables = EmasInitializer.get_clauses_from_file(filename)
            self.population = self.generate_population(population_size, self.clauses, self.variables)

    def __call__(self, *args, **kwargs):
        return self.population

    def process(self, population):
        for i in range(self.size):
            population.append(self.population[i])

    def generate_population(self, number_of_genotypes, clauses, variables):
        return [SATGenotype(clauses, variables) for _ in xrange(0, number_of_genotypes)]

def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory