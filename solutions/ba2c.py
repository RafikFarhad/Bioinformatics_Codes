import itertools

def ProfileMostProbable(dna, k, profile):
    dd = {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3
    }
    ans = (0, '')
    for i in range(len(dna)-k+1):
        local = 1
        for j in range(k):
            local *= profile[dd[dna[i+j]]][j]
        ans = max(ans, (local, dna[i:i+k]))
    return ans

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = ProfileMostProbable(inp[0], 
            int(inp[1]), 
            [ [float(b) for b in a.split(' ')] for a in inp[2:]])
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)