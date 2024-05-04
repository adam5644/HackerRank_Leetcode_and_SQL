
class Solution:
    def twoEggDrop(self, n: int) -> int:
        # x = 0
        # while x * (x + 1) // 2 < n:
        #     x += 1
        # return x
        change = 1
        cum = 0
        while cum < n:
            cum += change
            change +=1
            #print('cum = ', cum)
        return change -1