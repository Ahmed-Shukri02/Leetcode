# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        # get all pathsums
        sums = []
        
        def dfs(node, numsum, arr):
            numsum += node.val
            arr.append(node.val)
            
            if not node.left and not node.right:
                sums.append([numsum, [i for i in arr]])
                arr.pop()
                return
            if node.left:
                dfs(node.left, numsum, arr)
            if node.right:
                dfs(node.right, numsum, arr)
                
            arr.pop()
            
        dfs(root, 0, [])
        return [i[1] for i in sums if i[0] == targetSum]
        
        
            
            
            
            