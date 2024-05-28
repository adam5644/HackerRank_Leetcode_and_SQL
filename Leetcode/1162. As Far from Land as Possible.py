class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        # print('queue = ', queue)


        # if len(queue) == 0 or len(queue) == n**2:
        #     return -1

        # distance = -1

        # while queue:
        #     distance += 1

        #     for _ in range(len(queue)):
        #         x, y = queue.pop(0)

        #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
        #                 grid[nx][ny] = 1
        #                 queue.append((nx, ny))

        # return distance


        n=len(grid)

        stack=[]

        # stack=[()] # (i,j) = land
        for i in range(n):
            for j in range(n):
                if grid[i][j]: stack.append((i,j))
        directions=[(-1,0), (1,0), (0,-1), (0,1)]

        if not len(stack) or len(stack)==n*n: return -1

        res=-1
        while stack:
            for _ in range(len(stack)): 
                i,j=stack.pop(0) # deque
                
                for dx,dy in directions:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<=n-1 and 0<=nj<=n-1 and not grid[ni][nj]:
                        grid[ni][nj] = 1
                        stack.append((ni,nj))
                        
            res+=1

        return res
                
                
    
        