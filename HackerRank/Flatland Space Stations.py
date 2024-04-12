#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    #print('c = ', c)
    res = 0
    # o(n^2)
    c = sorted(c)
    res = max(res, c[0] - 0)
    res = max(res, n-1- c[-1])
    num_station = len(c)
    for i in range(num_station-1):
        res = max(res,(c[i+1] - c[i])//2)
    return res        
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'],'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().strip().split()))
    result = flatlandSpaceStations(n, c)
    f.write(str(result)+'\n')
    f.close()
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()

    # n = int(nm[0])

    # m = int(nm[1])

    # c = list(map(int, input().rstrip().split()))

    # result = flatlandSpaceStations(n, c)

    # fptr.write(str(result) + '\n')

    # fptr.close()
