#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.

# Completed in O(n) time and 0(1) space
def plusMinus(arr):
    arrayGreaterThanZero = 0
    arrayLessThanZero = 0
    arrayEqualToZero = 0
    lenOfArray = len(arr)
    
    for element in arr:
        if element == 0:
            arrayEqualToZero += 1
        elif element > 0:
            arrayGreaterThanZero += 1
        elif element < 0:
            arrayLessThanZero += 1
            
        
    print(arrayGreaterThanZero/lenOfArray)
    print(arrayLessThanZero/lenOfArray)
    print(arrayEqualToZero/lenOfArray)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

