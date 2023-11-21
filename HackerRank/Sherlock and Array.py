#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    left = 0
    right = sum(arr[1:])
    # print('left = ', left)
    # print('right = ', right)
    # print('\nstart')
    
    if arr.count(0) == len(arr) - 1:
        return 'YES'

    for i in range(1, len(arr)-1):
        left += arr[i-1]
        right -= arr[i]
        # print(' i = ', i)
        # print('arr[i-1] = ', arr[i-1])
        # print('left = ', left)
        # print('right = ', right)
        if left == right: return 'YES'
    
    # print()
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
