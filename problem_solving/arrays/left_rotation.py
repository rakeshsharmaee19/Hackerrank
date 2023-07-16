#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    n=len(arr)
    b=len(arr[0])
    sum=[]
    for i in range(0,n-2):
        for j in range(0,b-2):
            sum_h=0
            for c in range(j,j+3):
                sum_h=arr[i][c]+sum_h+arr[i+2][c]
            sum_h=sum_h+arr[i+1][j+1]
            sum.append(sum_h)
    return max(sum)    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
