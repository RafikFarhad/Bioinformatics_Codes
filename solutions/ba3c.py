import itertools

def overlapGraph(all_dna):
    ans = []
    for a in all_dna:
        b = a[1:]
        c = ''
        for k in all_dna:
            if b == k[:-1]:
                c = k
                break
        if c != '':
            ans.append([a,c])
    return ans
def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = overlapGraph(inp)
    print(output)
    output = '\n'.join(''.join(str(i[0])+' -> ' + str(i[1])) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)