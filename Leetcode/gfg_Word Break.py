# 
class Solution:
    def wordBreak(self, n, s, word_set):
        res = False

        def solve(i):
            nonlocal res
            if res:  # If res is already True, terminate further recursion
                return
            
            if i == len(s):  # Base case: if the end of the string is reached
                res = True
                return
            
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr in word_set:
                    solve(j)  # Recurse with the next index

        solve(0)
        return res
