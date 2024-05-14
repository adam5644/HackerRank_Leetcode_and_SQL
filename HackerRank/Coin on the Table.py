n,m,k=map(int,input().rstrip().split())
graph=[]
for _ in range(n):
    graph.append(input())
    
from heapq import heappush, heappop, heapify
from functools import cache
# #edge
















def possible(i,j,left):
    if left<0: 
        return False
    if not 1<=i<=n or not 1<=j<=m: 
        return False
    return True
    
def f(n,m,k,graph):
    # main
    b=[(0,1,1,k)]

    # u,l,d,r
    #(i-1,j),(i,j-1),(i+1,j),(i,j+1)
    
    vis=set()

    while b:
        #print('b = ',b)
        
        c,i,j,left=heappop(b)
        #print('c,i,j,left = ', c,i,j,left)
        if (i,j, left) in vis: continue
        vis.add((i,j, left))
                
        #print('graph[i-1][j-1] = ', graph[i-1][j-1])
        
        if graph[i-1][j-1]=='*': 
            print(c)
            return
                    
        if not possible(i,j,left): 
            #print('not possible')
            continue
        #main
        # if graph[i-1][j-1]=='U':
        #     heappush(b,(c,i-1,j,k-1)) # u
        #     heappush(b,(c+1,i,j-1,k-1))#l
        #     heappush(b,(c+1,i+1,j,k-1)) # d
        #     heappush(b,(c+1,i,j+1,k-1))#r
        # elif graph[i-1][j-1]=='L':
        #     heappush(b,(c+1,i-1,j,k-1)) # u
        #     heappush(b,(c,i,j-1,k-1))#l
        #     heappush(b,(c+1,i+1,j,k-1)) # d
        #     heappush(b,(c+1,i,j+1,k-1))#r
        # elif graph[i-1][j-1]=='D':
        #     heappush(b,(c+1,i-1,j,k-1)) # u
        #     heappush(b,(c+1,i,j-1,k-1))#l
        #     heappush(b,(c,i+1,j,k-1)) # d
        #     heappush(b,(c+1,i,j+1,k-1))#r
        # elif graph[i-1][j-1]=='R':
        #     heappush(b,(c+1,i-1,j,k-1)) # u
        #     heappush(b,(c+1,i,j-1,k-1))#l
        #     heappush(b,(c+1,i+1,j,k-1)) # d
        #     heappush(b,(c,i,j+1,k-1))#r
 
        directions = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
        current_dir = graph[i-1][j-1]
        for dir, (di, dj) in directions.items():
            ni, nj = i + di, j + dj
            new_left = left - 1
            if possible(ni, nj, new_left):
                new_cost = c if dir == current_dir else c + 1
                if (ni, nj, new_left) not in vis:
                    heappush(b, (new_cost, ni, nj, new_left))

    #print('****')
    print(-1)
    return
    
f(n,m,k,graph)


# def f(n, m, k, graph):
#     heap = [(0, 1, 1, k)]  # cost, row, column, remaining moves
#     visited = set()

#     while heap:
#         cost, i, j, left = heappop(heap)
        
#         if (i, j, left) in visited:
#             continue
#         visited.add((i, j, left))
        
#         if left < 0:
#             continue
#         if graph[i-1][j-1] == '*':
#             print(cost)
#             return
        
#         # Directions mapping
#         directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
#         for direction, (di, dj) in directions.items():
#             ni, nj = i + di, j + dj
#             if 1 <= ni <= n and 1 <= nj <= m:
#                 new_cost = cost if graph[i-1][j-1] == direction else cost + 1
#                 if (ni, nj, left-1) not in visited:
#                     heappush(heap, (new_cost, ni, nj, left-1))

#     print(-1)
    
# f(n,m,k,graph)



 
# def possible(n, m, i, j, left):
#     # Check if it's possible to reach '*' based on the remaining moves and distance to the target
#     return left >= 0 and 1 <= i <= n and 1 <= j <= m

# def f(n, m, k, graph):
#     # Starting position (1, 1) with 0 changes and k moves allowed
#     b = [(0, 1, 1, k)]
#     visited = set()  # To avoid revisiting the same state

#     while b:
#         c, i, j, left = heappop(b)
        
#         # Avoid revisiting the same cell with the same or fewer moves left
#         if (i, j, left) in visited:
#             continue
#         visited.add((i, j, left))

#         if graph[i-1][j-1] == '*':
#             print(c)
#             return c
        
#         # Explore all 4 possible directions
#         directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
#         for dir in directions:
#             ni, nj = i + directions[dir][0], j + directions[dir][1]
#             if possible(n, m, ni, nj, left-1):
#                 if graph[i-1][j-1] == dir:
#                     heappush(b, (c, ni, nj, left-1))
#                 else:
#                     heappush(b, (c+1, ni, nj, left-1))

#     # If no solution found
#     print(-1)
#     return -1

 
# f(n, m, k, graph)
