# 

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        @lru_cache(1000)
        def dfs(i,j,summ):
            # base
            if i>j: return 0

            # main
            return max(
                summ-stones[i] - dfs(i+1, j , summ-stones[i]),
                summ-stones[j] - dfs(i, j-1, summ-stones[j])
            )


        # init
        n = len(stones)
        return dfs(0,n-1,sum(stones))