class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # for x in obstacleGrid:
        #     print(x)
        # return(0)

        if obstacleGrid[0][0]==1:return 0

        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=[[0 for _ in range(c+1)] for _ in range(r+1) ]
        dp[1][1]=1


        for i in range(1,r+1):
            for j in range(1,c+1):
                #print('i,j = ', i,j)
                if i==1 and j==1:
                    continue
                elif obstacleGrid[i-1][j-1]==0:
                    # print('i,j = ', i,j)
                    # print('dp[i-1][j] = ', dp[i-1][j])
                    # print('dp[i][j-1] = ', dp[i][j-1])
                    # print('dp[i][j] = ', dp[i][j])
                    # print()
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        # for x in dp:
        #     print(x)
            
        return dp[-1][-1]