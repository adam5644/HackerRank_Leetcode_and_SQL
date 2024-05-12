from collections import *
import sys

graph = defaultdict(list)
N,E = map(int,input().split())
for _ in range(E):
    u,v,c = map(int,input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))
start,end = map(int,input().split())

# inputs
# print(N)
# print(graph)
# print(start,end)
# 3
# defaultdict(<class 'list'>, {1: [(2, 1), (2, 1000), (3, 100)], 2: [(1, 1), (1, 1000), (3, 3)], 3: [(2, 3), (1, 100)]})
# 1 3

dq=deque()
distance=[ dict()  for j in range (N+1)]
dq.append((start,0))
distance[start][0] = 0
print('distance = ', distance)
'''BFS'''
while dq:
    print('dq = ', dq)
    vertex,dist = dq.popleft()
    for k,v in graph[vertex]:
        cost = v|dist
        '''Calculate the new cost , if cost is not in the dictionary of that node it means it is new so add it.Do not add cost that is greater then 1024 as that is the limit.'''
        if cost not in distance[k]: 
            distance[k][cost] = 1
            dq.append((k,cost))
    print('distance=',distance)
    print()
    
if distance[end]:
    print(sorted(distance[end])[0])  
else:
    "-1" 