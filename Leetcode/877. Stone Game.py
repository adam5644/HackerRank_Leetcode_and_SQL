class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        from functools import lru_cache

        n = len(piles)

        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            # Calculate the difference in score if picking the left or right pile
            pick_left = piles[l] - dp(l + 1, r)
            pick_right = piles[r] - dp(l, r - 1)
            # The current player will choose the option with the maximum difference
            return max(pick_left, pick_right)

        alice = dp(0, n - 1)
        return alice > 0