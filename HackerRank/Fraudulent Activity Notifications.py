#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

import heapq

def activityNotifications(expenditure, d):
    e = expenditure
    if d ==1:
        res = 0
        for i in range(1,len(e)):
            if e[i] >= e[i-1]*2:
                res+=1
        return res
        
    if n==d:
        return 0
        
    res = 0
    for i in range(d, len(e)):
        # i = d,d+1,..., len(e)
        window = sorted(e[i-d:i])
        if d%2 ==0:
            median = (window[int(d/2-1)] + window[int(d/2)])/2        
        else:
            median = window[d//2]
        if e[i] >= 2*median: res+=1
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
