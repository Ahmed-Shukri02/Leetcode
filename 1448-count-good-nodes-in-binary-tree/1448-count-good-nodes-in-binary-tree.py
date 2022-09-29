# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs(node, maxval):
            if not node:
                return 0 
            if node.val < maxval:
                return dfs(node.left, maxval) + dfs(node.right, maxval)     
            else:
                maxval = node.val
                return 1 + dfs(node.left, maxval) + dfs(node.right, maxval)
        
        return dfs(root, -10 ** 4)
            
            
            