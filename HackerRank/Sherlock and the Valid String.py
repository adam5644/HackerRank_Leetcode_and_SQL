#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    from collections import Counter
    freq = Counter(s)
    values = [value for key,value in freq.items()]
    # >=3 freq , return no
    freq_of_freq = Counter(values)
    
    print('freq = ', freq)
    print('freq_of_freq = ', freq_of_freq)
    
    if len(freq_of_freq.keys()) == 1:
        return 'YES'
    
    values2 = [value for key,value in freq_of_freq.items()]
    keys2 = [key for key,value in freq_of_freq.items()]
    
    if (len(freq_of_freq.keys()) == 2) and (values2[1]==1 or values2[0]==1) and (abs(keys2[0] - keys2[1]) == 1    or    
    (keys2[0]== 1 and values2[0]==1) or (keys2[1]==1 and values2[1]==1)):
        return 'YES'
    
    return 'NO'

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
