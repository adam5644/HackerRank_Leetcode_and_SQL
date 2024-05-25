class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, v, adj):
	    if len(adj)<=1:
	        return 0
	    
	    
		#Code here
# 		print('V = ',v)
# 		print('adj = ', adj)
# V =  5
# adj =  [[2, 3, 4], [3], [0, 4], [0, 1], [0, 2]]

        n=len(adj)
        parent=[i for i in range(n)]
        rank=[1]*n
        vis=set()
        
        def find(i):
            if i!=parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i,j):
            pi = find(i)
            pj=find(j)
            if rank[pi]>rank[pj]:
                parent[pj]=pi
                rank[pi]+=rank[pj]
            else:
                parent[pi]=pj
                rank[pj]+=rank[pi]
                
        # main
        for i in range(n):
            for j in adj[i]:
                if (i,j) in vis or (j,i) in vis:
                    continue
                
                vis.add((i,j))
                p1=find(i)
                p2=find(j)
                if p1==p2: 
                    # print('parent = ', parent)
                    # print('rank = ', rank)
                    # print('vis = ', vis)
                    print('parent = ', parent)
                    print('rank = ', rank)
                    print('vis = ', vis)
                    return 1
                
                union(i,j)
                
                
        print('parent = ', parent)
        print('rank = ', rank)
        print('vis = ', vis)
        return 0