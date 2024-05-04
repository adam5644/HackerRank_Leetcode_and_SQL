from typing import List
from functools import cache

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        num_words = len(words)
        connections = [[] for _ in range(num_words)]
        word_lengths = [len(word) for word in words]

        for i, (word, group, length) in enumerate(zip(words, groups, word_lengths)):
            for j in range(i + 1, num_words):
                if (
                    group != groups[j]
                    and length == word_lengths[j]
                    and sum(c1 != c2 for c1, c2 in zip(word, words[j])) == 1
                ):
                    connections[i].append(j)
        
        # print('connections = ', connections)
        # connections =  [[1, 2], [], []] --> bab's valid hamming string is bab, and dab. not sure about whether bab and dab are hamming string of each other

        @cache
        def dfs(index: int) -> tuple:
            """ Perform a depth-first search (DFS) to find the longest subsequence starting from a given index. """
            longest_subsequence = max(
                [dfs(next_index) for next_index in connections[index]],
                key=len,
                default=[] # if input to max() is empty, system will raise error if default isnt specified
            )
            return tuple([index] + list(longest_subsequence))

        longest_indices = max(
            [dfs(i) for i in range(num_words)],
            key=len
        )
        return [words[index] for index in longest_indices]

words = ["bab", "zab","dab", 'jab',"cab", "cab"]
groups = [1,1, 2,2,2, 3]
print(Solution().getWordsInLongestSubsequence(words, groups))