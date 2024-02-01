#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

#def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
#     print(g_nodes)
#     print(g_from)
#     print(g_to)
#     print(g_weight)  
# 5
# [1, 3, 1, 4, 2]
# [2, 5, 4, 5, 3]
# [60, 70, 120, 150, 80]

    # find a line between first to last that has smallest max number
    
def getCost(g_nodes, g_from, g_to, g_weight):
    # dp[x] = min(each dp[y to x] + each weight)
    info = [[] for _ in range(g_nodes + 1)]
    
    for i in range(len(g_from)):
        info[g_from[i]].append([g_to[i], g_weight[i]])
        info[g_to[i]].append([g_from[i], g_weight[i]])
    
    dp = [math.inf]* (g_nodes+1) # dp[x] is min fare to go from pos 0 to pos x
    dp[1]=0
    
    
    curr = set([1])
    while curr:
        nxt = set([])
        
        for i in curr:
            for (j,w) in info[i]:
            
                alt = max(dp[i], w)
                
                if alt < dp[j]:
                    dp[j] = alt
                    nxt.add(j)
            
        curr = nxt
        
    #rint(dp)
    print(dp[g_nodes] if dp[g_nodes] != math.inf else "NO PATH EXISTS")
    



# def getCost(g_nodes, g_from, g_to, g_weight):
#     # Correctly initialize the adjacency list for each node
#     info = [[] for _ in range(g_nodes + 1)]
    
#     # Fill in the adjacency list with connections and weights
#     for i in range(len(g_from)):
#         info[g_from[i]].append([g_to[i], g_weight[i]])
#         info[g_to[i]].append([g_from[i], g_weight[i]])
    
#     # Initialize dp where dp[i] is the minimum fare to reach station i from station 1
#     dp = [math.inf] * (g_nodes + 1)
#     dp[1] = 0  # Starting point, cost is 0
    
#     # Use a set to keep track of the current station(s) being processed
#     curr = set([1])
#     while curr:
#         nxt = set()
        
#         for i in curr:
#             for j, w in info[i]:
#                 # Determine if the current path offers a lower maximum fare to station j
#                 alt = max(dp[i], w)
                
#                 if alt < dp[j]:
#                     dp[j] = alt
#                     nxt.add(j)
            
#         curr = nxt
    
#     # Print the minimum fare to reach the last station or "NO PATH EXISTS" if not reachable
#     print(dp[g_nodes] if dp[g_nodes] != math.inf else "NO PATH EXISTS")


    
    # # Create an adjacency list where each node points to its neighbors and the corresponding weights
    # edges = [[] for _ in range(g_nodes + 1)]
    # for i in range(len(g_from)):
    #     edges[g_from[i]].append((g_to[i], g_weight[i]))
    #     edges[g_to[i]].append((g_from[i], g_weight[i]))
    
    # # Set the fare to reach the first station as 0 and infinity for others as they are initially unreachable
    # dp = [math.inf] * (g_nodes + 1) # dp[x] is the min far to reach position x from 0
    # dp[1] = 0

    # # Use a set to keep track of the current station(s) being considered for exploration
    # current = set([1])
    # while current:
    #     next_set = set()
    #     for f in current: # o(n)
    #         for (t, w) in edges[f]: #o(n^2)
    #             # Calculate the fare required to reach station 't' from station 'f' considering the fare rules
    #             alt = max(dp[f], w)
    #             if alt < dp[t]:
    #                 dp[t] = alt
    #                 next_set.add(t)
    #     current = next_set
    
    # # Print the minimum fare to reach the last station or 'NO PATH EXISTS' if it's unreachable
    # print(dp[g_nodes] if dp[g_nodes] != math.inf else 'NO PATH EXISTS')


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
