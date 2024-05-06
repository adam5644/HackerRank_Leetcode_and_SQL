# 
class Solution:
    def findCircleNum(self, isConnected) -> int:
        n=len(isConnected)
        # edge
        if n==1: return 1

        # main
        vis= set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in vis: 
                    vis.add(j)
                    print('same p, i = ',j )
                    dfs(j)

        res = 0
        for i in range(n):
            if i not in vis:
                dfs(i)
                res +=1
        return res

