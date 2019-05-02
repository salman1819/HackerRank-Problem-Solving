#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    # print(type(p), type(q))
    pk=[]
    for i in range(p,q+1):
        m=len(str(i**2))
        n=int(m/2)
        l=''
        r=''
        if n%2==0:
            l=(str(i**2)[0:n])
            r=(str(i**2)[n:])
        else:
            r=(str(i**2)[m-int((m+1)/2):])
            l=(str(i**2)[0:m-int((m+1)/2)])

        # print(i)
        # print(l,r)
        
        if l=='':
            l=0
        if int(l)+int(r) == i:
            pk.append(str(i))
    
    if len(pk)!=0:
        prev=pk[0]
        for i in range(1,len(pk)):
            prev+=' '+pk[i]
        print(prev)
    else:
        print('INVALID RANGE')




if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
