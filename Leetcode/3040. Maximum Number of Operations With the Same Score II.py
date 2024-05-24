# 

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums) - 1

        @lru_cache(None)
        def dfs(prev_sum, l, r):
            if r - l + 1 < 2:
                return 0

            opt1 = nums[l] + nums[l + 1]
            opt2 = nums[r] + nums[r - 1]
            opt3 = nums[l] + nums[r]

            opt1Score = 1 + dfs(opt1, l + 2, r) if opt1 == prev_sum else 0
            opt2Score = 1 + dfs(opt2, l, r - 2) if opt2 == prev_sum else 0
            opt3Score = 1 + dfs(opt3, l + 1, r - 1) if opt3 == prev_sum else 0

            return max(opt1Score, opt2Score, opt3Score)

        # Initialize the maximum operations by considering all starting options
        return max(
            1 + dfs(nums[0] + nums[1], 2, n),
            1 + dfs(nums[n] + nums[n - 1], 0, n - 2),
            1 + dfs(nums[0] + nums[n], 1, n - 1)
        )