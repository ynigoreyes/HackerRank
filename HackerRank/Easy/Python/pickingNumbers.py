#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.

# Completed in O(n) time
def pickingNumbers():
    """
    Explaination:
    1. I save the occurances of each element in the into a hashMap which is O(n)
    2. I go through the found numbers in the second for loop and do the following
        - Find the maximum occurence between current value and int value above or bellow
        - If there are no integer values 1 bellow or above the current value, then save
            the current value as it is since, there is an edge case that one lone integer
            occurs more often that everything combined
        - Else, I save the max or either current value + 1 above or bellow
    3. I instantiate the answer to 0 since the spec says that the answer will always be above 2
    4. I check to see whether or not the value saved in occurances is greater than previou
        since we are really trying to find greatest occurance
    """
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    
    # We save the integer as the key and the ocurrances as the value
    hashMap = {}
    for element in a:
        if hashMap.get(element, False):
            hashMap[element] += 1
        else:
            hashMap[element] = 1
            
    maxInt = 0
    maxVal = 0
    answer = 0
    occurences = 0
    
    for key, value in hashMap.items():

        minusOne = hashMap.get(key - 1, -1)
        plusOne = hashMap.get(key + 1, -1)
        
        if minusOne == plusOne:
            check = max(minusOne, plusOne)
            if check != -1:
                occurences = value + check
            else:
                occurences = value
        else:
            occurences = value + max(minusOne, plusOne)
        
        # Update the answer if the occurances we found were be greater than before
        if answer < occurences:
            answer = occurences

    print(answer)
    
if __name__ == "__main__":
    pickingNumbers()

