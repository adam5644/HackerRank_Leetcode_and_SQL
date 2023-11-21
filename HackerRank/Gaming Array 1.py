#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    p = 'ANDY'
    
    curr_max = float('-inf')
    for x in arr:
        # print('x = ', x)
        if x > curr_max:
            if p == 'BOB': p = 'ANDY'
            else: p = 'BOB'
            curr_max = x
            # print('p changed')
            # print('p = ', p)
    print()
    return p
        
    
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
