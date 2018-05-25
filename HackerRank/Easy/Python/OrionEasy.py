# Easy:
# You have a function, random(), that returns a random number in the range[0, 1).
# Write code to get a random number in the range[3, 8) using the random() function and any math operations necessary.

import random
def main(number):
  answer = (number * 7)
  if answer < 3:
    answer += 3
  return answer


def test():
  for i in range(1, 21):
    answer = main(random.random())

    if answer >= 3 and answer < 8:
      print(f"{i}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test Case Passed: {answer}")
    else:
      print(f"{i} Test Case Failed: {answer}")

test()