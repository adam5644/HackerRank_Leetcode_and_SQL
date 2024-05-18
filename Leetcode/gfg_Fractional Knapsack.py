from collections import defaultdict
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        dd = defaultdict(int) # v/w = total weight available
        
        for x in arr:
            dd[x.value/x.weight] += x.weight
            
        c_left=w
        kk = dd.keys()
        kk = sorted(kk, reverse=True)
        
      # print('dd = ', dd)
        
        res=0
        for k in kk:
            #print('k = ', k)
            if c_left >= dd[k]:
                res+=(dd[k]*k)
                c_left-=dd[k]
                #print('res = ', res)
            else:
                res+=(k * c_left)
                #print('res = ', res)
                break
 
        return res
        #return 1