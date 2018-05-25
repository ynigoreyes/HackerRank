class Solution:
  def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """

    hashSet = {}
    answer = 0

    for jewel in J:
      hashSet[jewel] = True

    for rock in S:
      if hashSet.get(rock, False) == True:
        answer += 1

    return answer