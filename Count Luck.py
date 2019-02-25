#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countLuck function below.
step = [[0,1],[0,-1],[1,0],[-1,0]]
def getlocol(x, y, m, n):
    return filter(lambda v:v[0] >=0 
    and v[0]<m
    and v[1]>=0
    and v[1]<n,
    [
        [x, y+1],
        [x, y-1],
        [x+1, y],
        [x-1, y]
    ])

resultt = 0

def gettheresult(matrix, now, end, count, queue):
    global resultt
    if now[0] == end[0] and now[1] == end[1]:
        resultt = count
        return count

    if resultt > 0:
        return count
    
    locol = getlocol(now[0], now[1], len(matrix), len(matrix[0]))
    flag = 0
    for i in locol:
        if matrix[i[0]][i[1]] in [".", "*"] and i not in queue:
            flag += 1
    
    if flag > 1:
        count += 1
    
    for i in locol:
        if matrix[i[0]][i[1]] in [".", "*"] and i not in queue:
            queue.append(i)
            gettheresult(matrix, i, end, count, queue)
            queue.remove(i)
    
    return count



def countLuck(matrix, k):
    global resultt
    resultt = 0
    m = len(matrix)
    if m > 0:
        n = len(matrix[0])
    start = [0, 0]
    end = [0, 0]
    
    # Get M and *
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "M":
                start = [i, j]
            if matrix[i][j] == "*":
                end = [i, j]
    
    gettheresult(matrix, start, end, 0, [start])
    if resultt == k:
        return "Impressed"
    else:
        return "Oops!"
                
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in xrange(n):
            matrix_item = raw_input()
            matrix.append(matrix_item)

        k = int(raw_input())

        result = countLuck(matrix, k)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
