576. Out of Boundary Paths

class Solution:
    def findPaths(self, maxRow: int, maxCol: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def move(r, c, left):
            if (r, c, left) in memo:
                return memo[(r, c, left)]
            
            if left < 0:
                return 0
            
            # If the ball is out of the boundary, return 1
            if r < 0 or r >= maxRow or c < 0 or c >= maxCol:
                return 1
            
            # Calculate the number of paths for each direction
            up = move(r-1, c, left-1)
            down = move(r+1, c, left-1)
            left_move = move(r, c-1, left-1)
            right = move(r, c+1, left-1)
            
            # Store the result in memo dictionary to use later
            memo[(r, c, left)] = (up + down + left_move + right) % MOD

            return memo[(r, c, left)] # number of path at this r,c,left
        
        return move(startRow, startColumn, maxMove)

# Example usage:
sol = Solution()
print(sol.findPaths(2, 2, 2, 0, 0))  # Output: 6