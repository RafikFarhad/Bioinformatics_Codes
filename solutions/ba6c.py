import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def prettyGenome(arr):
    return '(' + ' '.join('{0:+d}'.format(_) for _ in arr) + ')'

def BreakPoints(genome):
    genome = [0] + genome + [len(genome)+1]
    ans = 0
    for i in range(len(genome)-1):
        if genome[i] != genome[i+1] - 1:
            ans+=1
    return [ans]
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = BreakPoints([int(a) for a in inp[0][1:-1].split(' ')])
    output = '\n'.join(str(_) for _ in output)
    print(output)
    
    # Write the output.
    outfile.write(output)