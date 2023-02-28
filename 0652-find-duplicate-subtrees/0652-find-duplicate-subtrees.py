# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        f = set()
        f_tracker = set()
        visited = set()
        def dfs(node):
            l = [node]
            if node.left:
                l += dfs(node.left)
            else:
                l.append(TreeNode(None))
            if node.right:
                l += dfs(node.right)
            else:
                l.append(TreeNode(None))
            
            l1 = tuple([i.val for i in l])
            if l1 and l1 in visited and l1 not in f_tracker:
                f.add(node)
                f_tracker.add(l1)
            visited.add(l1)

            return l

        dfs(root)
        return list(f)