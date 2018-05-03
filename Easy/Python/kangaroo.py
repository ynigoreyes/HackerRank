import sys


def kangaroo(x1, v1, x2, v2):
  totalDistance = 0
  relativeVelocity = 0

  # Find Absolute Value of Distance
  totalDistance = max([x1, x2]) - min([x1, x2])
  relativeVelocity = max([v1, v2]) - min([v1, v2])  # Found Relative Speed

  # EDGE case to avoid divide by 0 error
  if x1 != x2 and relativeVelocity == 0:
    return("NO")

  # Main Algorithm
  if totalDistance % relativeVelocity != 0:
    return ("NO")

  # Certain Situations where there is no chance
  elif x1 > x2 and v1 > v2:
    return ("NO")
  elif x1 < x2 and v1 < v2:
    return ("NO")

  return ("YES")


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
