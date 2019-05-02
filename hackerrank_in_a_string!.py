#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    lst=list('hackerrank')
    ca=[]
    kk=0
    for i in range(len(lst)):
        for j in range(kk, len(s)):
            if s[j]==lst[i]:
                ca.append(s[j])
                kk=j+1
                break
    print('ca: ', ca)
    print('lst: ', lst)
    if len(ca)==len(lst):
        count=0
        for i in range(len(lst)):
            if ca[i]==lst[i]:
                count+=1  
        
        if count==len(lst):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
