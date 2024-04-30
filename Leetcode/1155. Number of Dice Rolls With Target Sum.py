class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target == n: return 1
        if target < n: return 0
        if n ==1:
            if target <= k:
                return 1
            elif target > k:
                return 0
        if k ==1:
            if n == k: return 1
            else: return 0
        if target ==1:
            if n == 1: return 1
            else: return 0
        if n == 1 and k ==1: 
            if t == 1: return 1
            else: return 0
        if k ==1 and t==1: 
            if n ==1: return 1
            else: return 0
        if n==1 and k==1 and t==1:
            return 1
        if n*k < target: return 0

        dp=[[0 for _ in range(num_dice*k + 1)] for num_dice in range(n+1)]
        # dp[num_dice][sum] = num of possible ways , e.g. dp[2][3]=x means 2 dice sum to 3 has x ways

        dp[1] = [1] * (k+1)
        #print(dp)

        for total_dice in range(2, n+1):
            for last_dice_sum in range(1,k+1): # last dice roll what sum
                for other_dice_sum in range(total_dice-1, len(dp[total_dice -1])):
                    #p[1][last_dice_sum]

                    # print(dp)
                    # print('total_dice - 1 = ', total_dice - 1)
                    # print('other_dice_sum = ', other_dice_sum)
                    # dp[total_dice - 1][other_dice_sum]

                    dp[total_dice][last_dice_sum + other_dice_sum] += dp[total_dice - 1][other_dice_sum]

        #print(dp)
        
        return dp[n][target]%(10**9+7)

# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         MOD = 10**9 + 7
#         # Initialize a DP table where dp[i][j] represents the number of ways to get sum j with i dice
#         dp = [[0] * (target + 1) for _ in range(n + 1)]
#         dp[0][0] = 1  # Base case: one way to get sum 0 with 0 dice

#         # Populate the DP table
#         for dice in range(1, n + 1):
#             for roll in range(1, k + 1):
#                 for current_target in range(roll, target + 1):
#                     dp[dice][current_target] = (dp[dice][current_target] + dp[dice - 1][current_target - roll]) % MOD

#         # The desired result is the number of ways to achieve 'target' with 'n' dice
#         return dp[n][target]