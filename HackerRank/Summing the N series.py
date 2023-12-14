#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):

    
    ap = (n/2)*(2+ (n-1)*2)
    return int(ap % (10**9 + 7))



    
'''
1, 1
4, 3
9, 5
16, 7
25, 9
36, 11
47, 13 
'''
    

# def summingSeries(n):
#     return (n * n) % (10**9 + 7)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'],'w')
    n = int(input().strip())
    for _ in range(n):
        res = summingSeries(int(input().strip()))
        f.write(str(res) + '\n')
    
    f.close()
    
    
    
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     result = summingSeries(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
