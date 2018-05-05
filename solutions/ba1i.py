def Hamming(Dna, Pat):
    return len([i for (i, j) in zip(Dna, Pat) if i!=j])
    
def Kamla(Dna, Pat, d):
    arr = []
    i = 0
    for i in range(len(Dna) - len(Pat) + 1):
        k = Hamming(Pat, Dna[i:i+len(Pat)])
        if k<=d:
            arr.append(i)
    return len(arr)

def Best(Text, mer, d):
    cur = 0
    res = {}
    for i in range(len(Text)-mer+1):
        a = Kamla(Text, Text[i:i+mer], d)
        res[Text[i:i+mer]] = a
    ans = []
    for r in res.keys():
        if r=='GCACACAGAC':
            print(r, res[r])
        if res[r] > cur:
            ans = [r]
            cur = res[r]
        elif res[r]==cur:
            ans.append(r)
    return ans


# print(Count('CGATATATCCATAG ', 'ATA'))

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = Best(inp[0], int(inp[1].split(' ')[0]), int(inp[1].split(' ')[1]))
    
    # output = ' '.join(output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)