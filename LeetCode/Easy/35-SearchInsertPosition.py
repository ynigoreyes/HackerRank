class Solution:
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    answer = 0

    if target < nums[0]:
      answer = 0
    elif target > nums[-1]:
      answer = len(nums)

    else:
      for index, currentNumber in enumerate(nums):
        if currentNumber == target:
          answer = index
          break
        elif currentNumber < target and nums[index + 1] > target:
          answer = index + 1
          break

    return answer