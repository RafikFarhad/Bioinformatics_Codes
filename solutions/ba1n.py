import itertools

def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])

def Neighborhood(Dna, d):
    ans = []
    L= 'ACGT'
    perms = itertools.product(L, repeat=len(Dna))
    all_str = []
    for k in perms:
        all_str.append(''.join(k))
    for a in all_str:
        if Hamming(Dna, a) <= d:
            ans.append(a)
    return ans

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = Neighborhood((inp[0]), int(inp[1]))
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)