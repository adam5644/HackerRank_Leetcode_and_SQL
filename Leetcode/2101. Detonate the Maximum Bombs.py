class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, G = len(bombs), defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i!=j and bombs[i][2]**2 >= (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2:
                    G[i].append(j)

        print('G = ', G)
        
        def dfs(i,visited): # function to populate visited for i. it recursively calls bombed indexes too
            for node in G[i]:
                if node not in visited:
                    visited.add(node)
                    dfs(node,visited)
        
        ans = 0
        for i in range(n):
            visited = set([i])
            dfs(i,visited)
            ans = max(ans,len(visited))

        return ans
