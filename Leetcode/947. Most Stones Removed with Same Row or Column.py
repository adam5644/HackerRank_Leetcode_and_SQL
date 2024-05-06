# 947. Most Stones Removed with Same Row or Column

class Solution:
    def removeStones(self, stones) -> int:
        
        def dfs(x, y):
            seen.add((x, y))
            for x2, y2 in stones:
                if (x == x2 or y == y2) and (x2, y2) not in seen:
                    dfs(x2, y2)
            
        seen = set() # set of set
        cnt = 0
        
        for x, y in stones:
            if (x, y) not in seen:
                dfs(x, y)
                cnt += 1
                
        return len(stones) - cnt

#stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
#stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
#stones = [[0,0]]
stones = [[0,1],[1,1]] # 1
print(Solution().removeStones(stones))