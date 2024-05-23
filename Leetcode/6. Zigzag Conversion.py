# 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # c=[x for x in range(0,4)]
        # c=c+c[::-1][1:-1]
        # print(c)

        # edge
        if len(s) == 1: return s[0]
        if numRows==1: return s

        # main
        res=[[] for _ in range(numRows)]

        loop=[x for x in range(numRows)]
        loop=loop+loop[::-1][1:-1]

        maxx=numRows*2-2
        c = 0

        for x in s:
            if c==maxx: c=0
            res[loop[c]].append(x)
            c+=1

        res2 = ''
        for i in range(numRows):
            for j in res[i]:
                res2+=j

        return res2