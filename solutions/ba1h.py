def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])
    
def Kamla(Dna, Pat, d):
    arr = []
    i = 0
    for i in range(len(Dna) - len(Pat) + 1):
        k = Hamming(Pat, Dna[i:i+len(Pat)])
        if k<=d:
            arr.append(i)
    return arr
    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    ans = Kamla(inp[1], inp[0], int(inp[2]))

    output = ' '.join([str(i) for i in ans])

    print(output)

    # Write the output.
    outfile.write(output)