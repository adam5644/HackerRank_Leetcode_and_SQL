#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    res = 0
    r = len(A)
    c = len(A[0])
    for i in range(r):
        for j in range(c):
            # up, down
            res += 2
            # left, all if leftmost 
            if i==0:
                res += A[i][j]
            else:
                res += max(0, A[i][j]- A[i-1][j])
            # right
            if i == r-1:
                res += A[i][j]
            else:
                res += max(0, A[i][j] - A[i+1][j])
                            
            # front
            if j==0:
                res += A[i][j]
            else:
                res += max(0, A[i][j] - A[i][j-1])
            
            # back
            if j == c-1:
                res += A[i][j]
            else:
                res += max(0, A[i][j] - A[i][j+1])
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
