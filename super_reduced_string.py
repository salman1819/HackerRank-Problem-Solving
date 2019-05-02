#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    lst=[str(x) for x in s]
    i=0
    while i < (len(lst)-1):
        if lst[i]==lst[i+1]:
            print(lst[i], lst[i+1], i, i+1)
            del lst[i]
            print(''.join(lst), len(lst))
            del lst[i]
            print(''.join(lst))
            print(len(lst))
            i=0
        else:
            i+=1
    # print(''.join(lst))
    if len(lst)==0:
        return 'Empty String'
    else:
        return ''.join(lst)

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
