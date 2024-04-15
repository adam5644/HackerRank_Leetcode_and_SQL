#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k): # [1, 2, 3, 4, 5] 1

    x = sorted(x)
    #logic
    # 2 4 5 6 7 9 12
    # Go as right as possible for first iteration
    # Again go as right as possible for second iteration
    # what does this mean that place transmitter in a such way that it will handle houses on left and right sides comfortably
    # So first you are at left most position.. iterate over and find middle position where (middle-left==k) and then find right most position where (right-middle<=k)

    count_trans = 0
    last = x[0]
    i = 0
    n = len(x)
    while(i < n):
        count_trans = count_trans + 1
        next_point = x[i] + k
        while(i < n and x[i] <= next_point):
            i = i + 1
        next_point = x[i-1] + k
        while(i < n and x[i] <= next_point):
            i = i + 1
            
    return count_trans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
