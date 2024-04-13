#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    # This function is called once before all queries.
    s = list(s) # list of str
    
#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

from collections import Counter
import math

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    sub = s[l-1:r]
    c = Counter(sub)
    
    #print('c = ', c)
    
    same_pairs = []
    single = 0
    for k, v in c.items():
        # print('k = ', k)
        # print('v = ', v)
        same_pairs.append(v//2)
        if v%2 ==1:
            single+=1
        
    # print('same_pairs = ', same_pairs)
    # print('single = ', single)
        
    if single ==0:
        single = 1
    res = single* math.factorial(sum(same_pairs))
    for i in same_pairs:
        res = res / math.factorial(i)
    
    #print('----------------')
    return int(res%1000000007)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
