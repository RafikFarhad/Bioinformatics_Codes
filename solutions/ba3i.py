import itertools
import random

def kUniversal(graph):
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = kUniversal(int(inp[0]))
    print(output)
    output = '->'.join(str(a) for a in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)