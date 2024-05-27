# 

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # Dictionary to store the lengths of arithmetic subsequences
        dp = {}
        # Variable to keep track of the maximum length
        max_length = 2
        
        for i in range(len(nums)):
            for j in range(i):
                # Calculate the difference
                diff = nums[i] - nums[j]
                # Create a key using the current element and the difference
                key = (j, diff)
                # Update the dp dictionary with the length of the subsequence
                # Either take the previous length and add one, or start with 2
                dp[(i, diff)] = dp.get(key, 1) + 1
                # Update the maximum length
                max_length = max(max_length, dp[(i, diff)])
        
        return max_length
