# Completed using Kadane's Algorithm
# O(n) time O(1) space

def main(n):
	for element in n:
		maxCurrent += element
		  if maxCurrent > maxOverall:
	      maxOverall = maxCurrent
      if maxCurrent < 0:
	  maxCurrent = 0

return maxOverall

