import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def prettyGenome(arr):
    return '(' + ' '.join('{0:+d}'.format(_) for _ in arr) + ')'

def GreedySorting(genome):
    length = len(genome)
    res = []
    for i in range(1, length+1):
        try:
            pos = genome.index(i)
        except:
            pos = genome.index(-i)
        if pos==i-1 and genome[pos] > 0:
            continue
        if i==1:
            part = genome[pos::-1]
        else:
            part = genome[pos:i-2:-1]
        part = [-_ for _ in part]
        genome[i-1:pos+1] = part
        res.append(prettyGenome(genome))
        if genome[i-1] < 0:
            genome[i-1] *= -1
            res.append(prettyGenome(genome))
    return res
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = GreedySorting([int(a) for a in inp[0][1:-1].split(' ')])
    output = '\n'.join(output)
    print(output)
    
    # Write the output.
    outfile.write(output)