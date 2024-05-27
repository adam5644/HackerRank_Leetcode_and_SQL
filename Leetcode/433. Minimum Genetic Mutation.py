# 

from heapq import heappush, heappop

class Solution:
    def minMutation(self, st: str, ed: str, bank: List[str]) -> int:

        # EDGE
        if ed not in bank: return -1

        # may not have intermediate mutation

        stack=[(0, st)] # (cum_steps, currStr)
        vis=set() # add currStr

        while stack:
            cum_steps,curr = heappop(stack)
            #print('cum_steps,curr = ', cum_steps,curr)

            if curr in vis: continue
            vis.add(curr)

            if curr==ed: return cum_steps

            for b in bank:
                #print('b = ', b)
                diff = 0
                for x,y in zip(b,curr):
                    if diff>1: break
                    if x!=y: diff+=1

                if diff==1: 
                    heappush(stack, (cum_steps+1, b))

        return -1