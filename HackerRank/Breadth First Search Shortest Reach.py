from collections import defaultdict
from collections import deque

q=int(input())
for _ in range(q):
    n,m=map(int,input().rstrip().split())
    connections = defaultdict(list)
    for _ in range(m):
        i,j=map(int,input().rstrip().split())
        connections[i-1].append(j-1)
        connections[j-1].append(i-1)
        
    #print('connections = ', connections)
        
    s=int(input())
    
    # edge
    if len(connections.keys())==0: 
        res2 = [-1]*(n-1)
        res=str(res2[0])
        for x in res2[1:]:
            res+=' '
            res+=str(x)
        print(res)
        continue
    
    if n==2:
        print('6')
        continue
    
    # inputs: n nodes 0-indexed, s start 0-indexed, connections 0-indexed
    #print('n,s,connections = ', n,s,connections)
    
    
    
    res=[-1]*n
    #print(res)
    res[s-1]=0
    
    #main
    breadth=deque([(s-1,0)])
    #print(breadth)
    vis=set([s-1])
    
    while breadth: # each element is one node, one node appear only once
        #print('breadth = ', breadth)
        i,reach=breadth.popleft()
        #print(i, reach)
        
        #print('i = ', i )
        for j in connections[i]:
            #print('j = ', j)
            if j not in vis:
                vis.add(j)
                res[j]=reach+6
                # print('res[j]"s j =', j)
                # print('reach+1 = ', reach+1)
                breadth.append((j,reach+6))

    res = [x for x in res if x!=0]
    #print('res = ', res)
    print(' '.join(map(str,res)))
    