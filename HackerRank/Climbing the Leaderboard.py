#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# def climbingLeaderboard(ranked, player):
#     '''
#     for x in player:
#         recalculate ranked
#     * use set for unique iterable
#     '''
#     ranked = sorted(set(ranked),reverse=True) # o(n) for sorted
#     res = []
#     for x in player:
#         if x in ranked:
#             res.append(ranked.index(x)+1)
#         else:
#             ranked.append(x)
#             print(ranked)
#             ranked = sorted(ranked,reverse=True) 
#             res.append(ranked.index(x)+1)
#     return res

def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort in descending order
    ranked = sorted(set(ranked), reverse=True)
    res = []
    l = len(ranked)
    start = l
    
    for x in player:
        while start >= 0 and x>ranked[start-1]:
            start-=1
        res.append(start+1)
    return res
    # for x in player:
    #     # Use a reverse loop to find the rank
    #     while start > 0 and x >= ranked[start - 1]:
    #         start -= 1
    #     res.append(start + 1)

    # return res
            
            

    # for x in player:
    # ranked.append(100)
    # print(ranked)
    
    # ordered list?

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
