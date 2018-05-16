import itertools

def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])

def GetAllString(mer):
    L= 'ACGT'
    perms = itertools.product(L, repeat=mer)
    all_str = []
    for k in perms:
        all_str.append(''.join(k))
    return all_str

def GetTotal(Dna, Pat):
    ans = 10000000

    for i in range(len(Dna) - len(Pat) + 1):
        k = Hamming(Pat, Dna[i:i+len(Pat)])
        ans = min(ans, k)
    return ans


def MedianString(k, all_dna):
    ans = []
    x = 1000000000
    perms = GetAllString(k)
    for a in perms:
        b = 0
        for Dna in all_dna:
            b += GetTotal(Dna, a)
        # print(a, b)

        if x>=b:
            x = b
            ans = [a]
    return ans

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = MedianString(int(inp[0].split()[0]), inp[0:])
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)