#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    next_p = 'Louise'
    
    while True: # o(n)
        # print(bin(n).count(1) == 1)
        # print(bin(n)[-1])
    
        print('start n =', n)
    
        
        if bin(n).count('1')== 1 and bin(n)[-1] != '1': # if power of 2, divde by 2
            print('a')
            n = n >>1  
            print('new n1 = ', n)
        else:    
            print('b')        
            binary_length = len(bin(n))
            lower_power = '0b' + '1' + '0'*(binary_length-3)
            print('lower_power = ', int(lower_power, 2))
            n = n - int(lower_power, 2)
            print('new n2 = ', n)
            
        
        if n == 1:
            print('end!')
            return next_p
            
        if next_p == 'Richard': next_p = 'Louise'
        else: next_p = 'Richard'
        
        print()

    
    
        
    
    # print(0b110)
    # print(0b110 >> 1)
    # print(6)
    # print(6 >> 1)
    
    # print(n)
    # print(bin(n))
    # print(type(bin(n)))
    # print(str(n))
    # print(str(bin(n)))
    # print(type(str(bin(n))))
    

        
    
    
    # def one_reduction(m):
    #     c = 0 
    #     while m < # o(n). overall o(n^2) 
        
    # p = 'Louise'
    # while n >1:  # o(n) 
    #     if n == 1:
    #         return p
    #     else:
    #         n = one_reduction(n)
    #         if p = 'Richard ':
    #             p = 'Louise'
    #         else: 'Richard' 
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
