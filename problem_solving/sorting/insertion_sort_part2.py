#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    temp = arr[0]
    for i in range(1,n):
        if temp>arr[i]:
            temp = arr[i]
            for j in range(i-1, -1,-1):
                if temp<arr[j]:
                    arr[j+1]=arr[j]
                    if j==0:
                        arr[j]=temp
                else:
                    arr[j+1]=temp
                    break
        print(' '.join(str(i) for i in arr))    
        temp = arr[i]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
