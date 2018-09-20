#!/bin/python

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []

    climbing = [1]
    count = 1
    for i in range(1, len(scores)):
        if scores[i] != scores[i-1]:
            count += 1
        climbing.append(count)

    for j in alice:
        left = 0
        right = len(scores)
        if j > scores[left]:
            result.append(1)
            continue
        if j < scores[right-1]:
            result.append(climbing[right-1] + 1)
            continue
        while left < right:
            mid = (left + right) / 2
            if j < scores[mid]:
                left = mid + 1
            elif j > scores[mid]:
                right = mid
            else:
                left = mid
                break
        if j >= scores[left]:
            result.append(climbing[left])
        else:
            result.append(climbing[left] + 1)
                
    return result
        

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)
    print(result)

#    fptr.write('\n'.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()