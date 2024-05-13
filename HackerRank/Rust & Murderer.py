
not_visited = roads[start_loc]
newly_visited = set()
curr_dist = 2
while not_visited:
    # print('not_visited = ', not_visited)
    for i in not_visited:
        
        # print('i=',i)
        # print('not_visited = ', not_visited)
        # print('roads[i] = ', roads[i])
        diff = not_visited.union(roads[i]) # nodes not visited union with children of i
        #print('diff = ', diff)
        
        if len(diff) < n:
            dists[i-1] = curr_dist
            #print('dists[i-1] = ', dists[i-1])
            # dists[i-1] =  2
            # dists[i-1] =  3
            newly_visited.add(i)
            
    not_visited = not_visited - newly_visited
    newly_visited = set()
    curr_dist += 1

# print('dists = ', dists) # dists =  [1, 3, 1, 2]
    
del dists[start_loc-1]
print(" ".join(str(i) for i in dists)) # 3 1 2
# print('*')