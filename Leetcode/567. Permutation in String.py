class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        d1 = Counter(s1)
        for i in range(0, len(s2) - l1 + 1):
            d2 = Counter(s2[i:i + l1])
            if d1 == d2:
                return True
        return False