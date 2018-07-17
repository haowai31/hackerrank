#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    loc_apples = 0
    loc_oranges = 0
    for i in apples:
        tmp = (a + i)
        if tmp >= s and tmp <= t:
            loc_apples += 1
    print(loc_apples)

    for i in oranges:
        tmp = (b + i)
        if tmp >= s and tmp <= t:
            loc_oranges += 1
    print(loc_oranges)


if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
