#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    # Write your code here
    if n == 1 and m == 1:
        return 0
        
    if n == 1:
        return m -1
        
    if m == 1:
        return n -1
    
    else:
        res = (n*m) - 1
        
        
    return res
    
# 841251657 841251657
# 707704350405245648


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'],'w')
    
    n, m = input().strip().split()
    n = int(n)
    m = int(m)
    res = solve(n,m)
    f.write(str(res) + '\n')
    f.close()
    
    
    
    


    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # result = solve(n, m)

    # fptr.write(str(result) + '\n')

    #fptr.close()
    