#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

from heapq import heappop, heappush
from collections import defaultdict

def shop(n, k, centers, roads):
    #print('n, k, centers, roads = ', n, k, centers, roads)
    
    fish_types = []
    for center in centers:
        parts = list(map(int, center.split()))
        fish_count = parts[0]
        mask = 0
        for i in range(1, fish_count + 1):
            mask |= (1 << (parts[i] - 1))
        fish_types.append(mask)

    # Construct the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, time in roads:
        graph[u-1].append((v-1, time))
        graph[v-1].append((u-1, time))

    #print('fish_types = ', fish_types)
    #print('graph = ', graph)
    
    #n, k, centers, roads =  5 5 ['1 1', '1 2', '1 3', '1 4', '1 5'] [[1, 2, 10], [1, 3, 10], [2, 4, 10], [3, 5, 10], [4, 5, 10]]
        
    #fish_types =  [1, 2, 4, 8, 16]

    #graph =  defaultdict(<class 'list'>, {0: [(1, 10), (2, 10)], 1: [(0, 10), (3, 10)], 2: [(0, 10), (4, 10)], 3: [(1, 10), (4, 10)], 4: [(2, 10), (3, 10)]})

        # Multi-state Dijkstra's Algorithm to find the shortest paths
        # Priority queue holds (time, current node, fish mask)
        
    # Initialize the priority queue with the starting node (node 0), its travel time (0), and the fish types it offers
    pq = [(0, 0, fish_types[0])]

    # Create a dictionary to store the minimum travel time for each state (node and fish mask)
    min_time = defaultdict(lambda: float('inf'))

    # Set the initial state (node 0 with its fish types) to have 0 travel time since it's the starting point
    min_time[(0, fish_types[0])] = 0

    # Loop until there are no more states to process in the priority queue
    while pq:
        # Extract the state with the minimum travel time from the priority queue
        current_time, current_node, current_mask = heappop(pq)

        # If we've found a cheaper way to this state since adding this instance to the queue, skip processing
        if current_time > min_time[(current_node, current_mask)]:
            continue

        # Explore all neighbors of the current node in the graph
        for neighbor, travel_time in graph[current_node]:
            # Calculate the new mask by combining the current fish mask with the fish types available at the neighbor
            new_mask = current_mask | fish_types[neighbor]
            # Calculate new total travel time to this neighbor
            new_time = current_time + travel_time

            # If this new path to the neighbor with the new mask is cheaper, update the state's minimal travel time
            if new_time < min_time[(neighbor, new_mask)]:
                min_time[(neighbor, new_mask)] = new_time
                # Push the new state into the priority queue for further processing
                heappush(pq, (new_time, neighbor, new_mask))

    # Define the bitmask representing all fish types available (all bits set for the number of fish types)
    all_fish = (1 << k) - 1

    # Initialize the minimum meeting time to infinity to start finding the minimum
    min_meeting_time = float('inf')

    # Loop through all possible combinations of fish masks for the two cats
    for mask1 in range(all_fish + 1):
        for mask2 in range(all_fish + 1):
            # Check if together these masks cover all fish types
            if (mask1 | mask2) == all_fish:
                # Ensure both states exist in the min_time dictionary
                if (n-1, mask1) in min_time and (n-1, mask2) in min_time:
                    # Retrieve the travel times for both masks at the final shopping center
                    time1 = min_time[(n-1, mask1)]
                    time2 = min_time[(n-1, mask2)]
                    # Calculate the minimal time when both cats have met and all fish types are collected
                    min_meeting_time = min(min_meeting_time, max(time1, time2))

    # Return the computed minimum meeting time
    return min_meeting_time
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()
