#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the bricksGame function below.
#
def bricksGame(arr):
    #
    # Write your code here.
    #
    n = len(arr)
    summ = [0] * n 
    summ[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        summ[i] = summ[i+1] + arr[i]
    dp = [0] * n
    dp[n-1] = arr[n-1]
    dp[n-2] = dp[n-1] + arr[n-2]
    dp[n-3] = dp[n-2] + arr[n-3]
    for i in range(n-4, -1, -1):
        dp[i] = max(summ[i] - dp[i+1], summ[i] - dp[i+2], summ[i]-dp[i+3])
    return dp[0]


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        arr_count = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = bricksGame(arr)
        print(result)

#        fptr.write(str(result) + '\n')

#    fptr.close()
