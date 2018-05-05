def Count(Text, Pattern):
    i = 0
    res = 0
    while(True):
        i = Text.find(Pattern, i)
        if i != -1:
            res+=1
        else:
            break
        i+=1
    return res

def Best(Text, mer, t):
    cur = 0
    res = {}
    for i in range(len(Text)-mer+1):
        a = Count(Text, Text[i:i+mer])
        res[Text[i:i+mer]] = a
    ans = []
    for r in res.keys():
        if res[r] >= t:
            ans.append(r)
    return ans

def Kamla(Dna, k, L, t):
    res = []
    for i in range(len(Dna) + L - 1):
        res += Best(Dna[i:i+L], k, t)
    return res;

# print(Count('CGATATATCCATAG ', 'ATA'))

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    k = int(inp[1].split(' ')[0])
    L = int(inp[1].split(' ')[1])
    t = int(inp[1].split(' ')[2])

    ans = Kamla(inp[0], k, L, t)

    output = ' '.join(set(ans))

    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)