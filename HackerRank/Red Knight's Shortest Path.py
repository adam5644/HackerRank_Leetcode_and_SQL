from collections import deque

# Directions in the priority order: UL, UR, R, LR, LL, L
MOVES = [
    (-2, -1, 'UL'),
    (-2, 1, 'UR'),
    (0, 2, 'R'),
    (2, 1, 'LR'),
    (2, -1, 'LL'),
    (0, -2, 'L')
]

def is_in_bounds(n, r, c):
    return 0 <= r < n and 0 <= c < n

def printShortestPath(n, si, sj, ei, ej):
    # Breadth-First Search (BFS)
    queue = deque([(si, sj, [], 0)])  # (row, col, path, count)
    visited = set((si, sj))

    while queue:
        r, c, path, count = queue.popleft()

        if r == ei and c == ej:
            print(count)
            print(' '.join(path))
            return

        for dr, dc, move in MOVES:
            nr, nc = r + dr, c + dc
            if is_in_bounds(n, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, path + [move], count + 1))

    # If no path is found
    print("Impossible")

if __name__ == '__main__':
    # Input
    n = int(input())
    si, sj, ei, ej = map(int, input().split())

    printShortestPath(n, si, sj, ei, ej)