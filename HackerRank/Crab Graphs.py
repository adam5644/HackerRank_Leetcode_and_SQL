#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crabGraphs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER t
#  3. 2D_INTEGER_ARRAY graph
#

def crabGraphs(n, t, graph):
    print('n, t, graph = ', n, t, graph)
    cnn={x:[] for x in range(1,n+1)}
    for u,v in graph:
        cnn[u].append(v)
        cnn[v].append(u)
    # print('cnn = ', cnn)
    # cnn =  {1: [4], 2: [4], 3: [4], 4: [1, 2, 3, 5], 5: [4, 8, 7, 6], 6: [5], 7: [5], 8: [5]}
    # u =  4 # 4 and 5 have length of 4
    # u =  5
    # u =  1
    # u =  2
    # u =  3
    # u =  6
    # u =  7
    # u =  8

    nodes=set() 
    
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True): # choose head 
        print('u = ', u)
        if u not in nodes and len(cnn[u])>=t:
            nodes.add(u)
            
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True): # choose tail
        feetofu=0
        for v in cnn[u]: # choose feet for u
            if v not in nodes and feetofu<t:
                nodes.add(v)
                feetofu+=1
                
    print('------------------------')
    return len(nodes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()
