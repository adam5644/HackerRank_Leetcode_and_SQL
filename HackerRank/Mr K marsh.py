def kMarsh(grid):
    rows = len(grid)  # Get the total number of rows in the grid
    cols = len(grid[0])  # Get the total number of columns in the grid
    up = [[0] * cols for _ in range(rows)]  # Prepare a matrix to store the distance above for each cell
    left = [[0] * cols for _ in range(rows)]  # Prepare a matrix to store the distance to the left for each cell
    
    # Fill the matrices with the distances to the nearest marsh to the left and above each cell
    for i in range(rows):
        for j in range(cols):
            if j > 0:  # Avoiding index out of range error for the first column
                left[i][j] = left[i][j - 1] + 1 if grid[i][j - 1] != 'x' else 0
            if i > 0:  # Avoiding index out of range error for the first row
                up[i][j] = up[i - 1][j] + 1 if grid[i - 1][j] != 'x' else 0
    
    max_perimeter = 0  # Initialize the maximum perimeter found to 0
    # Check each cell to see if it can be the bottom-right corner of a rectangle
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] != 'x':  # We only consider non-marshy cells
                print('i = ', i)
                print('j = ', j)
                a = i - up[i][j]  # Calculate the upper boundary of the potential rectangle
                b = 0  # Initialize the left boundary of the potential rectangle
                # Expand the rectangle to the maximum possible size and check if its perimeter is the largest found so far
                while a < i and 2 * (i - a) + 2 * (j - b) > max_perimeter:
                    # Calculate the leftmost boundary by checking the distance above and to the left
                    b = max(j - left[a][j], j - left[i][j])
                    # Keep shifting left boundary right until we hit a marshy cell or the boundary of the rectangle
                    while up[i][b] < i - a and b < j and 2 * (i - a) + 2 * (j - b) > max_perimeter:
                        b += 1
                    # If a valid rectangle is found that is larger than the current maximum, update max_perimeter
                    if b < j and left[i][j] >= j - b and grid[a][b] != 'x':
                        print('a = ', a)
                        print('b = ', b)
                        print('curr perimter = ', 2 * (i - a) + 2 * (j - b))
                        max_perimeter = max(max_perimeter, 2 * (i - a) + 2 * (j - b))
                    a += 1  # Move the upper boundary down one row
                    b = 0  # Reset the left boundary for the next iteration
                print('---------------------')

    # Output the result: either the maximum perimeter found or 'impossible' if no rectangle can be formed
    print(max_perimeter if max_perimeter > 0 else 'impossible')

# Test cases
grid1 = [
    "....",
    "..x.",
    "..x.",
    "x..."
]

grid2 = [
    ".....",
    ".x.x.",
    ".....",
    "....."
]

grid3 = [
    ".x",
    "x."
]

grid4 = [
    ".....",
    "xxxx."
]

# Execute test cases
kMarsh(grid1) # Expected output: 10
kMarsh(grid2) # Expected output: 14
kMarsh(grid3)# Expected output: "impossible"
kMarsh(grid4) # Expected output: "impossible"