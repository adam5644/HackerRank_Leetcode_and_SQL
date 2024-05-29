
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and mat[i][j]:
                    dp[i][j] = 1
                elif mat[i][j]:
                    dp[i][j] = dp[i - 1][j] + 1

        for x in dp: print(x)
        print()

        total = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    for k in range(j + 1, n + 1):
                        total += min(dp[i][j:k])
                        print('i,j,k = ', i,j,k)
                        print('dp[i][j:k] = ', dp[i][j:k])
                        print('total = ', total)
                        print()
                    

        return total
        