#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# def legoBlocks(n, m):
#     # Write your code here
#     width_ways = [0] * (m+1)
#     if m >= 1: width_ways[1] = 1
#     if m >= 2:  width_ways[2] = 2
#     if m >= 3: width_ways[3] = 4
#     if m >= 4:  width_ways[4] = 8
#     for i in range(5, m+1):
#         width_ways[i] = width_ways[i-1] + width_ways[i-2] + width_ways[i-3] + width_ways[i-4]
        
#     all_walls = (width_ways[-1]**n)%1000000007
    
#     # calc all_walls of diff width
#     all_walls_diff_width = [0] * (m+1)
#     for i in range(1, m):
#         all_walls_diff_width[i] = (width_ways[i]**n)%1000000007
    
#     # minus bad walls 
#     for i in range(1,m):
#         left_bad_walls = all_walls_diff_width[i]
#         right_bad_walls = all_walls_diff_width[m-i]
#         bad_walls = left_bad_walls * right_bad_walls
#         all_walls -= (bad_walls)%1000000007
    
    
    # return all_walls

def legoBlocks(h,w):
    row = [0] * (w+1)
    if w>=1: row[1] = 1
    if w>=2: row[2] = 2
    if w>=3: row[3] = 4
    if w>=4: row[4] = 8
    if w>=5:
        for i in range(5, w+1):
            row[i] = (row[i-1] + row[i-2] + row[i-3] + row[i-4]) %1000000007
            
            
            
    total = row.copy()
    for _ in range(2, h+1):
        for i in range(w+1):
            total[i] = (row[i] * total[i])%1000000007
            
    print('total = ', total)
            
    solid = [0] * (w+1)
    solid[1] = 1
    for ww in range(2, w+1):
        unsolid_sum = 0
        for i in range(1,ww):
            unsolid_sum += ((solid[i] * total[ww-i])%1000000007)
        solid[ww] = (total[ww] - unsolid_sum)%1000000007
        
    print('solid = ', solid)
        
    return solid[w]%1000000007
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
