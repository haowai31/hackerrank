#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    tmp = sorted(price)
    result = 0
    h = {}
    count = 0
    for i in price:
        h[i] = count
        count += 1
    for i in range(len(price)-1, 0, -1):
        if h[tmp[i]] < h[tmp[i-1]]:
            if tmp[i] > tmp[i-1]:
                if result == 0:
                    result = tmp[i]-tmp[i-1]
                else:
                    result = min([result, tmp[i]-tmp[i-1]])
    return result

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    price = map(long, raw_input().rstrip().split())

    result = minimumLoss(price)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
