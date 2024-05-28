# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         # can take 2m stones, next round's m = nax(m,x)
#         # initially m = 1
#         n = len(piles)
#         s = sum(piles)

#         @lru_cache(None)
#         def dfs(i, m):
#             if 2*m>=n-(i+1):
#                 print('i,m, sum(piles[i:]) = ',i,m, sum(piles[i:]))
#                 return sum(piles[i:])

#             res = float('-inf')
#             for x in range(1,2*m+1):
#                 alice = sum(piles[i:i+x]) + sum(piles[i+x:]) - dfs(i+x, max(m,x))
#                 res = max(alice, res)
#             return res

#         return dfs(0, 1) # alice can take index 0
  

from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # n = len(piles)
        
        # # Convert piles to a suffix sums array
        # for i in range(n - 2, -1, -1):
        #     piles[i] += piles[i + 1]


        # @lru_cache(None)
        # def dp(left, m):
        #     if left + 2 * m >= n:
        #         return piles[left]
        #     else:
        #         return piles[left] - min(dp(left + i, max(m, i)) for i in range(1, 2 * m + 1))
        
        # return dp(0, 1)

        n=len(piles)

        piles2=[0]*n
        piles2[0] = sum(piles)

        for i in range(1, n):
            piles2[i]=piles2[i-1]-piles[i-1]

        @cache
        def dfs(i,m):
            if 2*m >= n-i:
                return piles2[i]
            
            bob = float('inf')
            for x in range(1,2*m+1):
                temp = dfs(i+x, max(m,x))
                bob = min(bob, temp)
            
            return piles2[i] - bob

        return dfs(0,1) 