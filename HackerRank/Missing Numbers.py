#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    arr = sorted(arr)
    brr = sorted(brr)
    
    from collections import Counter
    # for key in dic_a.keys:
    #      if val_a != value_b or key not in :
    #           res.append(val_a)
    # do same for dic_b
    
    dict_a = Counter(arr)
    dict_b = Counter(brr)
    
    res = []

    for key, value in dict_a.items():
        if key not in dict_b.keys():
            if key not in res:
                res.append(key)
        elif value != dict_b[key]:
            if key not in res:
                res.append(key)
                
    for key, value in dict_b.items():
        if key not in dict_a.keys():
            if key not in res:
                res.append(key)
        elif value != dict_a[key]:
            if key not in res:
                res.append(key)
                
    return sorted(res)
            
            
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
