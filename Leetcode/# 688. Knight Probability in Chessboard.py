
from functools import cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k ==0:return 1.0
        if n==1 and k>=1: return 0

        @cache
        def move(left, r, c):
            #print('left, r, c = ', left, r, c)

            #base
            if left ==0 and 0<=r<=n-1 and 0<=c<=n-1: 
                return 1
            if r<0 or r>n-1 or c<0 or c>n-1:
                return 0
            if left<0:
                return 0
            return sum([
                move(left-1, r+1, c+2),
                move(left-1, r+2, c+1),
                move(left-1, r+2, c-1),
                move(left-1, r+1, c-2),
                move(left-1, r-1, c-2),
                move(left-1, r-2, c-1),
                move(left-1, r-2, c+1),
                move(left-1, r-1, c+2),
            ])

        #print('move(k, row, column) = ', move(k, row, column))
        return move(k, row, column)/(8**k)

print(Solution().knightProbability(3,2,0,0))