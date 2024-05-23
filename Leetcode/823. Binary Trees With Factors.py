class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        dp = {}
        
        for num in arr:
            dp[num] = 1  # Each number can form a single-node tree
        
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[j] is a factor of arr[i]
                    right = arr[i] // arr[j]
                    if right in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[right]
                        dp[arr[i]] %= mod
        
        return sum(dp.values()) % mod