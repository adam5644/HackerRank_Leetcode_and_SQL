n,m=map(int,input().rstrip().split())
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
# print(n,m)
# print(a)
# print(b)

dp = [[0] * (n + 1) for _ in range(m + 1)]

# Fill the dp table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            

lcs = []
x, y = m, n
while x > 0 and y > 0:
    if b[x - 1] == a[y - 1]:
        lcs.append(b[x - 1])
        x -= 1
        y -= 1
    elif dp[x - 1][y] > dp[x][y - 1]:
        x -= 1
    else:
        y -= 1
lcs=lcs[::-1]
print(" ".join(str(x) for x in lcs))