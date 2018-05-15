import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def ChromosomeToCycle(genome):
    res = []
    for i in genome:
        if i<0:
            j = -i
            res.append(2*j)
            res.append(2*j-1)
        else:
            
            res.append(2*i-1)
            res.append(2*i)
    return res

def ColoredEdges(arr):
    res = []
    for block in arr:
        cycle = ChromosomeToCycle(block)
        for i in range(1, len(cycle)-1, 2):
            res.append([cycle[i], cycle[i+1]])
        res.append([cycle[len(cycle)-1], cycle[0]])
    return res

    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    inp = [ [int(p) for p in a.split(' ')] for a in inp[0][1:-1].split(')(')]
    output = ColoredEdges(inp)
    output = ', '.join(['(' + str(a[0]) + ', ' + str(a[1]) + ')' for a in output])
    print(output)
    
    # Write the output.
    outfile.write(output)