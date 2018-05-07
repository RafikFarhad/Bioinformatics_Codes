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
def make_profile(kMers):
    """ return list of dictionaries where each dictionary is column of the profile """

    if len(kMers) == 0:
        print "None!!!"
        return None

    k = len(kMers[0])
    t = len(kMers)
    profile = list(dict())
    for i in xrange(k):
        profile_col = {'A':0, 'C':0, 'G':0, 'T':0}
        for j in xrange(t):
            profile_col[kMers[j][i]] += 1

        for key in profile_col.keys():
            profile_col[key] = 1.0 * profile_col[key] / t

        profile.append(profile_col)

    return profile

def pattern_probability(profile, pattern):
    probability = 1
    for i in xrange(0, len(pattern)):
        probability *= profile[i][pattern[i]]

    return probability

def profile_most_probable_kmer(dna, profile, k):
    start = 0
    length = len(dna)
    max_probability = 0
    most_probable = dna[0:k]
    while start + k <= length:
        substr = dna[start:start+k]
        probability = pattern_probability(profile, substr)
        if probability > max_probability:
            most_probable = substr
            max_probability = probability

        start += 1

    return most_probable

def hamming_dist(str_one, str_two):
    """ returns number of hamming_dist between two strings """

    len_one = len(str_one)
    len_two = len(str_two)
    if len_one != len_two:
        raise ValueError("Strings have different lengths.")

    mismatches = 0
    for i in xrange(len_one):
        if str_one[i] != str_two[i]:
            mismatches += 1

    return mismatches

def make_consensus(motifes):
    profile = make_profile(motifes)
    consensusList = list()
    for item in profile:
        consensusList.append(max(item, key=item.get))

    return ''.join(consensusList)
 
def getScore(motifes):
    consensus = make_consensus(motifes)
    score = 0
    for motif in motifes:
        score += hamming_dist(consensus, motif)

def GetProfile(all_dna):
    k = len(all_dna)
    return [[ m.count(base)/k for m in zip(*all_dna) ] for base in "ACGT"]

def GreedyMotifSearch(k, t, all_dna):
    best_motifs = [a[0:k] for a in all_dna]
    for j in range(len(all_dna[0])-k+1):
        motifs = [all_dna[0][j:j+k]]
        for i in range(1, t):
            profile = GetProfile(motifs[0:i])
            motifs.append(ProfileMostProbable(all_dna[i], k, profile)[1])
            # print(j, ProfileMostProbable(all_dna[i], k, profile)[1])
        print(getScore(motifs),getScore(best_motifs), motifs)
        if getScore(motifs) <= getScore(best_motifs):
            best_motifs = motifs
    return best_motifs

    

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = GreedyMotifSearch(int(inp[0].split()[0]),int(inp[0].split()[1]), inp[1:])
    
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)