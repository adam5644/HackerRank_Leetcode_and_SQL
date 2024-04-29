2571. Minimum Operations to Reduce an Integer to 0

import math

class Solution:
    # 56 - 64
    # 8
    def minOperations(self, n: int) -> int:
        rem = n
        count = 0
        while rem > 0:
            rem = abs(rem - 2**round(math.log(rem, 2)))
            count += 1
        return count