class Solution:
    def countWays(self, n: int, k: int) -> int:
        MOD = 1000000007
        
        # Base case: if there's only one post, return k (number of colors)
        if n == 1:
            return k
        
        # Initialize for the first two posts
        ways_with_same_color = k # next one has to be diff as prev last
        ways_with_diff_color = k * k # next one can be (k-1) ways. this is because we want next one to be same as prev last one. there is 1 way that is not valid
        
        total_ways = ways_with_diff_color
        
        # Iterate from the third post to the nth post
        for i in range(2, n):
            total_ways = ((ways_with_same_color + ways_with_diff_color) * (k - 1)) % MOD
            ways_with_same_color = ways_with_diff_color
            ways_with_diff_color = total_ways
        
        return total_ways