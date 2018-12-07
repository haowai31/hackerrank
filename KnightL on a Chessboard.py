#!/bin/python

import math
import os
import random
import re
import sys

h = [[]]

def getlocol(a,b,x,y,n):
    return filter(lambda v:v[0]>=0
    and v[1]>=0
    and v[0]<n
    and v[1]<n,
    [
        [x+a, y+b],
        [x+a, y-b],
        [x-a, y+b],
        [x-a, y-b],
        [x+b, y+a],
        [x+b, y-a],
        [x-b, y+a],
        [x-b, y-a], 
    ])

def get(a, b, n):
    if h[a][b] is not None:
        return h[a][b]
    
    visited = [[False] * n for _ in range(n)]
    queue = [[0, 0, 0]]
    while len(queue) > 0:
        x, y, l = queue.pop()
        if x==n-1 and y == n-1:
            h[a][b] = l
            h[b][a] = l
            return l
        tmp = getlocol(a, b, x, y, n)
        locall = [
            [xi, yi]
            for xi, yi in tmp
            if visited[xi][yi] == False
        ]
        for xi, yi in locall:
            visited[xi][yi] = True
            visited[yi][xi] = True
            queue.insert(0, [xi, yi, l+1])
    h[a][b] = -1
    h[b][a] = -1
    return -1


def knightlOnAChessboard(n):
    global h
    h = [[None for _ in range(n+1)] for _ in range(n+1)]
    result = []
    for i in range(1, n):
        result.append([])
        for j in range(1, n):
            tmp = get(i, j, n)
            result[i-1].append(tmp)
    
    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = knightlOnAChessboard(n)
    print(result)

#    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
#    fptr.write('\n')

#    fptr.close()
