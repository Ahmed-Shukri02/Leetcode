# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.f = 0
        self.s = ""

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                self.f += int(self.s + str(node.val))
                return
            
            self.s += str(node.val)
            dfs(node.left)
            dfs(node.right)
            self.s = self.s[:-1]
        
        dfs(root)
        return self.f