import itertools

def is_greater(a, b):
    for (i,j) in zip(a,b):
        if i<j:
            return False
    return True

def custom_sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if is_greater(a[i], a[j]) == False:
                a[j], a[i] = a[i], a[j]
    return a


def SuffixTree(str1):
    res = []
    l = len(str1)
    for i in range(len(str1)):
        res.append(str1[i:l])
    return res
    return custom_sort(res)

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = [line.rstrip('\n') for line in infile]
    print(inp)
    output = SuffixTree(inp[0])
    print(output)
    output = '\n'.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)