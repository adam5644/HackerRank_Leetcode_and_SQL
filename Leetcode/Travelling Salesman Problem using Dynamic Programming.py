# 

from functools import lru_cache

n = 4  # there are four nodes in example graph (graph is 1-based)
 
# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using 
# all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
    0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]


@lru_cache(None)
def fun(i, mask):
    # base case
    # if only ith bit and 1st bit is set in our mask,
    # it implies we have visited all other nodes already
    if mask == ((1 << i) | 3): # 1 means unvisited 
        return dist[1][i]
 
    res = float('inf')  # result of this sub-problem
 
    # we have to travel all nodes j in mask and end the path at ith node
    # so for every node j in mask, recursively calculate cost of 
    # travelling all nodes in mask
    # except i and then travel back from node j to node i taking 
    # the shortest path take the minimum of all possible j nodes
    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1: # (mask & (1 << j)) != 0  --> if true, it means j has been visited 
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    
    return res
 
# Driver program to test above logic
ans = float('inf')
for i in range(1, n+1):
    # try to go from node 1 visiting all nodes in between to i
    # then return from i taking the shortest route to 1
    ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])
 
print("The cost of most efficient tour = " + str(ans))