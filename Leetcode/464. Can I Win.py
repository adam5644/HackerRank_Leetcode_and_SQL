# 464. Can I Win
class Solution:
    def canIWin(self, maxInt: int, total: int) -> bool:
        if maxInt * (maxInt+1) / 2 < total: return False

        @cache
        def func(nums, total):
            if total <= max(nums): return True 
            return any(not func(nums-{x}, total-x) for x in nums)

        return func(frozenset(range(1,maxInt+1)), total)