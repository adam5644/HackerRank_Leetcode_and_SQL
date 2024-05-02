class Solution:
    def maximalSquare(self, matrix) -> int:
        rows, cols = len(matrix), len (matrix[0])
        maxsqlen = 0

        dp = [[0] * (cols ) for _ in range(rows )]

        for i in range( rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        
        for x in dp:
            print(x)
        return maxsqlen * maxsqlen
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","0","1","1","1"],
          ["1","0","1","1","1"]]

print(Solution().maximalSquare(matrix))