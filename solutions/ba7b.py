import itertools
import random
import networkx as nx
import sys

def LimbLengthsinaTree(n, j, mat):
    ll = 1000000
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            if i!=j and j!=k and i!=k:
                ll = min(ll, (mat[i][j] + mat[j][k] - mat[i][k])/2)
    return ll

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    mat = []
    for a in inp[2:]:
        b = a.split(' ')
        mat.append([int(_) for _ in b if _!=''])
    ans = LimbLengthsinaTree(int(inp[0]), int(inp[1]), mat)
    output = str(ans)
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)