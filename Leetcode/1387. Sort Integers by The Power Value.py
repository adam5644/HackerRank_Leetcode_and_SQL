from heapq import heappush, heappop

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
    
        res = [] # res=[[steps, x]]
        for num in range(lo,hi+1):
            x=num
            steps=0
            while x != 1:
                if x%2==0:
                    x=x/2
                else:
                    x=3*x+1
                steps+=1
            
            res.append((steps,num))
        
        res= sorted(res)
       # print('res = ', res)
        return res[k-1][1]

