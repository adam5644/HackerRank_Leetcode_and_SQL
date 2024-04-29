1043. Partition Array for Maximum Sum

class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        from functools import cache

        @cache
        def f(i): # f(i) returns max for a[i:]
            # base
            if i == len(a): 
                return 0

            # main
            summ=0
            for j in range(i, min(len(a), i+k)): # j from i+1 to min(len(a), i+k+1)
                a11 = (j-i+1)*(max(a[i:j+1]))
                #print('a11 = ', a11) 
                a22 = f(j+1)
                #print('a22 = ', a22) 

                summ = max(summ, 
                        a22 + a11
                            )
            return summ



        return f(0)