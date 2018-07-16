#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if "PM" in s:
        hour = int(s[0:2])
        hour += 12
        if hour >=24:
            hour -= 12
    else:
        hour = int(s[0:2])
        if hour >= 12:
            hour -= 12
    result = str(hour) + s[2:len(s)-2]
    if len(result) < 8:
        result = "0" + result

    return result

if __name__ == '__main__':
#    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)
    print(result)

#    f.write(result + '\n')

#    f.close()
