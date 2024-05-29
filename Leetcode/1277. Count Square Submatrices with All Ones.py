class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        matrix=[
            [1,1,0,0],
            [1,1,1,1],
            [0,1,1,1],
            [0,1,1,1]
        ]
        # Iterate through the matrix starting from the second row and second column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # Only update if the current cell is 1
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        for x in matrix: print(x)
        # Sum up all values in the matrix to get the total number of square submatrices
        return sum(map(sum, matrix))