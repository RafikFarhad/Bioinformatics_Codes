import itertools
import random
import networkx as nx
import sys

def distanceBetweenTwoLeaves(n, mat):
    G = nx.Graph()
    G.add_weighted_edges_from(mat)
    leaves = [x for x in G.nodes() if G.degree(x)==1]
    ans = nx.floyd_warshall(G)
    res = []
    for leaf1 in leaves:
        a = []
        for leaf2 in leaves:
            a.append(ans[leaf1][leaf2])
        res.append(a)
    return res

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    temp = [ [i for i in x.split('->')] for x in inp[1:] ]
    mat = []
    for a in temp:
        b = a[1].split(':')
        mat += [(int(a[0]),int(b[0]),int(b[1]))]
    ans = distanceBetweenTwoLeaves(inp[0], mat)
    output = ''
    for a in ans:
        for b in range(len(a)-1):
            output += '{0:<3s} '.format(str(a[b]))
        output += str(a[-1])
        output += '\n'
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)