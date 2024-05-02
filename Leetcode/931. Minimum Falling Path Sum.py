
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # for x in matrix:
        #     print(x)

        m,n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = matrix[0]

        for i in range(1,m):
            for j in range(n):

                dp[i][j] = min(
                    dp[i-1][max(0,j-1)], dp[i-1][j], dp[i-1][min(n-1,j+1)]
                    ) + matrix[i][j]

                # print('top left = ', dp[i-1][max(0,j-1)])
                # print('dp[i-1][j] = ', dp[i-1][j])
                # print('dp[i-1][min(n-1,j+1)]) = ', dp[i-1][min(n-1,j+1)])
                # print('matrix[i][j] = ', matrix[i][j])
                # print('dp[i][j] = ', dp[i][j])
                # print()

        # print('matrix')
        # for x in matrix:
        #     print(x)

        # print('dp')
        # for x in dp:
        #     print(x)

        return min(dp[-1])