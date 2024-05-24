#          
from collections import Counter

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [n] * (n + 1)  # Initialize dp array with maximum possible partitions
        dp[0] = 0  # No partitions needed for an empty string
        
        for i in range(1, n + 1):
            cur = Counter()
            for j in range(i, 0, -1):  # Iterate backwards from i to 1
                cur[s[j - 1]] += 1
                if len(set(cur.values())) == 1:  # Check if all frequencies are the same
                    dp[i] = min(dp[i], 1 + dp[j - 1])
        
        return dp[n]