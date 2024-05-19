class Solution:
    def findCatalan(self, n : int) -> int:
        # base case
        if n == 0 or n == 1:
            return 1
        
        mod = 10**9 + 7
        # Initializing dp[0] and dp[1] as 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(i):
                dp[i] = (dp[i] + (dp[j] * dp[i - j - 1]) % mod) % mod
        
        # returning the nth catalan number.
        return dp[n]