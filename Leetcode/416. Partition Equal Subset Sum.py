
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:  # If total sum is odd, it's impossible to split it evenly
            return False
        
        half_sum = total_sum // 2
        
        dp = [False] * (half_sum + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(half_sum, num - 1, -1):  # Update dp array from right to left
                if dp[j - num]:
                    dp[j] = True

        print('nums = ', nums)
        print('dp = ', dp)
        
        return dp[half_sum]

# Example usage:
sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))  # Output: True