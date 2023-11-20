#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    res = ''
    for each in s:
        if each in letters:
            curr_idx = letters.find(each)
            new_idx = curr_idx + k
            if new_idx >= 26:
                new_idx = new_idx % 26
            each = letters[new_idx]
        
        if each in letters2:
            curr_idx = letters2.find(each)
            new_idx = curr_idx + k
            if new_idx >= 26:
                new_idx = new_idx % 26
            each = letters2[new_idx]
        
        res+=each
    return res
 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
