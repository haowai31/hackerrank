#!/bin/python

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    result = 1
    switch = 0
    for i in range(n):
        if switch == 0:
            result = result * 2
        else:
            result += 1
        switch = 1 - switch
    return result
        


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = utopianTree(n)
        print(result)

#        fptr.write(str(result) + '\n')

#    fptr.close()
