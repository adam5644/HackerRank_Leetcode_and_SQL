class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # edge
        if len(connections)< n-1: return -1


        def find(i):
            if i != parent[i]:
                parent[i]=find(parent[i])
            return parent[i]

        def union(i,j):
            p1=find(i)
            p2=find(j)
            if p1!=p2:
                if rank[p1]<=rank[p2]:
                    p1,p2=p2,p1
                rank[p1]+=rank[p2]
                parent[p2]=p1
                

        # main
        parent=[x for x in range(n)]
        rank=[1]*n
        vis=set()

        for i,j in connections:
            if (i,j) in vis or (j,i) in vis: continue
            union(i,j)

        for i in range(n):
            find(i)

        print('parent = ', parent)
        return len(set(parent)) - 1