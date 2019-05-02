#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[0 for _ in range(n+1)]
    for i in range(m):
        arr[queries[i][0]-1]+=queries[i][2]
        arr[queries[i][1]]-=queries[i][2]
    for i in range(1, len(arr)):
        arr[i]+=arr[i-1]

    return max(arr)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
