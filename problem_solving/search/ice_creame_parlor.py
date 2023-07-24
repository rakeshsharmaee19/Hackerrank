import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    sm = 0
    for i in range(len(arr)-1):
        # sm = i
        j=i+1
        while j<len(arr):
            sm = arr[i]+arr[j]
            
            if sm==m:
                break
            j+=1
        if sm==m:
            break
    return [i+1,j+1]
    # Write your code her

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
