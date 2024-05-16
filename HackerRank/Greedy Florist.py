#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    #print(k,c)
    count=0
    c=sorted(c, reverse=True)
    res=0
    p_count=0
    
    for x in c:
        if p_count==k:
            count+=1
            p_count=0
        res+=(count+1)*x
        p_count+=1
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
