x = 10
n=2
dp = [1] + [0] * x
for i in range(1, int(pow(x, 1 / n)) + 1):
    u = i ** n
    for j in range(x, u - 1, -1):
        dp[j] += dp[j - u]
print(dp[-1])