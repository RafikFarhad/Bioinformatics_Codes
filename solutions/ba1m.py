import itertools


def Best(digit, mer):
    dd = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T',
    }
    ans = ''
    while(True):
        a = int(digit/4)
        b = int(digit%4)
        ans += dd[b]
        digit = a
        if a==0:
            break
    ans = ans + ''.join(['A' for _ in range(mer - len(ans))])
    return [ans[::-1]]

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = Best(int(inp[0]), int(inp[1]))
    
    output = ' '.join(str(i) for i in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)