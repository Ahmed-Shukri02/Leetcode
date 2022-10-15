# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return root
        
        
        def dfs(node):
            if not node:
                return None
            
            if (node.val == p.val or node.val == q.val) or (p.val > node.val and q.val < node.val) or (p.val < node.val and q.val > node.val):
                return node
            
            if node.val > p.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
            
        return dfs(root)