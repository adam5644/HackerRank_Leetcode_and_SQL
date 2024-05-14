arr =  [999, 1, 1, 1, 0]
n = len(arr)


# dp[i] will store the maximum score you can achieve starting from brick i
dp = [0] * (n + 1)

# total_sum[i] will store the sum of all bricks from i to the end
total_sum = [0] * (n + 1)
# Calculate the total sums from the back
for i in range(n - 1, -1, -1):
    total_sum[i] = total_sum[i + 1] + arr[i]
# print('total_sum = ', total_sum)

# Base cases
dp[n] = 0  # No bricks to take
for i in range(n - 1, -1, -1):
    # Check if there are fewer than 3 bricks after the current brick i
    if i + 3 < n:
        # Calculate the minimum dp value from the next three possible positions
        # dp[i+1], dp[i+2], and dp[i+3] represent the scores opponent can get starting from those positions
        min_score_next_moves = min(dp[i + 1], dp[i + 2], dp[i + 3])
        # Set the current dp[i] as the total sum of bricks from i to the end minus the minimum score from next moves
        # This is because your opponent tries to leave you with the least advantageous position
        dp[i] = total_sum[i] - min_score_next_moves
    else:
        # If there are less than three bricks left, take all of them
        dp[i] = total_sum[i]

print('dp = ', dp)
print('ans = ',dp[0])