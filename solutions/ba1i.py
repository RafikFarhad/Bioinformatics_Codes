import itertools

def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])
    
def Occurance(Dna, Pat, d):
    arr = []
    i = 0
    for i in range(len(Dna) - len(Pat) + 1):
        k = Hamming(Pat, Dna[i:i+len(Pat)])
        if k<=d:
            arr.append(i)
    return len(arr)

def MostFrequentWords(Text, mer, d):
    res = {}
    L= 'ACGT'
    cur = 0
    perms = itertools.product(L, repeat=mer)
    for k in perms:
        pat = ''.join(k)
        res[pat] = Occurance(Text, pat, d)
        cur = max(res[pat], cur)
    ans = []

    for r in res.keys():
        if res[r]==cur:
            ans.append(r)
    return ans


# print(Count('CGATATATCCATAG ', 'ATA'))

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = MostFrequentWords(inp[0], int(inp[1].split(' ')[0]), int(inp[1].split(' ')[1]))
    
    output = ' '.join(output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)