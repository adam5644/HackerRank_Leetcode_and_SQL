#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

# def gridlandMetro(n, m, k, track):
#     track.sort()                                        #1
#     out = n * m                                         #2
#     r0 = t1 = t2 = 0
#     for r, c1, c2 in track:                             #3
#         if r == r0 and c1 - 1 < t2: t2 = max(t2, c2)    #4
#         else:
#             out -= t2 - t1                              #5
#             r0, t1, t2 = r, c1 - 1, c2                  #6
#     return(out - t2 + t1)                               #7

def gridlandMetro(n, m, k, tracks):
    # Dictionary to hold the covered ranges for each row
    track_dict = {}
    for track in tracks:
        row, start, end = track
        if row in track_dict:
            track_dict[row].append((start, end))
        else:
            track_dict[row] = [(start, end)]
            
    print('track_dict = ', track_dict)
    
    # Merge intervals for each row to minimize the covered columns
    for row in track_dict:
        intervals = sorted(track_dict[row], key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0] - 1:
                merged.append(interval)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        track_dict[row] = merged
        
    print('track_dict = ', track_dict)

    # Calculate the total number of covered cells
    covered_cells = 0
    for row in track_dict:
        for start, end in track_dict[row]:
            covered_cells += end - start + 1
    
    # Total cells in grid minus the covered cells
    total_cells = n * m
    return total_cells - covered_cells

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
