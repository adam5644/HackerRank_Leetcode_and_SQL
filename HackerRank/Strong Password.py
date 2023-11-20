#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    
    # cond1 say to add 2 more
    # the rest ok, cond2 say add 1 digit, cond 3 say add 1 
    # overall: add 2 = max(cond1, cond2+cond3+cond4+cond5). 
    # overall time o(n)
    
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    cond1 = 0 
    # condition 1
    if len(password) <= 5:
        cond1 = 6 - len(password)
    
    # condition 2 to 5
    cond2, cond3, cond4, cond5 = 1,1,1,1
    
    for each in password:
        try:
            if int(each):
                None
            cond2 = 0
        except:
            None 
    
        if each in lower_case:
            cond3 = 0
        if each in upper_case:
            cond4 = 0
        if each in special_characters:
            cond5 = 0
    
    print('cond1 =', cond1)
    print('cond2 =', cond2)
    print('cond3 =', cond3)
    print('cond4 =', cond4)
    print('cond5 =', cond5)
    
    res = max(cond1, cond2+cond3+cond4+cond5)
    return res 

    # obj = '1'
    # try:
    #     if int(obj):
    #         None
    #     print(99)
    # except:
    #     print(100)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
