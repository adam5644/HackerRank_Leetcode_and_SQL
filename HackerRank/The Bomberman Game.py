#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# def bomberMan(n, grid):
#     '''
#     1 initial
    
#     2 full  (remainder = 0)
#     3 bomb   (1) (note: full then bomb)
#     4 full    (2)
#     5 initial   (3)
#     '''
    
#     if n == 1: return grid
    
#     n = n-2
#     n = n % 4
#     # pri/nt('n = ', n)
    
#     if n == 3: return grid
#     if n == 0 or n == 2:
#         grid = ['O'*len(grid[0])] * len(grid)
#         return grid
        
#     if n == 1:
#         lst = []
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 'O':
#                     lst.append([i,j])
        
#         grid = ['O'*len(grid[0])] * len(grid)
#         # print('full grid = ', grid)
        
#         for i,j in lst:
#             grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
#             if i != 0:
#                 grid[i-1] = grid[i-1][:j] + '.' + grid[i-1][j+1:]
                
#             if i != len(grid)-1:
#                 grid[i+1] = grid[i+1][:j] + '.' + grid[i+1][j+1:]
#             if j != 0:
#                 grid[i] = grid[i][:j-1] + '.' + grid[i][j:]
#             if j != len(grid[0])-1:
#                 grid[i] = grid[i][:j+1] + '.' +grid[i][j+2:]
#         # print('bombed grid = ', grid)
#         return grid

def bomberMan(n, grid):
    '''
    1 initial
    
    2 full  (remainder = 0)
    3 bomb   (1) (note: full then bomb)
    4 full    (2)
    5 2nd bomb   (3)
    '''
    
    if n == 1: return grid
    
    n = n-2
    n = n % 4
    # pri/nt('n = ', n)
    
    if n == 0 or n == 2:
        grid = ['O'*len(grid[0])] * len(grid)
        return grid
        
    if n == 1:
        lst = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    lst.append([i,j])
        
        grid = ['O'*len(grid[0])] * len(grid)
        # print('full grid = ', grid)
        
        for i,j in lst:
            grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
            if i != 0:
                grid[i-1] = grid[i-1][:j] + '.' + grid[i-1][j+1:]
                
            if i != len(grid)-1:
                grid[i+1] = grid[i+1][:j] + '.' + grid[i+1][j+1:]
            if j != 0:
                grid[i] = grid[i][:j-1] + '.' + grid[i][j:]
            if j != len(grid[0])-1:
                grid[i] = grid[i][:j+1] + '.' +grid[i][j+2:]
        # print('bombed grid = ', grid)
        return grid
    
    if n == 3 :
        lst = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    lst.append([i,j])
        
        grid = ['O'*len(grid[0])] * len(grid)
        # print('full grid = ', grid)
        
        for i,j in lst:
            grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
            if i != 0:
                grid[i-1] = grid[i-1][:j] + '.' + grid[i-1][j+1:]
                
            if i != len(grid)-1:
                grid[i+1] = grid[i+1][:j] + '.' + grid[i+1][j+1:]
            if j != 0:
                grid[i] = grid[i][:j-1] + '.' + grid[i][j:]
            if j != len(grid[0])-1:
                grid[i] = grid[i][:j+1] + '.' +grid[i][j+2:]
                
        lst = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    lst.append([i,j])
                    
        grid = ['O'*len(grid[0])] * len(grid)
        # print('full grid = ', grid)
        
        for i,j in lst:
            grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
            if i != 0:
                grid[i-1] = grid[i-1][:j] + '.' + grid[i-1][j+1:]
                
            if i != len(grid)-1:
                grid[i+1] = grid[i+1][:j] + '.' + grid[i+1][j+1:]
            if j != 0:
                grid[i] = grid[i][:j-1] + '.' + grid[i][j:]
            if j != len(grid[0])-1:
                grid[i] = grid[i][:j+1] + '.' +grid[i][j+2:]
            
        return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
