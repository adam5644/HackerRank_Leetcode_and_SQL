#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    
    contain = set()
    
    current = s[0]
    contain.add(ord(current) - ord('a') + 1) 
    c = 1
    
    for i in range(1,len(s)):
        if s[i] == current:
            contain.add(c* (ord(current) - ord('a') + 1))
            c += 1
        else:
            current = s[i]
            contain.add(ord(current) - ord('a') + 1)
            c = 2
        
    
    
    res = ['Yes' if i in contain else 'No' for i in queries]
    # print('contain = ', contain)
    # print('res = ', res)
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'],'w')
    s = input()
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(int(input()))
    result = weightedUniformStrings(s, queries)
    
    
    for i in range(len(result)):
        temp = result[i]
        f.write(str(temp) + '\n')
    f.close()
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # queries_count = int(input().strip())

    # queries = []

    # for _ in range(queries_count):
    #     queries_item = int(input().strip())
    #     queries.append(queries_item)

    # result = weightedUniformStrings(s, queries)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
