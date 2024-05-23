# 474. Ones and Zeroes
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [[x.count('0'), x.count('1')] for x in strs]
        res = float('-inf')
        size = len(strs)

        @cache
        def dfs(i, c0, c1, cum):
            nonlocal res
            if c0 > m or c1 > n: 
                return

            if cum> res: 
                res = cum

            # if i == size:  # Base case when reaching the end of the list
            #     nonlocal res
            #     res = max(res, cum)
            #     return
                
            if i <= size-1:
                dfs(i + 1, c0 + strs[i][0], c1 + strs[i][1], cum + 1)
                dfs(i + 1, c0, c1, cum)

        dfs(0, 0, 0, 0) # cum of 0, c0 of 0, c1 of 0, when we have yet to choose i
        return res