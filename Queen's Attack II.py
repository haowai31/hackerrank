#!/bin/python

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
        
def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0
    option = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    tmpob = obstacles[:]
    re = {}
    for op in option:
        re[op] = n+1

    for ob in tmpob:
        tmpi = ob[0]-r_q
        tmpj = ob[1]-c_q
        if tmpi == 0 and tmpj !=0:
            step = tmpj / sign(tmpj)
            tmpj = sign(tmpj)
            
        elif tmpj == 0 and tmpi !=0:
            step = tmpi / sign(tmpi)
            tmpi = sign(tmpi)
        elif tmpi != 0 and tmpj != 0:
            stepi = tmpi / sign(tmpi)
            stepj = tmpj / sign(tmpj) 
            if abs(stepi) != abs(stepj):
                continue
            else:
                step = stepi / sign(stepi)
                tmpi = sign(tmpi)
                tmpj = sign(tmpj)
        re[(tmpi, tmpj)] = min(re[(tmpi, tmpj)], step-1)
        if ob in obstacles:
            obstacles.remove(ob)
    
    for op in option:
        if re[op] != n+1:
            result += re[op]
            continue
        tmp = n+1
        if op[1] != 0:
            if op[1] > 0:
                tmp = min([tmp, n - c_q])
            else:
                tmp = min([tmp, c_q-1])
        if op[0] != 0:
            if op[0] > 0:
                tmp = min([tmp, n - r_q])
            else:
                tmp = min([tmp, r_q-1])
        re[op] = tmp
        result += tmp

    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = raw_input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in xrange(k):
        obstacles.append(map(int, raw_input().rstrip().split()))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
