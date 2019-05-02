#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    lst=[1]
    temp=1
    n=0
    while t>=temp:
        # print('t temp n: ', t, temp, n)
        lst.append(1+3*(1+2*n))
        n=1+2*n
        temp=lst[-1]
    print('lst: ', lst)
    inde=len(lst)-2
    print('inde: ', inde, lst[inde])
    return ((3*(2**inde))-(t-lst[inde]))




        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
