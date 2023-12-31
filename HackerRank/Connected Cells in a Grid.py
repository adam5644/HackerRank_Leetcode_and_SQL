def dfs(matrix, row, col, visited):
    # Base condition to stop recursion if we're out of bounds, or at a cell with 0, or already visited
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0 or visited[row][col]:
        return 0
    
    # Mark the current cell as visited
    visited[row][col] = True
    
    # Start the count with the current cell
    count = 1
    
    # Visit all 8 neighbors (horizontally, vertically, and diagonally)
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr != 0 or dc != 0: # Avoid the cell itself
                count += dfs(matrix, row + dr, col + dc, visited)
    
    return count

def connectedCell(matrix):
    # Initialize the result and a visited matrix
    res = 0
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    # Go through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not visited[row][col]:
                # Perform DFS and update the result if we found a larger region
                res = max(res, dfs(matrix, row, col, visited))
    
    return res