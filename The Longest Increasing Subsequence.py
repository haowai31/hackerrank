#!/bin/python

import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def longestIncreasingSubsequence(arr):
    dp = [1] * len(arr)
    maxx = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        maxx = max(maxx, dp[i])
    return maxx

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()