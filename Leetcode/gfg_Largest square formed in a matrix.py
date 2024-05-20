from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        
        res = 0
        
        for nn in range(1,n+1):
            for mm in range(1,m+1):
                if mat[nn-1][mm-1]==1:
                    temp = 1 + min(
                        dp[nn-1][mm], dp[nn-1][mm-1],
                        dp[nn][mm-1])
                    dp[nn][mm] = temp
                    if temp > res: res = temp
                 
        #for x in dp: print(x)   
        return res