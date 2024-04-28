class Solution:
    def numSquares(self, n: int) -> int:
        
        length = int(n**0.5)

        global res
        res = float('inf')
        from functools import cache

        @cache
        def next(length, left, count, store):
            global res

            if left == 0:
                res = min(res, count)
                return

            for i in range(length+1, 0, -1):
                if left - i**2 >=0:
                    #print('i = ', i)
                    next(i, left - i**2, count +1, store+str(i))
                    return # add this pass
                

        for i in range(length+1, 0, -1):
            next(i, n-i**2, 1, str(i))

        return res
        
            

        