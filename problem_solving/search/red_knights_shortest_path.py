#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    if i_start>=i_end:
        c = 0
        res= []
        while i_end<i_start:
            if j_start>=j_end:
                j_start-=1
                i_start-=2
                c+=1
                res.append('UL')
            else:
                j_start+=1
                i_start-=2
                c+=1
                res.append('UR')
        # print(res)
        if i_start==i_end:
            # print('1')
            if (j_end-j_start)%2==0:
                # print(2)
                if j_end<=j_start:
                    c+=(j_start-j_end)//2
                    res.extend(['L' for i in range((j_start-j_end)//2)])
                else:
                    c+=(j_end-j_start)//2
                    res.extend(['R' for i in range((j_end-j_start)//2)])
            else:
                print('Impossible')
                return
        else:
            print('Impossible')
            return
    else:
        c = 0
        res= []
        while i_end>i_start:
            if j_start>j_end:
                j_start-=1
                i_start+=2
                c+=1
                res.append('LL')
            else:
                j_start+=1
                i_start+=2
                c+=1
                res.append('LR')
        res.sort(reverse=True)
        
        if i_start==i_end:
            if (j_end-j_start)%2==0:
                if j_end<=j_start:
                    c+=(j_start-j_end)//2
                    res.extend(['L' for i in range((j_start-j_end)//2)])
                else:
                    c+=(j_end-j_start)//2
                    res.extend(['R' for i in range((j_end-j_start)//2)])
            else:
                print('Impossible')
                return
        else:
            print('Impossible')
            return
    d = {i:res.count(i) for i in res}
    print(c)
    res = []
    s = ''
    aa = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    for i in aa:
        if d.get(i):
            ddd = [i for j in range(d[i])]
            res.extend(ddd)
    print(' '.join(res))


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
