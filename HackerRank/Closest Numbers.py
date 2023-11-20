#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    min_diff = float('inf')
    min_diff_lst = []
    
    from itertools import combinations
    
    for a,b in combinations(arr, 2):
        diff = abs(a - b)
        if diff == min_diff:
            min_diff_lst.append(a)
            min_diff_lst.append(b)
        
        elif diff < min_diff:
            min_diff_lst = []
            min_diff_lst.append(a)
            min_diff_lst.append(b)
            min_diff = diff

            
        # print('a = ', a)
        # print('b = ', b)
        # print('type(a) = ', type(a))
        # print('type(b) = ', type(b))

        # print()
            
    return min_diff_lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
