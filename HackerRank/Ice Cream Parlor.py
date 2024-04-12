#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr): # m=6, cost = [1,3,4,5,6]
    arr = [int(i) for i in arr]
    arr_dict = {flavor+1: cost  for flavor, cost in enumerate(arr)}
    arr_dict2 = {cost: flavor+1  for flavor, cost in enumerate(arr)}
        
    for flavor, cost in arr_dict.items():
        left = m - cost
        flavor1 = flavor
        
        if left in arr_dict2.keys():
            flavor2 = arr_dict2[left]
            
            if flavor1 < flavor2:
                return f'{flavor1} {flavor2}'
            else:
                return f'{flavor2} {flavor1}'
        
    
    
    # res sort ascending

if __name__ == '__main__':
    f=open(os.environ['OUTPUT_PATH'],'w')
    
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        arr = input().split()
        # print('m = ', m)
        # print('n = ', n)
        # print('arr = ', arr)
        # m =  4
        # n =  5
        # arr =  ['1', '4', '5', '3', '2']
        
        res = icecreamParlor(m, arr)
        f.write(res + '\n')
    
    
    f.close()
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     m = int(input().strip())

    #     n = int(input().strip())

    #     arr = list(map(int, input().rstrip().split()))

    #     result = icecreamParlor(m, arr)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
