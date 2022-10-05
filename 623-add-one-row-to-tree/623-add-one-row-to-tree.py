# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # base cases
        if not root:
            return root
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        
        # bfs, reach depth - 1
        d = 1
        q = deque([root])
        while q and d < depth - 1:
            length = len(q)
            for i in range(length):
                if q[0].left: q.append(q[0].left)
                if q[0].right: q.append(q[0].right)
                
                q.popleft()
            d += 1
            
        # we're at depth - 1
        if q:
            for node in q:
                l, r = node.left, node.right
                node.left, node.right = TreeNode(val, None, None), TreeNode(val, None, None)
                
                if l: node.left.left = l 
                if r: node.right.right = r
        
        return root