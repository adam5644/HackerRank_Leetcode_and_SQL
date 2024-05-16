#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'travelAroundTheWorld' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  3. LONG_INTEGER c
#

def travelAroundTheWorld(a, b, c):
    n = len(a)
    
    net_fuel_and_capacity = [(min(a[i], c) - b[i], c - b[i]) for i in range(n)]
    #print(net_fuel_and_capacity)
    
    # If total net fuel is negative, return 0 as no starting point is feasible
    if sum(pair[0] for pair in net_fuel_and_capacity) < 0:
        return 0
        
    if any(x>c for x in b):
        return 0
        
    # Create a doubled list to handle circular array by linear processing
    extended_net_fuel = net_fuel_and_capacity + net_fuel_and_capacity
    infeasible_starts = set()
    cumulative_fuel = 0
    #print('extended_net_fuel = ', extended_net_fuel)

    # Check from the last to the first to determine the minimum required starting fuel
    for i in range(len(extended_net_fuel)-1, -1, -1):
    #for i in range(len(extended_net_fuel)):
        #print('i = ', i)
        self_sufficient, max_gasoline_left = extended_net_fuel[i]

        # print('max_capacity_delta + cumulative_fuel = ', max_capacity_delta + cumulative_fuel)

 
        
        cumulative_fuel = self_sufficient + cumulative_fuel
        #print('cumulative_fuel = ', cumulative_fuel)
        if cumulative_fuel < 0:
            infeasible_starts.add(i % n)
        cumulative_fuel = min(cumulative_fuel, 0)
        #print('cumulative_fuel = ', cumulative_fuel)
    
    return n - len(infeasible_starts)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = travelAroundTheWorld(a, b, c)

    fptr.write(str(result) + '\n')

    fptr.close()
