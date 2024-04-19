class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [0.0]*(k+maxPts+1)
        
        for i in range(k, n+1):
            dp[i] = 1.0
    
        window = sum(dp[k:k+maxPts])
        for j in range(k-1, -1, -1):
            dp[j] = window/maxPts
            window += dp[j] - dp[j + maxPts]
        # dp[0] = window/maxPts
        return dp[0]


print(Solution().new21Game(21,17,10))


        


        