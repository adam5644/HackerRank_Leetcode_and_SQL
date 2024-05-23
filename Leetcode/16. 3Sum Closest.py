class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")

        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = n + nums[left] + nums[right]
                diff = min(diff, target - s, key=abs)
                if s < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break

        return target - diff