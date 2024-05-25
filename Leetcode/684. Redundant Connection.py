class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]

        def find(i):
            while par[i] != i:
                i = par[i]
            return i

        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return True
            else:
                par[p1] = p2
                return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                return edge