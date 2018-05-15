import itertools
import random

def coinChange(n, coin):
    total = n+5
    ans = []
    for i in range(total):
        ans.append(100000)
    ans[0] = 0
    for i in range(total):
        for j in coin:
            if i+j < total:
                ans[i+j] = min(ans[i] + 1, ans[i+j])
    return ans[n]

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    n,m = int(inp[0].split(' ')[0]), int(inp[0].split(' ')[1])
    mat1 = [ [int(a) for a in x.split(' ')] for x in inp[1:n+1] ]
    output = mat2 = [ [int(a) for a in x.split(' ')] for x in inp[n+2:] ]
    print(mat2)
    
    # output = coinChange(int(inp[0]), [int(i) for i in inp[1].split(',')])
    # print(output)
    # output = str(output)
    # # For debugging, print something to console
    # print(output)

    # Write the output.
    outfile.write(output)