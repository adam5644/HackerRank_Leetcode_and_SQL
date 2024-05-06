# 

class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms)
        if len(rooms[0]) == 0: return False

        # main
        vis = set([0])
        def goto(i, cum):
           # print('i, cum = ', i, cum)
            for j in rooms[i]:
                if j in vis: continue
                vis.add(j)
                goto(j, cum+[j])

        # initiate
        goto(0,[0])
        if len(vis) == n: return True
        return False