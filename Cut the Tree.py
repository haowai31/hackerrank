#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

summ = 0
result = 0

def sumtree(root, children, data, visited):
    global result

    tmp = 0
    visited[root-1] = 1

    for index in children[root]:
        if visited[index-1] == 0:
            tmp += sumtree(index, children, data, visited)
    
    summm = tmp + data[root-1]
    result = min(result, abs(summ-2*summm))

    return summm


def cutTheTree(data, edges):
    # Write your code here
    children = {}
    global summ
    global result
    n = len(data)
    visited = [0] * n
    for i in range(len(edges)):
        if edges[i][0] not in children.keys():
            children[edges[i][0]] = []
        if edges[i][1] not in children.keys():
            children[edges[i][1]] = []
        children[edges[i][0]].append(edges[i][1])
        children[edges[i][1]].append(edges[i][0])
    
    summ = 0
    for i in data:
        summ += i
        
    result = 1000000000
    sumtree(1, children, data, visited)
    
    
    return result
        

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    data = map(int, raw_input().rstrip().split())

    edges = []

    for _ in xrange(n - 1):
        edges.append(map(int, raw_input().rstrip().split()))

    result = cutTheTree(data, edges)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
