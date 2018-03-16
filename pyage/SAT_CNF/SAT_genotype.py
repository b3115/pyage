# coding=utf-8
import random


class SATGenotype(object):
    def __init__(self, clauses, variables):
        self.clauses = clauses
        self.n = len(variables)
        self.list = [False if random.random() < 0.5 else True for _ in range(0, 4)]
        self.fitness = self.calculate_fitness()

    def __str__(self):
        return "SATGenotype{list=" + str(self.list) + ", fitness=" + str(self.fitness) + "}"

    def calculate_fitness(self):
        fitness = 0
        for clause in self.clauses:
            clause_satisfied = 0
            for variable_id, is_variable_negative in clause:
                if self.list[variable_id] == is_variable_negative:
                    clause_satisfied = 1
            fitness += clause_satisfied
        return fitness

    def set_list(self, list):
        self.list = list[:]
        self.fitness = self.calculate_fitness()
