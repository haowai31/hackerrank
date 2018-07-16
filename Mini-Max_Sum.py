#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort(cmp=None, key=None, reverse=False)
    mini = 0
    maxx = 0
    for i in range(4):
        mini += arr[i]
        maxx += arr[i+1]
    print("%d %d" %(mini, maxx))


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
