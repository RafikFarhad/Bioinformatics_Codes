import itertools
import random
import networkx as nx
import sys

def Distance(a, b):
    a = [ (p-q)**2 for (p,q) in zip(a,b) ]
    return sum(a)**.5

def SquaredErrorDistortion(k, m, centers, data):
    ans = 0
    for a in data:
        k = 14000000
        for b in centers:
            k = min(k, Distance(a, b))
        ans += k**2
    ans /= len(data)
    return '{0:.3f}'.format(ans)

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    k,m = int(inp[0].split(' ')[0]), int(inp[0].split(' ')[1])
    mat = []
    for a in inp[1:k+1]:
        b = a.split(' ')
        mat.append([float(_) for _ in b if _!=''])
    ans = SquaredErrorDistortion(k, m, mat, [[float(_) for _ in b.split(' ') if _!=''] for b in inp[k+2:] ])
    output = str(ans)
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)