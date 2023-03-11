# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def binTree(l, r):
            if l == r:
                return TreeNode(nums[l])
            elif l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = binTree(l, mid - 1)
            node.right = binTree(mid + 1, r)

            return node
    
        return binTree(0, len(nums) - 1)