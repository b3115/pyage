# coding=utf-8
import os
import sys

__author__ = 'Michał Ciołczyk'

# Parameters

emas = [False]
mutation_prob = [0.01, 0.03, 0.1]
mutation_func = [0, 1]

generate = False
filename = ""

proc_base = "python -m pyage.core.bootstrap pyage.SAT_CNF.SAT_conf DEBUG "

# Main routine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python run.py <filename-with-cities>"
        exit(1)
    filename = sys.argv[1]
    for e in emas:
        for pr in mutation_prob:

            args = ('1' if e else '0') + " " + str(pr) + " 1 " + filename
            print "Executing: " + proc_base + args + "..."
            os.system(proc_base + args)
    print "Done"