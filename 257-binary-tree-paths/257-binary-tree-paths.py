# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        f = []
        def helper(node, final):
            if not node:
                return
            if not node.left and not node.right:
                final += str(node.val)
                f.append(final)
                return

            final += str(node.val) + "->"
            helper(node.left, final)
            helper(node.right, final)
        
        helper(root, "")
        return f