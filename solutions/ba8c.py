import itertools
import random
import networkx as nx
import sys

def Distance(a, b):
    a = [ (p-q)**2 for (p,q) in zip(a,b) ]
    return sum(a)**.5

def getCluster(centers, data):
    ans = [ [] for _ in centers ]
    for a in data:
        k = 1000000
        index = -1
        for (i, b) in enumerate(centers):
            p = Distance(a, b)
            if p<k:
                k = p
                index = i
        ans[index].append(a)
    return ans

def getCenter(centers, cluster, m):
    # print('###########', centers)
    
    ans = centers[:]
    for (i, a) in enumerate(cluster):
        if a == []:
            continue
        ans[i] = []
        for j in range(m):
            ans[i].append(sum([ b[j] for b in a ])/(len(a)))
    
    # print('###########', centers)
    # print('###########', cluster)
    # print('###########', ans)
    return ans

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def is_same(p, q):

    for (a,b) in zip(p,q):
        for i in range(len(a)):
            if isclose(a[i], b[i]) == False:
                return False        
    return True

def LloydAlgorithm(k, m, data):
    centers = []
    for _ in range(k):
        centers.append(data[_])
    # print('###########', centers)
    
    while True:
        cluster = getCluster(centers, data)
        # print('***********', centers)
        new_centers = getCenter(centers, cluster, m)
        # print('$$$$$$$$$$$$', centers)
        # print('$$$$$$$$$$$$', new_centers)

        if is_same(centers, new_centers):
            # print('breaked')
            break
        centers = new_centers
        # print(centers)
        # print('\n\n')
    return centers


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    # print(inp)
    mat = []
    for a in inp[1:]:
        b = a.split(' ')
        mat.append([float(_) for _ in b if _!=''])
    ans = LloydAlgorithm(int(inp[0].split(' ')[0]), int(inp[0].split(' ')[1]), mat)
    output = '\n'.join([' '.join(['{0:.3f}'.format(_) for _ in a]) for a in ans])
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)