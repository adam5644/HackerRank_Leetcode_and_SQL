#!/bin/python3

import math
import os
import random
import re
import sys

def floyd(road_nodes, road_edges, road_from, road_to, road_weight, queries):
    dist = [[math.inf for _ in range(road_nodes+1)] for _ in range(road_nodes+1)]
    for i in range(road_edges):
        dist[road_from[i]][road_to[i]] = road_weight[i]
    for i in range(road_nodes+1):
        dist[i][i] = 0
    
    for k in range(road_nodes+1):
        for i in range(road_nodes+1):
            for j in range(road_nodes+1):
                if dist[i][j] > dist[i][k] + dist[k][j]: 
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    for q in queries:
        if dist[q[0]][q[1]] == math.inf:
            print(-1)
        else:
            print(dist[q[0]][q[1]])
        
                    

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    q = int(input().strip())

    queries = []
    
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])
        
        queries.append([x, y])
        
    floyd(road_nodes, road_edges, road_from, road_to, road_weight, queries)