#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
from collections import Counter

def biggerIsGreater(w):
    # Convert the string into a list of characters
    w = list(w)
    
    # Step 1: Find the rightmost character which is smaller than its next character
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"

    # Step 2: Find the smallest character on the right of the pivot that is larger than the pivot
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    w[i], w[j] = w[j], w[i]  # Swap the pivot with the smallest larger successor

    # Step 3: Reverse the sequence from the pivot + 1 to the end
    w = w[:i + 1] + w[i + 1:][::-1]
    return ''.join(w)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
