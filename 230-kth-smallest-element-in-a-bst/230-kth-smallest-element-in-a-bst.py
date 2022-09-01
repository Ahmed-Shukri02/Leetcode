# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        counter = 0
        stack = []
        
        
        # inorder traversal. add left to stack
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                continue
            
            root = stack.pop()
            counter += 1
            
            if counter == k:
                return root.val
            
            root = root.right
            