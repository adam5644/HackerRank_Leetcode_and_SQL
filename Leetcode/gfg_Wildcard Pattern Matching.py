
pattern = 'd****a***b**c'
s='dsfsabc'

n, m = len(s), len(pattern)

# Create a DP table with (n+1) x (m+1) dimensions
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# An empty pattern can match an empty string
dp[0][0] = 1

# Fill in the first row where the pattern contains '*'
for j in range(1, m+1):
    if pattern[j-1] == '*':
        dp[0][j] = dp[0][j-1]
        
for x in dp: print(x)

# Fill the rest of the DP table
for i in range(1, n+1):
    for j in range(1, m+1):
        if pattern[j-1] == '*':
            dp[i][j] = dp[i-1][j] or dp[i][j-1]
        elif pattern[j-1] == '?' or pattern[j-1] == s[i-1]:
            dp[i][j] = dp[i-1][j-1]

print()
for x in dp: print(x)

print(dp[n][m])