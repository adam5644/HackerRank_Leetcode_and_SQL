class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for l in range(n-1,-1,-1):
            for r in range(n-1,l,-1):
                if nums[l]<nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                    nums[l+1:] = sorted(nums[l+1:])
                    return

        nums.sort()
        return