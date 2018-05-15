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
    output = coinChange(int(inp[0]), [int(i) for i in inp[1].split(',')])
    print(output)
    output = str(output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)