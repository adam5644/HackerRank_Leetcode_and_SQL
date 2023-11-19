#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    from itertools import combinations
    max_len = 1
    
    a = sorted(a)
    for each in a:
        temp_a = [x - each for x in a]
        temp_len = temp_a.count(0) + temp_a.count(1)
        if temp_len > max_len: max_len = temp_len
    return max_len



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
