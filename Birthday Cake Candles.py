#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxx = 0
    num = 0
    for i in range(len(ar)):
        if maxx < ar[i]:
            maxx = ar[i]
            num = 1
        elif maxx == ar[i]:
            num += 1
    
    return num

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
