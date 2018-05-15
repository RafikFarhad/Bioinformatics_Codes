import itertools
import random
import sys

def dagLongestPath(src, sink, mat):
    return [5];

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    src = inp[0]
    sink = inp[1]
    temp = [ [i for i in x.split('->')] for x in inp[2:] ]
    mat = {}
    for a in temp:
        mat[int(a[0])] = {}

    for a in temp:
        b = a[1].split(':')
        mat[int(a[0])][int(b[0])] = int(b[1])
    output = mat
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)