# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def diameterRecursive(root):
            if not root:
                return -1
            
            l, r = diameterRecursive(root.left) , diameterRecursive(root.right)
            diameter = l + r + 2
            height = max(l, r)
            
            maxVal[0] = max(maxVal[0], diameter)
            return 1 + height
        
        maxVal = [0]
        diameterRecursive(root)
        return maxVal[0]