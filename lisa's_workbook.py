#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    print('n no.of chaps: ', n)
    print('k max limit on each page: ', k)
    print('arr probs in each chap: ', arr)
    pg = 1
    fin_count = 0 
    for i in range(n): # n is the total number of chapters
        probs = arr[i]
        print('arr[i]: ', arr[i])
        print('int((probs//k)): ', int((probs//k)))
        print('int((probs%k)): ', int((probs%k)))
        tot_pages = 1
        if int((probs//k))==0:
            tot_pages = 1
        if int((probs//k))!=0 and int((probs%k))==0:
            tot_pages = int((probs//k))
        if int((probs//k))!=0 and int((probs%k))!=0:
            tot_pages+=int((probs//k))

        print('tot_pages: ', tot_pages)
        one_tmp_pgs = []
        a = 0
        for ll in range(tot_pages):
            one_tmp_pgs = [a+las for las in range(1, k+1) if a+las <= arr[i]]
            print('one_tmp_pgs: ', one_tmp_pgs)
            if pg in one_tmp_pgs:
                fin_count+=1
            print('page number: ', pg)
            print('fin_count: ', fin_count)
        
            a = one_tmp_pgs[-1]
            one_tmp_pgs = []
            pg+=1
    return fin_count            

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
