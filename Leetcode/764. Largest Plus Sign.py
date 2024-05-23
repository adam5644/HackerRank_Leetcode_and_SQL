class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(n)]
        for x in grid: print(x)
        print()

        for i in range(n):
            for j in range(n):
                grid[i][j] = min(i+1, j+1, n-i, n-j)

        for x in grid: print(x)
        print()

        for mine in mines:
            a, b = mine
            for i in range(n):
                grid[a][i] = min(abs(i-b), grid[a][i])
                grid[i][b] = min(grid[i][b], abs(a-i))

        for x in grid: print(x)

        return max(max(grid[i]) for i in range(n))

        