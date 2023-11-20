#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # loop thru possible length_of_digits of starting num, o(n)
    # based on remaining length of s, compute the valid remaining string, check if match, o(1)
    
    for num_digit in range(1, len(s)+1):
        start_num = int(s[:num_digit])
        next_num = start_num
        
        valid_remain_string = ''
        remain_len = len(s) - num_digit 
        
        while remain_len >= len(str(next_num + 1)):  # compute valid remaining string
            next_num = next_num + 1
            valid_remain_string += str(next_num)
            remain_len -= len(str(next_num))
            
        # print('start_num = ', start_num)
        # print('valid_remain_string = ', valid_remain_string)
        # print('s[num_digit:] = ', s[num_digit:])
        
        
        if valid_remain_string == s[num_digit:] and valid_remain_string != '':
            print(f'YES {start_num}')
            return
    print('NO')
    # print()
    return
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
