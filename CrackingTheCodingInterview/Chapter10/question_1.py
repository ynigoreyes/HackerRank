# O(n) Time and Space
def mergeLists(AList, BList):
    back = 0

    # Find last element of list A (On)
    for i, val in reversed(list(enumerate(AList))):
        if val is not None:
            back = i
            break

    # Check B[-1] is greater than A[back]
    position = -1
    while len(BList) > 0:
        if AList[back] <= BList[-1]:
            AList[position] = BList.pop()
        else:
            AList[position] = AList[back]
            back -= 1

        position -= 1
    return AList

ans = mergeLists([1, 3, 5, 7, None, None, None, None, None, None], [1, 6, 7, 8, 9, 10])

print(ans)
