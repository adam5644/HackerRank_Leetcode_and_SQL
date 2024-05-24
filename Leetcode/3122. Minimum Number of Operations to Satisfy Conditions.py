# 

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid2 = list(zip(*grid))

        @cache
        def dp(p, i):
            if i == n:
                return 0
            res = inf
            kvs = Counter(grid2[i]).items()
            for k, v in list(kvs) + [(-1, 0)]:
                if k != p:
                    cur = dp(k, i + 1) + m - v
                    res = min(res, cur)
            return res
        
        return dp(-1, 0)
        