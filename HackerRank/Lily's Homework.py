#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def calc_swaps_num(arr, target):
    # To avoid modifying the original array passed to calc_swaps_num, work on a copy
    arr = arr[:]
    # Map each element to its index in the target sorted array for quick lookup
    target_index = {value: idx for idx, value in enumerate(target)}
    swaps = 0
    for i in range(len(arr)):
        # Correct position of current element in the target array
        correct_pos = target_index[arr[i]]
        # If element is not in the correct position, swap it with the element that is currently in its correct position
        while i != correct_pos:
            # Position of the element that should be at i
            to_swap_idx = target_index[arr[i]]
            # Swap elements
            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            # Update the position, since arr[i] has changed
            correct_pos = target_index[arr[i]]
            swaps += 1
    return swaps

def lilysHomework(arr):
    target1 = sorted(arr)
    target2 = sorted(arr, reverse=True)
    
    return min(calc_swaps_num(arr, target1),
               calc_swaps_num(arr, target2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
