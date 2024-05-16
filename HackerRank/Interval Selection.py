#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'intervalSelection' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def intervalSelection(intervals):
    #print('intervals = ', intervals)
    intervals.sort(key = lambda x : x[1])
    noOfSelections = 0
    busy = [[0, 0], [0, 0]] # tracking 2 most recent intervals, busy[0] is the earlier one
    
    for interval in intervals:
        if busy[0] > busy[1][1]:
            (busy[0], busy[1]) = (busy[1], busy[0])
        if interval[0] > busy[1][1]:
            noOfSelections += 1
            busy[1] = interval
        elif interval[0] > busy[0][1]:
            noOfSelections += 1
            busy[0] = interval

                
    return noOfSelections


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()