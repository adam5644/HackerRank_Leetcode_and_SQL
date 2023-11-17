#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    n = len(s)
    res = 0 
    sos = 'SOS'
    loop = 0 # 'sos' = 0,1,2
    
    for i in range(n):
        letter = s[i]
        if letter == sos[loop]: 
            None
        else: 
            print(i)
            print(letter)
            print(sos[loop])
            res +=1
        
        loop +=1
        if loop >= 3: loop = 0
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
