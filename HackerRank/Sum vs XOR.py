#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Count the number of zeros in the binary representation of n
    zeros_count = bin(n)[2:].count('0')
    
    # The answer is 2 to the power of zeros_count
    # Special case: if n is 0, the answer should be 1
    return 1 if n == 0 else 2**zeros_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
