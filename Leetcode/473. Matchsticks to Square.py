# 473. Matchsticks to Square
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4:
            return False
        target = s // 4

        curr = [0, 0, 0, 0]

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            length = matchsticks[idx]
            for side in range(4):
                if curr[side] + length <= target:
                    curr[side] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    curr[side] -= matchsticks[idx]
            return False
        
        matchsticks.sort(reverse=True)
        return dfs(0)