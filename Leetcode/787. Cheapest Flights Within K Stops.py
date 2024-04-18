from collections import defaultdict
from collections import deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        queue = deque([(src, 0)]) # queue contain tuples of {node, cost} which is the lowest cost to reach each node
        costs = [float('inf')] * n
        while queue and k >= 0:
            for _ in range(len(queue)):
                node, cost = queue.popleft()
                for next, price in adj[node]:
                    if cost + price < costs[next]:
                        costs[next] = cost + price
                        queue.append((next, cost + price))
            k -= 1

        return costs[dst] if costs[dst] != float('inf') else -1
    
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))