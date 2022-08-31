# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # edge case: depth 0
        if not root:
            return root
        
        self.invertTreeRecursion(root)
        return root
        
        
        
    def invertTreeRecursion(self, node):
        # preorder traversal: search left node, then right node, then parent. ASSUME PERFECT TREE
        if node.left:
            self.invertTreeRecursion(node.left)

        if node.right:
            self.invertTreeRecursion(node.right)

        if not node.right and not node.left:
            return
        
        node.left, node.right = node.right, node.left
        return
        