# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and q: # leaf node
            return False
        elif not q and p:
            return False
        elif not p and not q:
            return True
        
        # comapare nodes
        if p.val != q.val:
            return False
           
        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)
        
        return leftTree and rightTree
            
            
        
        
        
        
        
        