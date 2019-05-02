#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    # print(p//2)

    count=0
    count_ar=[]

    if p==1 or p==n:
        return 0
    elif n%2==0 and p%2==0:
        return (min(p//2, (n-p)//2))
    elif n%2==0 and p%2!=0:
        return(min((p-1)//2, (n-p+1)//2))
    elif n%2!=0 and p%2==0:
        return min(p//2, (n-p)//2)
    elif n%2!=0 and p%2!=0:
        return min(p//2, (n-p)//2)

    # elif n%2!=0 and p!=n:
    #     lst_ar=[x for x in range(1, n+1)]
    #     for i in range(n):
    #         if lst_ar[i]==p:
    #             break
    #         else:
    #             count+=1
    #     count_ar.append(count//2)
    #     count=0
    #     if not count_ar:
    #         count_ar.append(0)
