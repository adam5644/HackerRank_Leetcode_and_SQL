# 

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if len(s) > len(t):
            s, t = t, s
        Ns = len(s)
        Nt = len(t)
        N = len(s)

        total = 0
        for i in range(Ns):
            for j in range(Nt):

                count = 0
                for L in range(N):
                    if i + L >= Ns or j + L >= Nt:
                        break
                    if s[i + L] != t[j + L]:
                        count += 1
                    if count == 1:
                        total += 1
                    if count>1:
                        break

        return total