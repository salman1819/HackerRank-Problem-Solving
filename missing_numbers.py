#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    # Complete this function
    count_a = Counter(arr)
    # print('count_a: ', count_a, type(count_a))
    count_b = Counter(brr)
    # print('count_b: ', count_b, type(count_b))
    miss = []
    for key in count_b.keys():
        if count_a[key] != count_b[key]:
            miss.append(key)
    return sorted(miss)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
