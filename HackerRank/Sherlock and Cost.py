#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(b):
    # Write your code here
    n=len(b)
    dp=[[0,0] for _ in range(n)]
    
    for i in range(1,n):
        #print('i=',i)
        # print('dp[i-1][0] = ', dp[i-1][0])
        # print('dp[i-1][1] + abs(1-b[i-1]) = ', dp[i-1][1] + abs(1-b[i-1]))
        dp[i][0]=max(dp[i-1][0], dp[i-1][1] + abs(1-b[i-1]))
        
        # print('dp[i-1][0] = ', dp[i-1][0])
        # print('dp[i-1][1] = ', dp[i-1][1])
        dp[i][1]=max(dp[i-1][0] + abs(b[i]-1), dp[i-1][1] + (abs(b[i]-b[i-1])))
        #print('dp=',dp)
    return max(dp[n-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
