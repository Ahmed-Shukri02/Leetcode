# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, currmax, currmin):
            if not node:
                return currmax - currmin
            currmax = max(currmax, node.val)
            currmin = min(currmin, node.val)
            return max(dfs(node.left, currmax, currmin), dfs(node.right, currmax, currmin))
        return dfs(root, root.val, root.val)
            
