# 

from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Initialize the graph with empty adjacency lists
        graph = [[] for _ in range(n)]
        
        # Build the adjacency list representation of the graph
        for garden1, garden2 in paths:
            graph[garden1 - 1].append(garden2 - 1)
            graph[garden2 - 1].append(garden1 - 1)
        print('graph = ', graph)
        
        # Initialize the answer array with zero (meaning uncolored)
        flower_types = [0] * n
        
        # For each garden, choose a flower type
        for garden in range(n):
            # Set of available flower types
            available_flowers = {1, 2, 3, 4}
            
            # Remove flower types used by adjacent gardens
            for neighbor in graph[garden]:
                if flower_types[neighbor] in available_flowers:
                    available_flowers.discard(flower_types[neighbor])
            
            # Assign the first available flower type to the current garden
            flower_types[garden] = available_flowers.pop()
        
        return flower_types
 