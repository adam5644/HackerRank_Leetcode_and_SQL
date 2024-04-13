#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import defaultdict
import math

def sherlockAndAnagrams(s):
    res = 0 
    # all possible substring
    d = defaultdict(int)
    
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substr = ''.join(sorted(s[i:j]))
            #print('substr = ', substr)
            d[substr]+=1
            
    for count in d.values():
        if count >=2:
            res += count * (count - 1) // 2
            
    return int(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
