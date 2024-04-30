class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1) # dp[j] = 
        for i in range(len(text2)):
            count = 0

            for j in range(len(text1)):
                if count < dp[j]:
                    count = dp[j]

                elif text2[i] == text1[j]:
                    dp[j] = count + 1

        return max(dp)