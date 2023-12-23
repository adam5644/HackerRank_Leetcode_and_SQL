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

def icecreamParlor(m, arr):
    # print()
    # print('start')
    # print('m = ', m)
    # print('arr = ', arr)
    store = {}
    for i in range(len(arr)):
        left = m - arr[i]
        # print('left = ', left)
        if left in store:
            res = [store[left]+1, i+1]
            # print('res = ', res)
            return res
        store[arr[i]] = i
        # print(store)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    
    for _ in range(t):    
        m = int(input().strip())
        n = int(input().strip())
        cost = []
        # cost = (int(input().strip().split()))
        cost = list(map(int,input().split()))
        res = icecreamParlor(m, cost) 
        res2 = str(res[0])
        for i in range(1,len(res)):
            res2+=f' {res[i]}'
        f.write(res2 + '\n')
        
    f.close()
    
    #####################
    
    # # res = '1 4'
    # res = [1,4]
    # res2 = str(res[0])
    # for i in range(1,len(res)):
    #     res2+=f' {res[i]}'
        
    # f.write(res2 + '\n')
    
    # #res = '1 2'
    # res = [1,2]
    # res2 = str(res[0])
    # for i in range(1,len(res)):
    #     res2+=f' {res[i]}'
    
    # f.write(res2 + '\n')
    
    # f.close()
            

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
