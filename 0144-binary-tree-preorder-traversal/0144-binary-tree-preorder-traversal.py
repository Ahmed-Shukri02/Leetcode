# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        final = []
        def dfs(node):
            final.append(node.val)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        dfs(root)
        return final