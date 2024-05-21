# 


height, width, length, n =  [4, 1, 4, 10], [6, 2, 5, 12], [7, 3, 6, 32], 4


# List to store all possible rotations of boxes
rotations = []

# Generate all possible rotations for each box and add to rotations list
for i in range(n):
    h = height[i]
    w = width[i]
    l = length[i]
    rotations.append([[h, w], l])  # Rotation with base (h, w)
    rotations.append([[w, h], l])  # Rotation with base (w, h)
    rotations.append([[h, l], w])  # Rotation with base (h, l)
    rotations.append([[l, h], w])  # Rotation with base (l, h)
    rotations.append([[w, l], h])  # Rotation with base (w, l)
    rotations.append([[l, w], h])  # Rotation with base (l, w)

dp = [0 for _ in range(len(rotations))]

# rotations[0] = [[1, 2], 3] = [[l,w], h]

# Sort the rotations lexicographically by base dimensions (width, length)
rotations.sort()

# Iterate over all rotations to calculate the maximum stack height
for i in range(len(rotations)):
    # Initialize the height of the current box rotation
    dp[i] = rotations[i][1] # [i][1] is height
    for j in range(i):
        # Check if the current box can be placed on top of the previous box
        if rotations[i][0][0] > rotations[j][0][0] and rotations[i][0][1] > rotations[j][0][1]:
            # Update dp[i] to the maximum height by placing current box on previous box
            dp[i] = max(dp[i], dp[j] + rotations[i][1])

# Return the maximum height from all possible stack heights
print(max(dp))