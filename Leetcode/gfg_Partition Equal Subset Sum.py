# 
class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        
        # If total sum is odd, we cannot partition it into two equal parts
        if total_sum % 2 != 0:
            return 0
        
        target_sum = total_sum // 2
        
        # Initialize a dp array where dp[j] means whether we can form sum j with the
        # elements seen so far
        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        for num in arr:
            # Traverse backwards to avoid using the same element multiple times
            for j in range(target_sum, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        
        return 1 if dp[target_sum] else 0
