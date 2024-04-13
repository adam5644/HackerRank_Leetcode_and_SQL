#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    
    nums = [i+1 for i in range(n)] # 1 indxing
    
    if k==0:
        return nums
    if n%(2*k)!=0:
        return [-1]
    
    #print('n-2*k+1 = ', n-2*k+1)
    for i in range(0,n-2*k+1,2*k):
        #print('i = ', i)
        
        for j in range(k):
            nums[i+j], nums[i+j+k] = nums[i+j+k], nums[i+j]
            
    #return ''.join(str(i) for i in nums)
    return nums
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
