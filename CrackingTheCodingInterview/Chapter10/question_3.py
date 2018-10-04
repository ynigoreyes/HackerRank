# Assuming that there are no duplicates

def search_sorted_array(arr, left, right, target):
    if left == None: left = 0
    if right == None: right = len(arr) - 1

    mid = (right + left) // 2

    index = None


    # Found it!
    if arr[mid] == target:
        return mid
    elif right < left:
        return -1
    elif arr[left] == arr[right]:
        index = search_sorted_array(arr, left + 1, right -1, target)
    elif arr[right] < arr[left]: # right side is ordered
        if arr[right] < target: # It is not on the right side
            index = search_sorted_array(arr, left, mid - 1, target)
        else:
            index = search_sorted_array(arr, mid + 1, right, target)
    else: # We are dealing with a sorted array now
        if arr[mid] < target:
            index = search_sorted_array(arr, mid + 1, right, target)
        else:
            index = search_sorted_array(arr, left, mid - 1, target)

    return index

ans = search_sorted_array([15, 16, 19, 20, 1, 4, 5, 7, 10, 14], None, None, 10)
print('You have answered correctly' if ans == 8 else 'Incorrect, the answer is 8, you printed {}'.format(ans))

ans = search_sorted_array([14, 15, 16, 19, 20, 1, 4, 5, 7, 10, 14, 14], None, None, 10)
print('You have answered correctly' if ans == 9 else 'Incorrect, the answer is 9, you printed {}'.format(ans))

