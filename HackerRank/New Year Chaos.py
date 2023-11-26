#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    c = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            print('\n\n\n\n')
            return
        # Only need to check from one place before the original position
        # of each person to their current position, not the entire queue
        print('i = ', i)
        for j in range(max(0, q[i] - 2), i):
            print('j = ', j)
            if q[j] > q[i]:
                c += 1
    print('\n\n\n\n')
    # print(c)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
