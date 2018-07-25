#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the playWithWords function below.
#
def playWithWords(s):
    #
    # Write your code here.
    #
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(1, len(s)):
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                if i-1==j:
                    dp[j][i] = 2
                elif dp[j+1][i-1] > 0:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = 0
            else:
                dp[j][i] = max(dp[j+1][i], dp[j][i-1])
    result = max([dp[0][i]*dp[i+1][-1] for i in range(len(s)-1)])
    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = playWithWords(s)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
