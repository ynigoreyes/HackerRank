# Time Complexity: O(n)
# Space Complexity: 0(n)
def main(houses):
    length = len(houses)
    for i, val in enumerate(houses):
        if (length - (i + 1) != val):
            return False

    return True

print(main([5, 4, 3, 2, 1, 0]))
