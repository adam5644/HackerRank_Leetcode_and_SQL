#!/bin/python3

import math
import os
import random
import re
import sys

# def componentsInGraph(gb):
#     clusters = []
#     for x,y in gb:
#         # create fuse
#         fuse = []
#         for cluster in clusters:
#             if x in cluster or y in cluster:
#                 fuse.append(cluster)
#         # if fuse not empty
#         if fuse:
#             #print('fuse = ', fuse)
#             fused = []
#             for cluster in fuse:
#                 for x in cluster:
#                     fused.append(x)
#             clusters.append(fused)
#             #print('fused = ', fused)
#         # no fuse, just add
#         else:
#             clusters.append([x,y])
            
#         # print('x,y = ',x,y)
#         # print('clusters = ', clusters)
#         # print()
           
#     size = [len(x) for x in clusters] 
#     return [min(size), max(size)]

def componentsInGraph(gb):
    clusters = []
    for x, y in gb:
        # create fuse
        fuse = []
        for cluster in clusters:
            if x in cluster or y in cluster:
                fuse.append(cluster)

        # if fuse not empty
        if fuse:
            fused = set()
            for cluster in fuse:
                fused = fused.union(set(cluster))
                
            for cluster in fuse:
                clusters.remove(cluster)  # Remove the old cluster

            fused.add(x)  # Ensure x is in the fused cluster
            fused.add(y)  # Ensure y is in the fused cluster
            clusters.append(fused)  # Add the fused cluster back

        # no fuse, just add
        else:
            clusters.append({x, y})  # Use a set to avoid duplicates

    size = [len(cluster) for cluster in clusters]
    return [min(size), max(size)]

            
    
'''
1,6
clusters = [[1,6]]

2,7
clusters = [[1,6], [2,7]]

clusters = [[1,6], [2,7],[3,8],[4,9]]

2,6
fuse = [[1,6],[2,7]]
clusters = [[1,2,6,7], [3,8], [4,9]]
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
