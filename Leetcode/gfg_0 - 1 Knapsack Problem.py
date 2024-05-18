class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, weight, wt, val, n):
        dp = [0] * (weight + 1)
        
        for i in range(n):
            print('i = ', i)
            for w in range(weight, wt[i] - 1, -1):
                print('w = ', w)
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
                print('dp = ', dp)
                
        print('final, dp = ', dp)
        return dp[weight]

# Example usage
s = Solution()
N = 3
W = 4
values = [1, 2, 3]
weights = [4, 5, 1]
print(s.knapSack(W, weights, values, N))  # Output: 3
