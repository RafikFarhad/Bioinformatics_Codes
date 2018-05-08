import itertools
import random
import networkx as nx
visitedCount = 0

def isEulerGraph(graph):
    degree = {}
    for (key, value) in graph.items():
        degree[key] = 0;
        for v in value:
            degree[v] = 0
    for (key, value) in graph.items():
        degree[key] += len(value)
        for v in value:
            degree[v] -= 1
    
    for val in degree.values():
        if(val!=0):
            return False
    return True

def DFS(root, graph, cycle):
    for i in graph[root]:
        if i not in cycle:
            cycle += [i]
            DFS(i, graph, cycle)
            return 

def EulerianCycle(graph):
    if(not isEulerGraph(graph)):
        return ['Not Euler Graph']
    total = len(graph)
    cycle = []
    DFS(list(graph.keys())[random.randrange(0, total)], graph, cycle)
    while(len(cycle)!=total):
        newStart = -1
        for i in cycle:
            for j in graph[i]:
                if j not in cycle:
                    newStart = i
                    index = cycle.index(i)
                    cycle = cycle[index:] + cycle[0:index] + [i]
                    break
        # return cycle + [newStart*100]
        if(newStart==-1):
            break
        DFS(newStart, graph, cycle)
    return cycle + [ cycle[0] ]

def getSource(graph):
    degree = {}
    for (key, value) in graph.items():
        degree[key] = 0;
        for v in value:
            degree[v] = 0
    for (key, value) in graph.items():
        degree[key] += len(value)
        for v in value:
            degree[v] -= 1
    a = b = 0
    for (key,val) in degree.items():
        if(val==-1):
            a = key
        elif(val==1):
            b = key
    return (a,b)

def EulerianCycle2(graph):
    src = getSource(graph)[1]
    dest = getSource(graph)[0]
    graph[dest] = [src]
    G = nx.DiGraph(graph)
    ans = list(nx.eulerian_circuit(G, source=src))
    return [ a[0] for a in ans]

def main(infile, outfile):
    # Read the input, but do something non-trivial instead of count the lines in the file
    inp = lines = [line.rstrip('\n') for line in infile]
    print(inp)
    output = EulerianCycle2( {int(a.split(' -> ')[0]): [int(p) for p in a.split(' -> ')[1].split(',')]  for a in inp})
    print(output)
    output = '->'.join(str(a) for a in output)
    # For debugging, print something to console
    print(output)

    # Write the output.
    outfile.write(output)