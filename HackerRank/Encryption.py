#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from itertools import zip_longest 

def encryption(s): # haveaniceday
    length = len(s)
    #print('length = ', length)
    l = int(length**0.5)
    if l == length**0.5:
        u = l
    else:
        u = l+1

    # print('s = ', s)
    # print('l = ', l)
    # print('u = ', u)

    res = []
    for i in range(0,length, u):
        # print('i = ', i)
        row = s[i:i+u]
        res.append(row)
    
    # print('res = ', res)
    
    res2 = []
    for col in zip_longest(*res, fillvalue=''):
        res2.append(col)
        
    # print('res2 = ', res2)
    
    res3 = ''
    for i in range(len(res2)):
        for j in range(len(res2[0])):
            res3+=str(res2[i][j])
        res3+= ' '
    # print('res3 = ', res3)
    
    return res3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
