# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lvs1, lvs2 = [], []
        
        def dfs(node, target):
            if not node.left and not node.right:
                target.append(node.val)
                return
            if node.left: dfs(node.left, target)
            if node.right: dfs(node.right, target)
        
        
        dfs(root1, lvs1)
        dfs(root2, lvs2)
        return lvs1 == lvs2
            
            
            
            