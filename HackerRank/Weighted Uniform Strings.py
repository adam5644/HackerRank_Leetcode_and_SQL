#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

# def weightedUniformStrings(s, queries):
#     # Write your code here
    
#     exist = []
    
#     # cont value = (ord(conti[0]) - ord('a')) * len(conti)
        
    
#     prev = None
#     conti = ''
#     for i in range(len(s)):
#         print('prev = ', prev)
#         print('s[i] = ', s[i])
        
#         if s[i] == prev:
#             print('same')
#             print('old conti = ', conti)
#             conti = conti + s[i]
#             print('new conti = ', conti)
            
#         else:
#             if len(conti) >= 1:
#                 print('conti = ', conti)
#                 conti_value = (ord(conti[0]) - ord('a')) * len(conti)
#                 exist.append(conti_value)
#             prev = s[i]
            
#         print()    
        
#     res = []
#     for x in queries:
#         if x in exist:
#             res.append('Yes')
#         else:
#             res.append('No')
    
#     return res

def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    
    # Initialize previous character and weight
    prev = None
    weight = 0
    
    # Iterate over the string
    for char in s:
        # Check if we have a sequence of the same character
        if char == prev:
            # Increase the weight by the character's value
            weight += (ord(char) - ord('a') + 1)
        else:
            # Reset the weight to the current character's value
            weight = (ord(char) - ord('a') + 1)
            # Update the previous character
            prev = char
        
        # Add the weight to the set of possible weights
        weights.add(weight)
    
    # Check if each query weight is in the set of possible weights
    res = ['Yes' if q in weights else 'No' for q in queries]
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
