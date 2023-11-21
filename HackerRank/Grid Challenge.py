#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
        
    new_grid = []    
    for row in grid:
        row = sorted(row, key=lambda x: ord(x))
        new_grid.append(row)
    
    for each in zip(*new_grid):
        each = list(each)
        new_each = list(sorted(each, key = lambda x: ord(x)))
        
        print('each = ', each)
        print('type(each) = ', type(each))
        print('new_each = ', new_each)
        print('type(new_each) = ', type(new_each))
        
        if each != new_each:
            return 'NO'
    return 'YES'


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
