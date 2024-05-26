import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initial filter pattern with the first character of the pattern string.
        # fp = p[0]

        fp=''

        # Iterate through the pattern to filter out consecutive '*' characters.
        for i in range(len(p)):
            if p[i-1] == '*' and p[i] == '*':
                continue
            else:
                fp += p[i]
        
        # Create the regular expression pattern by adding start (^) and end ($) anchors.
        pattern = f'^{fp}$'
        
        # Use re.fullmatch() to check if the entire string s matches the pattern.
        return bool(re.fullmatch(pattern, s))
