# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirrorTree(root, root)

    def isMirrorTree(self, TreeNode1, TreeNode2):
    	if not TreeNode1 and not TreeNode2:
    		return True
    	elif not TreeNode1 or not TreeNode2:
    		return False
    	else:
    		return (TreeNode1.val == TreeNode2.val) and self.isMirrorTree(TreeNode1.left, TreeNode2.right) \\
    		        and self.isMirrorTree(TreeNode1.right, TreeNode2.left)

        