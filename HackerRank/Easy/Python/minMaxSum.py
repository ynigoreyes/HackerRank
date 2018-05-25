# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/5/2018
# Min-Max Sum

def miniMaxSum(arr):
    maxTerm = max(arr) # Saves the max value in the given list
    minTerm = min(arr) # Saves the min value in the given list

    minAnswer = 0
	maxAnswer = 0

    minArray = list(arr)     # Saves a copy of the given array as minArray
							 # arr is will be the array having the highest sum
							 # minArray will be the array having the smallest sum

    minArray.remove(maxTerm) # the max term of the array is removed
    arr.remove(minTerm)      # The min term of the array is removed

    for i in arr:
        maxAnswer += i

    for j in minArray:
        minAnswer += j

    print(minAnswer, end=" ")
    print(maxAnswer)


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
