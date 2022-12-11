# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.alone = float("-inf")
        def dfs(node):
            if not node.left and not node.right:
                return (node.val, float("-inf"))
            
            l, r = (float("-inf"), float("-inf")), (float("-inf"), float("-inf"))
            if node.left: l = dfs(node.left)
            if node.right: r = dfs(node.right)
                
            w, wout = max(node.val, node.val + l[0], node.val + r[0]), max(max(l), max(r))
            self.alone = max(self.alone, w, node.val + l[0] + r[0])
            
            return (w, wout)
        
        return max(max(dfs(root)), self.alone)