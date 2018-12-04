#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def getnext(x, left, k):
    nextstation = x
    tmp = left
    while (x[tmp] <= x[left] + k):
        tmp += 1
        if tmp >= len(x):
            return -1
    right = tmp
    while (x[right] - k <= x[tmp-1]):
        right += 1
        if right >= len(x):
            break 
    return right

def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    result = 0
    i = 0
    while (i < len(x)):
        result += 1
        loc = x[i] + k
        while (i<n and x[i] <= loc):
            i += 1
        loc = x[i-1] + k
        while (i<n and x[i] <= loc):
            i += 1
    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = map(int, raw_input().rstrip().split())

    result = hackerlandRadioTransmitters(x, k)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
