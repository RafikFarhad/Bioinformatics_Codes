import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def prettyGenome(arr):
    return '(' + ' '.join('{0:+d}'.format(_) for _ in arr) + ')'

def CycleToChromosome(arr):
    res = []
    for i in range(0, len(arr), 2):
        if arr[i] < arr[i+1]:
            res.append(int((arr[i+1])/2))
        else:
            res.append(int(-arr[i]/2))
    return res
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output =  CycleToChromosome([int(a) for a in inp[0][1:-1].split(' ')])
    output = prettyGenome(output)
    print(output)
    
    # Write the output.
    outfile.write(output)