def bellman_ford(edges, V, src):
    # Step 1: Initialize distances from src to all other vertices as INFINITE
    dist = [float("Inf")] * V
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            return "Graph contains negative weight cycle"

    return dist

# Example usage:
edges = [
    [0,1,5],
    [1,2,1],
    [1,3,2],
    [4,3,-1],
    [3,5,2],
    [5,4,-3]
]
V = 6 # v = num of vertices
src = 0
print(bellman_ford(edges, V, src))
