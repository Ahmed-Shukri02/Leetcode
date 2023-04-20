# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque([(root, 1)])
        f, d = 1, 0
        d_sum = 0
        while q:
            l = len(q)
            max_n, min_n = float("-inf"), float("inf")
            for i in range(l):
                node, ind = q.popleft()
                max_n, min_n = max(max_n, ind), min(min_n, ind)
                if node.left: q.append((node.left, ind * 2))
                if node.right: q.append((node.right, (ind * 2) + 1))

            f = max(f, max_n - min_n + 1)
            
            d_sum += 2 ** d
            d += 1

        return f

            


        

