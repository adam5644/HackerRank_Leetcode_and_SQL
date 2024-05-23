# 808. Soup Servings
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        
        @cache
        def dfsoup(a, b):
            if a <= 0:
                if b <= 0:
                    return 0.5
                else:
                    return 1
            elif b <= 0:
                return 0
            return 0.25 * (dfsoup(a-100, b) + dfsoup(a-75, b-25) + dfsoup(a-50, b-50) + dfsoup(a-25, b-75))
        
        return dfsoup(n, n)             
