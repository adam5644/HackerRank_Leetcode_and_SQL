class Solution:
    def nCr(self, n: int, r: int) -> int:
        # MOD = 1000000007
        
        # # If r is greater than n, nCr is 0
        # if r > n:
        #     return 0
        
        # # Initialize a DP array of size r+1 with all zeros
        # dp = [0] * (r + 1)
        
        # # Base case: nC0 is 1 for any n
        # dp[0] = 1
        
        # # Fill the DP table
        # for i in range(1, n + 1): # 
        #     print('i = ', i)
        #     # Update the table from right to left
        #     for j in range(min(i, r), 0, -1):
        #         print('j = ', j)
        #         dp[j] = (dp[j] + dp[j - 1]) % MOD
        #     print('dp = ', dp)
        #     print()
        
        # return dp[r]
        
        #print('n,r = ',n,r)
        
        # edge
        if n==0 or r==0 or n==r: return 1
        if r>n: return 0
        
        
        # main
        
        mod = 10**9+7
        
        dp=[1]*(n+1)
        
        for i in range(2,n+1):
            for j in range(i-1, 0,-1):
                dp[j] = (dp[j] + dp[j-1]) % mod
                
        return dp[r]