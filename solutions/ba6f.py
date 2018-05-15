import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def prettyGenome(arr):
    return '(' + ' '.join('{0:+d}'.format(_) for _ in arr) + ')'

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

    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = ChromosomeToCycle([int(a) for a in inp[0][1:-1].split(' ')])
    output = '(' + ' '.join(str(_) for _ in output) + ')'
    print(output)
    
    # Write the output.
    outfile.write(output)