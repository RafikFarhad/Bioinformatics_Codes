# import matplotlib.pyplot as plt
# %matplotlib inline
def Skew(Dna):
    g = 0
    c = 0
    ans = [0]
    for a in Dna:
        if a == 'G':
            g+=1
        elif a == 'C':
            c+=1
        ans.append(g-c)
    mini = min(ans)
    # return ans;
    ans = [i for i, x in enumerate(ans) if x == mini]
    # plt.plot(ans)
    # plt.show()
    return ans

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    ans = Skew(inp[0])

    output = ' '.join([str(i) for i in ans])

    print(output)

    # Write the output.
    outfile.write(output)