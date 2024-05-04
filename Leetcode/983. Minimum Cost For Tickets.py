
from functools import cache

class Solution:
    def mincostTickets(self, days, costs) -> int:
        @cache
        def dp(curr_day):
            # Base case: if the current day exceeds the last travel day, return 0.
            if curr_day > days[-1]:
                return 0

            # If the current day is not a travel day, skip to the next day.
            if curr_day not in days:
                return dp(curr_day + 1)

            # Return the minimum cost among the options.
            return min(costs[0] + dp(curr_day + 1),
                       costs[1] + dp(curr_day + 7),
                       costs[2] + dp(curr_day + 30))

        return dp(1)

# Example usage
print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # Output: 11