# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        
        def buildTreeRecursion(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            newNode = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            del preorder[0]
            
            newNode.left = buildTreeRecursion(preorder, inorder[0:index])
            newNode.right = buildTreeRecursion(preorder, inorder[index + 1:])
            
            return newNode
        
        return buildTreeRecursion(preorder, inorder)
            
            