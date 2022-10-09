# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        if not root:
            return False
        
        
        hmap = {}
        
        # traversal
        def dfs(node):
            if not node:
                return False
            
            if k - node.val in hmap:
                return True
            else:
                hmap[node.val] = 1
                # do dfs
                return True if (dfs(node.left) or dfs(node.right)) else False
        
        return dfs(root)