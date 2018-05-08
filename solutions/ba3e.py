import itertools

def getComposition(k, dna):
    return sorted([ dna[i:i+k] for i in range(len(dna)-k+1) ])

def DeBruijnFromKMer(all_mer):
    res = {}
    for p in all_mer:
        a = p
        b = a[1:]
        c = a[:-1]
        res[c] = []
    for p in all_mer:
        a = p
        b = a[1:]
        c = a[:-1]
        res[c].append(b)
        
    return res

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = DeBruijnFromKMer(inp)
    print(output)
    output = '\n'.join(''.join(str(i)+' -> ' + ','.join(a for a in output[i])) for i in sorted(output.keys()))
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)