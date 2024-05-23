# 397. Integer Replacement
class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def recurse(n: int) -> int:
            if n == 1:
                return 0
            if not (n & 1): # last bit set to 1 
                return 1 + recurse(n // 2) 
            return 1 + min(recurse(n - 1), recurse(n + 1))

        return recurse(n)