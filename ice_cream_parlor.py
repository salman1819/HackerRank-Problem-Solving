#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    # arr = sorted(arr)
    nava = []
    for idx, val in enumerate(arr):
        if val < m:
            nava.append(val)
    print('nava: ', nava)
    xz=[]
    for i in range(len(nava)-1):
        for j in range(i+1, len(nava)):
            if nava[i]+nava[j] == m:
                xz.append(nava[i])
                xz.append(nava[j])

    print('xz: ', xz)

    if len(xz)!=0:
        sx=[]
        for idx, val in enumerate(arr):
            if val==xz[0]:
                sx.append(str(idx+1))
                continue
            if val==xz[1]:
                sx.append(str(idx+1))
                continue
            if len(sx)==2:
                break
    # print('sx: ', sx)
    return sx


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
