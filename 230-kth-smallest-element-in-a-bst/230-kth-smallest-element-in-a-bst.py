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
        
        
        def kthSmallestRecursion(node, k, stack):
            if not node:
                return
            
            # for each tree, search all the way left. INORDER TRAVERSAL:
            # LEFT, ROOT THEN RIGHT
            kthSmallestRecursion(node.left, k, stack) # left
            stack.append(node.val) # root
            kthSmallestRecursion(node.right, k, stack) # right
            
            return stack
                
        stack = kthSmallestRecursion(root, k, [])
        return stack[k - 1]