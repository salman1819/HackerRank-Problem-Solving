#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step=0
    j=0
    while j <= (len(c)-2):
        print('j:', j)
        k=j+2
        # print('k value (j+2): ', k)
        if j==(len(c)-3):
            print('elements in iff loop:', c[j], c[j+1], c[j+2])
            step+=1
            break

        elif j==(len(c)-2):
            print('elemenst in iff loop:', c[j], c[j+1])
            step+=1
            break

        else:
            if c[k-1]==1 and c[k]==0:
                print('inside first if loop: ', c[k-1], c[k])
                step+=1
                j=k
            elif c[k-1]==0 and c[k]==0:
                print('inside second if loop:', c[k-1], c[k])
                step+=1
                j=k
            elif c[k-1]==0 and c[k]==1:
                print('inside third if loop:', c[k-1], c[k])
                step+=1
                j=k-1
    return step



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
