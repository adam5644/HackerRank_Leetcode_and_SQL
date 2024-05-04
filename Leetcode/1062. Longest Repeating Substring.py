from collections import Counter

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if len(s) == 1: return 0
        c=Counter(s)
        c2 = {k:v for k,v in c.items() if v>=2}
        res = float('-inf')
        n=len(s)
        #print('n = ',n)

        for i,x in enumerate(s):
            count, word, j, s2, s3 = 0, x, i, s[:i], s[i+1:]
            #print('i = ', i )
            #print('s2 = ', s2)

            while (word in s2 or word in s3) and j+1<=n-1:
                #print('inside word = ', word)
                count+=1
                j+=1
                #print('j = ', j)
                word+=s[j]
            res = max(res, count)   
            #print('------------')         

        return res