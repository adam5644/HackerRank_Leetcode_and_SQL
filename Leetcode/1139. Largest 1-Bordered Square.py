import copy  # Import the copy module to use deepcopy

class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(A), len(A[0])
        
        # Initialize the result to 0 (default if no 1-bordered square is found)
        res = 0
        
        # Create deep copies of the grid A for top and left matrices
        top, left = copy.deepcopy(A), copy.deepcopy(A)
        # top[i][j] = consecutive i above index i,j
        
        # Build the top and left matrices
        for i in range(m):
            for j in range(n):
                if A[i][j]:  # If the current cell is 1
                    if i:  # If not in the first row
                        top[i][j] = top[i - 1][j] + 1  # Increment top count from the cell above
                    if j:  # If not in the first column
                        left[i][j] = left[i][j - 1] + 1  # Increment left count from the cell to the left
        
        for x in top: print(x)
        print()
        for x in left: print(x)
        print()

        # Check for the largest possible 1-bordered square
        for r in range(min(m, n), 0, -1):  # Start from the largest possible square size

            # top side of square = i
            # left side of square = j
            for i in range(m - r + 1):  
                for j in range(n - r + 1):  
                    # Check if there are enough consecutive 1s on all four borders of the square
                    if min(top[i + r - 1][j],  # Left border
                           top[i + r - 1][j + r - 1],  # Right border
                           left[i][j + r - 1],  # Top border
                           left[i + r - 1][j + r - 1]  # Bottom border
                          ) >= r:  # All borders should have at least 'r' consecutive 1s
                        return r * r  # Return the area of the square (side length squared)
        
        return 0  # If no valid square is found, return 0