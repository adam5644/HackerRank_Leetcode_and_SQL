
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, interval = [], newInterval
        for idx, curr in enumerate(intervals):
            if curr[1] < interval[0]:
                res.append(curr)
            elif interval[1] < curr[0]:
                res.append(interval)
                return res + intervals[idx:]
            else:
                interval[0] = min(curr[0], interval[0])
                interval[1] = max(curr[1], interval[1])
        res.append(interval)
        return res
        