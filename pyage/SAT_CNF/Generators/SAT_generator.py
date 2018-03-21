import random
import sys

# from pyage.SAT_CNF.SAT_clause_util import check_satisfiability, is_clause_satisfied

def check_satisfiability(clauses, variables):

    for clause in clauses:
        if not is_clause_satisfied(clause,variables):
            print("not satisfied for clause: ",clause)


def is_clause_satisfied(clause, variables):
    satisfied = False
    for variable_id, variable_value in clause.iteritems():
        if (variable_value == variables[variable_id]):
            satisfied = True
    if not satisfied:
        return False
    else:
        return True

args = sys.argv
variables_count = 10
clauses_count = 20
if len(args) > 1:
    variables_count = int(args[1])
if len(args) > 2:
    clauses_count = int(args[2])
print(variables_count)
variables = [True if random.random() < 0.5 else False for _ in range(variables_count)]
clauses = []
for i in range(clauses_count):
    variables_in_clause_count = random.randrange(2, 5)
    clause = {}
    for j in range(variables_in_clause_count):
        random_variable_id = random.randrange(0, variables_count)
        while random_variable_id in clause:
            random_variable_id = random.randrange(0, variables_count)
        clause[random_variable_id] = True if random.random() < 0.5 else False
    if not is_clause_satisfied(clause, variables):
        variable_id_to_be_changed = random.choice(list(clause))
        clause[variable_id_to_be_changed] = not clause[variable_id_to_be_changed]
    clauses.append(clause)
for clause in clauses:
    output_str = ''
    for variable_id, variable_value in clause.iteritems():
        if not variable_value:
            output_str += '!'
        output_str += str(variable_id)
        output_str += ','
    print(output_str[:-1])
check_satisfiability(clauses, variables)