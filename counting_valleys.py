#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    count_ar=[0]
    for i in range(len(s)):
        if s[i]=='U':
            count+=1
            count_ar.append(count)
        else:
            count-=1
            count_ar.append(count)
    # print('count_ar:', count_ar)
    sub_count=0
    sub_count_ar=[]
    # sub_att=[]
    i=1
    while (i > 0 and i < len(count_ar)):   
        # print('i inside loop:', i)
        # print('count_ar[i]:', count_ar[i])
        # print('start sub_count value:', sub_count)
        j=i
        while count_ar[j] != 0:
            # print('inside while loop element:', count_ar[j])
            # print('before sub_count:', sub_count)
            sub_count+=count_ar[j]
            # print('after adding sub_count=', sub_count)
            j+=1
        sub_count_ar.append(sub_count)    
        i=j+1

        # print('sub_count_ar final outside one value:', sub_count_ar)
        # print('sub_att before:', sub_att)
        # sub_att.append(sum(sub_count_ar))
        # print('sub_att after:', sub_att)
        sub_count=0
    
    # print('final sub_count_ar:', sub_count_ar)

    final_count=0
    for i in range(len(sub_count_ar)):
        if sub_count_ar[i]<0:
            final_count+=1
    return final_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
