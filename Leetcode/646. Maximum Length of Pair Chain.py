# 646. Maximum Length of Pair Chain
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # edge
        if len(pairs)==1: return 1

        # main
        pairs=sorted(pairs, key=lambda x: (x[1],-x[0]))
        #print('pairs = ', pairs)

        head,tail = pairs[0]

        res = 1
        for a,b in pairs[1:]:
            if tail<a:
                res+=1
                head,tail = a,b
        return res
        # 2