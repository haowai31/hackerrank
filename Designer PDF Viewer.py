#!/bin/python

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max = 0
    for letter in word:
        tmp = ord(letter) - 97
        if max < h[tmp]:
            max = h[tmp]
    return max*len(word)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = map(int, raw_input().rstrip().split())

    word = raw_input()

    result = designerPdfViewer(h, word)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
