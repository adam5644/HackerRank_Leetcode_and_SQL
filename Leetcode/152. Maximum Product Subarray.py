class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, left, right,n = float('-inf'), 1, 1, len(nums)
        for i in range(n):
            left*=nums[i]
            right*=nums[n-1-i]
            res = max(res, left, right)
            if left==0: left=1
            if right==0: right=1

        return res
