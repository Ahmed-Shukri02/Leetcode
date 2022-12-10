# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
            self.final = 0

            def nodesum(node):
                if not node:
                    return 0
                return node.val + nodesum(node.left) + nodesum(node.right)
            total = nodesum(root)

            def dfs(node):
                if not node:
                    return 0
                left, right = dfs(node.left), dfs(node.right)
                self.final = max(self.final, left * (total - left), right * (total - right))
                return node.val + left + right
            dfs(root)
            return self.final % ((10 ** 9) + 7)
            
        