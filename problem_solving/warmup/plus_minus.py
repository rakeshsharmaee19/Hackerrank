#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    c_p=0
    c_n=0
    c_z=0
    for i in arr:
        if i>0:
            c_p+=1
        elif i<0:
            c_n+=1
        else:
            c_z+=1
    r_p=c_p/n
    print('%.6f'%r_p)
    r_n=c_n/n
    print('%.6f'%r_n)
    r_z=c_z/n
    print('%.6f'%r_z)
    pass

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
