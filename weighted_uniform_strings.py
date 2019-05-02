#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    d={}
    for i in range(97, 123):
        d[chr(i)]=len(d)+1
    # print(d)
    scores = set()
    ctr=1
    for i in range(len(s)):
        if i!=len(s)-1 and s[i]==s[i+1]:
            ctr+=1
        else: 
            ctr=1
        scores.add(d[s[i]]*ctr)
    az=[]
    for i in queries:
        if i in scores:
            az.append('Yes')
        else:
            az.append('No')
    return az

    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
