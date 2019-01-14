# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        stack = [root]
        if not root:
        	return list()
        while len(stack):
        	tmp = []
        	res_each = []
        	for node in stack:
        		res_each.append(node.val)
        		if node.left:
        			tmp.append(node.left)
        		if node.right:
        			tmp.append(node.right)
        	stack = tmp
        	res.append(res_each)
        return res[::-1]

