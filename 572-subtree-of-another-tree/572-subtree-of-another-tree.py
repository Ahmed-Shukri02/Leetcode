# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        # do is same tree for every elem
        if self.isSameTree(root, subRoot):
            return True
        elif not root: # end of tree, but subroot is not null
            return False
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        
            
    def isSameTree(self, p, q):
        if not p and not q: # both elems were leaves
            return True
        elif not p or not q: # one was leaf, one was branch
            return False
        
        if p.val != q.val: # both were branches
            return False
        
        # nodes were compared and are the same. Check their left and right
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right