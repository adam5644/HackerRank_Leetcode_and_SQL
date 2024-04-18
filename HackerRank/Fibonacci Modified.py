#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

# def fibonacciModified(t1, t2, n):
#     # Write your code here
    
#     n-=2
#     while n>0:
#         t2, t1 = t1 + t2**2, t2
#         n-=1
        
#     return t2

import sys
sys.set_int_max_str_digits(0)
def fibonacciModified(t1, t2, n):
    sys.int_max_str_digits = 0
    for x in range(n-2):
        tn=t1+t2**2
        t1=t2
        t2=tn
    return tn
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
