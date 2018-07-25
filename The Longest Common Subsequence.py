#!/bin/python

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    hx = [['' for i in range(len(b)+1)] for j in range(len(a)+1)]
    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                dp[i+1][j+1] = dp[i][j] + 1
                hx[i+1][j+1] = hx[i][j] + ' ' + str(x)
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                hx[i+1][j+1] = max([hx[i+1][j], hx[i][j+1]], key = lambda x: len(x))
    result = hx[-1][-1].split(" ")
    while "" in result:
        result.remove("")
    result = list(map(int, result))
    
    return result


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
