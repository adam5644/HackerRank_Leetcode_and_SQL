import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        b, s = [], []
        heapq.heapify(b)
        heapq.heapify(s) # min-heap[0] is minimum value
        
        for p,a,o in orders:
            if o == 0:
                heapq.heappush(b, [-p, a])
            elif o == 1:
                heapq.heappush(s, [p, a])
            
            while s and b and s[0][0] <= -b[0][0]:
                a1, a2 = b[0][1], s[0][1]
                
                if a1 > a2:
                    b[0][1] -= a2
                    heapq.heappop(s)
                elif a1 < a2:
                    s[0][1] -= a1
                    heapq.heappop(b)
                else:
                    heapq.heappop(b)
                    heapq.heappop(s)
                    
        count = sum([a for p,a in b]) + sum([a for p,a in s])
        return count % (10**9 + 7)

# Test case
sol = Solution()
print(sol.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))
