# class Solution:
#     def minimumCoins(self, prices: List[int]) -> int:
#         if len(prices) <= 1: return prices[0]
#         from functools import cache
#         n= len(prices)
#         global res
#         res = float('inf')

#         @cache
#         def choose(i, cumsum, last):
#             global res
#             # base
#             if i == n-1:
#                 res = min(res, cumsum)
#                 return
#             if cumsum>= res: return

#             if i == n-2:
#                 if last == 1:
#                     choose(i+1, cumsum, 1)
#                 elif last ==0:
#                     choose(i+1, cumsum+prices[i-1],1)

#             # main
#             if last == 1:
#                 choose(i+1, cumsum+prices[i+1], 1)
#                 choose(i+1, cumsum, 0)
#             if last == 0:
#                 choose(i+1, cumsum+prices[i+1], 1)



#         choose(0,prices[0],1)
#         return res


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        if len(prices) <= 1: return prices[0]
        from functools import cache
        n= len(prices)
        global res
        res = float('inf')

        @cache
        def choose(i, cumsum, free_left):
            #print('i, cumsum, free_left, taken = ', i, cumsum, free_left)
            global res
            # base
            if i == n-1:
                res = min(res, cumsum)
                return
            if cumsum>= res: return

            if free_left >= 1:
                choose(i+1, cumsum, free_left-1)
                choose(i+1, cumsum+prices[i+1], i+2)
            else:
                choose(i+1, cumsum+prices[i+1],i+2)

        choose(0,prices[0],1)
        return res
