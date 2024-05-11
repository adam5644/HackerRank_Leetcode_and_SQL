from collections import defaultdict

n,p=map(int,input().rstrip().split())

connections = defaultdict(list)
for _ in range(p):
    i,j = list(map(int,input().rstrip().split()))
    connections[i].append(j)
    connections[j].append(i)
    
# print(connections)
clusters=[]
vis = set()
for i in range(n):
    if i not in vis:
        cluster=set([i]) # new cluster for j
        breadth=set([i]) # inititate breadth
        
        while breadth: # while more to add to this cluster
            j=breadth.pop()
            if j not in vis:
                cluster.add(j) # add to cluster
                vis.add(j) # j visited
                breadth=breadth.union(set(connections[j]))
                
        clusters.append(cluster) # this cluster completed
        
res =0
for a in range(len(clusters)):
    for b in range(a+1, len(clusters)):
        res+=(len(clusters[a])*len(clusters[b]))
print(res)
        
