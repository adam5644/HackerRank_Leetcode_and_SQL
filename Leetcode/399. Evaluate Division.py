
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        first_second = defaultdict(list)
        for a,b in equations:
            first_second[a].append(b)
            first_second[b].append(a)
        first_second_ans = defaultdict(list)
        for i, ans in enumerate(values):
            first_second_ans[equations[i][0]].append(ans)
            first_second_ans[equations[i][1]].append(1/ans)

        # print('first_second = ', first_second)
        # print('first_second_ans = ', first_second_ans)

        def branch(nums_visited, cum_value, curr_num, end):
            #print('nums_visited, cum_value, curr_num, end = ', nums_visited, cum_value, curr_num, end)
            if curr_num == end:
                #print('return cum_value = ', cum_value)
                return cum_value

            max_list = []
            for i, nxt in enumerate(first_second[curr_num]):
                #print('nxt = ', nxt)
                if nxt not in nums_visited:
                    # print('nxt = ', nxt)
                    # print('i = ', i)
                    temp = first_second_ans[curr_num][i]
                    #print('temp = ', first_second_ans[curr_num][i])
                    cum_value *= temp
                    nums_visited_temp = nums_visited.copy()
                    nums_visited_temp.append(nxt)
                    #print('nums_visited_temp = ', nums_visited_temp)
                    max_list.append(branch(nums_visited_temp, cum_value, nxt, end))
            if max_list:
                return max(max_list)
            else:
                #print('return -1.0')
                return -1.0

        res = []
        for start,end in queries:
            #print('start,end = ', start,end)
            if start not in  first_second or end not in first_second:
                ans=-1.0
            elif start ==end:
                ans = 1.0
            else:
                if first_second_ans[start]:
                    possiblities = [
                        branch(
                            [start, nxt], first_second_ans[start][i], nxt, end
                        ) for i, nxt in enumerate(first_second[start])
                    ]
                    #print('possiblities = ', possiblities)
                    ans = max(possiblities)

            res.append(ans)
            #print('-------------------------------')

        return res