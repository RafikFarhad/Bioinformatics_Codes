
def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])
    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    ans = Hamming(inp[1], inp[0])

    output = str(ans)

    print(output)

    # Write the output.
    outfile.write(output)