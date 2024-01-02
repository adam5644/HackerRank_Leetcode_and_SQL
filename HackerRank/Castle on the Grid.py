import math
import os
import random
import re
import sys



from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    c = 0
    visit = set()
    q = deque([([startX, startY, c])])
    moves = [[1,0], [-1,0], [0,1], [0,-1]]

    # main logic
    while q:
        pathx, pathy, c = q.popleft()
        c += 1

        for xi, yi in moves:
            x, y = pathx, pathy
            while True:
                x, y = x+xi, y+yi
                # check the condition
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.':
                    if x == goalX and y == goalY:
                        return c
                    elif (x, y) not in visit:
                        visit.add((x, y))
                        q.append([x, y, c])
                else:
                    break
            
grid = ['...', 
        '.X.', 
        '.X.']
startX, startY, goalX, goalY = 2,0,0,2
result = minimumMoves(grid, startX, startY, goalX, goalY)
print(result)