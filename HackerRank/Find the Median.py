#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # # Write your code here
    # arr = arr.sort()
    # print(arr)
    # posi = len(arr)//2
    # print(posi)
    # res = arr[posi]
    # print(res)
    # return res
    
    arr = sorted(arr)
    res = arr[len(arr)//2]
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
