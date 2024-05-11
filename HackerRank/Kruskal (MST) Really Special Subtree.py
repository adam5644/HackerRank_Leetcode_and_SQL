#!/bin/python3

import math
import os
import random
import re
import sys

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n # length of each parent

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u] # 

    def union(self, u, v): # let u and v have the same parent
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskals(g_nodes, g_from, g_to, g_weight):
    # List of edges
    edges = [(g_from[i], g_to[i], g_weight[i]) for i in range(len(g_from))]
    # Sort edges based on the weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize the disjoint set
    ds = DisjointSet(g_nodes + 1)  # +1 because node numbering starts at 1
    
    mst_cost = 0  # total cost of mst so far
    mst_edges = [] # nodes included in the mst so far

    for u, v, weight in edges:
        print('u, v, weight = ', u, v, weight)
        # Check if the current edge forms a cycle
        if ds.find(u) != ds.find(v): # check they u and v have different root in the ds. diff set means no cycle
            ds.union(u, v) # combine diff sets into 1 set
            mst_edges.append((u, v, weight))
            mst_cost += weight
            # Stop if we have enough edges
            if len(mst_edges) == g_nodes - 1:
                break
        print('mst_cost, mst_edges = ', mst_cost, mst_edges)
        print('ds.parent = ', ds.parent)
        print('ds.rank = ', ds.rank)

    return mst_cost  # or return mst_edges if you need the actual MST edges



g_nodes, g_edges = map(int, input().rstrip().split())

g_from = [0] * g_edges
g_to = [0] * g_edges
g_weight = [0] * g_edges

for i in range(g_edges):
    g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

res = kruskals(g_nodes, g_from, g_to, g_weight)

# Write your code here.
print(res)




    
    
    
    
    
    
    
    
    
# from collections import defaultdict

# g_nodes, g_edges=map(int,input().rstrip().split())
# connections=defaultdict(lambda: float('inf'))
# for _ in range(g_edges):
#     g_from,g_to,g_weight=map(int,input().rstrip().split())
#     if g_from>g_to:
#         g_from,g_to=g_to,g_from
#     if g_weight<connections[(g_from,g_to)]:
#         connections[(g_from,g_to)]=g_weight
    
# # inputs: g_nodes, connections    
# print(g_nodes)
# print(connections)

# # edge
# if g_nodes==2:
#     return connections[(0,1)]
    
# # main

