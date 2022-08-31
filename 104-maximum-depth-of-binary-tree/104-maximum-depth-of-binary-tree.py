# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.maxDepthRecursive(root, 1)
        
        
    def maxDepthRecursive(self, node, counter):
        
        counter += 1
        if node.left:
            leftMax = self.maxDepthRecursive(node.left, counter)
        if node.right:
            rightMax = self.maxDepthRecursive(node.right, counter)
        counter -= 1
        
        if not node.left and not node.right: # at leaf
            return counter
        else:
            if not node.left:
                return rightMax
            elif not node.right:
                return leftMax
            
            return max(leftMax, rightMax)
            