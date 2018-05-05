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

def Best(Text, mer):
    cur = 0
    res = {}
    for i in range(len(Text)-mer+1):
        a = Count(Text, Text[i:i+mer])
        res[Text[i:i+mer]] = a
    ans = []
    for r in res.keys():
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
    output = Best(inp[0], int(inp[1]))
    output = ' '.join(output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)