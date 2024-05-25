class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # res=0
        # n=len(s)
        # l,r = 0,n-1
        # while l<r:
        #     if s[l] == s[r]:
        #         res+=2
        #         l+=1
        #         r-=1
        #     else:
        #         l+=1

        # return res

        n=len(s)
        s2 = s[::-1]
        dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(
                        dp[i-1][j], dp[i][j-1]
                    )

        #for x in dp: print(x)

        return dp[-1][-1]