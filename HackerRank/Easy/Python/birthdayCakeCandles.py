# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/5/2018
# Birthday Cake Candles


def birthdayCakeCandles(n, ar):

    count = 0

    for index, value in enumerate(ar):

        if index == 0: maxValidHeight = value

        if value == maxValidHeight:  # Adds 1 to the count when we find a
			count += 1				 # matching candle

		elif value > maxValidHeight: # When we find a new max height value, we
			maxValidHeight = value	 # reset the count to 1 to account for the
			count = 1				 # new found maxValidHeight

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)


