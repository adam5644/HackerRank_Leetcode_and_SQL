#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):

# # [['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]
    res = [[] for _ in range(200)]
    n = len(arr) # 20 
    half = n//2-1 # 0 to 9 turn to '-'
    
    #print('half = ', half)
    for index, string in enumerate(arr):
        #print('index = ', index)
        integer = int(string[0])
        word = string[1]

        if index <= half:
            res[integer].append('-')
            #print('-')
        else:
            res[integer].append(word)
            #print('word = ',word)
        #print()

    res2 = ''
       
    
    for x in res:
        for y in x: 
            res2+=' '
            res2+=str(y)
    print(res2[1:])



if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
