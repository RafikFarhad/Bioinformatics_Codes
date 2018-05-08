import itertools

def reconstructComposition(all_dna):
    return ''.join(a[0] for a in all_dna[:-1]) + all_dna[-1]

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = reconstructComposition(inp)
    print(output)
    output = ''.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)