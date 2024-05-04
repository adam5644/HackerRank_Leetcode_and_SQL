from functools import cache
from collections import defaultdict, Counter

class Solution:
    def deleteAndEarn(self, nums) -> int:
        points = defaultdict(int)
        maxi = float('-inf')
        for num in nums:
            points[num] += num
            maxi = max(num, maxi)
        print('maxi = ', maxi)
        print('points = ', points)

        @cache
        def dp(i):
            if i < 1:
                return 0
                
            return max(dp(i-1), points[i] + dp(i-2))

        return dp(maxi)
    
print(Solution().deleteAndEarn([3,4,2]))