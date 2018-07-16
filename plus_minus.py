#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    num_zero = 0
    num_pos = 0
    num_neg = 0

    for i in range(0, len(arr)):
        if arr[i] == 0:
            num_zero += 1
        if arr[i] > 0:
            num_pos += 1
        if arr[i] < 0:
            num_neg += 1
    print('%6f' % (num_pos / float(len(arr))))
    print('%6f' % (num_neg / float(len(arr))))
    print('%6f' % (num_zero / float(len(arr))))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
