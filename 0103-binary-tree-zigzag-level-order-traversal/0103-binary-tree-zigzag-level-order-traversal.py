# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        left = True
        f = []
        while q:
            l = len(q)
            if not left:
                f.append(reversed([i.val for i in q]))
            else:
                f.append([i.val for i in q])

            for i in range(l):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            left = not left
        return f
