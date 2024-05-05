import heapq

class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        vis = set()
        next_edges = [(0, 0)]
        total_cost = 0

        while len(vis) < n:
            curr_cost, curr = heapq.heappop(next_edges)
            if curr in vis:
                continue
                
            vis.add(curr)
            total_cost += curr_cost
            x1, y1 = points[curr]

            for i in range(n):
                if i not in vis:
                    x2, y2 = points[i]
                    next_cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(next_edges, (next_cost, i))

        return total_cost
    
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))