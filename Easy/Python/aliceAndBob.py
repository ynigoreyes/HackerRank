# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/6/2018
# Alice and Bob

def solve(a0, a1, a2, b0, b1, b2):

    pointsList = [0, 0]

    if a0 > b0:
        pointsList[0] += 1
    elif a0 < b0:
        pointsList[1] += 1

    if a1 > b1:
        pointsList[0] += 1
    elif a1 < b1:
        pointsList[1] += 1

    if a2 > b2:
        pointsList[0] += 1
    elif a2 < b2:
        pointsList[1] += 1

    return pointsList

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
