class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        from collections import deque

        # a = deque([1,2,3])
        # a.append(4)
        # print(a)
        # a.appendleft(5)
        # print(a)
        # print(a.pop())
        # print(a.popleft())

        def valid(curr):
            global res
            d = deque()
            for x in curr:
                if x == '(':
                    d.append(x)
                else:
                    if len(d) ==0:
                        # print('curr = ', curr)
                        # print('123false')
                        return
                    else:
                        d.popleft()
            if d:
                # print('curr = ', curr)
                # print('123false')
                return
            else:
                # print('curr = ', curr)
                # print('123true')
                res.append(curr)
                return

        def find_combi(curr, count):
            global combi
            if count == length-1:
                combi.append(curr+')')
                return
            find_combi(curr+'(', count+1)
            find_combi(curr+')', count+1)

        length = n*2
        global combi, res
        combi = []
        res = []
        find_combi('(',1)
        #print('combi = ', combi)

        for i in combi:
            valid(i)

        #print('res = ', res)
        return res

        
        

