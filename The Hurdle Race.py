#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max = 0
    for i in height:
        if max < i:
            max = i
    if max > k:
        return max-k
    else:
        return 0

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = map(int, raw_input().rstrip().split())

    result = hurdleRace(k, height)

    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
