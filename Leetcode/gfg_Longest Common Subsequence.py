
class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        #print('x,y,s1,s2 = ', x,y,s1,s2)
        # code here
        
        # edge
        if s1==s2: return x
        if s1 in s2: return x
        if s2 in s1: return y
        
        # main
        dp=[[0 for _ in range(x+1)] for _ in range(y+1)]
        
        # for h in dp:
        #     print(h)
        # print()
        
        for yy in range(1,y+1):
            for xx in range(1,x+1):
                # if s1[xx-1] == s2[yy-1]:
                #     dp[yy][xx]=max(dp[yy-1][xx],
                #                     dp[yy][xx-1],
                #                     dp[yy-1][xx-1])+1
                # else:
                #     dp[yy][xx]=max(dp[yy-1][xx],
                #                     dp[yy][xx-1],
                #                     dp[yy-1][xx-1])
                
                if s1[xx-1] == s2[yy-1]:
                    dp[yy][xx]=dp[yy-1][xx-1]+1
                else:
                    dp[yy][xx]=max(dp[yy][xx-1], dp[yy-1][xx])
                   
        # for h in dp:
        #     print(h)
            
        return dp[-1][-1]
