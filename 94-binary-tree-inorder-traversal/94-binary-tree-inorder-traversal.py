# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        final = []
        
        def inorderRecursive(node):
            if not node:
                return
            
            inorderRecursive(node.left)
            final.append(node.val)
            inorderRecursive(node.right)
        
        inorderRecursive(root)
        return final
            