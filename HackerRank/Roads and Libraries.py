from collections import defaultdict

q = int(input())
for _ in range(q):
    n,m,c_lib,c_road=map(int,input().rstrip().split())
    
    cities=[]
    for _ in range(m):
        cities.append(list(map(int,input().rstrip().split())))
        
    #print(n,c_lib,c_road, cities)
    if c_lib<c_road: 
        print(c_lib*n)
        continue
    if len(cities)==0:
        print(c_lib*n)
        continue
    
    # main
    connections=defaultdict(list)
    for i,j in cities:
        connections[i-1].append(j-1)
        connections[j-1].append(i-1)
    #print('connections = ', connections)
    
    # main
    vis=set()
    clusters=[]
    for i in range(n):
        if i not in vis:
            #print('i = ', i)
            cluster=set([i]) # new cluster
            breadth=set([i]) # breadht of i
            while breadth:
                j=breadth.pop() # j
                if j not in vis:
                    #print('j = ', j)
                    cluster.add(j) # add j to cluster
                    vis.add(j) # visited j
                    breadth=breadth.union(set(connections[j])) # breadth of j
            #print('cluster = ', cluster)
            clusters.append(cluster) # add new cluster to clusters
    #print('clusters = ', clusters)
    
    # main, clusters
    res=0
    res+=c_lib * len(clusters)
    for x in clusters:
        res+=((len(x)-1)*c_road)
    print(res)
    continue
        
    
    
