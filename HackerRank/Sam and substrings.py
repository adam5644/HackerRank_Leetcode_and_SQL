#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    l = len(n)
    n = [int(i) for i in n]
    f=d=n[0]
    
    print('n = ', n)
    print('f = ',f)
    # n =  [1, 6]
    # f =  [1, 0]
    
    for i in range(1, l):
        print('i = ', i )
        d = (10* d + (i+1) * n[i]) % 1000000007
        f = (f + d)% 1000000007
        print('d = ', d)
        print('f = ',f)
        
    return (f)% 1000000007
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
