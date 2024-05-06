class Solution:
  def removeStones(self, stones: List[List[int]]) -> int:
    visited = set()
    def dfs(i,j):     
      if (i,j) in visited: 
        return 0
      visited.add((i,j))
      ans=0
      for x,y in stones:  
        if (i==x or j==y) and (x,y) not in visited: 
          ans+=1+dfs(x,y)       
      return ans

    ans=0
    for x,y in stones:
      ans+=(dfs(x,y))
    return ans 