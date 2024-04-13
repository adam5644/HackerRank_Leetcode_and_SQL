#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # print('arr = ', arr)
    
    if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
        print('yes')
        return
    
    change = [1 if arr[i+1] > arr[i] else -1 for i in range(len(arr)-1) ]
    change = [0] + change
    problem_i = [i for i, value in enumerate(change) if value == -1]
        
    #if dec_count == 1:
        
    if len(problem_i) == 1:
        idx = problem_i[0]
        arr[idx-1], arr[idx] =  arr[idx], arr[idx-1]
        #print('arr222 = ', arr)
        
        if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
            print('yes')
            print(f'swap {idx} {idx+1}')
            return
            
    else:
        #print('problem_i[0] = ',problem_i[0])
        #print('problem_i[-1] = ', problem_i[-1])
        arr[problem_i[0]-1: problem_i[-1]+1] = arr[problem_i[-1]: problem_i[0]-2:-1]
        
        #print('arr333 = ', arr)
        if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
            print('yes')
            print(f'reverse {problem_i[0]} {problem_i[-1]+1}')
            return
        
            
    print('no')
    return 
            
    
    # 1 indexing

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = almostSorted(arr)
