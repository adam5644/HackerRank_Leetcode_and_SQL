# 
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        summ = s.count('1')
        n = len(s)
        res = n-summ # change all to 1
        #print(s)

        prev_sum=0
        
        for i,x in enumerate(s): # to change all s[i:] # 
            #print('i = ', i)
            if x=='1':
                prev_sum+=1

            front_change=prev_sum
            # 
            #back_change = n-i-1 - (summ-prev_sum)
            back_change = n-i-1 - (summ-prev_sum)

            total_sum=front_change+back_change
            if total_sum<res: res=total_sum

            #print('res = ', res)

        return res
