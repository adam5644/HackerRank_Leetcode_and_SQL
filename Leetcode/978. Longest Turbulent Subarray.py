
# 

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)

        # edge
        if n ==1: return 1
        if n==2:
            if arr[0]==arr[1]: return 1
            return 2

        res = 0

        prev = [1,1]
        curr=[0,0]

        for i in range(1,n):
            
            if arr[i]>arr[i-1]:
                #print('inc')
                curr[0]=1+prev[1]
                curr[1]=1
            elif arr[i]<arr[i-1]:
                #print('prev = ', prev)
                #print('dec')
                curr[0]=1
                #print('prev[0] = ', prev[0])
                curr[1]=1+prev[0]
            else:
                #print('others')
                curr=[1,1]
            if curr[0] > res: res = curr[0]
            if curr[1] > res: res = curr[1]
            prev=curr.copy()

            #print('i, arr[i], res = ', i, arr[i], res)
            #print('curr = ', curr)
            #print()

        return res