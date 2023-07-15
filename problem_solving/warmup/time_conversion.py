#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    a=''
    # Write your code here
    if s[-2:] == "AM" :
        if s[:2] == '12':
            a = str('00' + s[2:8])
        else:
            a = s[:-2]
    else:
        if s[:2] == '12':
            a = s[:-2]
        else:
            a = str(int(s[:2]) + 12) + s[2:8]
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
