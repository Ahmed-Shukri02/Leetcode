# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Complexities
        # Time: O(n)
        # Space: O(1)
        
        if not head:
            return head
        
        f, s = head, head
        prev = None
        while f and f.next:
            f = f.next.next
            prev = s
            s = s.next
        
        if not prev:
            return None
        
        prev.next = s.next
        return head