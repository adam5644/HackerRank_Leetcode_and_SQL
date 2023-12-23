#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    if len(s) == 0:
        return 'Empty String'
    
    
    def find(s):
        # print('before = ', s)
        for i in range(0, len(s)-1):
            # print('i = ', i)
            if s[i] == s[i+1]:
                # print('s[i] = ', s[i])
                # print('s[i+1] = ', s[i+1])
                s = s[:i] + s[i+2:]
                # print('after = ', s)
                s = find(s)
                return s 
        # print('final s = ', s)
        return s
            
    s = find(s)
        
    if len(s) == 0:
        return 'Empty String'
    else: 
        return s
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
