#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substringDiff' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s1
#  3. STRING s2
#
from collections import deque
def substringDiff(k, s1, s2):
    # Write your code here
    
    def matches(str1, str2):
        maxLen = 0
        lengthS1 = len(str1)
        lengthS2 = len(str1)
        for idx in range(lengthS1):
            j = 0
            queue = deque() # queue is the sliding window compared between s1 and s2
            res = [0] * 2 # res[0] is mismatched of current window, res[1] is matched
            trackLen = 0
            print('idx = ', idx)
            
            for i in range(idx, lengthS1):
                print('i = ', i)
                print('queue = ', queue)
                
                if j > lengthS2: # ensure doesnt exceed
                    break
                    
                print('str1[i] = ', str1[i])
                print('str2[j] = ', str2[j])
                if str1[i] == str2[j]:
                    res[1] += 1
                    queue.append(1)
                    trackLen += 1
                else: 
                    res[0] += 1
                    queue.append(0)
                    trackLen += 1
                    
                print('********')
                while res[0] > k:
                    val = queue.popleft()
                    print('val = ', val)
                    res[val] -= 1
                    trackLen -= 1
                    print('res = ', res)
                print('********')
                    
                if trackLen > maxLen:
                    maxLen = trackLen
                
                print('maxLen = ', maxLen)
                j += 1
            print('---------------')
        return maxLen

    return max(matches(s1, s2), matches(s2, s1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        s1 = first_multiple_input[1]

        s2 = first_multiple_input[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
