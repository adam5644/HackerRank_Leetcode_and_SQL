#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr = sorted(arr)
    
    global_min = float('inf')
    for index in range(0,len(arr)-k+1):  #o(n)
        temp_list = arr[index: index+k]
        temp_min = temp_list[-1] - temp_list[0]
        if temp_min < global_min:
            global_min = temp_min
    
    return global_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    # k = 3
    # arr = [10,100,300,200,1000,20,30]
    # print(maxMin(k, arr))
