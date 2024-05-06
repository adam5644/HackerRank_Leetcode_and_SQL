# 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # edge
        n = len(graph)
        if n ==2: 
            if 1 not in graph[0]: 
                return 0

        # main
        res = []
        def dfs(cum, last):
            # base
            if last == n-1: 
                if cum not in res:
                    res.append(cum)
                return
            # main
            for j in graph[last]:
                if j not in cum:
                    dfs(cum+[j], j)

        # initiate
        dfs([0],0)
        return res