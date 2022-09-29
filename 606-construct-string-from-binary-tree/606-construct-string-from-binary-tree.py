# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        #dfs
        if not root:
            return ""
        
        
        def dfs(node):
            if not node:
                return ""
            
            ans = str(node.val)
            if not node.left and not node.right:
                return ans
            
            if not node.left:
                ans += "()"
            else:
                ans += "(" + dfs(node.left) + ")"
                
            if node.right:
                ans += "(" + dfs(node.right) + ")"
            
            return ans
        
        return dfs(root)