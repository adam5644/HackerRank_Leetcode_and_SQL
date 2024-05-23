# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # edge
        if word1 == word2: return 0
        if len(word1)==1 and len(word2)==1 and word1!=word2: return 2

        # main
        res = float('inf')

        @cache
        def dfs(deleted, w1, w2):
            #print('deleted, w1, w2 = ', deleted, w1, w2)

            nonlocal res
            if deleted>res: return

            if not w1 and not w2:
                if deleted< res: 
                    res=deleted
                return     
            
            if w1==w2:
                if deleted< res: 
                    res=deleted
                return

            if not w1 and w2:
                deleted+=len(w2)
                if deleted< res: 
                    res=deleted
                return
            if w1 and not w2:
                deleted+=len(w1)
                if deleted< res: 
                    res=deleted
                return


            # main
            if w1[0]==w2[0]:
                dfs(deleted, w1[1:], w2[1:])
            else:
                if len(w1)>0:
                    dfs(deleted+1, w1[1:], w2)
                if len(w2)>0:
                    dfs(deleted+1, w1, w2[1:])


        # init
        dfs(0, word1, word2)
        return res