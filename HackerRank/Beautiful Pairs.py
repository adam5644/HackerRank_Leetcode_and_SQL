#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

from collections import Counter

def beautifulPairs(A, B):
    from collections import Counter

    # Count frequencies of each number in both arrays
    countA = Counter(A)
    countB = Counter(B)

    # Calculate initial beautiful pairs
    beautiful_pairs = sum(min(countA[num], countB[num]) for num in countA)

    # Check if all pairs are already beautiful and handle this edge case
    if beautiful_pairs == len(A):
        # If all are beautiful, we have to break one by the problem condition (change one element)
        return beautiful_pairs - 1
    else:
        # Otherwise, we can form one more beautiful pair by changing one non-beautiful element
        return beautiful_pairs + 1
    
    
# a = 3 5 7 11 5 8
# b = 5 7 11 10 5 8
# beautiful (1,0), (1,5), (2,1), (4,0), (4,5), (3,2), (5,5)
# curr pairwise disjoint: (1,2), (2,1)(4,0), (3,2), (5,5)
# pairwise disjoint 4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
