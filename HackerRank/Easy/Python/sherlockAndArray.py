# Sherlock And Array
# Algorithm Efficiency: O(n)

def solve(a):
    iteration = 0
    if len(a) == 1:
        return ("YES")

    while a[0] != a[-1] and len(a) > 2:
        iteration += 1
        if a[-1] + a[-2] > a[0] + a[1]:  # right side is greater
            sumOfSide = a.pop(1) + a.pop(0)
            a.insert(0, sumOfSide)

        elif a[-1] + a[-2] < a[0] + a[1]:  # if left side is greater
            sumOfSide = a.pop(-2) + a.pop(-1)
            a.insert(len(a), sumOfSide)

        else: # When the sum of the two ends are equal and there is still a lot
              # of elements left in the list
            a.pop(-1)
            a.pop(-1)
            a.pop(0)
            a.pop(0)

    if len(a) == 2: # When only two elements are left
        return("NO")
    else:
        return("YES")


T = 1
for a0 in range(T):
    n = 100
    a = [185, 170, 208, 216, 236, 155, 88, 206, 211, 209, 84, 99, 130, 245, 232, 125, 127, 232, 187, 140, 92, 213, 221, 231, 129, 197, 221, 168, 95, 186, 136, 180, 94, 125, 150, 244, 249, 248, 140, 207, 125, 84, 123, 85, 100, 175, 67, 116, 107, 143, 158, 75, 165, 172, 115, 134, 175, 123, 115, 123, 159, 181, 63, 176, 158, 109, 67, 154, 126, 141, 111, 95, 138, 161, 71, 118, 151, 189, 126, 109, 194, 176, 159, 151, 189, 71, 95, 133, 154, 157, 109, 78, 101, 174, 169, 152, 94, 193, 176, 137]
    result = solve(a)
    print(result)
