#!/bin/python

# Not AC
import math
import os
import random
import re
import sys

# Complete the shortPalindrome function below.
def shortPalindrome(s):

    #Stage 1 get first two in BFS
    queue = []
    for i in range(len(s)-3):
        for j in range(len(s)-1, i+2, -1):
            if s[i] == s[j]:
                queue.append(s[i+1:j])
    
    #Sstage 2 get second two in BFS
    result = 0
    for ss in queue:
        for i in range(len(ss)-1):
            for j in range(len(ss)-1, i, -1):
                if ss[i] == ss[j]:
                    result += 1
    return result

    

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = shortPalindrome(s)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
