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
        n = 1
        if not root:
        	return 0
        if not root.left and not root.right:
        	return n
        return n + max([self.maxDepth(root.left),self.maxDepth(root.right)])
