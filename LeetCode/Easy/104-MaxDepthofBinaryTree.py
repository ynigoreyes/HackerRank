# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0
    else:
      left = self.maxDepth(root.left)
      right = self.maxDepth(root.right)

      return 1 + max(left, right)
