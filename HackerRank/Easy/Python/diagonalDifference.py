#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.

# Completed in O(n) time
def diagonalDifference(a):
    diag_1 = 0
    diag_2 = 0
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                diag_1 += a[i][j]
            if i + j == len(a) - 1:
                diag_2 += a[i][j]
                
    print(diag_1, diag_2)
    return abs(diag_1 - diag_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()

