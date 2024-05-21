

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        dp=[0]*(W+1)
        
        for w1 in range(W):
            for v,w2 in zip(val, wt):
                if w1+w2<=W and dp[w1]+v>dp[w1+w2]:
                    dp[w1+w2]=dp[w1]+v
        #print('dp = ', dp)
        return dp[-1]