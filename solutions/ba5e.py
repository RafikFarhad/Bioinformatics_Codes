import itertools
import random
import networkx as nx
import sys
import pandas as pd

def globalAllignment(str1, str2):
    errorMat = pd.read_csv('inputs/BLOSUM62.txt', delim_whitespace=True)
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    mat = []
    path = []
    mat.append([0 for _ in range(len2)])
    path.append([0 for _ in range(len2)])
    for i in range(1, len1):
        mat.append([0] + [-1000000 for _ in range(len2-1)])
        path.append([0 for _ in range(len2)])
        
    for i in range(len1):
        mat[i][0] = -5*i
        path[i][0] = 2
    for i in range(len2):
        mat[0][i] = -5*i
        path[0][i] = 3

    for i in range(len1):
        for j in range(len2):
            if i==0 or j==0:
                continue
            a = b = c = -1
            a = mat[i-1][j-1] + errorMat[str1[i-1]][str2[j-1]]
            b = mat[i-1][j] - 5
            c = mat[i][j-1] - 5
            maxi = max([a, b, c])
            if maxi == a:
                mat[i][j] = a
                path[i][j] = 1
            elif maxi == b:
                mat[i][j] = b
                path[i][j] = 2
            else:
                mat[i][j] = c
                path[i][j] = 3

    return (mat[len1-1][len2-1], printRecursive(str1, str2, path, i, j))

def printRecursive(str1, str2, path, i, j):
    if i==0 or j==0:
        return ('', '')
    if path[i][j] == 1:
        ans = printRecursive(str1, str2, path, i-1, j-1)
        return (ans[0] + str1[i-1], ans[1] + str2[j-1])
    elif path[i][j] == 2:
        ans = printRecursive(str1, str2, path, i-1, j)
        return (ans[0] + str1[i-1], ans[1] + '-')
    else:
        ans = printRecursive(str1, str2, path, i, j-1)
        return (ans[0] + '-', ans[1] + str2[j-1])
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = globalAllignment(inp[0], inp[1])
    output = str(output[0]) + "\n" + '\n'.join(output[1])
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)