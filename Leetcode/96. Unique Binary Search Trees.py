96. Unique Binary Search Trees

class Solution:

    def numTrees(self, n):
        dp = [-1] * (n + 1) # dp[i] is the total unique tree when n = 1,2,3,...

        def solve(n):
            if n <= 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            
            ans = 0
            for i in range(1, n + 1):
                ans += solve(i - 1) * solve(n - i)
            dp[n] = ans

            return dp[n]

        return solve(n)
    
print(Solution().numTrees(3))

