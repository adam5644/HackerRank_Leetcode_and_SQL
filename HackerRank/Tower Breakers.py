#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Player 2 wins if the height of each tower is 1 or if the number of towers is even
    if m == 1 or n % 2 == 0:
        return 2
    else:
        # Otherwise, Player 1 wins
        return 1
    
    
    
    ######################### recursion
    
    # Write your code here
    # assume each player must make a move
    # qn seem to assume that given any kind combination of n and m, at some 
    # ... point of the rounds, one of the player will definitely have a sure
    # ... win choice. 
    # *** if only 1 non-1 tower, fate sealed
    # *** if 2 non-1 tower and 1 of them can only go to 1, fate sealed 
    
    # # backtracking
    # tower = [m]*n
    
    # def find(player_facing, tower):
        
    #     # base case
    #     if all(x==1 for x in tower):
    #         if player_facing == 1: return 2
    #         else: return 1
        
    #     # possibilites + recursion
    #     for each in # o(n)
    
    # find(1,n,m )
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
