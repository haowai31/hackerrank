#!/bin/python

import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def longestIncreasingSubsequence(arr):
    nums = [arr[0]]
    for i in range(1, len(arr)):
        left = 0
        right = len(nums)
        if arr[i] > nums[right - 1]:
            nums.append(arr[i])
            continue
        while left < right:
            mid = (left + right) / 2 
            if (nums[mid] < arr[i]):
                left = mid + 1
            elif nums[mid] == arr[i]:
                left = mid
                break
            else:
                right = mid
        else:
            nums[left] = arr[i]

    return len(nums)



if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()