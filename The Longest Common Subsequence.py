#!/bin/python

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    dp = []
    rdp = []
    for i in range(len(a)):
        dpj = []
        rdpj = []
        for j in range(len(b)):
            dpj.append(0)
            rdpj.append('')
        dp.append(dpj)
        rdp.append(rdpj)
    for i in range(len(a)):
        rdp[i][0] = str(a[i])
    for j in range(len(b)):
        rdp[0][j] = str(b[i])
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                rdp[i][j] = rdp[i-1][j-1] + " " + str(a[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if dp[i][j] == dp[i-1][j]:
                    rdp[i][j] = rdp[i-1][j]
                else:
                    rdp[i][j] = rdp[i][j-1]
    print(rdp)
    return dp[len(a)-1][len(b)-1]

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = longestCommonSubsequence(a, b)
    print(result)

#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()
