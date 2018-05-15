import itertools
import random
import sys

sys.setrecursionlimit(1500)

def printRecursive(i, j, mat, str1):
    if i==0 and j==0:
        return ''
    if i==0:
        return printRecursive(i, j-1, mat, str1)
    if j==0:
        return printRecursive(i-1, j, mat, str1)
    
#     print(i,j, mat[i][j])

    if mat[i][j] == 1:
        return printRecursive(i-1, j-1, mat, str1) + str1[i-1] 
    elif mat[i][j] == 2:
        return printRecursive(i-1, j, mat, str1)
    else:
        return printRecursive(i, j-1, mat, str1)
    
def longestSubsequense(str1, str2):
    l1 = len(str1) + 1
    l2 = len(str2) + 1
    mat = []
    score = []
    for i in range(l1):
        mat.append([])
        score.append([])
        for j in range(l2):
            mat[i].append(-1)
            score[i].append(-1)
    for i in range(l1):
        score[i][0] = 0
        mat[i][0] = 0
    for i in range(l2):
        score[0][i] = 0
        mat[0][i] = 0
    
    for i in range(l1):
        for j in range(l2):
            if i==0 or j==0:
                continue
            a = b = c = -1
            if str1[i-1] == str2[j-1]:
                    a = score[i-1][j-1] + 1
            else:
                b = score[i][j-1] + 0
                c = score[i-1][j] + 0
            maxScore = max([a,b,c])
#             print(i, j, maxScore)
            if maxScore == a:
                score[i][j] = a
                mat[i][j] = 1
            elif maxScore == b:
                score[i][j] = b
                mat[i][j] = 3
            else:
                score[i][j] = c
                mat[i][j] = 2
    return printRecursive(l1-1, l2-1, mat, str1)

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    
    output = longestSubsequense(inp[0], inp[1])
    print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)