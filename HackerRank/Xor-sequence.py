#!/bin/python3

import math
import os
import random
import re
import sys

def xor_sum(n):
    # XOR sum is periodic
    # print the first 30 or so XOR sums (e.g. A[1]...A[30])
    # and you'll notice the pattern below
    # which is periodic with period 8
    m = n % 8
    if m==3 or m==4:
        return 2
    if m==7 or m==0:
        return 0
    if m==1 or m==2:
        return n-1
    if m==5 or m==6:
        return n+1

def xorSequence(l, r):
    # key idea is to notice that 
    # 1) x XOR x = 0s  
    # 2) 0s XOR x = x
    # 3) x XOR y = y XOR x

    # with these relations it's straightforward to show that
    # XOR_SUM = A[L] XOR ... XOR A[R] = A[R] XOR A[L-1]

    # finally, make sure you index correctly with l and r
    # for example, to be r inclusive, you need to index r+1
    
    # solution is O(r-l) time and O(1) space
    return xor_sum(r+1)^xor_sum(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
