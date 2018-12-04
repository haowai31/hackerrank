#!/bin/python

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    nk = {}
    for i in range(k):
        nk[i] = 0
    
    for i in S:
        nk[i % k] += 1
    if nk[0] > 1:
        nk[0] = 1
    for i in range(1, k):
        tmp = k - i
        if tmp == i:
            nk[tmp] = 1
        else:
            if nk[i] > nk[tmp]:
                nk[tmp] = 0
            else:
                nk[i] = 0
    
    result = 0
    for i in range(k):
        result += nk[i]
    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, S)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
