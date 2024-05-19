
class Solution:
    def isSubsetSum (self, N, arr, sum1):

        # # edge
        # if sum in arr: return 1
        # if sum(arr)<sum1: return 0
        # if sum(arr)==sum1: return 1
        
        # code here 
        dp=[0]*(sum1+1)
        dp[0]=1
        
        for c in arr:
            for i in range(sum1-c,-1,-1):
                if dp[i]>0 and i+c<=sum1:
                    dp[i+c]+=dp[i]
                    
        #print('dp = ', dp)
                    
        if dp[-1]>0:
            return 1
        else:
            return 0
        
        
        