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

def cost(B):
    # Get the length of the array B
    L = len(B)
    
    # Initialize a dynamic programming table where
    # dp[i][0] represents the max cost if A[i] = 1
    # dp[i][1] represents the max cost if A[i] = B[i]
    dp = [[0] * 2 for _ in range(L)]
    
    # Iterate over each element in B starting from the second element
    for i in range(1, L):
        # Update dp for A[i] = 1
        # Max of: 
        #   1. Continuing with A[i-1] = 1, add |1 - 1| = 0
        #   2. let a[i-1] = b[i-1], hence add |B[i-1] - 1|
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + abs(B[i-1] - 1))
        
        # Update dp for A[i] = B[i]
        # Max of: 
        #   1. Continuing with A[i-1] = 1, add |B[i] - 1|
        #   2. let a[i-1] = b[i-1], hence add |B[i-1] - 1|, hence add |B[i] - B[i-1]|
        dp[i][1] = max(dp[i-1][0] + abs(B[i] - 1), dp[i-1][1] + abs(B[i] - B[i-1]))

    # Return the maximum value possible at the last position in B
    # This will be the maximum of either ending with A[L-1] = 1 or A[L-1] = B[L-1]
    return max(dp[L-1][0], dp[L-1][1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
