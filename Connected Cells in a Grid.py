#!/bin/python

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def adj(xi, yi, n, m):
    return filter(lambda v:v[0] >= 0
    and v[0]<n
    and v[1]>=0
    and v[1]<m,[
        [xi+1, yi],
        [xi+1, yi+1],
        [xi+1, yi-1],
        [xi, yi+1],
        [xi, yi-1],
        [xi-1, yi+1],
        [xi-1, yi],
        [xi-1, yi-1],
    ])
def connectedCell(matrix):
    filled = []
    n = len(matrix)
    if n > 0:
        m = len(matrix[0])
    else:
        return 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 1:
                filled.append([x, y])
    
    result = 0
    while len(filled) > 0:
        xi, yi = filled[0]
        queue = [[xi, yi]]
        index = 0
        while index < len(queue):
            xtmp, ytmp = queue[index]
            tmp = adj(xtmp, ytmp, n, m)
            neibers = [
                [x, y]
                for x, y in tmp
                if [x, y] in filled
            ]            
            for x, y in neibers:
                if [x,y] not in queue:
                    queue.append([x,y])
            index += 1
        tmp = len(queue)
        if result < tmp:
            result = tmp
        for x,y in queue:
            filled.remove([x,y])
    return result

            

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    m = int(raw_input())

    matrix = []

    for _ in xrange(n):
        matrix.append(map(int, raw_input().rstrip().split()))

    result = connectedCell(matrix)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
