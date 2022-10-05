# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        final = []
        def dfs(node, total):
            total += node.val
            if not node.left and not node.right:
                final.append(total)
                return
            if node.left:
                dfs(node.left, total)
            if node.right:
                dfs(node.right, total)
        
        dfs(root, 0)
        return targetSum in final