#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1<x2:
        if v1>v2:
            while (x1-x2)<0:
                x1=x1+v1
                x2=x2+v2
                if x1==x2:
                    return 'YES'
                elif x1>x2:
                    print('NO')
                    return 'NO'
                else:
                    pass
        else:
            print('NO')
            return 'NO'
    else:
        if v2>v1:
            while (x1-x2)>0:
                x1=x1+v1
                x2=x2+v2
                if x1==x2:
                    print('YES')
                    return 'YES'
                elif x1<x2:
                    print('NO')
                    return 'NO'
                else:
                    pass
        else:
            print('NO')
            return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
