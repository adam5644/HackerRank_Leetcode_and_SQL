#User function Template for python3

class Solution:
	def DistinctSum(self, arr):
		# Code here
		
		# edge
		if len(arr) == 1: return [0,arr[0]]
		
		# main
		s = sum(arr)
		dp=[0]*(s+1)
		dp[0]=1
		dp[-1]=1
		
		res=set([0,s])
		
		for x in arr:
		    for i in range(s,x-1,-1):
		        if dp[i-x]:
		            dp[i]=1
		            res.add(i)
		            
		res = list(res)
		res.sort()
		            
	    return res