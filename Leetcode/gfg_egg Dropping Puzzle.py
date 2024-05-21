from functools import lru_cache

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self, n, k):
        
        @lru_cache(None)
        def solve(n, k):
            if n == 0 or k == 0:
                return 0
            if n == 1:
                return k
            if k == 1:
                return 1
            
            mn = float("inf")
            for i in range(1, k + 1):
                tmp = max(solve(n - 1, i - 1), solve(n, k - i))
                if tmp < mn:
                    mn = tmp
            return mn + 1
        
        return solve(n, k)