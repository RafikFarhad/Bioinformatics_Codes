import itertools

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

def FrequencyArray(Dna, mer):
    ans = []
    L= 'ACGT'
    perms = itertools.product(L, repeat=mer)
    all_str = []
    for k in perms:
        all_str.append(''.join(k))
    sorted(all_str)
    for pat in all_str:
        print(pat)
        ans.append(Count(Dna, pat))
    return ans


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = FrequencyArray(inp[0], int(inp[1]))
    
    output = ' '.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)