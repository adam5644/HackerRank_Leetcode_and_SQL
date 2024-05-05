class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        #bellman
        dists = [float('inf')]*n
        dists[k-1] = 0

        for _ in range(n):
            for s, d, length in times:
                if dists[s-1]+length < dists[d-1]:
                    dists[d-1] = dists[s-1]+length
        
        return max(dists) if max(dists) != float('inf') else -1
    
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n,k))