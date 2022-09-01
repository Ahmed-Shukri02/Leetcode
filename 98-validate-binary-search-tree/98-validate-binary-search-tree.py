# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, float("-inf"), float("inf"))
    
    
    def isValid(self, node, left, right):
        if not node:
            return True
        
        # check if node val within range
        if not left < node.val < right:
            return False
        
        return (self.isValid(node.left, left, node.val) and
                self.isValid(node.right, node.val, right))
        
        