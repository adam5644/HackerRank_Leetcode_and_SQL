#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def remove1(s, i):
    if i >= len(s) - 1:  # Adjust for index range
        return s
    if len(s) <= 1:
        return s
    if s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        return remove1(s, 0)  # Start from the beginning after a reduction
    else:
        return remove1(s, i+1)

def superReducedString(s):
    reduced_s = remove1(s, 0)
    if len(reduced_s) == 0:  # Check if the string is empty after reduction
        return "Empty String"
    else:
        return reduced_s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
