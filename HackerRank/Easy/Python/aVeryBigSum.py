# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/6/2018
# A Very Big Sum

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
