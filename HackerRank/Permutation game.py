#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from functools import cache
def permutationGame(arr):
    def is_increasing(remain):
        return all(remain[i] < remain[i+1] for i in range(len(remain)-1))
    def new_perm(remain, removed):
        return tuple(e for e in remain if e != removed)
    @cache
    def first_wins(remain):
        if is_increasing(remain):
            return False
        return any(not first_wins(new_perm(remain, e)) for e in remain)
    return 'Alice' if first_wins(tuple(arr)) else 'Bob'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
