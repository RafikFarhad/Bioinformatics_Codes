import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def prettyGenome(arr):
    return '(' + ' '.join('{0:+d}'.format(_) for _ in arr) + ')'

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

def SharedkMer(k, dna1, dna2):
    res = []
    for i in range(len(dna1) - k + 1):
        a = dna1[i:i+k]
        b = Reverse(a)
        x = 0
        while(True):
            x = dna2.find(a, x)
            if x==-1:
                break
            res.append([i, x])
            x+=1
        x = 0
        while(True):
            x = dna2.find(b, x)
            if x==-1:
                break
            res.append([i, x])
            x+=1
        
    return res
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = SharedkMer(int(inp[0]), inp[1], inp[2])
    output = '\n'.join(str('(' + str(_[0]) + ', ' + str(_[1]) + ')') for _ in output)
    # print(output)
    
    # Write the output.
    outfile.write(output)