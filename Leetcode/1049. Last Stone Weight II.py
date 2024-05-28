from functools import cache
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @cache
        def dfs(index, subset1_sum, subset2_sum):
            if index == len(stones):
                return abs(subset1_sum - subset2_sum)
            
            # Include the current stone in subset 1
            diff1 = dfs(index + 1, subset1_sum + stones[index], subset2_sum)
            
            # Include the current stone in subset 2
            diff2 = dfs(index + 1, subset1_sum, subset2_sum + stones[index])
            
            return min(diff1, diff2)
    
        total_sum = sum(stones)
        min_diff = dfs(0, 0, 0)
        return min_diff
