class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, weight, wt, val, n):
        dp = [0] * (weight + 1)
        
        for i in range(n):
            for w in range(weight, wt[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
                
        return dp[weight]