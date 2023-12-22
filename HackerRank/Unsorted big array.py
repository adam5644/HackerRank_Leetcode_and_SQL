#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Sort the array using a key that first considers the length of the string
    # and then the lexicographical order
    res2 = sorted(unsorted, key=lambda x: (len(x), x))
    return res2

# Rest of the code remains the same


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
