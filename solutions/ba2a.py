import itertools

def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])

def GetAllString(mer):
    res = {}
    L= 'ACGT'
    perms = itertools.product(L, repeat=mer)
    all_str = []
    for k in perms:
        all_str.append(''.join(k))
    return all_str

def GetTotal(Dna, Pat, d):
    arr = []
    i = 0
    for i in range(len(Dna) - len(Pat) + 1):
        k = Hamming(Pat, Dna[i:i+len(Pat)])
        if k<=d:
            arr.append(i)
    return len(arr)


def MotifEnumeration(k, d, all_dna):
    cur = 0
    res = {}
    ans = []
    L= 'ACGT'
    perms = GetAllString(k)
    for a in perms:
        b = True
        for Dna in all_dna:
            if GetTotal(Dna, a, d) > 0:
                b = b & True
            else:
                b = False
                break
        if b == True:
            ans.append(a)
    return ans

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = MotifEnumeration(int(inp[0].split()[0]), int(inp[0].split()[1]), inp[1:])
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)