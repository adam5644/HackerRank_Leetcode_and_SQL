# n = int(input())
# vals = list(map(int,input().split()))
# t = sum(vals)

# adjLi = [[] for i in range(n)]

# for i in range(n-1):
#     u,v = map(int,input().split())
#     adjLi[u-1].append(v-1)
#     adjLi[v-1].append(u-1)

# totVal = [0]*n
# explored = []
# waiting = {i for i in range(n) if len(adjLi[i]) == 1}
# while(len(waiting)):
#     for i in waiting:
#         totVal[i] += vals[i]
#         if(len(adjLi[i])):
#             adjLi[adjLi[i][0]].remove(i)
#             totVal[adjLi[i][0]] += totVal[i]
#     waiting = {adjLi[i][0] for i in waiting if len(adjLi[i]) and len(adjLi[adjLi[i][0]]) == 1}

# rt = abs(t- 2*totVal[0])
# for i in range(1,n):
#     k = abs(t-2*totVal[i])
#     if k < rt:
#         rt = k

















from collections import deque

n = int(input())
data = list(map(int, input().rstrip().split()))
edges = []
for _ in range(n-1):
    edges.append(list(map(int,input().rstrip().split())))
    
# print('n = ', n)
# print('data = ', data)
# print('edges = ', edges)

edges2 = []
for a,b in edges:
    edges2.append([a-1,b-1])
edges = edges2

connections = [deque([]) for _ in range(n)]
for a,b in edges:
    connections[a].append(b)
    connections[b].append(a)
    
sum_root=[0]*n

leaves = [node for node,branches in enumerate(connections) if len(branches)==1]
# print('leaves = ', leaves)

while leaves:
    new_leaves = []
    for leaf in leaves:
        sum_root[leaf]+=data[leaf]
        
    #     for branches in connections[leave]:
    #          if len(connections[branches])>=1:
    #             #print('connections = ', connections)
    #             connections[branches].popleft()
    #             sum_root[branches]+=sum_root[leave]
    #     connections[leave]=[]
        
    # #leaves = [node for node,branches in enumerate(connections) if len(branches)==1]
    

        if connections[leaf]:  # Check if there is a parent node
            parent = connections[leaf][0]
            connections[parent].remove(leaf)  # Remove the current leaf from the parent
            sum_root[parent] += sum_root[leaf]  # Update the parent's sum

            if len(connections[parent]) == 1:  # If the parent becomes a leaf
                new_leaves.append(parent)

        connections[leaf] = []  # Clear the connections of the processed leaf

    leaves = new_leaves  # Update leaves for the next iteration

    
# print('sum_root = ', sum_root)
# print('leaves = ', leaves)
# print('connections = ', connections)

# summ = sum(data)
# res = float('inf')
# for x in sum_root:
#     a = summ-x
#     diff = abs(a-x)
#     if diff< res: res=diff
    
# print(diff)


# Find the minimum difference
total_sum = sum(data)
res = float('inf')

for x in sum_root:
    diff = abs(total_sum - 2 * x)
    if diff < res:
        res = diff

print(res)




















# from collections import deque

# # Input Parsing
# n = int(input())
# data = list(map(int, input().rstrip().split()))
# edges = []
# for _ in range(n - 1):
#     edges.append(list(map(int, input().rstrip().split())))

# # Adjust edges to be 0-indexed
# edges = [[a - 1, b - 1] for a, b in edges]

# # Initialize connections (adjacency list)
# connections = [deque([]) for _ in range(n)]
# for a, b in edges:
#     connections[a].append(b)
#     connections[b].append(a)

# # Initialize sum of nodes starting with 0s
# sum_root = [0] * n

# # Find all initial leaf nodes
# leaves = [node for node, branches in enumerate(connections) if len(branches) == 1]

# # Process all leaves until no leaves are left
# while leaves:
#     new_leaves = []
#     for leaf in leaves:
#         sum_root[leaf] += data[leaf]  # Add the node's own value

#         if connections[leaf]:  # Check if there is a parent node
#             parent = connections[leaf][0]
#             connections[parent].remove(leaf)  # Remove the current leaf from the parent
#             sum_root[parent] += sum_root[leaf]  # Update the parent's sum

#             if len(connections[parent]) == 1:  # If the parent becomes a leaf
#                 new_leaves.append(parent)

#         connections[leaf] = []  # Clear the connections of the processed leaf

#     leaves = new_leaves  # Update leaves for the next iteration

# # Find the minimum difference
# total_sum = sum(data)
# res = float('inf')

# for x in sum_root:
#     diff = abs(total_sum - 2 * x)
#     if diff < res:
#         res = diff

# print(res)





























# from collections import deque

# # Input Parsing
# n = int(input("Enter number of nodes: "))
# data = list(map(int, input("Enter node values: ").rstrip().split()))
# edges = []
# for _ in range(n - 1):
#     edges.append(list(map(int, input("Enter an edge: ").rstrip().split())))

# # Adjust edges to be 0-indexed
# edges = [[a - 1, b - 1] for a, b in edges]

# # Initialize connections (adjacency list)
# connections = [deque([]) for _ in range(n)]
# for a, b in edges:
#     connections[a].append(b)
#     connections[b].append(a)

# # Initialize sum of nodes starting with 0s
# sum_root = [0] * n

# # Find all initial leaf nodes
# leaves = [node for node, branches in enumerate(connections) if len(branches) == 1]

# # Process all leaves until no leaves are left
# while leaves:
#     new_leaves = []
#     for leaf in leaves:
#         sum_root[leaf] += data[leaf]  # Add the node's own value

#         if connections[leaf]:  # Check if there is a parent node
#             parent = connections[leaf][0]
#             connections[parent].remove(leaf)  # Remove the current leaf from the parent
#             sum_root[parent] += sum_root[leaf]  # Update the parent's sum

#             if len(connections[parent]) == 1:  # If the parent becomes a leaf
#                 new_leaves.append(parent)

#         connections[leaf] = []  # Clear the connections of the processed leaf

#     leaves = new_leaves  # Update leaves for the next iteration

# print('sum_root = ', sum_root)