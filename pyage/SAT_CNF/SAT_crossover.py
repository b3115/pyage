# coding=utf-8
import logging
import random

from pyage.SAT_CNF.SAT_genotype import SATGenotype
from pyage.core.operator import Operator



logger = logging.getLogger(__name__)


class AbstractCrossover(Operator):
    def __init__(self, type=SATGenotype, size=20):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)


class SATCrossover(AbstractCrossover):
    def __init__(self, size):
        super(SATCrossover, self).__init__(SATGenotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing: " + str(p1) + " and " + str(p2))

        new_genotype_list = p1.list[:]

        for variable_index in range(len(new_genotype_list)):
            if random.random() < 0.5:
                new_genotype_list[variable_index] = p2.list[variable_index]

        genotype = SATGenotype(p1.clauses, p1.variables)
        genotype.set_list(new_genotype_list)

        logger.debug("Crossed genotype: " + str(genotype))

        return genotype