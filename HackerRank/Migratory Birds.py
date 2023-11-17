#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    set1 = set(arr)
    set1 = sorted(set1, reverse=True)
    list1 = [0] * len(set1)
    for index, each in enumerate(set1):
        list1[index] = arr.count(each)
    return1 = set1[0]
    highest_so_far = float('-inf')
    for index, each in enumerate(list1):
        if each >= highest_so_far:
            highest_so_far = each
            return1 = set1[index]
    return return1
    
    # dict1 = {}
    # for each in arr:
    #     if each not in dict1:
    #         dict[each] = 1
    #     else:
    #         dict[each] +=1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
