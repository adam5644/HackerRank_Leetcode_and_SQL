from functools import cache

class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        # Base case: if the string is empty, there's one valid way to decode it (the empty way)
        if not s:
            return 1
        
        if len(s) == 1 and s!='0':
            return 1

        # If the string starts with '0', it can't be decoded (no letter corresponds to '0')
        if s[0] == '0':
            return 0

        # Recursive calculation:
        # Start with taking just one digit (guaranteed not '0' here)
        result = self.numDecodings(s[1:])

        # If there are at least two digits and the first two digits form a number 10-26,
        # it can also be a valid letter
        if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
            result += self.numDecodings(s[2:])

        return result

# Test the function with an example that starts with '0' which should return 0
print(Solution().numDecodings('2101'))
