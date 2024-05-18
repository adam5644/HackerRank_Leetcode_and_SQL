
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        # Early return if lengths don't match
        if n1 + n2 != n3:
            return False




        # Use LRU cache to memoize the results of dfs
        @lru_cache(None)
        def dfs(i, j):
            # Current index in s3 is i + j
            k = i + j

            # If we have reached the end of s3, return True
            if k == n3:
                return True

            # Check if we can take a character from s1
            if i < n1 and s1[i] == s3[k] and dfs(i + 1, j):
                return True

            # Check if we can take a character from s2
            if j < n2 and s2[j] == s3[k] and dfs(i, j + 1):
                return True

            return False

        return dfs(0, 0)x   