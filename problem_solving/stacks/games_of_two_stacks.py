#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    ss=[]
    c = ['[','{','(']
    for i in s:
        if i in c:
            ss.append(i)
        else:
            if len(ss) and ((i==')' and ss[-1]=='(') or (i=='}' and ss[-1]=='{') or (i==']' and ss[-1]=='[')):
                ss.pop()
            else:
                return "NO"
    if len(ss):
        return 'NO'
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
