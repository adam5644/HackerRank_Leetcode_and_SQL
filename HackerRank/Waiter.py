#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

# def waiter(number, q):
# #     print('number = ', number)
# #     print('q = ', q)

#     def is_prime(x):
#         for c in range(20,int(x**0.5)+1):
#             if x%c == 0:#o(n^2)
#                 return False
#         return True
        

#     prime_list = [2,3,5,7,11,13,17,19]

#     b = 20
#     while len(prime_list) != q:
#         if is_prime(b):
#             prime_list.append(b)
#         b+=1
    
    
#     res = []
#     for prime in prime_list: 
#         for x in number: #o(n^2)
#             if x % prime == 0:  
#                 res.append(x)
        
    
#     return res
    
    
def waiter(numbers, q):
    prime_list = generate_primes(q)  # We will create this function to generate required primes
    answer = []
    A = numbers

    for i in range(q):
        B = []
        new_A = []
        current_prime = prime_list[i]

        while A:
            number = A.pop()
            if number % current_prime == 0:
                B.append(number)
            else:
                new_A.append(number)

        answer.extend(reversed(B))  # Add in reverse order because we pop from the end
        A = new_A  # Update A with the remaining numbers

    answer.extend(reversed(A))  # Add remaining numbers that were not divisible by any of the primes
    return answer

def generate_primes(n):
    # Generate first n primes (A simple but not highly efficient way)
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 1
    return primes
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
