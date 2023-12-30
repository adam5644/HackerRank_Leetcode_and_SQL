#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq
# heapq.heappush()
# heapq.heappop()
# heapq.heapify()

def cookies(k, A):
    if not A: 
        #print('here')
        return -1
    
    heapq.heapify(A)
    
    
    c = 0
    
    while A:
        # print('c = ', c)
        # print('A = ', A)
        # print()
                
        if A[0] >= k:
            return c
        if len(A) == 1 and A[0] < k:
            # print('here2')
            return -1
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        new = a + 2*b
        heapq.heappush(A, new)
        c+=1
    
    # print('here3')
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
