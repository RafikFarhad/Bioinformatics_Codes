
def Kamla(Dna, Pat):

    return [i for (i, j) in zip(Dna, Pat) if i!=j]
    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    ans = Kamla(inp[1], inp[0])

    output = str(len(ans))

    print(output)

    # Write the output.
    outfile.write(output)