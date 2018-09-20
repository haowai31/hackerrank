#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    result = 1
    a = sorted(a, reverse=True)
    for i in range(len(a)):
        j = i
        while a[i]-a[j]<=1:
            j += 1
            if j >= len(a):
                break
        if result < j - i:
            result = j - i
    return result
        
        

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
