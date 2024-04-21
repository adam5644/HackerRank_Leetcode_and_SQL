#!/bin/python3

import math
import os
import random
import re
import sys

a=input()
b=input()
x=int(a,2)
y=int(b,2)
p=0
for i in range(0,314160):
    p+=x^(y<<i)
print(p%((10**9)+7))