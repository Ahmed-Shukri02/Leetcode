# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        o, e = head, head.next
        obase, ebase = o, e
        curr = head.next.next
        
        odd = True
        while curr:
            if odd:
                o.next = curr
                o = o.next
            else:
                e.next = curr
                e = e.next
            curr = curr.next
            odd = not odd
        
        e.next = None
        o.next = ebase
        return obase
        