class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # dp array where dp[i] stores the maximum length of substring ending with the i-th letter of the alphabet
        dp = [0] * 26
        max_len = 0  # The length of the current valid substring
        
        for i in range(len(s)):
            # Check if the current character and the previous one are consecutive in the alphabet
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z')):
                max_len += 1
            else:
                max_len = 1
            
            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], max_len)
        
        # The result is the sum of the dp array
        print('dp = ', dp)
        return sum(dp)