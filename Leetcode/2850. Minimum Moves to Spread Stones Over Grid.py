class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        global res
        res = float("inf")

        def helper(cur, moves):
            global res
            if moves >= res:
                return

            if cur == 9:
                res = min(res, moves)
                return

            # curr = 1 to 9 inclusive
            # 
            i = cur // 3
            j = cur % 3

            if grid[i][j] != 0:
                helper(cur + 1, moves)

            # grid[i][j] == 0
            for x in range(3):
                for y in range(3):
                    if grid[x][y] > 1:
                        grid[x][y] -= 1
                        grid[i][j] += 1
                        helper(cur + 1, moves + abs(i - x) + abs(j - y))
                        grid[x][y] += 1
                        grid[i][j] -= 1

        helper(0, 0)
        return res
