#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the coinOnTheTable function below.
#
def coinOnTheTable(m, k, board):
    #
    # Write your code here.
    #
    index_i = 0
    index_j = 0
    count = 0
    step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    stepv = ['U', 'D', 'L', 'R']
    n = len(board)
    for i in board:        
        if '*' in i:
            index_i = count
            index_j = i.find('*')
            break
        count += 1
    
    dp = []
    for i in range(n):
        dpj = []
        for j in range(m):
            dpk = []
            for indexk in range(k+1):
                dpk.append(sys.maxint)
            dpj.append(dpk)
        dp.append(dpj)
    
    dp[0][0][0] = 0
    for indexk in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                minn = sys.maxint
                for indexx in range(4):
                    tmpi = i + step[indexx][0]
                    tmpj = j + step[indexx][1]
                    tmp = 0
                    if tmpi >= 0 and tmpi < n and tmpj >= 0 and tmpj < m:
                        if board[i][j] == stepv[indexx]:
                            tmp = dp[i][j][indexk-1]
                        else:                            
                            tmp = dp[i][j][indexk-1] + 1
                        if dp[tmpi][tmpj][indexk] > tmp:
                            dp[tmpi][tmpj][indexk] = tmp
    
    minn = sys.maxint
    for indexk in range(k+1):
        if minn > dp[index_i][index_j][indexk]:
            minn = dp[index_i][index_j][indexk]
    if minn > 2500:
        minn = -1
    return minn

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = raw_input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    board = []

    for _ in xrange(n):
        try:
            board_item = raw_input()
        except EOFError:
            result = -1
            fptr.write(str(result) + '\n')            
            fptr.close()
            sys.exit()            
        board.append(board_item)

    result = coinOnTheTable(m, k, board)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
