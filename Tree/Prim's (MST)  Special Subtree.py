#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

from collections import defaultdict

def prims(n, edges, start):
    
    # each loop, look at all connected dots, look at their possible edges to unconnected dots, connect the edge thats the smallest. repeat until all connected      
    
    # print(edges)
    # edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]

    dict1 = defaultdict(list)
    dict2 = defaultdict(list)
    for x in edges:
        dict1[x[0]].append([x[1], x[2]])
        dict2[x[1]].append([x[0], x[2]])
    
    connected = [False]*(n+1) # connected[0] is redundant
    connected[0] = True
    connected[start] = True
    res = 0
    
    while not all(connected) is True:

        to_connect = None
        res_add = float('inf')
        for i in range(1,len(connected)): # o(n)
            if connected[i] is True:
                
                for x in dict1[i]:  # o(n^2)
                
                    # print('dict1[i] = ', dict1[i])
                    # print('x[0] = ', x[0])
                    # print('connected = ', connected)
                    
                    if connected[x[0]] is False and x[1] < res_add:
                        to_connect = x[0]
                        res_add = x[1]
                        #print('add1')
                        
                for x in dict2[i]:  # o(n^2)
                    if connected[x[0]] is False and x[1] < res_add:
                        to_connect = x[0]
                        res_add = x[1]
                        #print('add2')
                    

                    
        connected[to_connect] = True
        res+=res_add
    
    # res = 3 + 4 + 2 + 6 = 15
    return res
    
'''
dic1 = {1:[[2,3],[3,4]],
        4:[[2,6]]
 }

dict2 = {}

'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
