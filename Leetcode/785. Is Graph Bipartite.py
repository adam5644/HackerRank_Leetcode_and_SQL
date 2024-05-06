# 

from collections import defaultdict

class Solution:
    def isBipartite(self, graph) -> bool:
        n=len(graph)
        if n == 1: 
            #print('aaa')
            return True

        # main
        d = defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                d[i].append(j)
        #print('d = ', d)

        i_grp = defaultdict(int)

        def assign_grp(i, grp):
            #print('i, grp = ', i, grp)
            # base
            if i_grp[i] !=0:
                if i_grp[i] != grp: 
                    #print('False')
                    #print('bb')
                    return False
                else: 
                    #print('True')
                    return True
            i_grp[i] = grp
            # main
            for j in d[i]:
                if not assign_grp(j, -grp): 
                    #print('cc')
                    return False
            return True
                
        # initiate recursion
        for i in range(n):
            if i_grp[i]==0:
                if not assign_grp(i, 1): 
                    #print('dd')
                    return False

        #print('i_grp = ', i_grp)
        return True