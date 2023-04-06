# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return None

        prev, curr = head, head.next
        while curr and curr.next:
            tmp = curr.next
            if curr.val == val:
                prev.next = tmp
                curr = tmp
            else:
                prev, curr = curr, curr.next
        
        if curr and curr.val == val:
            prev.next = None

        return head
