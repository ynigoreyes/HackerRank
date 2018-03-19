# Ynigo Reyes
# Computer Science - TTU
# Class of 2021
# 3/6/2018
# Simple Array Sum

def simpleArraySum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
