# #!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    res = 0 
    for each in combinations(ar,2):
        if sum(each) % int(k) == 0:
            res += 1
        
    return res
        
        
    # # Write your code here
    # res = 0
    # for each in combinations(ar, 2):
    #     if 
    
    # return res
    
    
if __name__ == '__main__':
    input1 = input()
    input1 = input1.split()
    n = input1[0]
    k = input1[1]
    
    input2 = input()
    ar = list(map(int, input2.split()))
    
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    res = divisibleSumPairs(n,k,ar)
    fptr.write(str(res) + '\n')
    fptr.close
    
    
    
# if __name__ == '__main__':

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     ar = list(map(int, input().rstrip().split()))

#     result = divisibleSumPairs(n, k, ar)

#     fptr = open(os.environ['OUTPUT_PATH'], 'w')


#     fptr.write(str(result) + '\n')
    
#     fptr.close()

