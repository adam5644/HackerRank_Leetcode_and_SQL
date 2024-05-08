# Input
n = int(input())
m = int(input())
matrix = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    matrix.append(temp)

# Directions (vertical, horizontal, diagonal)
directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

def dfs(i, j):
    global temp_res
    # Base case
    if (i, j) in vis or i < 0 or j < 0 or i >= n or j >= m:
        return
    vis.add((i, j))
    if matrix[i][j] == 1:
        temp_res += 1
        for ii, jj in directions:
            dfs(i + ii, j + jj)

# Initialize
res = 0
vis = set()

# Main loop
for i in range(n):
    for j in range(m):
        if (i, j) not in vis and matrix[i][j] == 1:
            global temp_res
            temp_res = 0
            dfs(i, j)
            res = max(res, temp_res)

print(res)
