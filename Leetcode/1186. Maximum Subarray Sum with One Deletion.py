class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        # 0 or 1 deletion

        # edge
        n = len(arr)
        if n==1: return arr[0]
        if all(not x for x in arr): return 0
        if all(x<0 for x in arr): return max(arr) # all negat
        if len([x for x in arr if x>0])==1: return max(arr)  # only 1 positive

        # # main
        # dp=[0]*n
        # minn=0
        # dp[0]=max(arr[0])
        # for i in range(1,n):
        #     x=arr[i]
        #     minn=min(minn, x)    
        #     dp[i]=max(0,arr[i]+dp[i-1]+minn, arr[i]) # chosen none, max up to prev - deletion + add curr, only curr

        # main
        maxx=0
        del_maxx=0
        res = float('-inf')
        for i,x in enumerate(arr):
            maxx=max(maxx + x, x)
            del_maxx = max(del_maxx+x, maxx-x)
            res = max(res, maxx, del_maxx)

            #print('i, maxx, del_maxx, res = ', i, maxx, del_maxx, res )

        return res



 