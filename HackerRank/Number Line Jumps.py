#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
            # 0 , 3, 4, 2
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
            # # 0, 4, 2,3
    def calc(short_dis, long_dis, fast_speed, slow_speed):
                # 0 , 4
                # 
        while short_dis <= long_dis:
            if short_dis == long_dis: return 'YES' 
            short_dis += fast_speed
            long_dis += slow_speed
        return 'NO' 
    
    if x1 == x2: return 'YES'
    
    if x1 > x2 and v2 > v1:
        return calc(x2, x1, v2,x1)
    
        # 4 > 0 and 3 > 2
    elif x2 > x1 and v1 > v2:
                    # 0, 4, 2,3
        return calc(x1,x2,v1,v2)
    else:
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
