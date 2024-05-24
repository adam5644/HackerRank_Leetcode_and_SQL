# 
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        from functools import cache  # Cache to memoize the results of dp
        
        @cache
        def dp(a, b):
            nonlocal limit
            if a == 0 and b == 0:  # Base case: no more zeros and ones to place
                return 1
            elif a < 0:  # Base case: invalid state
                return 0
            res = 0  # Initialize the result count
            for i in range(1, limit + 1):  # Iterate over all possible lengths
                res += dp(b, a - i)  # Recursive call with swapped and reduced counts
                res %= 10**9 + 7  # Take modulo to prevent overflow
            return res
        
        # Calculate the number of valid arrays starting with a 0 or a 1
        return (dp(zero, one) + dp(one, zero)) % (10**9 + 7)