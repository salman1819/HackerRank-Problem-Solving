 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ref_arr=sorted(arr)
    swp=0
    cor_dict_indx={val:idx for idx, val in enumerate(arr)}
   
    for i, v in enumerate(arr):
        if v!=ref_arr[i]:
            # print('ref_arr[i]: ', ref_arr[i])
            # print('v: ', v)
            ind_swp=cor_dict_indx[ref_arr[i]]
            # print('ind_swp: ', ind_swp)
            arr[ind_swp], arr[i]=arr[i], arr[ind_swp]
            # print('swapped array: ', arr)
            cor_dict_indx[ref_arr[i]]=i
            cor_dict_indx[v]=ind_swp
            # print('new i:', i)
            swp+=1

    return swp
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
