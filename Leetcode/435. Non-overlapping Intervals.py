
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        res = 0
        cur_end = float('-inf')
        a = sorted(intervals, key=lambda x : x[1])
        print('a  = ', a)

        for s, e in a:
            print('s = ', s)

            if s >= cur_end:
                cur_end = e
            else:
                res += 1
        return res

#test = [[1,3],[2,10],[3,4],[5,9]]
test = [[1,4],[2,10],[3,4],[5,9]]
print('ans = ', Solution().eraseOverlapIntervals(test))
