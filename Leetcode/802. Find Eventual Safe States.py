class Solution:
    def eventualSafeNodes(self, graph):
        visited = [0] * len(graph)
        
        def dfs(n):
            if visited[n] == -1:
                return False
            if visited[n] == 1 :
                return True
            visited[n] = -1
            for  node in graph[n]:
                if not dfs(node):
                    visited[n] = -1 
                    return False
                    
            visited[n] = 1
            return True

        ans  = []
        for i in range(len(graph)):
            if dfs(i): # true if its a safe node
                ans.append(i)
        return ans
    
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution().eventualSafeNodes(graph))