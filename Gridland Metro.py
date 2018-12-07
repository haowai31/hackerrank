#!/bin/python

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def takefirst(elem):
    return elem[0]

def gridlandMetro(n, m, k, track):
    tracks = {}
    
    
    for i in track:
        row = i[0]
        left = i[1]
        right = i[2]
        if row not in tracks.keys():
            tracks[row] = []
        tracks[row].append([left, right])
    
    for i in tracks.values():
        if len(i) == 0:
            continue
        i.sort(key=takefirst)
    
    result = n * m
    for i in tracks.values():
        tmp = i[:]
        index = 0
        while index<len(tmp)-1:
            if tmp[index][1] + 1< tmp[index+1][0]:
                index += 1
            else:
                tmp[index][1] = max([tmp[index][1], tmp[index+1][1]])
                tmp.remove(tmp[index+1])        
        for j in tmp:
            len1 = j[1] - j[0] + 1
            result -= len1        
    return result


        


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = raw_input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in xrange(k):
        track.append(map(int, raw_input().rstrip().split()))

    result = gridlandMetro(n, m, k, track)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
