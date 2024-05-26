# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         dp = [0] * len(s2)

#         for c1 in s1:
#             prev = 0
#             for i, c2 in enumerate(s2):
#                 last = dp[i]
#                 if c1 == c2:
#                     dp[i] = prev + ord(c1)
#                 if prev < last:
#                     prev = last

#         return sum(map(ord, f'{s1}{s2}')) - 2 * max(dp)

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # Initialize the DP table
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        # Base cases
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for x in dp: print(x)
        print()
        
        # Fill the DP table
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        for x in dp: print(x)
        print()

        # The result is in dp[len(s1)][len(s2)]
        return dp[len_s1][len_s2]
