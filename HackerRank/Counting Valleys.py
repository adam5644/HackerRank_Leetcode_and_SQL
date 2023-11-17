#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # valley occurs when D followed by sea level 
    res = 0
    position = 0
    print(path)
    for index,each in enumerate(path):
        print(index)
        if each == 'U':
            position +=1
        else:
            position -=1
        if index >= 1:
            if path[index] == 'U' and position == 0:
                res +=1
                print('yes')
            else:
                print('no')
        else:
            print('123')
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
