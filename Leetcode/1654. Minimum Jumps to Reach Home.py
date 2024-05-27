# 
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden=set(forbidden)
        #u=max(x,max(forbidden))+a+b
        u = 10000
        
        if 0 in forbidden:
            return -1
        q=[(0,False)]

        c=0

        while q:
            for i in range(len(q)):
                p,canback=q.pop(0)
                if p==x:
                    return c

                if canback and p-b>0 and p-b not in forbidden:
                    q.append((p-b,False))
                    forbidden.add(p-b)

                if p+a<=u and p+a not in forbidden:
                    q.append((p+a,True))
                    forbidden.add(p+a)
            c+=1

        return -1


 