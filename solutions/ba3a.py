import itertools

def getComposition(k, dna):
    return sorted([ dna[i:i+k] for i in range(len(dna)-k+1) ])

    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = getComposition(int(inp[0]), inp[1])
    print(output)
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)