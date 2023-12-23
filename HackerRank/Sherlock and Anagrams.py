#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # a = defaultdict(int)
    # s = 'abba'
    # print(a[s])

    # a = 'abba'
    # b = sorted(a)
    # c = ''
    # for x in b:
    #     c+=x
    # print('c = ', c)
    # print(type(c))

    # print()
    # print()
    # print('start')
    res = 0
    for n in range(1, len(s)):
        store = defaultdict(int) # sort before storing
        
        for i in range(len(s)):
            if i+n-1 >= len(s):
                break #breaks 'for i' loop
            
            curr = s[i:i+n]
            
            b = sorted(curr)
            c = ''
            for x in b:
                c+=x
            
            # print('c = ', c)
            # print('store = ', store)
            
            res += store[c]
            # print('res = ', res)
            
            store[c] += 1
            
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
