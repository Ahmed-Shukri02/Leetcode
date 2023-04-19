# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.f = 0

        def dfs(node, curr, isLeft):
            if not node:
                self.f = max(self.f, curr)
                return 1 

            if isLeft:
                dfs(node.right, curr + 1, not isLeft)
                dfs(node.left, 1, isLeft)
            else:
                dfs(node.left, curr + 1, not isLeft)
                dfs(node.right, 1, isLeft)

        dfs(root, 0, True)
        dfs(root, 0, False)

        return self.f - 1


            