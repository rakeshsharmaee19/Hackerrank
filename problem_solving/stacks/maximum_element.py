#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    # stck = []
    # rs = []
    # val = 0
    # for i in operations:
    #     if i[0] == '1':
    #         stck.append(int(i[-2:]))
    #         if int(i[-2:])>val:
    #             val=int(i[-2:])
    #     elif i[0] == '2':
    #         stck.pop()
    #         val = max(stck) if len(stck) else 0
    #     else:
    #         rs.append(val)
    # return rs
    arr=[]
    out=[]
    val=0
    for i in range(0,len(operations)):
        if operations[i]=='2':
            arr.pop()
            val=max(arr) if len(arr) else 0
        elif operations[i]=='3':
            out.append(val)
        else:
            ele=int(operations[i].split(" ")[1])
            arr.append(ele)

            if ele>val:
                val=ele
    return out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
