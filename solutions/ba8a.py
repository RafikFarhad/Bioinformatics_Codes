import itertools
import random
import networkx as nx
import sys

def Distance(a, b):
    a = [ (p-q)**2 for (p,q) in zip(a,b) ]
    return sum(a)**.5

def FarthestFirstTraversal(k, m, data):
    centers = [data[0]]
    while len(centers) < k:
        m = -1
        c = -1
        for (i, a) in enumerate(data):
            n = 1000000
            for b in centers:
                n = min(n, Distance(b, a))
            if n>m:
                m = n
                c = i
        centers.append(data[c])
    return centers

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    mat = []
    for a in inp[1:]:
        b = a.split(' ')
        mat.append([float(_) for _ in b if _!=''])
    ans = FarthestFirstTraversal(int(inp[0].split(' ')[0]), int(inp[0].split(' ')[1]), mat)
    output = '\n'.join([' '.join([str(_) for _ in a]) for a in ans])
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)