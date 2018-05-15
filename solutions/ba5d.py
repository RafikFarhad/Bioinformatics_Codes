import itertools
import random
import networkx as nx
import sys

def dagLongestPath(src, sink, mat):
    G = nx.DiGraph()
    G.add_weighted_edges_from(mat)
    print( G.number_of_edges())
    return nx.dag_longest_path_length(G), nx.dag_longest_path(G)

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    src = inp[0]
    sink = inp[1]
    temp = [ [i for i in x.split('->')] for x in inp[2:] ]
    mat = []
    for a in temp:
        b = a[1].split(':')
        mat += [(int(a[0]),int(b[0]),int(b[1]))]
    ans = dagLongestPath(src, sink, mat)
    output = str(ans[0]) + "\n" + '->'.join(str(a) for a in ans[1])
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)