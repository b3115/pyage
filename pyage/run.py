# coding=utf-8
import os
import sys

__author__ = 'Albert Mosiałek'

# Parameters

emas = [True]
# mutation_prob = [0.01, 0.03, 0.1]
mutation_prob = [0.1, 0.25, 0.5]
mutation_func = [0, 1]

generate = False
filename = ""

proc_base = "python -m pyage.core.bootstrap pyage.SAT_CNF.SAT_conf DEBUG "

# Main routine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "pass names of file with generated SAT-CNF as arguments"
        exit(1)
    filenames = sys.argv[1:]
    for filename in filenames:
        for e in emas:
            for pr in range(20):
                for f in mutation_func:
                    args = ('1' if e else '0') + " " + str(pr/20.0) + " "+ str(f) +" " + filename
                    print "Executing: " + proc_base + args + "..."
                    os.system(proc_base + args)
    print "Done"