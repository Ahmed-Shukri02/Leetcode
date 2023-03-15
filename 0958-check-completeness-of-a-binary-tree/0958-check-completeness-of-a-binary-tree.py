# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True
        q = deque([root])

        while q:
            l = len(q)
            n = False
            present = False
            for i in range(l):
                node = q.popleft()
                if n and node:
                    return False
                if not node:
                    n = True
                    continue
                if node.right and not node.left: # quick check
                    return False
                if node.left or node.right:
                    present = True

                q.append(node.left)
                q.append(node.right)

            if n and present:
                return False

        
        return True



                