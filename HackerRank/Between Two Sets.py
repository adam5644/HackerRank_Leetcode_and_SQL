#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    res = 0 
    max1 = max(max(a),max(b))
    min1 = min(min(a),min(b))
    for each_int in range(min1, max1+1):
        each_a_true = True 
        each_b_true = True
        for each_a in a:
            if each_int % each_a != 0: each_a_true = False
        for each_b in b:
            if each_b % each_int != 0: each_b_true = False
        if each_a_true and each_b_true:
            res +=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
