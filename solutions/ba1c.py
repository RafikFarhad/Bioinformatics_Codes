
def Reverse(Dna):
    tt = {
        'A' : 'T',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G',
    }
    ans = ''
    for a in Dna:
        ans += tt[a]
    return ans[::-1]

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = str(Reverse(inp[0]))

    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)