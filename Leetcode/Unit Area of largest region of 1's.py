from functools import lru_cache

class Solution:

        #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
    	    n,m=len(grid),len(grid[0])
    	    moves=[[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    	    
    	    #@lru_cache(None)
    		def dfs(x,y):
    		    grid[x][y]=-1
    		    ans=1
    		    for i,j in moves:
    		        nx=x+i
    		        ny=y+j
    		        if 0<=nx<=n-1 and 0<=ny<=m-1 and grid[nx][ny]==1:
    		            ans+=dfs(nx,ny)
    		    return ans
    		    
    		maxarea=0
    		for i in range(n):
    		    for j in range(m):
    		        if grid[i][j]==1:
    		            maxarea = max(maxarea,dfs(i,j))
    		return maxarea