#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr = sorted(arr)
    result = 0
    for i in range(len(arr)-1):
        left = i+1
        right = n
        while (left < right):
            mid = (left + right) / 2
            tmp = arr[mid] - arr[i]
            if tmp == k:
                result += 1
                break
            if tmp > k:
                right = mid
            else:
                left = mid + 1
    return result

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = pairs(k, arr)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
