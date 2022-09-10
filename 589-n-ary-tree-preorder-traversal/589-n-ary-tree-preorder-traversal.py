"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return root
        
        final = []
        def helper(node):
            final.append(node.val)
            if not node.children: # leaf node
                return
            for child in node.children:
                helper(child)
        helper(root)
        return final
        