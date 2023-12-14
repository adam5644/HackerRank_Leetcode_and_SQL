#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    #print('n = ', n )
    if n <= 1: 
        #print('i = ', 0)
        return 0
    
    # o(n) run from 1 to n
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,37,41,43,47]
    c_primes = [2]
    for i in range(1, len(primes)):
        add = c_primes[i-1] * primes[i]
        c_primes.append(add)
        
    # print('c_primes = ', c_primes)
    # print('len(c_primes) = ', len(c_primes))
    
    for i in range(len(c_primes)):
        if c_primes[i] == n:
            #print('res = ', i+1)
            return i+1
        if c_primes[i] > n:
            #print('res = ', i)
            return i
        
            
    return 15
    
    
    # prime = []
    # cum_prime = [], find max cum_prime which is <= n, return the index in cum_prime
    # time complexity = 2* o(n)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'],'w')
    num = int(input().strip())
    print('num = ', num)
    
    for _ in range(num):
        res = primeCount(int(input().strip()))
        f.write(str(res)+'\n')

        
    f.close()
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     n = int(input().strip())

    #     result = primeCount(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
