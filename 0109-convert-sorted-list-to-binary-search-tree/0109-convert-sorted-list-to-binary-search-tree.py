# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        def binTree(l, r):
            if l == r:
                return TreeNode(arr[l])
            elif l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            node.left = binTree(l, mid - 1)
            node.right = binTree(mid + 1, r)

            return node
        
        return binTree(0, len(arr) - 1)
