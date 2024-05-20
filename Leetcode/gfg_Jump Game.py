
class Solution:
    def canReach(self, A, N):
        # # code here 
        
        # # edge
        # if A[0]==0: return 0
        # if N==1: return 1
        
        # # main
        # dp=[0]*(N)
        # dp[0]=1
        # for i in range(N):
        #     if dp[i]==1:
                
            
        # print('final dp = ', dp)
        # return 0
        
        reached=0
        
        for i in range(N):
            if reached >= N-1:
                return 1
            if i <= reached:
                reached = max(reached, i+A[i])
        return 0