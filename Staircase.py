#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    step = "#"
    space = ""
    for i in range(n):
        space += " "
    for i in range(n):
        space = space[:len(space)-1]
        tmp = space + step
        print(tmp)
        step += "#"

        
if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
