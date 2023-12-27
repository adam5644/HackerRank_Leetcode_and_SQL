#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    
    if max(arr) < 0:
        return [max(arr),max(arr)]
    
    max_subarray = sum([x for x in arr if x>0])
    
    n = len(arr)
    
    dp = [0]*n # dp[i] is the cumulative max for optimal subsequence so far that ends at index i. 
    
    for i in range(len(dp)):
        dp[i] = max(0, dp[i-1] + arr[i])
        
    max_subsequence = max(dp)
        
    '''
    arr = [-1,2,3,-4,5,10]
    res = [0,2,5,1,6,16]
    '''
        
    
    return [max_subsequence, max_subarray]
    # return [-1, -1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
