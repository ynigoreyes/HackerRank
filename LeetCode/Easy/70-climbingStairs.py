class Solution:
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    prev_two = [0, 0]
    stair = 1

    # Prev will hold the previous 2 values
    if n <= 2:
      return n

    while stair < n:  # When we are not at n
      current_answer = prev_two[0] + prev_two[1]
      if stair <= 2:
        current_answer += 1
      prev_two[0] = prev_two[1]
      prev_two[1] = current_answer  # [3, 5]
      print(prev_two)

      stair += 1

    return prev_two[0] + prev_two[1]
