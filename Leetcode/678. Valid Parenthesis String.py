class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0: # more ) already
                return False
            if leftMin < 0: # left<0 and leftmin<0 only if leftmin<0 because of 0, hence ok
                leftMin = 0

            # print('c = ', c)
            # print('leftMin, leftMax = ', leftMin, leftMax)

        return leftMin == 0