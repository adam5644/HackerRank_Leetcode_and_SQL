#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

from collections import Counter 

def nonDivisibleSubset(k, s):
    # Write your code here
    remainder = [i%k for i in s]
    remainder_counter = Counter(remainder)
    #print(remainder_counter)
    
    res = 0
    unique = remainder_counter.keys()
    #print('k//2= ', k//2)
    
    for i in range(k//2+1):
        if i == k-i and remainder_counter[i] >= 1:
            res+= 1
        elif i != 0:
            res += max(remainder_counter[i], remainder_counter[k-i])
            
        elif i == 0 and remainder_counter[0] >= 1: # at most 1 '0'
            res+=1
        # print('i = ', i)
        # print('res = ',res)

    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
