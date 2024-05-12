from collections import defaultdict
import sys

# Reading number of nodes and edges
n, m = map(int, sys.stdin.readline().strip().split())

# Building the graph using defaultdict of dictionaries
graph = defaultdict(dict)
for _ in range(m):
    x, y, r = map(int, sys.stdin.readline().strip().split())
    if y not in graph[x] or graph[x][y] > r:  # This check is useful to handle multiple edges and keep the minimum weight
        graph[x][y] = r
        graph[y][x] = r

# Input the starting node
s = int(sys.stdin.readline().strip())


# inputs
# print('n,s = ', n,s)
# print('graph = ', graph)

# Using a dictionary to track visited nodes and their costs to the MST
visited = {s: 0}
mst_cost = 0

# Prim's algorithm
while len(visited) < n:
    lowest_cost = (None, float('inf'))  # (next_node, weight)
    for node in visited:
        for adj_node in graph[node]:
            if adj_node not in visited and graph[node][adj_node] < lowest_cost[1]:
                lowest_cost = (adj_node, graph[node][adj_node])


    # Adding the selected edge to the MST
    visited[lowest_cost[0]] = lowest_cost[1]
    mst_cost += lowest_cost[1]  # Accumulate the total cost of the MST

# Output the total cost of the MST
print(mst_cost)
