#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    fArray=[]
    arraySort=[]
    nMax=max(arr)
    count=0
    if nMax<=99:
        for i in range(100):
            fArray.append(0)
    else:
        for i in range(nMax+1):
            fArray.append(0) 
    for i in arr:
        fArray[i]+=1
    for i in fArray:
        for j in range(i):
            arraySort.append(count)
        count+=1
    return arraySort

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
