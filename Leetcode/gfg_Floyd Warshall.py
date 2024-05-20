class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Initialize the distance matrix
        for i in range(n):
            for j in range(n):
                if i != j and matrix[i][j] == -1:
                    matrix[i][j] = float('inf')

        # Apply Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # Convert 'inf' back to -1 to signify no path
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1