# coding=utf-8
import logging

from pyage.SAT_CNF.SAT_genotype import SATGenotype
from pyage.core.operator import Operator



logger = logging.getLogger(__name__)


class SATEvaluator(Operator):
    def __init__(self):
        super(SATEvaluator, self).__init__(SATGenotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        return genotype.calculate_fitness()