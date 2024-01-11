#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

# def journeyToMoon(n, astronaut):
#     def dfs(node):
#         visited[node] = True
#         size = 1
#         for neighbour in graph[node]:
#             if not visited[neighbour]:
#                 size += dfs(neighbour)
#         return size

#     # Create a graph
#     graph = {i: [] for i in range(n)}
#     for a, b in astronaut:
#         graph[a].append(b)
#         graph[b].append(a)

#     # Find clusters using DFS
#     visited = [False] * n
#     cluster_sizes = []
#     for i in range(n):
#         if not visited[i]:
#             cluster_sizes.append(dfs(i))

#     # Calculate combinations
#     total_pairs = (n * (n - 1)) // 2
#     invalid_pairs = sum((size * (size - 1)) // 2 for size in cluster_sizes)

#     return total_pairs - invalid_pairs

 
def journeyToMoon(n, astronaut):
    print(astronaut)
    
    # Efficient union-find with path compression
    print(n)
    parent = list(range(n))

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    # Creating clusters
    for a, b in astronaut:
        union(a, b)

    print('parent = ', parent)

    # Calculating the size of each cluster
    cluster_size = {}
    for i in range(n):
        root = find(i)
        if root in cluster_size:
            cluster_size[root] += 1
        else:
            cluster_size[root] = 1

    # Optimized combination calculation
    res = 0
    sum_so_far = 0
    for size in cluster_size.values():
        res += sum_so_far * size
        sum_so_far += size

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
