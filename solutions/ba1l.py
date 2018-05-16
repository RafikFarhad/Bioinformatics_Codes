import itertools


def PatternToNumber(Dna):
    digit = []
    for i in Dna:
        k = 0
        if i=='A':
            k = 0
        elif i=='C':
            k = 1
        elif i=='G':
            k = 2
        elif i=='T':
            k = 3
        digit.append(k)
    ans = 0
    for i in digit:
        ans = ans*4 + i
    return [ans]
def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    output = PatternToNumber(inp[0])
    
    output = ' '.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)