import heapq
from collections import defaultdict

def getCost(g_nodes, g_from, g_to, g_weight):
    # Graph initialization
    edges = defaultdict(list)
    for u, v, w in zip(g_from, g_to, g_weight):
        edges[u].append((v, w))
        edges[v].append((u, w))  # since the graph is undirected

    # Priority queue for Dijkstra-like approach
    pq = []
    heapq.heappush(pq, (0, 1))  # (cost, node), starting from node 1
    min_cost = {1: 0}  # Minimum cost to reach each node

    while pq:
        current_cost, u = heapq.heappop(pq)
        if u == g_nodes:
            return current_cost  # Return cost immediately if we reach the last node

        for v, weight in edges[u]:
            # Cost to move to the next node
            # next_cost = max(0, weight - current_cost)
            # total_cost = current_cost + next_cost
            total_cost = max(weight, current_cost)

            # Only push to heap if the next node can be reached with a cheaper cost
            if v not in min_cost or total_cost < min_cost[v]:
                min_cost[v] = total_cost
                heapq.heappush(pq, (total_cost, v))

    # If node g_nodes is never reached
    if g_nodes not in min_cost:
        return "NO PATH EXISTS"
    else:
        return min_cost[g_nodes]

# Input processing
g_nodes, g_edges = map(int, input().split())
g_from, g_to, g_weight = [], [], []

for _ in range(g_edges):
    u, v, w = map(int, input().split())
    g_from.append(u)
    g_to.append(v)
    g_weight.append(w)

# Function call
result = getCost(g_nodes, g_from, g_to, g_weight)
print(result)
