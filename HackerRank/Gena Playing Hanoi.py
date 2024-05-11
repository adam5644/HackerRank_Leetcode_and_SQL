n = int(input())
disk_rod = list(map(int,input().rstrip().split()))
num_disk=len(disk_rod)
#print(n, disk_rod)
rod_disk = [[],[],[],[]]
for disk,rod in enumerate(disk_rod):
    rod_disk[rod-1].append(disk)
#print(rod_disk)



from collections import deque


def is_valid(rod_disk):
    return (len(rod_disk[0]) == num_disk)
# rod_disk=((0,1),(2),(0))
# print('is_valid(rod_disk) = ', is_valid(rod_disk))


def tupify(rod_disk):
    return tuple(tuple(x) for x in rod_disk)

def listify(rod_disk):
    return list(list(x) for x in rod_disk)

def valid_moves(rod_disk):
    for i in [0,1,2,3]:
        if rod_disk[i]: 
            for j in [0,1,2,3]:
                if not rod_disk[j] or rod_disk[i][0]<rod_disk[j][0]:
                    yield (i,j)
                    
def make_move(rod_disk,i,j):
    #print('start rod_disk', rod_disk)
    rod_disk=listify(rod_disk)
    num_to_move = rod_disk[i][0]
    rod_disk[i] = rod_disk[i][1:]
    rod_disk[j] = [num_to_move]+rod_disk[j]
    #print('end rod_disk', rod_disk)
    return tupify(rod_disk)


def bfs(rod_disk):
    rod_disk = tupify(rod_disk)
    vis=set(rod_disk) # e.g. vis[0] = (rod_disk, 0 )
    breadth=deque([(rod_disk,0)])
    #print('breadth[0] = ', breadth[0])
    
    while breadth:
        rod_disk, depth = breadth.popleft()
        #print('rod_disk, depth = ', rod_disk, depth)
        #print('rod_disk = ', rod_disk) # rod_disk=((0,1,2),(),())
        if is_valid(rod_disk): return depth
        
        for i,j in valid_moves(rod_disk):
            #print(i,j)
            child=make_move(rod_disk,i,j)
            if child not in vis:
                vis.add(child)
                breadth.append((child, depth+1))
        


print(bfs(rod_disk))