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

def getScore(motifs):
    k = len(motifs)
    countMatrix = [[ m.count(base) for m in zip(*motifs) ] for base in "ACGT"]
    score = k * len(motifs[0]) - sum([ max(m) for m in zip(*countMatrix) ])
    return score

def GetProfile(all_dna):
    k = len(all_dna)*1.0
    return [[ m.count(base)/k for m in zip(*all_dna) ] for base in "ACGT"]

def GreedyMotifSearch(k, t, all_dna):
    
    best_motifs = [a[0:k] for a in all_dna]

    for j in range(len(all_dna[0])-k+1):
        motifs = [ all_dna[0][j:j+k] ]
        for i in range(1, t):
            profile = GetProfile(motifs)
            motifs.append(ProfileMostProbable(all_dna[i], k, profile)[1])
            # print(motifs[-1], all_dna[i])
            # print(j, ProfileMostProbable(all_dna[i], k, profile)[1])
        print(getScore(motifs), getScore(best_motifs), best_motifs)
        if getScore(motifs) < getScore(best_motifs):
            best_motifs = motifs
    return best_motifs

    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = GreedyMotifSearch(int(inp[0].split()[0]),int(inp[0].split()[1]), inp[1:])
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)