

class Solution:
    def findTargetSumWays(self, nums, k: int) -> int:
        from functools import cache

        if len(nums)==1 and (nums[0] == k or -nums[0] == k): return 1
        if sum(nums) < k or -sum(nums) > k: return 0

        n = len(nums)

        @cache
        def decide(i, cumsum):
            print('i, cumsum = ', i, cumsum)

            if i==n-1:
                if cumsum==k: 
                    print('final, i, cumsum = ', i, cumsum)
                    print('aa')
                    return 1
                else: 
                    print('final, i, cumsum = ', i, cumsum)
                    print('bb')
                    return 0

            if i>n-1: return 0

            return decide(i+1, cumsum+nums[i+1]) + decide(i+1, cumsum-nums[i+1])

        return decide(0, nums[0]) + decide(0, -nums[0])