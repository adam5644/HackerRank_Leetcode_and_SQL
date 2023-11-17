#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr) # arr = [[1,2,3],[...],....], n =3
    
    posi = 0 
    sum1 = 0
    for _ in range(n): # e.g. n = 2. 
                    # _ = 0,1 .posi = 0,1,2
        sum1 += arr[posi][posi]
        posi += 1

    right_to_left = n-1 # col
    up_to_down = 0 # row
    # arr[row][col]
    
    sum2 = 0
    for _ in range(n): 
        # _ = 0,1
        # right_to_left = 2,1,0
        
        sum2+= arr[up_to_down][right_to_left]
        right_to_left -= 1
        up_to_down+=1
        
    return abs(sum1 - sum2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
