from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        if n == 1:
            return 0

        # Initialize DP arrays
        dp_sell = [0] * n
        dp_buy = [0] * n
        dp_cooldown = [0] * n

        # Initial states
        dp_buy[0] = -prices[0]
        dp_sell[0] = 0
        dp_cooldown[0] = 0

        for i in range(1, n):
            dp_buy[i] = max(dp_buy[i - 1], dp_cooldown[i - 1] - prices[i])
            dp_sell[i] = dp_buy[i - 1] + prices[i]
            dp_cooldown[i] = max(dp_cooldown[i - 1], dp_sell[i - 1])

        return max(max(dp_sell), max(dp_buy), max(dp_cooldown))
