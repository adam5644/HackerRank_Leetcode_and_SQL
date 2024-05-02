
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_matrix = [[0]*n for _ in range(m)]
        for row in range(m):
            dp_matrix[row][0] = 1
        for column in range(n):
            dp_matrix[0][column] = 1
        for row in range(1, m):
            for column in range(1, n):
                dp_matrix[row][column] = dp_matrix[row-1][column] + dp_matrix[row][column-1]
        
        return dp_matrix[row][column]