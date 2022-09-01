# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        
        return self.levelOrderRecursive(deque([root]), [])
        
        
    def levelOrderRecursive(self, queue, final):
        # bredth first search
        if not queue:
            return final
        
        level = []
        length = len(queue)
        for i in range(length):
            level.append(queue[0].val)
            poppedNode = queue.popleft()
            if poppedNode.left:
                queue.append(poppedNode.left)
            if poppedNode.right:
                queue.append(poppedNode.right)
        
        final.append(level)
        return self.levelOrderRecursive(queue, final)
        