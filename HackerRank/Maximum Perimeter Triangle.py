#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    from itertools import combinations
    
    def can_triangle(a):
        sum1 = sum(a)
        for each in a:
            temp_sum = sum1 - each
            if each >= temp_sum:
                return False
        return True
    
    combi_1 = [sorted(each) for each in combinations(sticks, 3) if can_triangle(each)]
    
    highest = float('-inf')
    
    if len(combi_1) >= 1:
        return1 = combi_1[0]
    else:
        return [-1]
    
    
    for each in combi_1:
        if sum(each) > highest:
            highest = sum(each)
            return1 = each
        if sum(each) == highest:
            if max(each) > max(return1):
                 return1 = each
            if max(each) == max(return1):
                if min(each) <= min(return1):
                    return1 = each
    return return1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
