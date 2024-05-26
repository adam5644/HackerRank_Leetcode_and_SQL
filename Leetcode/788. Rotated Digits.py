class Solution:
    def rotatedDigits(self, n: int) -> int:
        # does not contain 3,4,7
        # contain at least one 2,5,6,9

        res = 0
        for x in range(1,n+1):
            x=str(x)
            if '3' in x or '4' in x or '7' in x:
                continue
            if '2' in x or '5' in x or '6' in x or '9' in x:
                res+=1

        return res