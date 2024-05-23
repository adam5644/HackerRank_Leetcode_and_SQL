# 518. Coin Change II
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP array to store the number of ways to make change for each amount
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make amount 0 - using no coins
        
        # Main DP update loop
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]