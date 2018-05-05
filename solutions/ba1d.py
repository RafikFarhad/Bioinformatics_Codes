
def Kamla(Dna, Pat):
    arr = []
    i = 0
    while(True):
        i = Dna.find(Pat, i)
        if i==-1:
            break
        arr.append(i)
        i+=1
    return arr
    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    ans = Kamla(inp[1], inp[0])

    output = ' '.join([str(i) for i in ans])

    print(output)

    # Write the output.
    outfile.write(output)