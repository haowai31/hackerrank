#!/bin/python

import math
import os
import random
import re
import sys
import itertools

def getcost(target, tmp):
    result = 0
    for i in range(9):
        result += abs(target[i]-tmp[i])
    return result

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    x = [1,2,3,4,6,7,8,9]
    list2 = list(itertools.permutations(x, 4))    
    target = list(itertools.chain(*s))
    result = 1000

    for i in list2:
        flag = 0
        for tmp1 in range(3):
            for tmp2 in range(tmp1+1, 4):
                if i[tmp1]+i[tmp2] == 10:
                    flag = 1
        if flag == 1:
            continue
        tmp = list(i)
        tmp.append(5)
        for j in range(4):
            tmp.append(10-tmp[3-j])
        flag = 0
        for tmp1 in range(3):
            heng = 0
            shu = 0
            for tmp2 in range(3):
                heng += tmp[tmp1*3+tmp2]
                shu += tmp[tmp2*3+tmp1]
            if heng != 15 or shu != 15:
                flag = 1
                break
        if flag == 1:
            continue
        cost = getcost(target, tmp)
        if result > cost:
            result = cost    
            print(tmp)
    return result


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()