class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        lengths = [0] * n  # lengths[i] will be the length of the longest ending in nums[i]
        counts = [0] * n   # counts[i] will be the number of the longest ending in nums[i]

        for i, num in enumerate(nums):
            lengths[i] = 1
            counts[i] = 1
            
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        longest = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == longest)