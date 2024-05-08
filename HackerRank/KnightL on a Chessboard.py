


from collections import deque

def min_knight_moves(n, a, b):
    # Possible movements of the Knight
    moves = [
        (a, b), (a, -b), (-a, b), (-a, -b),
        (b, a), (b, -a), (-b, a), (-b, -a)
    ]
    
    # Initialize the queue and visited set for BFS
    queue = deque([(0, 0, 0)])  # (current_x, current_y, moves_count)
    visited = set([(0, 0)])
    
    while queue:
        x, y, moves_count = queue.popleft()
        
        # Check if the destination is reached
        if x == n - 1 and y == n - 1:
            return moves_count
        
        # Explore all possible knight moves
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves_count + 1))
    
    return -1

# Read input
n = int(input())

# Initialize the results table
results = [[0] * (n - 1) for _ in range(n - 1)]

# Calculate the minimum moves for each (a, b) pair
for a in range(1, n):
    for b in range(1, n):
        results[a - 1][b - 1] = min_knight_moves(n, a, b)
        
for x in results:
    print(x)
print('-------------------------------')

# Print the results
for row in results:
    print(' '.join(map(str, row)))
