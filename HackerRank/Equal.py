#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(chocolates):
    # Minimum chocolates any colleague has.
    min_chocolates = min(chocolates)
    min_operations = float('inf')  # Initialize with a large number.

    # Try potential minimum values from min_chocolates down to min_chocolates - 4
    for base in range(min_chocolates - 4, min_chocolates + 1): # range(-2,3)
        current_operations = 0

        for chocolate in chocolates:
            # Calculate the difference from the current base being tested.
            difference = chocolate - base # 2 -(-2) = 4

            # Calculate the number of operations required to reduce the difference to zero.
            # Start with the largest step size (5), then 2, then 1 to minimize operations.
            five_steps = difference // 5
            two_steps = (difference % 5) // 2 # require 2 two_steps
            one_steps = (difference % 5) % 2

            current_operations += five_steps + two_steps + one_steps

        # Update the minimum operations if the current base results in fewer operations.
        min_operations = min(min_operations, current_operations)

    return min_operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
