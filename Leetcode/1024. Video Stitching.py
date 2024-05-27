# 

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        minn = min(x[0] for x in clips)
        maxx=max(x[1] for x in clips)
        if minn!=0 and maxx<time: return -1

        last_st = 0
        last_ed = 0

        res = 0
        temp = -1

        while last_ed<time:
            print('--------------------')
            

            for a,b in clips:
                if a<=last_ed<=b and b>temp:
                    temp=b

            #print('temp = ', temp)
            if last_ed!=temp:
                last_ed = temp
                res+=1
            else:
                return -1

            print('last_ed = ', last_ed)


        return res