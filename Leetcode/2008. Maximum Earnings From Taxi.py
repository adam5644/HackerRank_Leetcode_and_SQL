class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0]*(n+1)
        rides.sort()

        for i in range(n-1, -1, -1):
            dp[i] = dp[i + 1]
            while rides and rides[-1][0] == i:
                s, e, t = rides.pop()
                dp[i] = max(dp[i], dp[e] + e - s + t)

        print('dp = ', dp)

        return dp[0]        