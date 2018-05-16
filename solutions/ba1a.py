# ba1a

def Appears(Text, Pattern):
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

# print(Count('CGATATATCCATAG ', 'ATA'))

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = str(Appears(inp[0], inp[1]))

    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)