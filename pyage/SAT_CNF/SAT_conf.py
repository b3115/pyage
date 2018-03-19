# coding=utf-8
import logging
import sys

from pyage.SAT_CNF.SAT_crossover import SATCrossover
from pyage.SAT_CNF.SAT_eval import SATEvaluator
from pyage.SAT_CNF.SAT_init import SATInitializer, root_agents_factory, EmasInitializer
from pyage.SAT_CNF.SAT_mutation import SATMutation2
from pyage.SAT_CNF.SAT_naming_service import NamingService
from pyage.SAT_CNF.SAT_selection import TournamentSelection
from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

logger = logging.getLogger(__name__)


def parse_args():
    args = sys.argv

    if len(args) < 6:
        raise ValueError("Not enough parameters!")

    emas = args[3] == '1'
    logger.debug("Emas: " + str(emas))

    prob = float(args[4])
    logger.debug("Probability: " + str(prob))

    func = int(args[5])
    logger.debug("Mutation: " + str(func))

    filename = args[6]

    return [emas, prob, func, filename]


args = parse_args()
use_emas = args[0]
mutation_prob = args[1]
mutation_func = args[2]
filename = args[3]

agents_count = 10

if use_emas:
    logger.debug("EMAS, %s agents", agents_count)
    agents = root_agents_factory(agents_count, AggregateAgent)
else:
    logger.debug("EVO, %s agents", agents_count)
    agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(100)

if not use_emas:
    size = 130

    population_size = 10000
    operators = lambda: [SATEvaluator(), TournamentSelection(size=125, tournament_size=125),
                         SATCrossover(size=size),
                         SATMutation2(probability=mutation_prob)]
    initializer = lambda: SATInitializer(population_size=population_size, filename=filename)

else:
    agg_size = 40
    aggregated_agents = EmasInitializer(filename=filename, size=agg_size, energy=40)

    emas = EmasService

    minimal_energy = lambda: 10
    reproduction_minimum = lambda: 100
    migration_minimum = lambda: 120
    newborn_energy = lambda: 200
    transferred_energy = lambda: 40

    budget = 0
    evaluation = lambda: SATEvaluator()
    crossover = lambda: SATCrossover(size=30)
    mutation = lambda: SATMutation2(probability=mutation_prob)

    def simple_cost_func(x):
        return abs(x) * 10

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=1)