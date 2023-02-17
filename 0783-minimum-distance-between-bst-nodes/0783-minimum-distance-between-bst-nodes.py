# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = float("-inf")
        self.f = float("inf")
        def inorder(node):
            if not node:
                return
            # left -> node -> right
            inorder(node.left)
            self.f = min(self.f, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return 0 if self.f == float("inf") else self.f