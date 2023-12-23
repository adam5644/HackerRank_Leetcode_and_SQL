#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    store = []
    for x in s:  # O(n)
        if x in '([{':
            store.append(x)
        elif store:  # Check if store is not empty
            if x == ')' and store[-1] == '(':
                store.pop()
            elif x == ']' and store[-1] == '[':
                store.pop()
            elif x == '}' and store[-1] == '{':
                store.pop()
            else:
                return 'NO'
        else:
            return 'NO'
                    
    return 'YES' if not store else 'NO'

# Rest of the code remains the same

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
