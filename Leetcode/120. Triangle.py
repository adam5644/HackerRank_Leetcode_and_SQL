class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)

        # edge
        if n==1: return triangle[0][0]

        dp=triangle[-1]
        print('initial dp = ', dp)

        for i in range(n-2,-1,-1): # n=4, i=2,1,0
            for j in range(i+1):
                # i=1: j=0,1,2

                dp[j]=triangle[i][j] + min(dp[j],dp[j+1])

            print('dp = ', dp)

        print('final, dp = ', dp)
        return dp[0]