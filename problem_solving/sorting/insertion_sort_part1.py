#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    temp = arr[0]
    check = False
    for i in range(1, n):
        if temp>arr[i]:
            temp = arr[i]
            for j in range(i-1, -1,-1):
                if arr[j]>temp:
                    arr[j+1]=arr[j]
                    if j==0:
                        check = True
                else:
                    arr[j+1]=temp
                    print(' '.join(str(i) for i in arr))
                    break
                print(' '.join(str(i) for i in arr))
            if check:
                arr[0]=temp
                print(' '.join(str(i) for i in arr))
            break
        temp = arr[i]
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
