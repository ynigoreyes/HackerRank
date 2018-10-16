# O(1) Time O(n) space
def rotate(arr, d):
    d = d % len(arr)

    arr = arr[d:] + arr[:d]
    return " ".join(map(str, arr))
