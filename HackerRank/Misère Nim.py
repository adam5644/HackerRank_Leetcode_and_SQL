#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Calculate the XOR-sum of all piles
    xor_sum = 0
    for stones in s:
        xor_sum ^= stones

    # Special case: all piles have one stone
    if all(stones == 1 for stones in s):
        return 'First' if len(s) % 2 == 0 else 'Second'
    else:
        # General case: standard Nim strategy
        return 'First' if xor_sum != 0 else 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
