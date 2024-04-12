#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    from itertools import combinations
    combi = combinations(set(s),2)
    
    res = 0
    for c in combi:
        s2 = [_ for _ in s if _ in c]
        if all(s2[i] != s2[i+1] for i in range(len(s2)-1)):
            res = max(res, len(s2))
    return res
        
        
        
        
    #     s2 = s
    #     s2 = s2.replace(c[0],'')
    #     s2 = s2.replace(c[1],'')
    #     if len(s2) <= 1: # assume 'aaaa' is not valid
    #         continue
    #     if len(set(s2)) >= 3:
    #         continue
    #     if s2[0] == s2[1]:
    #         continue
    #     a = s2[0]
    #     b = s2[1]
    #     c = a
    #     for i in range(2, len(s2)):
    #         if s2[i] != c:
    #             break
    #         if c==a: c =b
    #         else: c = a
    #         res = max(res, len(s2))
    # return res
            



    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    
    length_of_s = int(input())
    
    s = input()
    
    result = alternate(s)
    f.write(str(result))
    f.close()

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # l = int(input().strip())

    # s = input()

    # result = alternate(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
