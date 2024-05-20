class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
        dp=[0]*(max(a)+2) # dp[0], dp[maxx+1] =0, boundary
        
        for x in a:
            dp[x]=max(dp[x+1], dp[x-1])+1
            
        #print('dp = ', dp)
        return max(dp)
