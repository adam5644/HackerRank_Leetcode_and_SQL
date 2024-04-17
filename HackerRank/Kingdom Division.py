import os
import sys
from collections import defaultdict

MOD = 10**9 + 7  # Modulus for large numbers to prevent overflow

def dfs(u, p, adj, same, diff):
    child = []  # List to store children of the current node u
    for v in adj[u]:  # Loop through the neighbors of u
        if v != p:  # Ensure we don't go back to the parent node
            dfs(v, u, adj, same, diff)  # Recursive DFS call
            child.append(v)  # Add to child list after it's fully processed
    
    same[u] = [1, 1]  # Initialize DP for current node for 'same' state
    for v in child:  # Calculate DP values using children's results
        same[u][0] = same[u][0] * diff[v][1] % MOD  # Product of different states for children when parent is in state 0
        same[u][1] = same[u][1] * diff[v][0] % MOD  # Product of different states for children when parent is in state 1

    diff[u] = [1, 1]  # Initialize DP for 'different' state
    for v in child:  # Calculate DP values for different states
        diff[u][0] = diff[u][0] * (same[v][0] + diff[v][1] + diff[v][0]) % MOD  # Combining children's states when parent is in state 0
        diff[u][1] = diff[u][1] * (same[v][1] + diff[v][1] + diff[v][0]) % MOD  # Combining children's states when parent is in state 1

    diff[u][0] = (diff[u][0] - same[u][0] + MOD) % MOD  # Ensure non-negative modulo results
    diff[u][1] = (diff[u][1] - same[u][1] + MOD) % MOD  # Ensure non-negative modulo results

def kingdomDivision(n, roads):
    adj = defaultdict(list)  # Dictionary to store the graph
    for a, b in roads:  # Create graph from roads input
        adj[a].append(b)
        adj[b].append(a)

    # Initialize DP tables
    same = [[0, 0] for _ in range(n + 1)]
    diff = [[0, 0] for _ in range(n + 1)]

    # Perform DFS to fill DP tables
    dfs(1, -1, adj, same, diff)  # Start DFS from node 1 with no parent

    # Result as sum of both configurations of the root
    return (diff[1][0] + diff[1][1]) % MOD  # Combine possible configurations for the root


print(kingdomDivision(5, [[1, 2], [1, 3], [3, 4], [3, 5]]))