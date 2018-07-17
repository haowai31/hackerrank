#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    result = []
    trans = [0, 0, 0, 2, 1, 0, 0, 0, 2, 1]
    for grade in grades:
        if grade < 38:
            result.append(grade)
            continue
        x = grade % 10
        x += trans[x]
        tmp = (grade / 10) * 10 + x
        result.append(tmp)
    return result


if __name__ == '__main__':
#    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

#    f.write('\n'.join(map(str, result)))
#    f.write('\n')

#    f.close()
