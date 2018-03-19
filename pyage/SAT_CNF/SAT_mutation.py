# coding=utf-8
import logging
import random

from pyage.SAT_CNF.SAT_genotype import SATGenotype
from pyage.core.operator import Operator



logger = logging.getLogger(__name__)


class AbstractMutation(Operator):
    def __init__(self, type=SATGenotype, probability=0.5):
        super(AbstractMutation, self).__init__(type)
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)


class SATMutation(AbstractMutation):
    def __init__(self, probability):
        super(SATMutation, self).__init__(SATGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (rand swap) genotype: " + str(genotype))

        l = genotype.list[:]
        random_index = l[random.randrange(0, len(l))]
        l[random_index] = not l[random_index]
        gen = SATGenotype(genotype.clauses, genotype.variables)
        gen.set_list(l)

        logger.debug("Mutated (rand swap) genotype: " + str(gen))

        return gen

class SATMutation2(AbstractMutation):
    def __init__(self, probability):
        super(SATMutation2, self).__init__(SATGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (rand swap) genotype: " + str(genotype))

        l = genotype.list[:]
        for clause in genotype.clauses:
            clause_satisfied = False
            for variable_id, value in clause.iteritems():
                if l[variable_id]==value:
                    clause_satisfied=True
            if not clause_satisfied:
                random_variable = random.choice( list(clause))
                l[random_variable] = not l[random_variable]
                break
        gen = SATGenotype(genotype.clauses, genotype.variables)
        gen.set_list(l)

        logger.debug("Mutated 2 (rand swap) genotype: " + str(gen))

        return gen
