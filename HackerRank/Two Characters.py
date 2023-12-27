#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    unique_characters = set(s)
    max_length = 0

    for char1 in unique_characters:
        for char2 in unique_characters:
            if char1 != char2:
                filtered = [c for c in s if c == char1 or c == char2]
                if all(filtered[i] != filtered[i+1] for i in range(len(filtered) - 1)):
                    max_length = max(max_length, len(filtered))

    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
