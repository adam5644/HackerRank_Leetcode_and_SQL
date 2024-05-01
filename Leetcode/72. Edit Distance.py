class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if j == len(word2):
                return len(word1) - i # to delete remaining of word1
            if i == len(word1):
                return len(word2) - j # to delete remaining of word2

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            
            return min(dp(i, j + 1), # insert word2's word to word1
                        dp(i + 1, j), # delete word1's word
                        dp(i + 1, j + 1)) # replace to make word1's word to equal to word2's word
                        + 1 # each of these 3 operations is a "+1"

        return dp(0, 0)
