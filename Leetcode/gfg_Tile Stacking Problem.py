# 
n, m, k = 3, 3, 2

dp = [[0 for i in range(4)]  
            for j in range(4)] 
# dp[i][j]=x --> height j, tile size up to (including) i, x valid ways, 
# last tile for each pattern must be the ith tile

presum=[[0 for i in range(4)] 
            for j in range(4)] 
# presum[i][j]=x --> dp[i][1] + dp[i][2] + ... + dp[i][j]
    
# Initializing 0th row to 0 
for i in range(1, n + 1): 
    dp[0][i] = 0
    presum[0][i] = 1
    
# Initializing 0th column to 0 
for i in range(0, m + 1): 
    presum[i][0] = 1
    dp[i][0] = 1
    
# for each from 1 to m 
for i in range(1, m + 1): 
        
    # for each column from 1 to n. 
    for j in range(1, n + 1): 
            
        # for each column from 1 to n 
        # Initializing dp[i][j] to presum  
        # of (i-1,j). 
        dp[i][j] = presum[i - 1][j] # all prev combi + 1 more tile

        if j > k: 
            dp[i][j] -= presum[i - 1][j - k - 1] 
                
    for j in range(1, n + 1): 
        presum[i][j] = dp[i][j] + presum[i][j - 1] 
        
for x in dp: 
    print(x)
print()

for x in presum:
    print(x)
print()

print('dp[m][n]  = ', dp[m][n] )
    