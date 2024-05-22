from functools import lru_cache

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    @lru_cache(None)
    def solve(self, p, q, r, last):
        # Base cases
        if p == 0 and q == 0 and r == 0:
            return 1
        
        ways = 0

        if last != 1 and p > 0:
            ways = (ways + self.solve(p - 1, q, r, 1)) % self.mod
        if last != 2 and q > 0:
            ways = (ways + self.solve(p, q - 1, r, 2)) % self.mod
        if last != 3 and r > 0:
            ways = (ways + self.solve(p, q, r - 1, 3)) % self.mod

        return ways

    def CountWays(self, p, q, r):
        # Clear the cache before each run
        self.solve.cache_clear()
        return self.solve(p, q, r, 0)