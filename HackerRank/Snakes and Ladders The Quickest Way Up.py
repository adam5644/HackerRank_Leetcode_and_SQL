#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

from collections import deque

# Complete the quickestWayUp function below.
from collections import deque


# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    paths = {}
    for s, d in ladders + snakes:
        paths[s] = d

    q = deque([(1, 0)])
    visited = set()
    while q:
        sq, rolls = q.popleft()
        if 100 == sq:
            return rolls

        visited.add(sq)
        for i in range(1, 7):
            nextt = sq + i
            if nextt in visited or nextt > 100:
                continue

            #q.append((next in paths and paths[next] or next, rolls + 1))
            
            # Determine the next square based on whether it's a ladder or snake
            if nextt in paths:
                final_square = paths[nextt]  # Move to the end of the ladder or snake
            else:
                final_square = nextt  # Move to the next square if no ladder or snake

            # Append the next move to the queue with incremented roll count
            q.append((final_square, rolls + 1))
    return -1
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
