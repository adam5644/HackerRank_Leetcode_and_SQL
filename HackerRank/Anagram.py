#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    
    
    # if not possible, return -1
    if len(s) % 2 != 0:
        return -1
        
    str1 = s[:len(s)//2]
    str2 = s[len(s)//2:]
    
    
    alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    str1_list = [0]*26
    str2_list = [0]*26
    
    for each in str1: # o(n)
        each_index = alpha_str.find(each)
        str1_list[each_index] +=1
        
    for each in str2:
        each_index = alpha_str.find(each)
        str2_list[each_index] +=1
    
    total_same = 0
    for index in range(26): # o(1)
        num_of_same = min(str1_list[index], str2_list[index] )
        total_same += num_of_same
      
    total_diff = len(str1) - total_same 
    
    return total_diff
    # overall = o(n), no nested loop
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
