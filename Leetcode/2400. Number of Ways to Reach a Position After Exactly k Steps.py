# class Solution:
#     def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
#         if (startPos - endPos - k) % 2: return 0
#         return comb(k, (endPos - startPos + k) // 2) % (10 ** 9 + 7)

from functools import cache

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def count_ways(pos, steps_left):
            # Base case: if no steps left, check if we're at the end position
            if steps_left == 0:
                return 1 if pos == endPos else 0
            
            # If it's impossible to reach the target with the remaining steps, return 0
            if abs(endPos - pos) > steps_left:
                return 0

            # Recurse for both possible movements
            return (count_ways(pos + 1, steps_left - 1) + count_ways(pos - 1, steps_left - 1)) % MOD

        return count_ways(startPos, k)