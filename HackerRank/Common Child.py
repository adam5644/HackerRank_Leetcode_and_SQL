def commonChild(s1, s2):
    # Create a 2D DP array with independent rows
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    # dp[s2][s1]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                # When the characters match, add 1 to the result from the previous indices
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                # If they don't match, carry over the max from either the previous row or column
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # The value in the bottom right corner is the length of the longest common subsequence
    return dp[-1][-1]

# This code is meant to be run on HackerRank, which handles input/output for you.
