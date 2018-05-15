import itertools
import random
import networkx as nx
import sys
import pandas as pd
sys.setrecursionlimit(2000)

def recursion(a, b, n, m):
    if n==0:
        return m
    if m==0:
        return n
    if a[n-1] == b[m-1]:
        return recursion(a, b, n-1, m-1)
    return 1 + min([
        recursion(a, b, n-1, m),
        recursion(a, b, n, m-1),
        recursion(a, b, n-1, m-1)
    ])

def EditDistance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    return recursion(str1, str2, len1, len2)

def printRecursive(str1, str2, path, i, j):
    if i==0 and j==0:
        return ('', '')
    if path[i][j] == 1:
        ans = printRecursive(str1, str2, path, i-1, j-1)
        return (ans[0] + str1[i-1], ans[1] + str2[j-1])
    elif path[i][j] == 2:
        ans = printRecursive(str1, str2, path, i-1, j)
        return (ans[0] + str1[i-1], ans[1] + '-')
    elif path[i][j] == 3:
        ans = printRecursive(str1, str2, path, i, j-1)
        return (ans[0] + '-', ans[1] + str2[j-1])
    else:
        return ('', '')
    


def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)    
    output = EditDistance(inp[0], inp[1])
    output = str(output)
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)